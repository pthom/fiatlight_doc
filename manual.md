Manual
======

Begin with the [First steps](manual_first) section to learn how to wrap functions and dataclasses and run them via Fiatlight.

Then, explore the following sections.

### Introductory topics:
* [Add types to signatures](manual_function.ipynb#typed-signatures) so that Fiatlight can generate a GUI for your functions
* [Use fiatlight command line tool](manual_cli) to list all supported types and their possible GUI customization options
* [Customize widgets using fiat_attributes](manual_fiat_attributes)
* [Fully customize any parameter's GUI](manual_function.ipynb#handwriting-the-gui) by writing it by hand
* [Add GUI only nodes](manual_gui_node) to your functions graph (i.e. nodes that do not have a function associated with them)
* [Run functions asynchronously](manual_function.ipynb#controlling-function-execution)
* [Create GUI for structured data](manual_dataclass_models), i.e pydantic models and dataclasses

### Advanced topics:
* [Validate inputs in the GUI](manual_validation)
* [Reuse Fiatlight widgets](manual_reuse_widgets)  in your own apps, not only in Fiatlight's functions graphs.
* [Fully customize functions GUI](manual_function.ipynb#sub-class-functionwithgui)
 subclassing FunctionWithGui
* [Fine-tune functions](manual_tuning) by viewing their internal status. Debug and replay exceptions.
* [Create complex functions graph](manual_functions_graph)
* [Create and register custom widgets for specific types](manual_custom)


### Domain-specific topics:
Explore [fiat_kits](fiat_kits), collections of pre-built widgets for specific domains, such as:
* [fiat_image](fiat_image) for image processing
* [fiat_matplotlib](fiat_matplotlib) for plotting with Matplotlib
* [fiat_dataframe](fiat_dataframe): a widget to display explore pandas dataframes

TODO:
manual_reuse_widgets
