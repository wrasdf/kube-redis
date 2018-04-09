import unittest
from namespaced_configmap import NamespacedConfigMapManager
from on_created_controller import OnCreatedController

class TestOnCreatedController(unittest.TestCase):

    def setUp(self):
        self.namespace = "platform-enablement"
        self.co_name = "test-redis-on-created"

        # setup cfg_manager
        self.cfg_manager = NamespacedConfigMapManager(self.namespace)
        self.cfg_name = self.namespace + '-' + self.co_name

        # clean env
        if self.cfg_manager.exist_namespaced_config_map(self.cfg_name):
            self.cfg_manager.delete_namespaced_config_map(self.cfg_name)

    def test_on_created_event_should_create_config_map(self):
        OnCreatedController({
            "name": self.co_name,
            "namespace": self.namespace
        })
        self.assertTrue(self.cfg_manager.exist_namespaced_config_map(self.cfg_name))
        self.assertEqual(self.cfg_manager.read_namespaced_config_map(self.cfg_name).metadata.name, self.cfg_name)

    def test_on_created_event_should_do_nothing(self):
        self.cfg_manager.create_namespaced_config_map(self.cfg_name, {"created": "already"})
        OnCreatedController({
            "name": self.co_name,
            "namespace": self.namespace
        })
        self.assertEqual(self.cfg_manager.read_namespaced_config_map(self.cfg_name).data, {"created": "already"})

    def tearDown(self):
        self.cfg_manager.delete_namespaced_config_map(self.cfg_name)
