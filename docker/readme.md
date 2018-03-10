
### Introduction Links

https://docs.docker.com/get-started/#test-docker-installation
https://docker-curriculum.com


#### Installation on Mac OS
https://docs.docker.com/docker-for-mac/install/

#### Installation on Ubuntu

```
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo apt-get update -y
sudo apt-get install software-properties-common -y
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
sudo apt-get update
sudo apt-get install dmsetup
sudo dmsetup mknodes
apt-cache policy docker-engine
sudo systemctl status docker
sudo apt-get install docker-engine -y
docker ps
```




#### Deploying nodejs with pure nodejs vs deploying with docker
* nodejs does not run in the background as a daemon
solution: use tools like pm2

* your need to install nodejs on all servers you want to deploy. installation may be tedious
solution: write an installation script

* the nodejs version in each server may be different
soultion: use nvm

#### Advantages of using docker
* Convenience: All you need is to install docker and pull images
* Customizable: You can create your own images with a Dockerfile
* Replicable: A container is isolated from the rest of the system. All images are versioned.
* Scalable: Docker Compose, Docker Swarm, Kubernetes.


#### Docker commands

```
docker run \
-w /apps/node \
node:latest \
pwd
```

`-w` `/container_directory`
Working directory is used to set the primary working directory of the container when the container starts


```
docker run \
-v /apps/notes/docker/node:/apps/node \
-w /apps/node \
node:latest \
ls
```
`-v` `/host_directory:/container_directory`
Volumes are used to share storage between the host and the container


```
docker run \
-v /apps/notes/docker/node:/apps/node \
-w /apps/node \
node:latest \
npm start
```

```
docker run \
-v /apps/notes/docker/node:/apps/node \
-w /apps/node \
-d \
node:latest \
npm start
```
`-d`
Run the docker container as a daemon.


#### List of running docker processes
```
docker ps
```
List of docker processed


#### Stoppping a container
```
docker stop ${container_id or container_name}
```
```
docker rm ${container_id or container_name}
```
or
```
docker rm -f ${container_id or container_name}
```

#### Naming docker containers
```
docker run \
-v /apps/notes/docker/node:/apps/node \
-w /apps/node \
-d \
--name my-node-server \
node:latest \
npm start
```

#### Restarting a docker server
```
docker restart my-node-server
```


#### Inspect what is inside docker
```
docker exec -it my-node-server bash
```
`-it` interactive mode
You are now inside the docker container! try to run:
`apt-get install curl -y`
`curl http://localhost:8080`


#### Binding container ports
```
docker run \
-v /apps/notes/docker/node:/apps/node \
-w /apps/node \
-d \
--name my-node-server \
-p 0.0.0.0:8080:8080 \
node:latest \
npm start
```
`-p` `host_port:contaier_port`



#### Automatic restart
```
docker run \
-v /apps/notes/docker/node:/apps/node \
-w /apps/node \
-d \
--name my-node-server \
-p 0.0.0.0:8080:8080 \
--restart always \
node:latest \
npm start
```
`--restart always` Always restarts the docker server

#### Environment variables
```
docker run \
-v /apps/notes/docker/node:/apps/node \
-w /apps/node \
-d \
--name my-node-server \
-p 0.0.0.0:8080:8080 \
--restart always \
-e NODE_ENV=dev \
--env-file /apps/env.list \
node:latest \
npm start
```

`-e` set an environment variable
`--env-file` set the path to a file with the environment variables


#### Access to docker logs
```
docker logs --tail 100 -f my-node-server
```
`--tail 100` log the last 100 lines
`-f` follow. print new logs as they are coming.


#### Pulling docker images from China
`docker pull registry.docker-cn.com/library/node:latest`












