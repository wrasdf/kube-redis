from kube.redis_custom_object import CustomObjectManager
from worker.event_hander import EventHander

co_manager = CustomObjectManager()
co_manager.watch_cluster_custom_object(
    EventHander.onCreated,
    EventHander.onDeleted,
    EventHander.onModifed
)
