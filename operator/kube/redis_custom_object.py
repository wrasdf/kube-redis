from kubernetes import client, config

class CustomObjectManager:

    def __init__(self):
        config.load_kube_config()
        self.api = client.CustomObjectsApi()
        self.redis_crd = {
            "group": "myob.com",
            "version": "v1alpha1",
            "plural": "redis"
        }

    # cluster based
    def redis_list_cluster_custom_object(self):
        return self.api.list_cluster_custom_object(self.redis_crd["group"], self.redis_crd["version"], self.redis_crd["plural"])

    # namespace based
    def redis_list_namespaced_custom_object(self, namespace):
        return self.api.list_namespaced_custom_object(self.redis_crd["group"], self.redis_crd["version"] ,namespace ,self.redis_crd["plural"])

    def redis_create_namespaced_custom_object(self, namespace, body):
        return self.api.create_namespaced_custom_object(self.redis_crd["group"], self.redis_crd["version"] ,namespace ,self.redis_crd["plural"], body)

    def redis_get_namespaced_custom_object(self, namespace, name):
        return self.api.get_namespaced_custom_object(self.redis_crd["group"], self.redis_crd["version"] ,namespace ,self.redis_crd["plural"], name)

    def redis_replace_namespaced_custom_object(self, namespace, name, details):
        namespaced_custom_object = self.redis_get_namespaced_custom_object(namespace, name).copy()
        namespaced_custom_object.update(details)
        return self.api.replace_namespaced_custom_object(self.redis_crd["group"], self.redis_crd["version"] ,namespace ,self.redis_crd["plural"], name, namespaced_custom_object)

    def redis_delete_namespaced_custom_object(self, namespace, name):
        return self.api.delete_namespaced_custom_object(self.redis_crd["group"], self.redis_crd["version"] ,namespace ,self.redis_crd["plural"], name, client.V1DeleteOptions())

    def redis_exist_namespaced_custom_object(self, namespace, name):
        cos = self.redis_list_namespaced_custom_object(namespace)["items"]
        cos_names = []

        for item in cos:
            cos_names.append(item["metadata"]["name"])

        if name in cos_names:
            return True

        return False
