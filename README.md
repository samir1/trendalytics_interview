# Trendalytics Software Engineer Take Home Test
REST API built with [Flask](http://flask.pocoo.org/) that takes in an image as a request and returns a prediction of "Cat" or "Dog".

## Installation
1. Install nvidia driver
2. Install docker: `https://docs.docker.com/install/linux/docker-ce/ubuntu/`
3. Install nvidia-docker2: `https://gist.github.com/Brainiarc7/a8ab5f89494d053003454efc3be2d2ef`

## Build
`make build`

## Run
`make run`

The app will run at http://0.0.0.0:80.

## API Calls
```sh
$ curl -F "image=@cat.jpg" http://0.0.0.0/predict
{"label":"Cat","probability":0.0,"success":true}

$ curl -F "image=@dog.jpg" http://0.0.0.0/predict
{"label":"Dog","probability":0.9999780654907227,"success":true}
```

## Unit Tests
After running the container, test the API with `python test/test.py`.
