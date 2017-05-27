#!/bin/bash

################################################################################
# Based on start.sh from C:\Program Files\Docker Toolbox
################################################################################

trap '[ "$?" -eq 0 ] || read -p "Error in step ´$STEP´. Press any key."' EXIT

################################################################################
# Name our virtual machine.
################################################################################

VM="${DOCKER_MACHINE_NAME-default}"

################################################################################
# Configure our Docker Machine dependency according to our OS.
################################################################################

if [[ "$OSTYPE" == "msys" ]]; then
  # Windows with lightweight shell and GNU utilities (part of MinGW)
  DOCKER_MACHINE="${DOCKER_TOOLBOX_INSTALL_PATH}/docker-machine.exe"
elif [[ "$OSTYPE" == "darwin"* ]]; then
  # Mac OSX
  DOCKER_MACHINE=/usr/local/bin/docker-machine
else
  echo "OSTYPE not recognized."
  exit 1
fi

################################################################################
# Confirm we found our Docker Machine dependency.
################################################################################

if [ ! -f "${DOCKER_MACHINE}" ]; then
  echo "Docker Machine not found."
  exit 1
fi

################################################################################
# Configure the environment for our specific machine.
################################################################################

STEP="Setting env"
eval "$("${DOCKER_MACHINE}" env --shell=bash ${VM})"

################################################################################
# Run our command.
################################################################################

if [[ "$OSTYPE" == "msys" ]]; then
  # Windows with lightweight shell and GNU utilities (part of MinGW)
  docker () {
    MSYS_NO_PATHCONV=1 "${DOCKER_TOOLBOX_INSTALL_PATH}/docker.exe" "$@"
  }
  export -f docker
fi

exec "$BASH" -c "$*"
