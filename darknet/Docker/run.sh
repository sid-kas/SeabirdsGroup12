
ROOT_DIR=$PWD/..
DATA_DIR="/home/grupp7/data"

nvidia-docker  run \
	-v $ROOT_DIR/src:/src \
	-v $DATA_DIR:/data \
	-it grupp7/seabird_opencv \
	bash



