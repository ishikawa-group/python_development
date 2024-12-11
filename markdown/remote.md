# Remote development guide
* Developing codes using remote development is advantageous in terms of computational resources, as you can execute the code with good CPU, GPU, Memories of remote server.
* Writing codes at your local computer is better than developing code at remote environment as you can use editors such as PyCharm or VSCode.
* Thus, setting up **remote development setting** in your editor is useful. This sections explains this technique.
* We focus on using PyCharm.

## Setup ssh connection
* Make ssh-key by `ssh-keygen`. For details, see other pages.

## Setup ssh connection in PyCharm
1. "Python interpreter" -> "New interpreter" -> "Add interpreter" then choose "SSH".
2. Add ssh information.
3. Remote environment is added to your Interpreter setting.
4. By making ssh connection to server, PyCharm copies codes in the project to some temporary place in the server (usually under `/tmp`).
5. Then `Run` will do execute the script on the server.

# References
* https://pleiades.io/help/pycharm/configuring-remote-interpreters-via-ssh.html
* https://qiita.com/himura-shitara/items/447af6baab0a33273b7d