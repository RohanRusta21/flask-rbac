# main.py

from flask import Flask, render_template, request
from k8s_client import get_k8s_client
from rbac_manager import create_role, delete_role
from auth import app, login_required

@app.route('/create_role', methods=['GET', 'POST'])
@login_required
def create_role_view():
    if request.method == 'POST':
        namespace = request.form['namespace']
        role_name = request.form['role_name']
        rules = request.form['rules']  # You need to parse this properly
        api_instance = get_k8s_client()
        create_role(api_instance, namespace, role_name, rules)
        return redirect(url_for('success'))
    return render_template('create_role.html')

@app.route('/success')
def success():
    return "Role created successfully!"

if __name__ == '__main__':
    app.run(debug=True)
