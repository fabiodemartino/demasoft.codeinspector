# to dos

1. Remove duplication of conftest.py from each test folder


1. Executing tests
   1. make install
   2. make test
   3. make lint
      make format

# Execute tests
$ cd /c/source/repos/DemaSoftAI/autogen-code-inspector/backend/workflows
$ cd /c/source/repos/DemaSoftAI/autogen-code-inspector/
$ python -m pytest

# Clear cache
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force
Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
Get-ChildItem -Recurse -Include "__pycache__", "*.pyc" | Remove-Item -Recurse -Force

