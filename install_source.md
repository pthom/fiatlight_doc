Installation
============

The recommended way to install fiatlight is from source:

```bash
git clone https://github.com/pthom/fiatlight.git
cd fiatlight

pip install -r requirements.txt
pip install -v -e .
```

(fiatlight is also available on PyPI, but installing from source makes it easier to access the examples in src/python/fiatlight/demos).

Install optional dependencies
-----------------------------

Several requirements files are provided, which you can install via `pip install -r requirements-<name>.txt`:

* requirements.txt: basic requirements
* requirements-ai.txt: requirements for AI demos
* requirements-audio.txt: requirements for audio demos
* requirements-dev.txt: requirements for development

Note: for AI demos, you may have to install pytorch manually.
