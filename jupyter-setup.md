# jupyter notebook setup

to run a jupyter noebook in vs code you need to

+ install jupyter notebook extension
+ create a venv
+ activate the venv
+ pip install ipykernel
+ install the venv with ipykernel
+ restart vscode
+ open notebook, select kernal, sectct python env and sellect your venv

```bash
python -m venv [evnname]
source [evnname]/bin/activate
# With your virtual environment activated, install the required packages:
pip install ipykernel 
python -m ipykernel install --user --name=[envname]_kernel --display-name "[envname]_kernel"
# ex: python -m ipykernel install --user --name=python3.12_kernel --display-name "Python 3.12_kernel"
```

+ Create a new Jupyter notebook:
  + You can do this by creating a new file with .ipynb extension
  + Or use the Command Palette (Ctrl+Shift+P) and select "Create New Blank Jupyter Notebook"
+ Select the kernel for your notebook:
  + Look for the "Select Kernel" button in the top right corner of your notebook
  + Choose your Python environment from the dropdown list
  + If your environment doesn't appear, you might need to refresh VS Code
+ Test your setup by creating a simple code cell:

```bash
print("Hello Jupyter!")
```
