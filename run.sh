#!/bin/sh

USER_UID=$(id -u)
USER_GID=$(id -g)
name="seabird_docker_all"

nvidia-docker run \
	-it \
	--init \
    --runtime=nvidia \
	--volume=/home/:/home/:rw \
	--volume=/media/:/media/:rw \
	--env="USER_UID=${USER_UID}" \
	--env="USER_GID=${USER_GID}" \
	--env="USER=${USER}" \
	--env="HOME=${HOME}" \
	-p 6006:6006 \
	-p 8888:8888 \
	--cap-add SYS_ADMIN \
	--cap-add MKNOD \
	--device /dev/fuse \
	--security-opt apparmor:unconfined \
	--name "$name" \
    ufoym/deepo:all-jupyter-py36-cu100 bash
