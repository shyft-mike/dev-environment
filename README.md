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
2. Install VSCode
3. In VSCode, install the Remote Development extension
4. In your terminal, run
```
sh start.sh
```
5. In VSCode, press F1 to bring up the command window and select "attach to running container..."
6. Select dev-env-1 to open your dev container
7. Install the Python extension
8. Select the Python 3.7 interpreter
9. To start Streamlit, run
```
sh start_streamlit.sh
```
10. To start jupyter, run
```
sh start_jupyter.sh
```