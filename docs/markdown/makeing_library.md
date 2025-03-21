# Making a custom Python library
* In this section, we will make a Python library. We will put your library to GitHub, and install it by `pip`.
* We take a simple example; the library that doubles your input value that can be used like
  ```python
  from my_library.double import double

  a = 1.0
  a2 = double(a)
  print(f"a = {a}, ax2 = {a2}")  # -> 1.0, 2.0
  ```

## 1. Create a GitHub Repository
* Go to GitHub and create a new public repository.
* Then get the URL to your repository by clicking "Code" -> "HTTPS", "Copy URL to clipboard".

<div align=center>
<img src="../figures/my_library.png" width=50%>
</div>

* Clone the repository locally:
```bash
git clone your_copied_url
cd my_library
```

## 2. Make code
* In your library, the directory structure should be like;

```
my_library/
├── my_library/
│   ├── __init__.py
│   └── double.py
├── setup.py
├── requirements.txt
└── README.md
```

* `__init__.py`: Here, this file can be empty.
* `module.py`: This contains the main functionality of your package. Here’s an example implementation:
  ```python
  def double(x):
      import numpy as np

      a = np.array(x)
      return float(a*2)
  ```
* `setup.py`: This contains the package information
  ```python
  from setuptools import setup, find_packages

  setup(
      name="my_library",
      version="0.1.0",
      packages=find_packages(),
      install_requires=[],
  )
  ```
* `requirements.txt`: This contains the libraries necessary for your package. In this case, only numpy is necessary. So the file becomes
  ```
  numpy
  ```

3. Add your package files and commit them:
  ```sh
  git add .
  git commit -m "Initial commit"
  git push origin main
  ```

## 3. Installing the Package via GitHub
* Once your package is pushed to GitHub, you can install it directly using `pip`.
* Go to the your repository on GitHub on the browser, and get the URL.
* Then download to your local PC with `pip`:
  ```sh
  pip install git+your_copied_url
  ```

## 4. Test your library
* After installing the package, you can use it as follows:
  ```python
  from my_library.double import double
  result = double(5)
  print(result)  # Output: 10
  ```

## Updating the Package
* You can update your code, upload to GitHub, and download via `pip`.
1. Edit your code
2. Then upload to the main branch: `git add; git commit -m "asdf"; git push`
3. Install again
  ```sh
  pip install git+your_repository_url
  ```
