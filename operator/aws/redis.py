import boto3
import yaml
import os

class RedisManager:

    def __init__(self, config):
        self.client = boto3.client('elasticache', region_name='ap-southeast-2')
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
        return client.create_cache_subnet_group(
            CacheSubnetGroupName=self.config.namespace + "-" +self.config.CacheSubnetGroupName,
            CacheSubnetGroupDescription=self.config.namespace + "-redis",
            SubnetIds=[
                'subnet-10460577',
                'subnet-2f324166'
            ]
        )


    def create_cache_cluster(self):
        response = self.client.create_cache_cluster(
            CacheClusterId=self.config.CacheClusterId,
            ReplicationGroupId=self.config.ReplicationGroupId,
            AZMode=self.config.AZMode,
            PreferredAvailabilityZone=self.config.PreferredAvailabilityZone,
            NumCacheNodes=self.config.NumCacheNodes,
            CacheNodeType=self.config.CacheNodeType,
            Engine=self.config.Engine,
            EngineVersion=self.config.EngineVersion,
            CacheSubnetGroupName=self.config.CacheSubnetGroupName,
            SecurityGroupIds=self.config.SecurityGroupIds,
            Port=6379,
            SnapshotRetentionLimit=5,
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'platform-enablement-redis'
                },
            ]
        )
