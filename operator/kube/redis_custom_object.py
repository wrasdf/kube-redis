from kubernetes import client, config, watch

class CustomObjectManager:

    def __init__(self):
        config.load_kube_config()
        self.coApi = client.CustomObjectsApi()
        self.redis_crd = {
            "group": "myob.com",
            "version": "v1alpha1",
            "plural": "redis"
        }

    # cluster based
    def redis_list_cluster_custom_object(self):
        return self.coApi.list_cluster_custom_object(
            self.redis_crd["group"],
            self.redis_crd["version"],
            self.redis_crd["plural"]
        )

    # namespace based
    def redis_list_namespaced_custom_object(self, namespace):
        return self.coApi.list_namespaced_custom_object(
            self.redis_crd["group"],
            self.redis_crd["version"],
            namespace,
            self.redis_crd["plural"]
        )

    def redis_create_namespaced_custom_object(self, namespace, body):
        return self.coApi.create_namespaced_custom_object(
            self.redis_crd["group"],
            self.redis_crd["version"],
            namespace,
            self.redis_crd["plural"],
            body
        )

    def redis_get_namespaced_custom_object(self, namespace, name):
        return self.coApi.get_namespaced_custom_object(
            self.redis_crd["group"],
            self.redis_crd["version"],
            namespace,
            self.redis_crd["plural"],
            name
        )

    def redis_replace_namespaced_custom_object(self, namespace, name, details):
        namespaced_custom_object = self.redis_get_namespaced_custom_object(namespace, name).copy()
        namespaced_custom_object.update(details)
        return self.coApi.replace_namespaced_custom_object(
            self.redis_crd["group"],
            self.redis_crd["version"],
            namespace,
            self.redis_crd["plural"],
            name,
            namespaced_custom_object
        )

    def redis_delete_namespaced_custom_object(self, namespace, name):
        return self.coApi.delete_namespaced_custom_object(
            self.redis_crd["group"],
            self.redis_crd["version"],
            namespace,
            self.redis_crd["plural"],
            name,
            client.V1DeleteOptions()
        )

    def redis_exist_namespaced_custom_object(self, namespace, name):
        cos = self.redis_list_namespaced_custom_object(namespace)["items"]
        cos_names = []

        for item in cos:
            cos_names.append(item["metadata"]["name"])

        if name in cos_names:
            return True

        return False

#
# {
#   'apiVersion': 'myob.com/v1alpha1',
#   'kind': 'Redis',
#   'metadata':{
#     'clusterName': '',
#     'creationTimestamp': '2018-04-07T12:27:12Z',
#     'deletionGracePeriodSeconds': None,
#     'deletionTimestamp': None,
#     'generation': 0,
#     'name': 'test-redis',
#     'namespace': 'platform-enablement',
#     'resourceVersion': '6189611',
#     'selfLink': '/apis/myob.com/v1alpha1/namespaces/platform-enablement/redis/test-redis',
#     'uid': 'ff884332-3a5e-11e8-99df-02b2b0b2e31e'
#   },
#   'spec': {'size': 'cache.t2.micro'},
#   'status': 'available'
# }

    def watch_cluster_custom_object(self, onCreated, onModifed, onDeleted):

        while True:
            stream = watch.Watch().stream(
                self.coApi.list_cluster_custom_object,
                self.redis_crd["group"],
                self.redis_crd["version"],
                self.redis_crd["plural"]
            )

            for event in stream:
                obj = event["object"]
                operation = event["type"]
                metadata = obj.get("metadata")

                if not metadata:
                    continue

                # ADDED
                if operation == "ADDED":
                    onCreated(metadata)

                # Modifed
                if operation == "MODIFIED":
                    onModifed(metadata)

                # DELETED
                if operation == "DELETED":
                    onDeleted(metadata)
