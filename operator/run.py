from kube.redis_custom_object import CustomObjectManager
from worker.on_created_controller import OnCreatedController
from worker.on_modified_controller import OnModifiedController
from worker.on_deleted_controller import OnDeletedController

co_manager = CustomObjectManager()
co_manager.watch_cluster_custom_object(
    OnCreatedController,
    OnModifiedController,
    OnDeletedController
)
