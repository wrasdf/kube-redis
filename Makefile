.PHONY: build sh

dcr := docker-compose run --rm

%-red: env := dev-red

build:
	docker build -t kube-redis:latest .

sh: build
	docker run --rm -it -v $$(pwd):/app -v $(HOME)/.kube:/root/.kube -v $(HOME)/.aws:/root/.aws kube-redis:latest /bin/bash

clean:
	$(dcr) kt clean

deploy-%: clean
	$(dcr) kt validate -e $(env)
	$(dcr) kt deploy -e $(env)
