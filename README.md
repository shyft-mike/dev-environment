# dev-environment
This is a basic python 3.7 dev environment.

# Features
- Formatting with black
- Linting with flake8
- Frontend with streamlit
- Jupyter lab

# TODO
- Refactor structure
- Add import sorting
- ?
# Getting Started
1. Install Docker Desktop
   - Version 19 worked for me
2. Install VSCode
1. In VSCode, install the [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension
2. In your terminal, run
```
sh build.sh # create local docker container
sh start.sh # start container
```
5. In VSCode, press F1 to bring up the command window and select "attach to running container..."
   * Or CTRL-Shift-P and type "Attach to running container"
6. Select dev-env-1 to open your dev container
7. Install the VSCode Python extension in the container (see window that opens from previous step)
8. Select the Python 3.7 interpreter in VSCode
   * CTRL-Shift-P and type "Python Interpreter", you should find it there
7. Install python packages (if necessary):
```
cd python
pip3 install -r requirements.txt
```
8.  To start Streamlit, on your docker container window run:
```
sh start_streamlit.sh
```
10. To start jupyter, run
```
sh start_jupyter.sh
```