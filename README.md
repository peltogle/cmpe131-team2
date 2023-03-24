## How to setup

- Install Python3: https://www.python.org/
- Install Virtualenv: `pip3 install virtualenv`
- Install Git: https://git-scm.com/
- Change active directory to Desktop folder: `cd Desktop`
- Clone repository: `git clone https://github.com/peltogle/cmpe131-team2.git`
- Change active directory to repository folder: `cd cmpe131-team2`
- Create your own branch: `git branch <your first name>`
- Switch to the branch you just made: `git checkout <your first name>`
- Activate Virtualenv:
  - Windows: `flask_folder\bin\activate.ps1`
  - MacOS/Linux: `source flask_folder/bin/activate`
- Install required packages: `pip3 install -r requirements.txt`
- Setup gitignore (download and put into the cmpe131-team2 folder):
  - Windows: https://github.com/github/gitignore/blob/main/Global/Windows.gitignore
  - MacOS: https://github.com/github/gitignore/blob/main/Global/macOS.gitignore


## Tips
- Run the server: `python3 flask_folder/app.py`
- Go to: http://127.0.0.1:5000
- To deactivate Virtualenv:
  - Any system: `deactivate`
  - VSCode users (one-time fix using settings): `"python.terminal.activateEnvironment": false`
- To turn off Flask server: `CTRL + C`
- To get the most recent code:
  - `git checkout main`
  - `git pull`
  - `git checkout <your first name>`

## Contribute to the repository
- To upload your code to github:
  - `git add .`
  - `git commit -m "<your message here>"`
  - `git push -u origin <your first name>`
- Create a pull request to the main branch and I will review your code and accept or deny the code


## Useful links
- Flask: https://www.tutorialspoint.com/flask/index.htm
- GitHub: https://education.github.com/git-cheat-sheet-education.pdf
- Flask: https://www.youtube.com/watch?v=Z1RJmh_OqeA
- GitHub: https://www.youtube.com/watch?v=RGOj5yH7evk

---

- We need to figure out the automated code testing part which the professor wants

---