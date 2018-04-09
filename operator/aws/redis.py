import boto3
import yaml
import os
import time

class RedisManager:

    def __init__(self, config):
        self.client = boto3.client('elasticache', region_name='ap-southeast-1')
        self.confg_merge(config)

    def yaml_reader(self):
        project_path = os.path.dirname(__file__)
        with open(os.path.join(project_path, 'default.yaml'), 'r') as stream:
            try:
                config = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return config

    def confg_merge(self, config):
        self.config = self.yaml_reader()
        for key in config:
            self.config[key] = config[key]

    def create_cache_subnet_group(self):
        self.config["CacheSubnetGroupName"] = self.config['namespace'] + "-" +self.config['name']
        self.config["CacheSubnetGroupDescription"] = self.config['namespace'] + "-redis",
        return self.client.create_cache_subnet_group(
            CacheSubnetGroupName=self.config["CacheSubnetGroupName"],
            CacheSubnetGroupDescription=self.config["CacheSubnetGroupDescription"],
            SubnetIds=self.config["SubnetIds"]
        )

    def on_event_handler(self, data):
        print('Be triggered from redis event ---> ', data)

    def create_cache_cluster(self):
        response = self.client.create_cache_cluster(
            CacheClusterId=self.config["CacheClusterId"],
            AZMode=self.config["AZMode"],
            PreferredAvailabilityZone=self.config["PreferredAvailabilityZone"],
            NumCacheNodes=self.config["NumCacheNodes"],
            CacheNodeType=self.config["CacheNodeType"],
            Engine=self.config["Engine"],
            EngineVersion=self.config["EngineVersion"],
            CacheSubnetGroupName=self.config["CacheSubnetGroupName"],
            SecurityGroupIds=self.config["SecurityGroupIds"],
            Port=self.config["Port"],
            Tags=[
                {
                    'Key': 'Name',
                    'Value': self.config["namespace"] + "-redis"
                },
            ]
        )

    def create_sanpshot(self):
        return self.client.create_snapshot(
            ReplicationGroupId=self.config["ReplicationGroupId"],
            CacheClusterId=self.config["CacheClusterId"],
            SnapshotName=self.config["name"] + "-snapshot-"+time.gmtime()
        )

    def describe_cache_clusters(self):
        # {
        #   'CacheClusters': [{
        #     'CacheClusterId': 'pe-cluster-id',
        #     'ClientDownloadLandingPage': 'https://console.aws.amazon.com/elasticache/home#client-download:',
        #     'CacheNodeType': 'cache.t2.micro',
        #     'Engine': 'redis',
        #     'EngineVersion': '3.2.10',
        #     'CacheClusterStatus': 'available',
        #     'NumCacheNodes': 1,
        #     'PreferredAvailabilityZone': 'ap-southeast-1a',
        #     'CacheClusterCreateTime': datetime.datetime(2018, 4, 9, 9, 41, 57, 793000, tzinfo=tzlocal()),
        #     'PreferredMaintenanceWindow': 'tue:19:30-tue:20:30',
        #     'PendingModifiedValues': {},
        #     'CacheSecurityGroups': [],
        #     'CacheParameterGroup': {
        #       'CacheParameterGroupName': 'default.redis3.2',
        #       'ParameterApplyStatus': 'in-sync',
        #       'CacheNodeIdsToReboot': []
        #     },
        #     'CacheSubnetGroupName': 'platform-enablement-test-elesticache-redis',
        #     'CacheNodes': [{
        #       'CacheNodeId': '0001',
        #       'CacheNodeStatus': 'available',
        #       'CacheNodeCreateTime': datetime.datetime(2018, 4, 9, 9, 41, 57, 793000, tzinfo=tzlocal()),
        #       'Endpoint': {
        #         'Address': 'pe-cluster-id.vtr1i7.0001.apse1.cache.amazonaws.com',
        #         'Port': 6379
        #       },
        #       'ParameterGroupStatus': 'in-sync',
        #       'CustomerAvailabilityZone': 'ap-southeast-1a'
        #       }],
        #     'AutoMinorVersionUpgrade': True,
        #     'SecurityGroups': [{
        #       'SecurityGroupId':
        #       'sg-232e995a', 'Status':
        #       'active'
        #     }],
        #     'AuthTokenEnabled':
        #     False,
        #     'TransitEncryptionEnabled': False,
        #     'AtRestEncryptionEnabled': False
        #   }],
        #   'ResponseMetadata': {
        #     'RequestId': '5a11df43-3bda-11e8-ac6b-673bf9b991e0',
        #     'HTTPStatusCode': 200,
        #     'HTTPHeaders': {
        #       'x-amzn-requestid':
        #       '5a11df43-3bda-11e8-ac6b-673bf9b991e0',
        #       'content-type': 'text/xml',
        #       'content-length': '2445',
        #       'date': 'Mon, 09 Apr 2018 09:42:43 GMT'},
        #       'RetryAttempts': 0
        #     }
        #   }

        return self.client.describe_cache_clusters(
            CacheClusterId=self.config["CacheClusterId"],
            MaxRecords=20,
            ShowCacheNodeInfo=True,
            ShowCacheClustersNotInReplicationGroups=True
        )

    def get_cache_cluster_status(self):
        for cluster in self.describe_cache_clusters()["CacheClusters"]:
            if cluster["CacheClusterId"] == self.config["CacheClusterId"]:
                return cluster

    def is_available(self):
        return self.get_cache_cluster_status()["CacheClusterStatus"] == "available"
