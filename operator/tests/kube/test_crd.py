import unittest
from crd import CRDManager

class TestCRDManager(unittest.TestCase):

    def setUp(self):
        self.crd_manager = CRDManager()
        self.crd_name = "redisnew.myob.com"
        self.crd_test_details = {
            "api_version": "apiextensions.k8s.io/v1beta1",
            "kind": "CustomResourceDefinition",
            "metadata": {
                "name": self.crd_name
            },
            "spec": {
                "group": "myob.com",
                "version": "v1alpha1",
                "names":{
                    "kind": "RedisNew",
                    "listKind": "RedisNewList",
                    "plural": "redisnew"
                },
            "scope": "Namespaced"}}

    def test_custom_resource_definition(self):
        self.assertFalse(self.crd_manager.exist_custom_resource_definition(self.crd_name))
        self.crd_manager.create_custom_resource_definition(self.crd_test_details)
        self.assertTrue(self.crd_manager.exist_custom_resource_definition(self.crd_name))
        self.assertEqual(
            self.crd_manager.read_custom_resource_definition(self.crd_name).api_version,
            self.crd_test_details['api_version']
        )
        self.assertEqual(
            self.crd_manager.read_custom_resource_definition(self.crd_name).metadata.name,
            self.crd_name
        )

    def tearDown(self):
        self.crd_manager.delete_custom_resource_definition(self.crd_name)
