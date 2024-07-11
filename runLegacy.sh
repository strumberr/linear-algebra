#!/bin/bash

# Colors for echo statements
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# failed load env variable 
ENV_LOADED=false

# activate virtual environment
# detect the os and activate the virtual environment
# Linux
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    source .laborantum_virtual_environment/bin/activate
    # if there is an error loading the environment variable
    if [[ $? -ne 0 ]]; then
        ENV_LOADED=false
    else
        ENV_LOADED=true
    fi

# MacOS
elif [[ "$OSTYPE" == "darwin"* ]]; then
    source .laborantum_virtual_environment/bin/activate
    # if there is an error loading the environment variable
    if [[ $? -ne 0 ]]; then
        ENV_LOADED=false
    else
        ENV_LOADED=true
    fi

# Windows
elif [[ "$OSTYPE" == "msys" ]]; then
    source .laborantum_virtual_environment\\\\Scripts\\\\activate
    # if there is an error loading the environment variable
    if [[ $? -ne 0 ]]; then
        ENV_LOADED=false
    else
        ENV_LOADED=true
    fi
fi


open_vs_code() {
    # Attempt to open VS Code
    echo -e "${YELLOW}Attempting to open VS Code...${NC}"
    if command -v code &> /dev/null; then
        code .
        echo -e "${GREEN}VS Code opened successfully.${NC}"
    else
        echo -e "${RED}The 'code' command is not available.${NC}"
        echo -e "${YELLOW}Please install the 'code' shell command from Visual Studio Code.${NC}"
        echo -e "${YELLOW}To do this, open Visual Studio Code, press ${BLUE}Command+Shift+P (macOS)${YELLOW} or ${BLUE}Ctrl+Shift+P (Windows/Linux)${YELLOW}, and type '${BLUE}Shell Command: Install 'code' command in PATH${YELLOW}'.${NC}"
        exit 1
    fi
}


# Check if in a virtual environment
if [[ "$ENV_LOADED" == true ]]; then
    echo -e "${GREEN}You are in a virtual environment.${NC}"

    # Attempt to open VS Code
    open_vs_code
else
    echo -e "${RED}You are not in a virtual environment. Please activate your virtual environment and try again.${NC}"
    exit 1
fi
