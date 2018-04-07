# kube-redis
Kubernetes redis operator


## kube-redis local watch kube-redis resources
```
make watch
```

## kube-redis test
```
make test
```

## kube-redis debug mode
```
make sh
```

## kube-redis debug mode run test
```
make test_in
```

## Redis running inside docker

```
make -f Makefile-redis docker-run
make -f Makefile-redis docker-local
make -f Makefile-redis compose-run
```
This will stand up the application on port 8081.


### Reference:
- https://boto3.readthedocs.io/en/latest/reference/services/elasticache.html
- https://github.com/kubernetes-client/python/tree/master/kubernetes/docs
- https://blog.openshift.com/writing-custom-controller-python/
- https://github.com/kubernetes-client/python/tree/master/examples
- https://github.com/kubernetes-client/python/tree/master/kubernetes/e2e_test
