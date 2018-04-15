# kube-redis
Kubernetes redis


## Redis running inside docker

```
make -f Makefile-redis docker-run
make -f Makefile-redis docker-local
make -f Makefile-redis compose-run
```
This will stand up the application on port 8081.


### Reference:
- https://docs.giantswarm.io/guides/using-persistent-volumes-on-baremetal/
