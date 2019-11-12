# SeabirdsGroup12

## all in one docker image
https://github.com/ufoym/deepo

- *pull* : docker pull ufoym/deepo:all-jupyter-py36-cu100
- *run* : nvidia-docker run --runtime=nvidia --rm -it --init --volume=/home/:/home/:rw ufoym/deepo:all-jupyter-py36-cu100 bash


run new container: bash run.sh
continue the same container: bash continue.sh

autossh -M 0 -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3" -NL 0.0.0.0:9876:localhost:9876 grupp9@dgx.cgit.se

