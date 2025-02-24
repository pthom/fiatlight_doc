# Comparisons w. other frameworks

Fiatlight integrates features from various tools into a unified, flexible framework for rapid prototyping and exploration.

Similar tools dedicated to rapid prototyping, exploration and visualization include:

- **[Scratch](https://scratch.mit.edu/)**: For visual graph creation.
- **[Jupyter](https://jupyter.org/)**: For interactive data exploration.
- **[Python Streamlit](https://streamlit.io/)** & **[Dash](https://plotly.com/dash/)**: For easy app creation with integrated GUI elements.
- **[Ryven](https://ryven.org/)**: For advanced graph creation.
- **[Unity Blueprints](https://docs.unrealengine.com/4.27/en-US/ProgrammingAndScripting/Blueprints/)**: For visual scripting and custom widgets.
- **[Comfy UI](https://github.com/comfyanonymous/ComfyUI)**: For AI workflow integration.

Compared to the aforementioned software frameworks, Fiatlight distinguishes itself by:

## **Pros**
- **Automatic GUI Generation** – Introspects functions & structured data to create interfaces.
- **Live Function State Visualization** – View intermediate values at any step.
- **Error Replay & Debugging** – Reproduce issues with the exact inputs that caused them.
- **State Persistence** – Save & restore multiple application states.
- **High-Performance Rendering** – Uses **Dear ImGui** with C++ and OpenGL for speed.
- **Runs Locally in the Browser** – Can be executed entirely **in-browser via Pyodide**, requiring **no server**.
- **Seamless Transition to Full Applications** – Prototypes can evolve into full **Dear ImGui** apps, with easy migration to C++.

## **Cons**
- **No Server-Side Computation** – Cannot rely on a remote server for **heavy computation** (e.g., large AI models like TensorFlow).

An extensive comparison of Fiatlight [with streamlit](comparison_streamlit.ipynb), [with dash](comparison_dash.ipynb), and [with ipywidgets](comparison_ipywidgets.ipynb) is available in the subsections.
