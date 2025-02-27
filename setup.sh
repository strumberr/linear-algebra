#!/bin/bash

# Function to show a spinner
show_spinner() {
    local pid=$!
    local delay=0.1
    local spinstr='|/-\'
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

# Colors for echo statements
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# first find the path of folder called .laborantum and save it to a variable
LABORANTUM_PATH=$(pwd)/.laborantum

# check if the folder exists
if [ -d "$LABORANTUM_PATH" ]; then
    echo -e "${RED}The folder '.laborantum' exists."
fi






# Update pip
echo -e "${YELLOW}Updating pip...${NC}"
python3 -m pip install --upgrade pip & show_spinner
wait $!
echo -e "${GREEN}done.${NC}"

# Install virtualenv if it's not already installed
echo -e "${YELLOW}Installing virtualenv...${NC}"
pip install virtualenv & show_spinner
wait $!
echo -e "${GREEN}done.${NC}"

# Create a virtual environment named 'venv'
echo -e "${YELLOW}Creating virtual environment 'laborantum_virtual_environment'...${NC}"

# get default python interpreter
PYTHON=$(which python3)

# create virtual environment
$PYTHON -m venv .laborantum_virtual_environment & show_spinner

# try with normal python
python -m venv .laborantum_virtual_environment & show_spinner

wait $!
echo -e "${GREEN}successfully created virtual environment.${NC}"

# activate virtual environment
# detect the os and activate the virtual environment
# Linux
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    source .laborantum_virtual_environment/bin/activate

    # give permission to run the script
    chmod +x ./run.sh

# MacOS
elif [[ "$OSTYPE" == "darwin"* ]]; then
    source .laborantum_virtual_environment/bin/activate

    # give permission to run the script
    chmod +x ./run.sh

# Windows
elif [[ "$OSTYPE" == "msys" ]]; then
    source .laborantum_virtual_environment\\\\Scripts\\\\activate
fi

# requirements variable not calling a file
REQUIREMENTS="""
anyio==4.4.0
appnope==0.1.4
argon2-cffi==23.1.0
argon2-cffi-bindings==21.2.0
arrow==1.3.0
asttokens==2.4.1
async-lru==2.0.4
attrs==23.2.0
Babel==2.15.0
beautifulsoup4==4.12.3
bleach==6.1.0
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
comm==0.2.2
contourpy==1.2.1
cycler==0.12.1
debugpy==1.8.1
decorator==5.1.1
defusedxml==0.7.1
executing==2.0.1
fastjsonschema==2.19.1
filelock==3.14.0
fonttools==4.52.4
fqdn==1.5.1
fsspec==2024.5.0
h11==0.14.0
httpcore==1.0.5
httpx==0.27.0
idna==3.7
ipykernel==6.29.4
ipython==8.24.0
ipywidgets==8.1.3
isoduration==20.11.0
jedi==0.19.1
Jinja2==3.1.4
json-tricks==3.17.3
json5==0.9.25
jsonpointer==2.4
jsonschema==4.22.0
jsonschema-specifications==2023.12.1
jupyter==1.0.0
jupyter-console==6.6.3
jupyter-events==0.10.0
jupyter-lsp==2.2.5
jupyter_client==8.6.2
jupyter_core==5.7.2
jupyter_server==2.14.0
jupyter_server_terminals==0.5.3
jupyterlab==4.2.1
jupyterlab_pygments==0.3.0
jupyterlab_server==2.27.2
jupyterlab_widgets==3.0.11
kiwisolver==1.4.5
MarkupSafe==2.1.5
matplotlib==3.9.0
matplotlib-inline==0.1.7
mistune==3.0.2
mpmath==1.3.0
nbclient==0.10.0
nbconvert==7.16.4
nbformat==5.10.4
nest-asyncio==1.6.0
networkx==3.3
notebook==7.2.0
notebook_shim==0.2.4
numpy==1.26.4
overrides==7.7.0
packaging==24.0
pandocfilters==1.5.1
parso==0.8.4
pexpect==4.9.0
pillow==10.3.0
platformdirs==4.2.2
prometheus_client==0.20.0
prompt_toolkit==3.0.45
psutil==5.9.8
ptyprocess==0.7.0
pure-eval==0.2.2
pycparser==2.22
Pygments==2.18.0
pyparsing==3.1.2
python-dateutil==2.9.0.post0
python-json-logger==2.0.7
PyYAML==6.0.1
pyzmq==26.0.3
qtconsole==5.5.2
QtPy==2.4.1
referencing==0.35.1
requests==2.32.3
rfc3339-validator==0.1.4
rfc3986-validator==0.1.1
rpds-py==0.18.1
Send2Trash==1.8.3
six==1.16.0
sniffio==1.3.1
soupsieve==2.5
stack-data==0.6.3
sympy==1.12.1
terminado==0.18.1
tinycss2==1.3.0
torch==2.3.0
tornado==6.4
traitlets==5.14.3
types-python-dateutil==2.9.0.20240316
typing_extensions==4.12.0
uri-template==1.3.0
urllib3==2.2.1
wcwidth==0.2.13
webcolors==1.13
webencodings==0.5.1
websocket-client==1.8.0
widgetsnbextension==4.0.11
"""

# install requirements
echo -e "${YELLOW}Installing requirements...${NC}"
pip install $REQUIREMENTS & show_spinner
wait $!
echo -e "${GREEN}done.${NC}"

echo -e "${BLUE}Virtual environment 'venv' created successfully. And all the requirements are installed.${NC}"


# Ask the user if they want to open VS Code
read -p "Do you wish to open VS Code? (yes/no) " response
if [[ "$response" == "yes" ]]; then
    # Run the second script in the same shell
    source ./run.sh
else
    echo -e "${YELLOW}Skipping opening VS Code.${NC}"
fi