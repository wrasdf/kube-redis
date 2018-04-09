
from namespaced_configmap import NamespacedConfigMapManager
from redis import RedisManager
from utility import UtilityManager

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

        self.utils = UtilityManager()

        self.cfg_manager = NamespacedConfigMapManager(self.namespace)
        self.redis_manager = RedisManager({
            "namespace": self.config["namespace"],
            "name": self.config["name"]
        })
        self.event_handler()

    def event_handler(self):

        if not self.cfg_manager.exist_namespaced_config_map(self.cfg_name):

            self.cfg_manager.create_namespaced_config_map(self.cfg_name, {})
            self.redis_manager.on_event_handler({"onCreated": "True"})
            # self.redis_manager.create_cache_cluster()

            # if self.utils.wait_until(self.redis_manager.is_available, 10*60, period=1):
            #     self.update_redis_config_map(self.cfg_name, self.redis_manager.get_cache_cluster_status()["CacheNodes"][0]["Endpoint"])

    def update_redis_config_map(self, name, data):
        self.cfg_manager.replace_namespaced_config_map(name, {
            "endpint": data["Address"]
        })
