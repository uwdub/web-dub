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
# Configure our Docker Machine and VirtualBox dependencies according to our OS.
################################################################################

if [[ "$OSTYPE" == "msys" ]]; then
  # Windows with lightweight shell and GNU utilities (part of MinGW)
  DOCKER_MACHINE="${DOCKER_TOOLBOX_INSTALL_PATH}/docker-machine.exe"

  STEP="Looking for vboxmanage.exe"
  if [ ! -z "$VBOX_MSI_INSTALL_PATH" ]; then
    VBOXMANAGE="${VBOX_MSI_INSTALL_PATH}VBoxManage.exe"
  else
    VBOXMANAGE="${VBOX_INSTALL_PATH}VBoxManage.exe"
  fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
  # Mac OSX
  DOCKER_MACHINE=/usr/local/bin/docker-machine

  VBOXMANAGE=/Applications/VirtualBox.app/Contents/MacOS/VBoxManage
else
  echo "OSTYPE not recognized."
  exit 1
fi

################################################################################
# Confirm we found our Docker Machine and VirtualBox dependencies.
################################################################################

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
