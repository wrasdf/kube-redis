build:
	docker build -t kube-redis:latest .

sh: build
	docker run --rm -it -v $$(pwd):/app -v $(HOME)/.kube:/root/.kube -v $(HOME)/.aws:/root/.aws kube-redis:latest /bin/bash

test:
	docker run --rm -it -v $$(pwd):/app -v $(HOME)/.kube:/root/.kube -v $(HOME)/.aws:/root/.aws kube-redis:latest green ./operator/tests

test_in:
	green ./operator/tests/kube
