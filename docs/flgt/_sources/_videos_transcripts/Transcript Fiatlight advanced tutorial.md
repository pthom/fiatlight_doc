# Fiatlight advanced tutorial

[00:00:00] In this tutorial, we will walk you through the process of creating an interactive application 

[00:00:06] 

[00:00:06] which allows you to visualize and compare the performance of various sorting algorithms.

[00:00:12] Thanks to Fiatlight, the GUI code is extremely concise and readable, focusing on the essential parts, making it easy to understand and maintain.

[00:00:23] The application starts with a function node that generates a list of random numbers. You can customize the number of values, the random seed, and the generation type, allowing for various initial conditions. Click on "Call Manually" to generate a list of numbers.

[00:00:42] This function output is redirected as an input to a series of functions. Each of these functions is a specific sorting algorithm. Thanks to Fiatlight, we can examine in real time the internal state of these functions and this way we can display their current status, even while they are running asynchronously in a separate thread. This allows you to visually compare their performance and behavior.

[00:01:09] You can control the speed of the sorting process using the latency control, which simulates different memory access speeds. As expected, bubble sort is the slowest, and the variations based on quicksort are often much faster.

[00:01:25] / Fiatlight goes beyond displaying Functions Graphs, and can also help you create full standalone applications, in which you can reuse its powerful GUI generation capabilities. The application you see now shows the same workflow, embedded in an application where you can fully customize the behavior and layout


## [00:01:46] Tutorial Outline

[00:01:46] First, let's summarize the different parts of this tutorial.

[00:01:50] In Part 1, we will cover how to create a GUI for a Pydantic BaseModel, set ranges for numeric widgets, and how to create functions that are invoked on demand.

[00:02:03] In Part 2, we'll dive into customizing the rendering of a function output, specifying widget sizes in DPI-independent units, and using ImPlot for high-performance plotting.

[00:02:15] Part 3 will focus on how to register a specific GUI for a given type.

[00:02:21] In Part 4, we'll explore advanced features like displaying a function's internal state, running functions asynchronously, and creating compositions of functions.

[00:02:33] Part 5 will teach you how to create custom function graphs, add "GUI Only" nodes, and documentation nodes to your graph. 

[00:02:42] Finally, in Part 6, we'll show you how to create a standalone app version of the sort visualization and manage application layouts using ImGui and dockable windows.


## [00:02:54] Intro - Ready-to-Use Sort Algorithms

[00:02:54] Before we dive into the content, let's quickly look at the sort algorithms and how the latency is handled.

[00:03:02] The code for this tutorial is located in "fiatlight/demos/tutorials/sort\_competition". "sort\_algorithms.py" " provides ready to use sort algorithms: bubble sort, quicksort, et cetera. 

[00:03:22] "numbers\_list.py" " provides a numbers list class which behaves like an integer array, but exposes a user settable latency for memory access and memory write.

[00:03:36] "numbers\_generator" provides a "NumbersGenerationOptions" class which describes how to generate a list of unordered numbers. It derives from pydantic's BaseModel : it behaves like a serializable dataclass. "make\_random\_number\_list" will generate the numbers that shall be sorted. ​


## [00:03:56] Part 1 - Add a GUI for the Numbers Generator

[00:03:56] Let's now add a user interface for the number generator. NumbersGenerationOptions" is a pydantic BaseModel. Let's try to use it and display it via Fiatlight: by default it cannot be edited, because we need to register it. we can do it by using "register base model" in our main script. Alternatively, we can place a decorator "base model with gui registration" on top of the class definition.

[00:04:25] In both cases, our data becomes editable with a nice GUI that reflects our class content. We can see the "edit" GUI in the function parameters, and the "present" GUI in its output.

[00:04:39] We can add "fiat attributes", to customize our user interface: here we set the labels, and ranges for the values, and select a knob widget for the seed. These attrributes are faithfully taken into account in the user interface. Refer to the tutorial "GUI for dataclasses and pydantic models" for more information. 

[00:05:01] We can now run "make random number list" via Fiatlight. As you can see, we have added two attributes to this function: "invoke manually" because we want to run it manually, and "invoke always dirty" because we want to be able to run it even if the inputs did not change. As you can see, the user interface works correctly and we have a button to call the function manually. 


## [00:05:29] Part 2 - Renders the numbers as bar chart

[00:05:29] Now, Let's use ImPlot to render our numbers as a bar chart. 

[00:05:33] ImPlot is a fast and capable plotting library. You can see here an extract of the kind of figures it can generate. 

[00:05:42] Let's see how we can change the appearance of the output of the function. First, we import imgui. Then, we wrap our function into a GUI and we override the "present" callback: this callback receives a data value and should display it. For the moment, it simply displays a string. Finally, we run the application, now using the wrapped function. And we can see that our string is correctly displayed.

[00:06:10] Let's now work on generating the chart. First we import the required libraries. The "draw\_bars" function will draw the bar chart. plot\_bar will plot our values. Each plot should be done between a call to "begin\_plot" and "end\_plot". Look at the definition for begin\_plot. As you can see, the documentation of the library is meticulously reproduced in the Python stub file. This is the case for all libraries inside Dear ImGui Bundle. 

