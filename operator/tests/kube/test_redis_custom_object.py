import unittest
from redis_custom_object import CustomObjectManager

class TestCustomObjectManager(unittest.TestCase):

    def setUp(self):
        self.co_manager = CustomObjectManager()
        self.namespace = "platform-enablement"
        self.co_name = "test-redis"
        self.co_test_details = {
            "apiVersion": "myob.com/v1alpha1",
            "kind": "Redis",
            "metadata": {
                "name": self.co_name
            },
            "spec":{
                "size": "cache.t2.micro"
            }
        }

    def test_redis_namespaced_custom_object(self):
        self.assertFalse(self.co_manager.redis_exist_namespaced_custom_object(self.namespace, self.co_name))
        self.co_manager.redis_create_namespaced_custom_object(self.namespace, self.co_test_details)

        self.assertTrue(self.co_manager.redis_exist_namespaced_custom_object(self.namespace, self.co_name))
        self.assertEqual(
            self.co_manager.redis_get_namespaced_custom_object(self.namespace, self.co_name)["apiVersion"],
            self.co_test_details["apiVersion"]
        )
        self.assertEqual(
            self.co_manager.redis_get_namespaced_custom_object(self.namespace, self.co_name)["kind"],
            self.co_test_details["kind"]
        )

    def tearDown(self):
        self.co_manager.redis_delete_namespaced_custom_object(self.namespace, self.co_name)
