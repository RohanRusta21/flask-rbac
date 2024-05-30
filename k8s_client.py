# k8s_client.py

from kubernetes import client, config

def get_k8s_client():
    config.load_kube_config()  # Make sure your kubeconfig is set up correctly
    return client.RbacAuthorizationV1Api()
