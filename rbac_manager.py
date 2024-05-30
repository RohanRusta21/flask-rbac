# rbac_manager.py

from kubernetes import client, config

def create_role(api_instance, namespace, role_name, rules):
    role = client.V1Role(
        metadata=client.V1ObjectMeta(name=role_name),
        rules=rules
    )
    api_instance.create_namespaced_role(namespace=namespace, body=role)

def delete_role(api_instance, namespace, role_name):
    api_instance.delete_namespaced_role(name=role_name, namespace=namespace)

# Similarly, implement functions for RoleBindings, ClusterRoles, and ClusterRoleBindings.
