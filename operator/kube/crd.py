from kubernetes import client, config

class CRDManager:

    def __init__(self):
        config.load_kube_config()
        self.api = client.ApiextensionsV1beta1Api()

    def list_custom_resource_definition(self):
        return self.api.list_custom_resource_definition()

    # crd_details = {
    #     "api_version": "apiextensions.k8s.io/v1beta1",
    #     "kind": "CustomResourceDefinition",
    #     "metadata": {
    #         "name": "redisnew.myob.com"
    #     },
    #     "spec": {
    #         "group": "myob.com",
    #         "version": "v1alpha1",
    #         "names":{
    #             "kind": "RedisNew",
    #             "listKind": "RedisNewList",
    #             "plural": "redisnew"
    #         },
    #     "scope": "Namespaced"}}

    def create_custom_resource_definition(self, crd_details):
        body = client.V1beta1CustomResourceDefinition(api_version=crd_details["api_version"], kind=crd_details["kind"], metadata=crd_details["metadata"], spec=crd_details["spec"])
        self.api.create_custom_resource_definition(body)

    def delete_custom_resource_definition(self, name):
        self.api.delete_custom_resource_definition(name, client.V1DeleteOptions())

    def read_custom_resource_definition(self, name):
        return self.api.read_custom_resource_definition(name)

    def exist_custom_resource_definition(self, name):
        crds_names = []
        crds = self.list_custom_resource_definition().items

        for item in crds:
            crds_names.append(item.metadata.name)

        if name in crds_names:
            return True

        return False
