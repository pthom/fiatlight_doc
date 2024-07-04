Run the demos
=============

**Install optional dependencies**

In order to run the demos, you may need to install per domain dependencies:

* For AI demos: `pip install -r requirements-ai.txt`
* For audio demos: `pip install -r requirements-audio.txt`

**Standard demos**

Several demos are available in the src/python/fiatlight/demos folder:

```bash
%%bash
tree -I "__pycache__|fiat_settings|priv_experiments|fonts|__init__.py" ../demos/ | grep -v directories
```

**Notebook demos**

You can also run all the demos that are present in the documentation (there are a lot of interesting demos, together with screenshots)

- install Jupyter: `pip install jupyter`
- Launch Jupyter with the following command: `jupyter lab`
- After Jupyter is launched, a browser page will open: navigate to the "src/python/fiatlight/doc" folder to find the demos.
