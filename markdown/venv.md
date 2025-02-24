# Virtual environment
* It is useful to use virtual environment, because necessary libraries depends on each project so usually no need to have many libraries just to use that project.
* Virtual environment enables installing libraries ONLY to that project.
* There are many ways to control the virtual environment. Here we use `pyenv` and `venv` to do this.
* Other tools are `poetry`, `rye`, and `anaconda/miniconda`. `poetry` is rather complicated for beginers, and `rye` is still not very popular among the community. Libraries installed in `anaconda` is tend to be old. Thus I introduce `pyenv` and `venv` but other tools are also welcomed.

## Usage
### Mac
#### pyenv
1. `brew install pyenv`
2. Write following to `~/.bashrc`
  ```bash
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  if command -v pyenv 1>/dev/null 2>&1; then
    eval "$(pyenv init -)"
  fi
  ```
3. `source ~/.bashrc`
4. `pyenv instal --list`: see what version is available
4. `pyenv install 3.X.X` (your favorite version)
5. `pyenv global 3.X.X`

#### Using venv
* Setup: `python -m venv venv`
* Activate: `source ./venv/bin/activate`
* Install libraries: `pip install numpy`
* Deactivate: `deactivate`

#### VSCode
* 拡張機能 -> install Python
* open python file and can see interpreter and virtual environement in the status bar

### Note
* Please DO NOT include `.venv` in the Git repository: add `.venv` in `.gitignore`, like
  ```bash
  .venv
  ```
* Instead, please make `requirements.txt` (under virtual environment), and add this to Git: `(.venv) $ pip freeze >  requirements.txt`
* This file can be used as `pip install -r requirements.txt`.
