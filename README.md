# Simple Docker Compose example script

The purpose of this docker-compose script is to highlight some basic networking issues with docker containers using the default bridged network setup across different operating systems: Windows, MacOS and Linux.

It contains a redis container and a simple python web frontend container with two endpoints:
* /hits - stores in memory (redis database) the number of hits
* /google - requests and returns external google endpoint

If all is working fine with the network configuration the docker container should be able to render the external www.google.com page and access the internal redis server to provide the number of hits. If not you will need to look at switching to --net=host based setup for external accesss.

## Run:
```
docker-compose up
```

## Test:

* http://localhost:5000/hits
* http://localhost:5000/google