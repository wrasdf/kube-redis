from kubernetes import client, config

class NamespacedSecretManager:

    def __init__(self, namespace):
        config.load_kube_config()
        self.api = client.CoreV1Api()
        self.namespace = namespace

    def list_namespaced_secret(self):
        return self.api.list_namespaced_secret(self.namespace)

    def read_namespaced_secret(self, name):
        return self.api.read_namespaced_secret(name, self.namespace)

    def create_namespaced_secret(self, name, data):
        return self.api.create_namespaced_secret(self.namespace, client.V1Secret(
            api_version="v1",
            kind="Secret",
            metadata=client.V1ObjectMeta(name=name),
            data=data,
            type="Opaque"
        ))

    def replace_namespaced_secret(self, name, data):
        return self.api.replace_namespaced_secret(name, self.namespace, client.V1Secret(
            api_version="v1",
            kind="Secret",
            metadata=client.V1ObjectMeta(name=name),
            data=data,
            type="Opaque"
        ))

    def delete_namespaced_secret(self, name):
        return self.api.delete_namespaced_secret(name, self.namespace, client.V1DeleteOptions())

    def exist_namespaced_secret(self, name):
        secret_names = []
        secrets = self.list_namespaced_secret().items

        for item in secrets:
            secret_names.append(item.metadata.name)

        if name in secret_names:
            return True

        return False
