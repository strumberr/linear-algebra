LABORANTUM_PATH=$(pwd)/.laborantum
if [ -d "$LABORANTUM_PATH" ]; then
    echo -e "${RED}The folder '.laborantum' exists."
fi
echo $LABORANTUM_PATH
