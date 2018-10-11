# theknow


## The know webbpage hasher

The know will run and download all .js file from the webpage.
The files will get a hashed name so that they have a uniq name.
And the file is hased.


This can be used to verify the confident of a webpage js files.
Run this script to verify that the js file on the webpage has not bean changes.


### Roadmap

- Save hash and file name to mongodb for storage (Done)
- Save a copy of the hash in redis for fast access (Done)
- Setup a timer and then timer is run check if has on live page matches the has in the db (Done)
- Setup for multi page setup (Done)



## How its used 

### Prereq

- docker
- docker-compose



### Edit the file docker-compose-yaml


In the file docker-compose.yaml set the site and sleep time 

```
    environment:
      - sites=www.elino.se,www.ollebo.com
      - sleep=3600

```

## Start the check


```
docker-compose up 
```





## Developer Guide

Edit the file and comment oup the command 


```
    command: tail -f /etc/fstab

```

Start docker compose


```
docker-compose up 
```

This will bring the stack up but will not start the hash

From a other shell run 


```
docker ps
```


You should se the following 

```
mahe@h:~/projects/theknow$ docker ps
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS               NAMES
7eb9424321d6        mongo                  "docker-entrypoint.s…"   6 minutes ago       Up 5 minutes        27017/tcp           theknow_mongo_1
94d1a6ed8176        mattiashem/know-site   "tail -f /etc/fstab"     3 days ago          Up 5 minutes        8080/tcp            theknow_api_1
b8d79f7b4a79        redis                  "docker-entrypoint.s…"   3 days ago          Up 5 minutes        6379/tcp            theknow_redis_1
```


Now run 

```
docker exec -it 94d1a6ed8176 /bin/bash
```


this will take you inside the docker contaner and now you can run the scan from in here


```
python getlinks.py
```


In the file getlinks.py you can set the domain to check.



