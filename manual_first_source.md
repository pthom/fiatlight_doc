First steps
===========

Running a single function
-------------------------

It is extremely simple to run and test a function with FiatLight.
Below is a function that accepts a text path as a parameter and outputs the number of words in this text file.

```python
import fiatlight as fl
# Note: TextPath is a synonym for str
#       Within fiatlight, it is associated with a file dialog widget
from fiatlight.fiat_types import TextPath

def count_words(filename: TextPath) -> int:
    """Count the number of words in a text file."""
    with open(filename, "r") as f:
        text = f.read()
    return len(text.split())

# Run the application
fl.run(count_words, app_name="Count Words")
```


Composing two functions
-----------------------

Below we create a simple application with two functions: "int_source" and "add":

* "int_source" generates an integer value
* "add" adds two or three integer values.

We use the "@fl.with_fiat_attributes" decorator to specify the range of values for the input parameters of the functions.

Finally, we run the application using the "fl.run" function.

**Code**

```python
import fiatlight as fl


# Define int_source, using a decorator to specify the range of values for "x"
@fl.with_fiat_attributes(x__range=(0, 100))
def int_source(x: int) -> int:
    """int_source is the first function of the application
    Since it is not linked to any other function, fiatlight will ask
    the user to specify the value of "x".
    As such, it serves as a source for the next function.
    """
    return x


# Define add, using a decorator to specify the range of values for "a" and "b"
@fl.with_fiat_attributes(a__range=(0, 10), b__range=(0, 20))
def add(a: int, b: int = 0, c: int | None = None) -> int:
    """add is the second function of the application
    It adds the values of "a", "b", and "c" and returns the result.

    In the interface:
    - "a" is linked to the output of int_source and is unspecified
       until "x" is specified in int_source.
    - "b" is equal to its default value (0). It is shown in gray to
       indicate that it is using the default value.
    - "c" is an optional, equal to its default value (None). It is also shown in gray.
      In order to specify a value for "c", the user must first click on the
      "Set" button, to specify that this optional has a value, and then specify the value.
    """
    if c is None:
        c = 0
    return a + b + c


# Run the application, which is a GUI around the composition of the two functions
# Notes:
#  - if running a single function, you can use fl.run(your_function)
#  - the app_name parameter is optional. It defines the name of the settings file, and the name of the window
fl.run([int_source, add], app_name="First Example")
```

*The image above shows the default state of the application*
> * int_source:
>   * "x" is unspecified
> * add:
>   * "a" is linked to the output of int_source and is unspecified, since int_source can not be executed (until "x" is specified)
>   * "b" is equal to its default value (0). It is shown in gray to indicate that it is using the default value.
>   * "c" is equal to its default value (None). It is also shown in gray.

Video Tutorial of the available controls
----------------------------------------

*The video below shows how to interact with the widgets in a function node*

<video controls>
  <source src="_static/videos/basic_manip.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

Save / Load user settings
-------------------------

**Automatic user settings saving**

Upon exit, Fiatlight automatically saves the user's settings in a folder named `fiat_settings` in the current directory.

The settings are named after the app_name param passed to `fl.run (if app_name is not set, the settings file will use the name of the main application module)

![settings_file.png](images/settings_file.png).


Three files are saved each time the application saves the settings:
* First_Example.ini: settings for Dear ImGui (since and positions of the window)
* First_Example.node_editor.json: settings for the node editor (positions of the nodes)
* First_Example.fiat_user.json: settings for the user (values of the parameters of the functions)

**Manually save the user settings**

When you manually save the user inputs by clicking on the buttons below,

 ![img.png](images/save_load_user_inputs.png)

only the user values are saved (in a file named "xxx.fiat_user.json", where "xxx" is the file name you selected).
