#!/bin/bash

# Colors for echo statements
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to open VS Code in a new window with the current folder
open_vs_code() {
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

# Function to close the current VS Code window
close_vs_code() {
    echo -e "${YELLOW}Closing current VS Code window...${NC}"
    # Get the process ID of the current VS Code instance
    VSCODE_PID=$(ps aux | grep '[c]ode ./' | awk '{print $2}')
    if [ -n "$VSCODE_PID" ]; then
        kill -9 "$VSCODE_PID"
        echo -e "${GREEN}VS Code window closed successfully.${NC}"
    else
        echo -e "${RED}No VS Code window found to close.${NC}"
    fi
}

# Activate virtual environment and set ENV_LOADED flag
ENV_LOADED=false
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    source .laborantum_virtual_environment/bin/activate && ENV_LOADED=true
elif [[ "$OSTYPE" == "darwin"* ]]; then
    source .laborantum_virtual_environment/bin/activate && ENV_LOADED=true
elif [[ "$OSTYPE" == "msys" ]]; then
    source .laborantum_virtual_environment\\\\Scripts\\\\activate && ENV_LOADED=true
fi

# Check if in a virtual environment
if [[ "$ENV_LOADED" == true ]]; then
    echo -e "${GREEN}You are in a virtual environment.${NC}"
    close_vs_code
    # Wait a moment to ensure the VS Code window has closed
    sleep 2
    open_vs_code
else
    echo -e "${RED}You are not in a virtual environment. Please activate your virtual environment and try again.${NC}"
    exit 1
fi
