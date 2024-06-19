Advanced Tutorials
==================

This documentation is full of advanced tutorials throughout the different pages. Below are some of the interesting tutorials you may find.

Before diving into those tutorials, it was advised to continue reading the rest of this page, notably to learn about the `fiatlight` command line utility.

**Creating a complex graph of functions**

Look at the page [FunctionsGraph](functions_graph.ipynb), where you will find several tutorials on the following topics:
* How to run an application in one line (when running a single function or a composition of functions)
* How to create a complex graph of functions, with custom connections between the functions

**Advanced customization of a function's Gui**

Look at the page [FunctionWithGui](function_with_gui.ipynb), where you will find many tutorials on the following topics:
* How to customize the GUI of the parameters: range, widget type, etc.
* How to control the function behavior (is it asynchronous, is it a real-time live function, etc.)
* How to create a function with an internal state (e.g., a counter, or a function that returns a live image from a camera)
* How to debug a function when it raised an exception, by replaying and debugging its execution with the exact same parameters
* How to use fiatlight to inspect the internal state of a function

**Customize the widgets for the parameters presentation and edition**

Look at the page [Gui Registry & Custom types](fiat_togui.ipynb), where you will find many tutorials on the following topics:
* How to use predefined bounded numeric types (Float_0_1, etc.)
* How to use file name types to get a Gui which provides file dialogs (for images, audio, text, etc.)
* How to display a widget specialized for color edition
* How to handle optional parameters
* How to handle lists
* How to automatically create a Gui for enum types
* How to automatically create a Gui for dataclasses
* How to automatically create a Gui for pydantic models
* How to create fully customized widgets for certain types (e.g. a sound player, a widget that displays a plot, a camera widget, etc.)
