from redis_custom_object import CustomObjectManager

co_manager = CustomObjectManager()

co_name = "test-redis"
namespace = "platform-enablement"
co_details = {
    "apiVersion": "myob.com/v1alpha1",
    "kind": "Redis",
    "metadata": {
        "name": co_name
    },
    "spec":{
        "size": "cache.t2.micro"
    }
}
co_manager.redis_create_namespaced_custom_object(co_name, namespace, co_details)
