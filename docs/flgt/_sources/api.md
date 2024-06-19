API
===

fiat_core
---------

fiat_core is the foundational package of the fiatlight framework. It focuses on wrapping data and functions with GUI elements to facilitate interaction.

Its most important classes are:

* [`FunctionWithGui`](function_with_gui): Encapsulates a function, enriching it with a GUI based on inferred input and output types. It handles function invocation and manages internal states like exceptions and execution flags.
* [`AnyDataWithGui`](any_data_with_gui): Wraps any type of data with a GUI. This class manages the data value and its associated callbacks, and it provides methods to serialize/deserialize the data to/from JSON.
* [`AnyDataGuiCallbacks`](any_data_gui_callbacks): Stores callback functions for AnyDataWithGui, enhancing interactivity by allowing custom widgets and presentations.
* [`FunctionsGraph`](functions_graph): Represents a graph of functions, enabling the creation of complex workflows and data pipelines.


Gui Registry
------------

fiat_togui is a package that extends fiat_core by providing tools to register a Gui associated with a type. It allows users to define custom GUIs for specific data types.

See the doc for the [GUI Registry](fiat_togui) for more information.
