Installation
============

Installation from source
------------------------
```
%%bash

git clone https://github.com/pthom/fiatlight.git --branch refact_io
cd fiatlight

# Optional: create a virtual environment
# (you can use whichever method you prefer)
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
pip install -v -e .
```

Installation from PyPI
----------------------
```
# To be done
```

Install optional dependencies
-----------------------------

Several requirements files are provided, which you can install via `pip install -r requirements-<name>.txt`:

* requirements.txt: basic requirements
* requirements-ai.txt: requirements for AI demos
* requirements-audio.txt: requirements for audio demos
* requirements-dev.txt: requirements for development

