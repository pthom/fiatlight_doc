Fiatlight command line utility
==============================


The `fiatlight` command line utility is a powerful tool that allows you to explore the available widgets and types in Fiatlight. It can be used to list the available types, to print the GUI info for a given type, and to run a GUI demo for a given type.

Here is the help message for the `fiatlight` command line utility (ignore the `%%bash` magic command, it is used to run bash commands in Jupyter notebooks):

```bash
%%bash
fiatlight --help
```

List registered types
---------------------

The `types` command lists the registered types in Fiatlight. You can filter the types by adding an optional query.

In the example below, we will run the `fiatlight types str` command to list all the types that contain the string "str".

```bash
%%bash
fiatlight types str
```

Notes:
- If you do not include the `str` argument, all the types will be printed.

Print the GUI info for a given type
-----------------------------------

The `gui_info` command prints the GUI info for a given type. You can specify the GUI type name or the data type name as an argument. If you do not provide a type name, all the GUI widget names will be printed.

### Example: Print the GUI info for StrWithGui

In the example below, we will run the `fiatlight gui_info StrWithGui` command to print the GUI info for the `StrWithGui` widget.

```bash
%%bash
fiatlight gui str
```

### Example: Print the GUI info for ImageWithGui

```bash
%%bash
fiatlight gui ImageWithGui
```


Annex: list of registered types
-------------------------------

By running the `fiatlight types` command, you can list all the registered types in Fiatlight. Here is a list of the available types:

```bash
%%bash
fiatlight types
```

