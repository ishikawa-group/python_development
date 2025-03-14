# Virtual environment
* If you are using some Python libraries, sometimes you want to use several versions for Python itself or Python libraries.
* This is because necessary Python libraries depends on each project.
* *Virtual environment* enables installing libraries ONLY to that project.
* There are many ways to control the virtual environment. Here we use `pyenv` and `venv` to do this.
* Other tools are `poetry`, `rye`, and `anaconda/miniconda`. `poetry` is rather complicated for beginers, and `rye` is still not very popular among the community. Libraries installed in `anaconda` is tend to be old. Thus I introduce `pyenv` and `venv` but other tools are also welcomed.

## pyenv
* `pyenv` is a Python version management tool.
1. Install `pyenv`.
  * Mac: `brew install pyenv`
  * Windows: `git clone https://github.com/pyenv/pyenv.git ~/.pyenv`
2. Write following to `~/.bashrc` (if you are using bash).
  ```bash
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  if command -v pyenv 1>/dev/null 2>&1; then
      eval "$(pyenv init -)"
  fi
  ```
3. `source ~/.bashrc`
4. `pyenv instal --list`: see what version is available
5. `pyenv install 3.X.X` (your favorite version)

### Usage
* Lists available version: `pyenv versions`
* Setting global Python (applies sysetm-wide): `pyenv global 3.X.X`
* Setting local Python (only applies to that directory
): `pyenv local 3.Y.Y`

## venv
* `venv` creates isolated Python environments for each project.
* Prevents library version conflicts between different projects.
* Allows installing libraries specific to each project.

### Usage
* Setup: `python -m venv .venv`
  - making setting directory to `./venv`.
* Activate: `source ./venv/bin/activate`
* Install libraries: `pip install numpy`
* Deactivate: `deactivate`

#### VSCode
* Extension(拡張機能) -> install Python
* open python file and can see interpreter and virtual environement in the status bar

### Note
* Please DO NOT include `.venv` in the Git repository. To do this, add `.venv` in `.gitignore`.
* Instead, please make `requirements.txt` (under virtual environment), and add this to Git: `(.venv) $ pip freeze >  requirements.txt`
* This file can be used as `pip install -r requirements.txt`.

## direnv
* When you are using `venv`, you need to do `source ./venv/bin/activate` at the beginning and you need to `deactivate` if you finish.
* To make these two steps automatic, you can use `direnv`.

### Install
1. Download direnv
  - (Mac) `brew install direnv`
  - (Windows, WSL) `sudo apt install direnv`
2. Edit `~/.bashrc` then add (when you're using `bash`)
```bash
export EDITOR=your_favorite_editor (e.g. vim)
eval "$(direnv hook bash)"
```
3. Go to your target directory and do `direnv edit .`
4. Add `source ./venv/bin/activate` to `.envrc`.

### Note
* Sometimes you need do `direnv allow`.