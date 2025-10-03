Installation
============

At the moment, the recommended way to install fiatlight is from source:

```bash
git clone https://github.com/pthom/fiatlight.git
cd fiatlight

pip install -r requirements.txt
pip install -v -e .
```

Install optional dependencies
-----------------------------

Several requirements files are provided, which you can install via `pip install -r requirements-<name>.txt`:

* requirements.txt: basic requirements
* requirements-ai.txt: requirements for AI demos
* requirements-audio.txt: requirements for audio demos
* requirements-dev.txt: requirements for development

Note: for AI demos, you may have to install pytorch manually.
