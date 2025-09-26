# Fiatlight architecture


## [00:00:00] Part 5 - Quick-look at the architecture of Fiatlight from 10,000 feet

[00:00:00] First, let's take a quick look at the architecture of Fiatlight.

[00:00:04] AnyDataWithGui can wrap any data type into a GUI, providing a lot of customizable callbacks.

[00:00:11] FunctionWithGui wraps a function into a GUI. It contains several instances of AnyDataWithGui, one for each input and output of the function.

[00:00:23] FunctionGraph represents a graph of functions. It contains multiple instances of FunctionWithGui, one for each function in the graph, with the corresponding connections between them.

[00:00:35] The fiat\_to\_gui module provides functions to register data types, associating them with a GUI. It contains a singleton where all the registered types are stored. The "register\_type" function is the main entry point to associate a new data type with its GUI.

[00:00:53] Primitive types - str, int, float, etc. - and enums are already registered by default. If a type is registered, its optional variant is also registered by default. As we saw before, dataclasses, Pydantic BaseModel, and tuple types are also handled nicely, provided their members are registered.

[00:01:16] Let's now take a look at AnyDataWithGui and its callbacks.

[00:01:20] AnyDataWithGui contains a value, which is an instance of the given DataType. However, it can also handle instances of Unspecified (if the user did not enter any value), Invalid (if validation failed), or Error.

[00:01:36] AnyDataGuiCallbacks provides numerous customizable callbacks. The most important ones are:

[00:01:43] " present" presents a value with a nice GUI.

[00:01:47] " edit" edits a value with a nice GUI, returning a bool indicating if the value was changed, along with the new value.

[00:01:56] Let's now look at the fiat\_kits module and the kit skeleton.

[00:02:00] fiat\_kits provides several submodules adapted to different domains. For example, fiat\_dataframe provides a GUI for pandas DataFrame, and fiat\_matplotlib provides a GUI for Matplotlib figures, etc.

[00:02:15] fiat\_kit\_skeleton is a template to help in the creation of new kits. In this skeleton, MyData is a simple example of a custom data type to be registered into Fiatlight. MyDataWithGui is A descendant of AnyDataWithGui that provides the GUI for MyData. It can implement several callbacks; and MyDataPresenter is an example of best practices for separating GUI handling from the implementation of AnyDataWithGui. MydataPossibleFiatAttributes is where you may want to add custom "fiat\_attributes". As mentioned before, MyData is registered into Fiatlight by calling register\_type

