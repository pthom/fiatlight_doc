Installation
============

Installation from source
------------------------
```
%%bash

git clone https://github.com/pthom/fiatlight.git
cd fiatlight

# Optional: create a virtual environment
# (you can use whichever method you prefer)
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
pip install -v -e .
```

Install imgui-bundle (from the main branch)
-------------------------------------------

Fiatlight relies on imgui-bundle, and will depend on the latest version on the main branch (version 1.5.2 from pypi is not sufficient).

To install it, you can
- either clone it and install it from source: 

```bash
git clone https://github.com/pthom/imgui_bundle.git
cd imgui_bundle
git submodule update --init --recursive # (1)
pip install -v . # (2)
pip install opencv-python
pip install pyGLM
```

- or download pre-compiled recent wheels from here: https://github.com/pthom/imgui_bundle/actions/workflows/wheels.yml


Installation from PyPI
----------------------
```
# Not available yet
```

Install optional dependencies
-----------------------------

Several requirements files are provided, which you can install via `pip install -r requirements-<name>.txt`:

* requirements.txt: basic requirements
* requirements-ai.txt: requirements for AI demos
* requirements-audio.txt: requirements for audio demos
* requirements-dev.txt: requirements for development

Note: for AI demos, you will have to install torch manually, as its installation is dependent on your system configuration. 
See https://pytorch.org/get-started/locally/ (you will of course need a GPU to run the demos)
