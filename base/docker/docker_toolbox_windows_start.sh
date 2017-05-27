#!/bin/bash

################################################################################
# Based on start.sh from C:\Program Files\Docker Toolbox
################################################################################

trap '[ "$?" -eq 0 ] || read -p "Error in step ´$STEP´. Press any key."' EXIT

################################################################################
# Confirm our Docker Machine and VirtualBox dependencies.
################################################################################

VM="${DOCKER_MACHINE_NAME-default}"
DOCKER_MACHINE="${DOCKER_TOOLBOX_INSTALL_PATH}/docker-machine.exe"

STEP="Looking for vboxmanage.exe"
if [ ! -z "$VBOX_MSI_INSTALL_PATH" ]; then
  VBOXMANAGE="${VBOX_MSI_INSTALL_PATH}VBoxManage.exe"
else
  VBOXMANAGE="${VBOX_INSTALL_PATH}VBoxManage.exe"
fi

if [ ! -f "${DOCKER_MACHINE}" ]; then
  echo "Docker Machine not found."
  exit 1
fi

if [ ! -f "${VBOXMANAGE}" ]; then
  echo "VirtualBox not found."
  exit 1
fi

################################################################################
# Check that our specific machine exists.
################################################################################

STEP="Checking if machine $VM exists"
"${VBOXMANAGE}" list vms | grep \""${VM}"\" &> /dev/null
VM_EXISTS_CODE=$?

set -e

if [ $VM_EXISTS_CODE -eq 1 ]; then
  "${DOCKER_MACHINE}" rm -f "${VM}" &> /dev/null || :
  rm -rf ~/.docker/machine/machines/"${VM}"
  #set proxy variables if they exists
  if [ -n ${HTTP_PROXY+x} ]; then
	PROXY_ENV="$PROXY_ENV --engine-env HTTP_PROXY=$HTTP_PROXY"
  fi
  if [ -n ${HTTPS_PROXY+x} ]; then
	PROXY_ENV="$PROXY_ENV --engine-env HTTPS_PROXY=$HTTPS_PROXY"
  fi
  if [ -n ${NO_PROXY+x} ]; then
	PROXY_ENV="$PROXY_ENV --engine-env NO_PROXY=$NO_PROXY"
  fi
  "${DOCKER_MACHINE}" create -d virtualbox $PROXY_ENV "${VM}"
fi

################################################################################
# Check that our specific machine is running.
################################################################################

STEP="Checking status on $VM"
VM_STATUS="$("${DOCKER_MACHINE}" status ${VM} 2>&1)"
if [ "${VM_STATUS}" != "Running" ]; then
  "${DOCKER_MACHINE}" start "${VM}"
  yes | "${DOCKER_MACHINE}" regenerate-certs "${VM}"
fi

################################################################################
# Configure the environment for our specific machine.
################################################################################

STEP="Setting env"
eval "$("${DOCKER_MACHINE}" env --shell=bash ${VM})"

################################################################################
# Run our command.
################################################################################

STEP="Finalize"
clear

BLUE='\033[1;34m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${BLUE}docker${NC} is configured to use the ${GREEN}${VM}${NC} machine with IP ${GREEN}$("${DOCKER_MACHINE}" ip ${VM})${NC}"
echo "For help getting started, check out the docs at https://docs.docker.com"
echo
cd

docker () {
  MSYS_NO_PATHCONV=1 "${DOCKER_TOOLBOX_INSTALL_PATH}/docker.exe" "$@"
}
export -f docker

if [ $# -eq 0 ]; then
  echo "Start interactive shell"
  exec "$BASH" --login -i
else
  echo "Start shell with command"
  exec "$BASH" -c "$*"
fi
