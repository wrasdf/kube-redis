import unittest
from namespaced_configmap import NamespacedConfigMapManager

class TestNamespacedSecretManager(unittest.TestCase):

    def setUp(self):
        self.namespace = 'platform-enablement'
        self.cfg_name = 'test-config-map'
        self.cfg_data = {"user": "kerry", "age": "18"}
        self.cfg_manager = NamespacedConfigMapManager(self.namespace)

    def test_create_namespaced_config_map(self):
        self.assertFalse(self.cfg_manager.exist_namespaced_config_map(self.cfg_name))
        self.cfg_manager.create_namespaced_config_map(self.cfg_name, self.cfg_data)
        self.assertTrue(self.cfg_manager.exist_namespaced_config_map(self.cfg_name))
        self.assertEqual(self.cfg_manager.read_namespaced_config_map(self.cfg_name).metadata.name, self.cfg_name)
        self.assertEqual(self.cfg_manager.read_namespaced_config_map(self.cfg_name).metadata.namespace, self.namespace)
        self.assertEqual(self.cfg_manager.read_namespaced_config_map(self.cfg_name).data, self.cfg_data)

    def test_replace_namespaced_config_map(self):
        self.cfg_manager.create_namespaced_config_map(self.cfg_name, self.cfg_data)
        self.cfg_manager.replace_namespaced_config_map(self.cfg_name, {
            "age": "90",
            "newKey": "value"
        })
        self.assertEqual(self.cfg_manager.read_namespaced_config_map(self.cfg_name).data, {
            "user": "kerry",
            "age": "90",
            "newKey": "value"
        })

    def tearDown(self):
        self.cfg_manager.delete_namespaced_config_map(self.cfg_name)
