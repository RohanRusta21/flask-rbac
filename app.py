from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from k8s_client import get_k8s_client
from rbac_manager import list_roles, list_role_bindings, list_cluster_roles, list_cluster_role_bindings, create_role, delete_role

app = Flask(__name__)
app.secret_key = 'supersecretkey'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['username']
        user = User(user_id)
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return "Welcome to the RBAC Management Webapp"

@app.route('/roles')
@login_required
def roles():
    namespace = request.args.get('namespace', 'default')
    api_instance = get_k8s_client()
    roles = list_roles(api_instance, namespace)
    return render_template('roles.html', roles=roles.items, namespace=namespace)

@app.route('/role_bindings')
@login_required
def role_bindings():
    namespace = request.args.get('namespace', 'default')
    api_instance = get_k8s_client()
    role_bindings = list_role_bindings(api_instance, namespace)
    return render_template('role_bindings.html', role_bindings=role_bindings.items, namespace=namespace)

@app.route('/cluster_roles')
@login_required
def cluster_roles():
    api_instance = get_k8s_client()
    cluster_roles = list_cluster_roles(api_instance)
    return render_template('cluster_roles.html', cluster_roles=cluster_roles.items)

@app.route('/cluster_role_bindings')
@login_required
def cluster_role_bindings():
    api_instance = get_k8s_client()
    cluster_role_bindings = list_cluster_role_bindings(api_instance)
    return render_template('cluster_role_bindings.html', cluster_role_bindings=cluster_role_bindings.items)

@app.route('/create_role', methods=['GET', 'POST'])
@login_required
def create_role_view():
    if request.method == 'POST':
        namespace = request.form['namespace']
        role_name = request.form['role_name']
        rules = request.form['rules']  # You need to parse this properly as JSON
        api_instance = get_k8s_client()
        create_role(api_instance, namespace, role_name, rules)
        return redirect(url_for('roles', namespace=namespace))
    return render_template('create_role.html')

@app.route('/delete_role', methods=['POST'])
@login_required
def delete_role_view():
    namespace = request.form['namespace']
    role_name = request.form['role_name']
    api_instance = get_k8s_client()
    delete_role(api_instance, namespace, role_name)
    return redirect(url_for('roles', namespace=namespace))

@app.route('/success')
def success():
    return "Role created successfully!"

if __name__ == '__main__':
    app.run(debug=True)