[00:06:43] As you can read, "title\_id" must be unique to the current ImGui ID scope. This is typical within Dear ImGui, where each widget should have a unique ID (which is typically the label of the widget). If you need to avoid ID collisions or don't want to display a title in the plot, you can use double hashes. Alternatively you can change the ImGui ID scope using "push\_obj\_id", and then you can use the same ID for multiple widgets.

[00:07:13] Then, we ensure that the plotted values will always be fully visible, by setting the axis flags. Finally, we specify the plot size in EM units. 1 EM unit is the height of the font.

[00:07:29] Then we can use this function as our "present" callback, and see that we have a nice bar chart in the application. 


## [00:07:37] Part 3 - Register a GUI to display bar charts

[00:07:37] Fiatlight maintains a GUI registry which associates types to GUI classes.

[00:07:43] First, we create a new GUI class that inherits from "Any Data With Gui". Since we only want to change how it is rendered, it is enough to set its "present" callback. 

[00:07:55] Refer to the video "Fiatlight Architecture" to learn more about the possible callbacks and the numerous presentation options.

[00:08:04] Then, we tell Fiatlight to always present "Numbers List" with this new GUI. 

[00:08:10] And we are done! 

[00:08:12] Let's look at the application, and see that it shows our bar chart. 


## [00:08:17] Part 4 - Animate one sort function

[00:08:17] Next, let's add a wrapper function for the bubble sort algorithm that enables real-time visualization of the sorting process and measures the elapsed time. 

[00:08:28] We start by using the "with\_fiat\_attributes" decorator to add the "invoke\_async' attribute. This ensures that the function will be called asynchronously, allowing the GUI to update while the function runs.

[00:08:42] Inside the function, we start a timer to measure the elapsed time. We make a copy of the numbers to ensure the original set remains unmodified.

[00:08:53] To enable real-time visualization, we create an instance of NumbersListWithGui and assign the copied numbers to its value. This GUI will display the numbers being sorted.

[00:09:05] We add this GUI instance to the "fiat tuning" dictionary. Fiatlight will automatically display the content of this dictionary at each frame, even if the function is running asynchronously. Since the numbers are updated in the background, their evolution will be visible in the user interface!

[00:09:25] Finally, we call the bubble sort function, which sorts the copied numbers in place. We return the elapsed time to complete the function.

[00:09:35] Now, let's run the function composition with Fiatlight to visualize our sorting algorithm in action. 

[00:09:42] First, we need to ensure that the GUI updates as quickly as possible. We start by instantiating runner parameters for Fiatlight's FunctionsGraph.

[00:09:53] Next, we disable idling to make the animations smoother, even when the user is not interacting with the GUI.

[00:10:01] Finally, we run the composition of functions with Fiatlight. This includes our random number generator and the "bubble sort wrapper" function.

[00:10:12] And we have a nice looking user interface, where the numbers being sorted are updated in real time, and the total elapsed time is returned. 


## [00:10:22] Part 5 - Animate all the sorting functions 

[00:10:22] Now, let's extend our initial implementation to create a more comprehensive application that showcases multiple sorting algorithms within an interactive GUI. 

[00:10:33] First, we import additional sorting algorithms and necessary modules to support our enhanced functionality.

[00:10:42] We've added a descriptive docstring at the beginning of the script to explain the purpose of the application and the role of various nodes. This docstring will be displayed in our application, via a markdown renderer.

[00:10:56] Next, we introduce the "make sort function visualizer" function. This higher-order function wraps each sorting algorithm with the same principle as before, adding a Fiat tuning dictionary to visually track the current status of the numbers and return the elapsed time.

[00:11:15] It also makes sure to preserve the original function name and docstring, so that it can be displayed in the graph

[00:11:23] To control the latency of the sorting algorithms, we define the gui\_latency function. This function will be added to the graph as a GUI node, in other words a node that will display the widgets defined by this function. It provides a slider to set the latency and a button to abort or enable sorting. Note that it is needed to call "set next item width" before displaying a slider.

[00:11:50] To manage the execution of our functions, we create a FunctionsGraph. This will enable us to manually link functions in the graph.

[00:12:00] We add the "make random number list" function to the graph.

[00:12:04] Next, we add each sorting algorithm to the graph, linking them to the random numbers generator. This setup allows us to visualize and compare the performance of different sorting algorithms.

[00:12:18] We also add a GUI node to control the latency, and a documentation node to display the docstring of this script.

[00:12:27] Finally, we run the function graph.

[00:12:30] And our function graph application is complete. You can see that it works perfectly. As always withFiatlight, the user inputs and GUI options - nodes locations, etc. - are saved and restored between different executions.


## [00:12:44] Part 6 - Standalone application

[00:12:44] Fiatlight goes beyond displaying Functions Graphs, and can also help you create full standalone applications. In the application shown here, we reuse Fiatlight's powerful GUI to recreate the same workflow, but we are totally free to add any other components and to change the layout. 

