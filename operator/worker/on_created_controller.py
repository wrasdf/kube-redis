
from namespaced_configmap import NamespacedConfigMapManager
from redis import RedisManager

# Config Object:
# {
#     'clusterName': '',
#     'creationTimestamp': '2018-04-08T09:50:49Z',
#     'deletionGracePeriodSeconds': None,
#     'deletionTimestamp': None,
#     'name': 'test-redis',
#     'namespace': 'platform-enablement',
#     'resourceVersion': '6450229',
#     'selfLink': '/apis/myob.com/v1alpha1/namespaces/platform-enablement/redis/test-redis',
#     'uid': '51714b3d-3b12-11e8-99df-02b2b0b2e31e'
# }


class OnCreatedController:

    def __init__(self, config):
        self.config = config;
        self.cfg_name =  self.config['namespace'] + '-' + self.config['name']
        self.namespace = self.config['namespace']

        self.cfg_manager = NamespacedConfigMapManager(self.namespace)
        self.redis_manager = RedisManager({})
        self.event_handler()

    def event_handler(self):
        if not self.cfg_manager.exist_namespaced_config_map(self.cfg_name):
            # TODO update aws_redis info into configMap
            aws_redis = self.redis_manager.on_event_handler({"onCreated": "True"})
            self.cfg_manager.create_namespaced_config_map(self.cfg_name, {
                "python": "Awesome"
            })
