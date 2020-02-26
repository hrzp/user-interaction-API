# user-interaction-API

This is a simple flask(connexion) API that provides some functionality to upload and download files and set and get data.

### How to launch?

In Linux(Ubuntu):

```bash
git clone https://github.com/hrzp/user-interaction-API.git
cd user-interaction-API

# you need python 3.7
virtualenv -p python3.7 venv

source venv/bin/activate

pip install -e .
python app/server.py

```

Now open : [http://0.0.0.0:5000/api/ui](http://0.0.0.0:5000/api/ui)

API routes and descriptions are available in the above link

## Running Tests

```bash
# if your virtual environment not active
source venv/bin/activate

python tests/api_tests.py

# result should be like this
# ......
# ----------------------------------------------------------------------
# Ran 6 tests in 0.032s
#
# OK
```

