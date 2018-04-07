import unittest
from namespaced_secret import NamespacedSecretManager

class TestNamespacedSecretManager(unittest.TestCase):

    def setUp(self):
        self.namespace = 'platform-enablement'
        self.secret_name = 'test-secret-python'
        self.secret_manager = NamespacedSecretManager(self.namespace)

    def test_create_secret(self):
        self.assertEqual(self.secret_manager.exist_namespaced_secret(self.secret_name), False)
        self.secret_manager.create_namespaced_secret(self.secret_name, {
            "USER": "cGFzc1dvcmQxCg=="
        })
        self.assertEqual(self.secret_manager.exist_namespaced_secret(self.secret_name), True)
        self.assertEqual(self.secret_manager.read_namespaced_secret(self.secret_name).data['USER'], "cGFzc1dvcmQxCg==")

    def test_replace_secret(self):
        self.secret_manager.create_namespaced_secret(self.secret_name, {
            "USER": "cGFzc1dvcmQxCg=="
        })
        self.assertEqual(self.secret_manager.exist_namespaced_secret(self.secret_name), True)
        self.secret_manager.replace_namespaced_secret(self.secret_name, {
            "USER": "a2Vycnkud2FuZwo="
        })
        self.assertEqual(self.secret_manager.exist_namespaced_secret(self.secret_name), True)
        self.assertEqual(self.secret_manager.read_namespaced_secret(self.secret_name).data['USER'], "a2Vycnkud2FuZwo=")

    def tearDown(self):
        self.secret_manager.delete_namespaced_secret(self.secret_name)
