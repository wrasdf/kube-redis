import unittest
from namespaced_configmap import NamespacedConfigMapManager
from on_deleted_controller import OnDeletedController

class TestOnDeletedController(unittest.TestCase):

    def setUp(self):
        self.namespace = "platform-enablement"
        self.co_name = "test-redis-on-deleted"

        # setup cfg_manager
        self.cfg_manager = NamespacedConfigMapManager(self.namespace)
        self.cfg_name = self.namespace + '-' + self.co_name

        # clean env
        if self.cfg_manager.exist_namespaced_config_map(self.cfg_name):
            self.cfg_manager.delete_namespaced_config_map(self.cfg_name)

    def test_on_deleted_controller_should_throw_error(self):
        with self.assertRaisesRegexp(ValueError, self.cfg_name + ' Should exist'):
            OnDeletedController({
                "name": self.co_name,
                "namespace": self.namespace
            })

    def test_on_deleted_controller_should_delete_cfg(self):
        self.cfg_manager.create_namespaced_config_map(self.cfg_name, {"created": "already"})
        OnDeletedController({
            "name": self.co_name,
            "namespace": self.namespace
        })
        self.assertFalse(self.cfg_manager.exist_namespaced_config_map(self.cfg_name))
