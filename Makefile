.PHONY: build sh

dcr := docker-compose run --rm

%-red: env := dev-red

build:
	docker build -t kube-redis:latest .

clean:
	$(dcr) kt clean

deploy-%: clean
	$(dcr) kt validate -e $(env)
	$(dcr) kt deploy -e $(env)
