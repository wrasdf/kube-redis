# kube-redis
Kubernetes redis


## Redis running with local docker

```
make -f Makefile-redis docker-run
make -f Makefile-redis docker-local
make -f Makefile-redis compose-run
```
This will stand up the application on port 8081.


## Deploy into Kubernetes

```
$ make deploy-red
```


### Reference:
- https://docs.giantswarm.io/guides/using-persistent-volumes-on-baremetal/
- https://sanderp.nl/running-redis-cluster-on-kubernetes-e451bda76cad
