from kubernetes import client, config

class SecretManager:

    def __init__(self, namespace):
        config.load_kube_config()
        self.api = client.CoreV1Api()
        self.namespace = namespace

    def list_namespaced_secret(self):
        secrets = []
        api_response = self.api.list_namespaced_secret(self.namespace).items
        for item in api_response:
            secrets.append(item.metadata.name)
        return secrets

    def read_namespaced_secret(self, name):
        return self.api.read_namespaced_secret(name, self.namespace)

    def create_namespaced_secret(self, name, data):
        self.api.create_namespaced_secret(self.namespace, client.V1Secret(
            api_version="v1",
            kind="Secret",
            metadata=client.V1ObjectMeta(name=name),
            data=data,
            type="Opaque"
        ))

    def replace_namespaced_secret(self, name, data):
        self.api.replace_namespaced_secret(name, self.namespace, client.V1Secret(
            api_version="v1",
            kind="Secret",
            metadata=client.V1ObjectMeta(name=name),
            data=data,
            type="Opaque"
        ))

    def delete_namespaced_secret(self, name):
        self.api.delete_namespaced_secret(name, self.namespace, client.V1DeleteOptions())

    def exist_namespaced_secret(self, name):
        secrets = self.list_namespaced_secret()
        if name in secrets:
            return True

        return False
