# rbac_manager.py

# from kubernetes import client, config

# def create_role(api_instance, namespace, role_name, rules):
#     role = client.V1Role(
#         metadata=client.V1ObjectMeta(name=role_name),
#         rules=rules
#     )
#     api_instance.create_namespaced_role(namespace=namespace, body=role)

# def delete_role(api_instance, namespace, role_name):
#     api_instance.delete_namespaced_role(name=role_name, namespace=namespace)

# # Similarly, implement functions for RoleBindings, ClusterRoles, and ClusterRoleBindings.


# from kubernetes import client

# def list_roles(api_instance, namespace):
#     return api_instance.list_namespaced_role(namespace=namespace)

# def list_role_bindings(api_instance, namespace):
#     return api_instance.list_namespaced_role_binding(namespace=namespace)

# def list_cluster_roles(api_instance):
#     return api_instance.list_cluster_role()

# def list_cluster_role_bindings(api_instance):
#     return api_instance.list_cluster_role_binding()

# def create_role(api_instance, namespace, role_name, rules):
#     role = client.V1Role(
#         metadata=client.V1ObjectMeta(name=role_name),
#         rules=rules
#     )
#     api_instance.create_namespaced_role(namespace=namespace, body=role)

# def delete_role(api_instance, namespace, role_name):
#     api_instance.delete_namespaced_role(name=role_name, namespace=namespace)


from kubernetes import client

def list_roles(api_instance, namespace):
    return api_instance.list_namespaced_role(namespace=namespace)

def list_role_bindings(api_instance, namespace):
    return api_instance.list_namespaced_role_binding(namespace=namespace)

def list_cluster_roles(api_instance):
    return api_instance.list_cluster_role()

def list_cluster_role_bindings(api_instance):
    return api_instance.list_cluster_role_binding()

def create_role(api_instance, namespace, role_name, rules):
    role = client.V1Role(
        metadata=client.V1ObjectMeta(name=role_name),
        rules=rules
    )
    api_instance.create_namespaced_role(namespace=namespace, body=role)

def delete_role(api_instance, namespace, role_name):
    api_instance.delete_namespaced_role(name=role_name, namespace=namespace)

