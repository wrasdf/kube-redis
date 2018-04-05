import boto3

class RedisManager:

    def __init__(self):
        self.client = boto3.client('elasticache')

    def create_cache_cluster(self):
        response = self.client.create_cache_cluster(
            CacheClusterId='string',
            ReplicationGroupId='string',
            AZMode='single-az'|'cross-az',
            PreferredAvailabilityZone='string',
            PreferredAvailabilityZones=[
                'string',
            ],
            NumCacheNodes=123,
            CacheNodeType='string',
            Engine='string',
            EngineVersion='string',
            CacheParameterGroupName='string',
            CacheSubnetGroupName='string',
            CacheSecurityGroupNames=[
                'string',
            ],
            SecurityGroupIds=[
                'string',
            ],
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'namespace-redis'
                },
            ],
            SnapshotArns=[
                'string',
            ],
            SnapshotName='string',
            PreferredMaintenanceWindow='string',
            Port=123,
            NotificationTopicArn='string',
            AutoMinorVersionUpgrade=True|False,
            SnapshotRetentionLimit=123,
            SnapshotWindow='string',
            AuthToken='string'
        )
