.PHONY: build sh test watch watch_in test_in

apply:
	@docker-compose run kubectl apply -f templates/redis-operator/crd.yaml

build:
	docker build -t kube-redis:latest .

sh: build
	docker run --rm -it -v $$(pwd):/app -v $(HOME)/.kube:/root/.kube -v $(HOME)/.aws:/root/.aws kube-redis:latest /bin/bash

test: build
	docker run --rm -it -v $$(pwd):/app -v $(HOME)/.kube:/root/.kube -v $(HOME)/.aws:/root/.aws kube-redis:latest make test_in

watch: build
	docker run --rm -it -v $$(pwd):/app -v $(HOME)/.kube:/root/.kube -v $(HOME)/.aws:/root/.aws kube-redis:latest python ./operator/run.py

watch_in:
	python ./operator/run.py

test_in:
	green ./operator/e2e-tests/kube
	green ./operator/e2e-tests/aws
	green ./operator/e2e-tests/worker
