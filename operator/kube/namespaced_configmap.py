from kubernetes import client, config

class NamespacedConfigMapManager:

    def __init__(self, namespace):
        config.load_kube_config()
        self.api = client.CoreV1Api()
        self.namespace = namespace

    def list_namespaced_configMaps(self):
        return self.api.list_namespaced_config_map(self.namespace)

    def read_namespaced_config_map(self, name):
        return self.api.read_namespaced_config_map(name, self.namespace)

    def create_namespaced_config_map(self, name, data):
        configmapTemplate = {
            "kind": "ConfigMap",
            "apiVersion": "v1",
            "metadata": {
                "name": name,
            },
            "data": data
        }
        self.api.create_namespaced_config_map(self.namespace, configmapTemplate)

    def delete_namespaced_config_map(self, name):
        return self.api.delete_namespaced_config_map(name, self.namespace, client.V1DeleteOptions())

    def replace_namespaced_config_map(self, name, data):
        namespaced_cfg_data = self.read_namespaced_config_map(name).data.copy()
        namespaced_cfg_data.update(data)
        configmapTemplate = {
            "kind": "ConfigMap",
            "apiVersion": "v1",
            "metadata": {
                "name": name,
            },
            "data": namespaced_cfg_data
        }
        return self.api.replace_namespaced_config_map(name, self.namespace, configmapTemplate)

    def exist_namespaced_config_map(self, name):
        cfg_names = []
        cfgs = self.list_namespaced_configMaps().items

        for item in cfgs:
            cfg_names.append(item.metadata.name)

        if name in cfg_names:
            return True

        return False
