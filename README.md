# Data analysis
- Document here the project: bdi_predict
- Description: Project Description
- Data Source:
- Type of analysis:

Please document the project the better you can.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for bdi_predict in github.com/{group}. If your project is not set please add it:

Create a new project on github.com/{group}/bdi_predict
Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "bdi_predict"
git remote add origin git@github.com:{group}/bdi_predict.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
bdi_predict-run
```

# Install

Go to `https://github.com/{group}/bdi_predict` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/bdi_predict.git
cd bdi_predict
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
bdi_predict-run
```
