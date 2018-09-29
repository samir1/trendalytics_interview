help:
	@cat Makefile

build:
	docker build -t trendalytics-interview .

run:
	docker run -it -d -p 80:5000 trendalytics-interview

