import unittest
from redis import RedisManager

class TestRedisManager(unittest.TestCase):

    def setUp(self):
        self.redis_manager = RedisManager({"namespace": "platform-enablement"})

    def test_yaml_reader(self):
        self.assertEqual(self.redis_manager.yaml_reader()['AZMode'], 'single-az')
        self.assertEqual(self.redis_manager.yaml_reader()['Engine'], 'redis')
        self.assertEqual(self.redis_manager.yaml_reader()['EngineVersion'], '3.2.10')

    def test_self_config(self):
        self.assertEqual(self.redis_manager.config['namespace'], 'platform-enablement')
        self.assertEqual(self.redis_manager.config['Engine'], 'redis')
        self.assertEqual(self.redis_manager.config['EngineVersion'], '3.2.10')
