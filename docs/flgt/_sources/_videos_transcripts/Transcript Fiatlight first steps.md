# Fiatlight - First steps

[00:00:00]   In this introduction to Fiatlight, we'll explore how to create a simple GUI for functions, how Fiatlight saves application state, and how to customize the GUI for your needs. By the end of this video, you will have a solid understanding of how to use Fiatlight to build interactive applications. 


## [00:00:18] Create a GUI for simple functions

[00:00:18]   Let's see how to create a simple GUI for functions. 

[00:00:22] We'll start with a basic function that adds two integers. In order to create a GUI for it, we simply import fiatlight, then run the function via fiatlight! 

[00:00:33] We can then interactively play with our function: we can enter input parameters, and see the output result.

[00:00:40] Widgets are generated automatically depending on the parameters type. For this dummy function - which accepts parameters of type string, integer, boolean, and enum - we will have a text input, an integer or float entry widget, two checkboxes - where the second handles our optional boolean parameter, and a combo box for the enum. 


## [00:01:02] How to compose functions (example with an image widget)

[00:01:02] Let's see how we can compose functions with fiatlight.

[00:01:06] In this example, we will compose two simple image processing functions: "read image", and "detect edges", using the Canny algorithm.

[00:01:16] Note that we are using two types from fiatlight: ImagePath, and "Image RGB" which are synonyms for a string and a numpy array respectively.

[00:01:26] ImagePath will be presented in the GUI as a file selector, and "Image RGB" will be presented with a widget to display the image.

[00:01:36] Then we use "fiatlight run" to run the application, passing the two functions as a list: the output of the first function will be passed as input to the second function (for its first parameter). 

[00:01:49] When we run the application, we get a GUI with two nodes: "read image" and "detect edges".

[00:01:56] We can see that the output of the first node is connected to the input of the second node.

[00:02:02] We can select an image file in the first node: we click on "\+", then we select our image file.

[00:02:09] After we selected our image, we can see it in the first node's output, and the detected edges in the second node's output.

[00:02:18] You can then adjust the parameters of the "detect edges" node to see how it affects the output.

[00:02:24] These images widgets can be resized, zoomed and panned, in a synchronized way.

[00:02:30] With high zoom, you can see the pixel values.

[00:02:33] You can also save the images, or send them to an "inspector" tab for further analysis. 


## [00:02:40] Fiatlight command line utility

[00:02:40] Fiatlight is provided with a command line utility. 

[00:02:43] Simply run "fiatlight" in a console to use it.

[00:02:47] It provides three different modes, which we will cover in this video: "types", "gui", and "fn attrs"

[00:02:55] With "fiatlight types", you can list all supported types and their corresponding GUI.

[00:03:01] With "fiatlight types path", you can filter types related to "path". There we can see the "Image Path" which we previously used, and which provides a file picker dialog for selecting image files.


## [00:03:15] Customize the GUI using fiat attributes

[00:03:15] Let's see how we can customize the GUI using fiat attributes.

[00:03:20] Here, we continue from the previous image example.

[00:03:23] Going back to the fiatlight command line interface, we can see that we can get info on how to customize the GUI for float parameters, by typing: "fiatlight gui float"

[00:03:36] There, we can see customization options such as "range", "edit type", "slider logarithmic", "label", "tooltip", etc.

[00:03:45] We will use some of these options to customize the GUI for the "detect edges" function:

[00:03:51] For this, we will use the "add fiat attributes" function which enables us to add customizations to the GUI for an existing function. 

[00:04:00] To customize the GUI for a function parameter, we use the following naming convention: parameter name followed by two underscores, followed by the attribute name.

[00:04:11] Here, we will customize the "low threshold" and "high threshold" parameters of the "detect edges" function.

[00:04:19] Then, going back to the fiatlight command line interface, we can see that we can get info on how to customize the GUI at a function level, by typing: "fiatlight fn attrs".

[00:04:31] There, we can see customization options such as "label", "invoke async", etc.

[00:04:37] Let's add a label to our function, by simply adding "label" as an argument to "add fiat attributes".

[00:04:45] Let's now add a label to the "read image" function.

[00:04:49] This time, instead of using "add fiat attributes", we will use the decorator named "with fiat attributes" to add the label directly to the function definition. This is shorter, but more intrusive as it modifies the function definition itself.

[00:05:05] Then, we can see that our GUI is updated with our customizations: our functions labels are applied, and the two thresholds are now sliders with logarithmic scale and a range from 0 to 5000.


## [00:05:19] Handle long computation times

[00:05:19] Let's see how fiatlight can handle functions which take more time to execute.

[00:05:24] First, we will add a delay in the "detect edges" function, to simulate a long processing time.

[00:05:31] Then using the command line "fiatlight fn attrs" we can see that "invoke async" enables to run the function in a separate thread, so that the GUI remains responsive.

[00:05:43] We may also set "invoke manually" to avoid running the function automatically when an input changes (this is completely up to you, depending on your use case).

[00:05:54] So, we will add these two attributes to our "detect edges" function: "invoke async" and "invoke manually".

[00:06:03] Then, in the user interface, we can see that when we change a parameter, the function is not invoked automatically.

[00:06:11] Instead we have to click on a button near the label "Refresh needed" to invoke the function. While the function is running, the user interface remains responsive, and you can see a spinning icon in the top right corner of the node.


## [00:06:25] How Fiatlight saves the application state

[00:06:25] Let's see how fiatlight saves the application state.

[00:06:29] Each time you exit the application, the current state is saved. This includes the values of all parameters, the positions and status of all functions nodes in the graph, the size and location of the application window.

[00:06:44] Let's demonstrate this by changing some parameter values and moving some function nodes around. Then, let's quit the application.

[00:06:53] When you restart the application, the previous state is automatically restored. This allows you to pick up right where you left off!

[00:07:01] The settings are saved in a folder named "fiat\_settings" in the current working directory : by default, they will use the name of the python script that was used to start the application. 

[00:07:13] You can also specify a custom name: the "app name" parameter of the "run" function will also be used for the settings file.

[00:07:22] You can also manually save the current state at any time using the "File Save" menu. 

[00:07:29] Later you can reload this saved state using the "File Load" menu. With only two functions plus a call to "fiatlight run", we could create a complete application, including customized GUI, and save/load functionality!

