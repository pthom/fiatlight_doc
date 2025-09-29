# Fiatlight advanced tutorial

[00:00:00] In this tutorial, we will walk you through the process of creating an interactive application 

[00:00:06] which allows you to visualize and compare the performance of various sorting algorithms.

[00:00:12] Thanks to Fiatlight, the GUI code is extremely concise and readable, focusing on the essential parts, making it easy to understand and maintain.

[00:00:23] The application starts with a function node that generates a list of random numbers. You can customize the number of values, the random seed, and the generation type, allowing for various initial conditions. Click on "Call Manually" to generate a list of numbers.

[00:00:42] This function output is redirected as an input to a series of functions. Each of these functions is a specific sorting algorithm. Thanks to Fiatlight, we can examine in real time the internal state of these functions and this way we can display their current status, even while they are running asynchronously in a separate thread. This allows you to visually compare their performance and behavior.

[00:01:09] You can control the speed of the sorting process using the latency control, which simulates different memory access speeds. As expected, bubble sort is the slowest, and the variations based on quicksort are often much faster.


## [00:01:25] Tutorial Outline

[00:01:25] First, let's summarize the different parts of this tutorial.

[00:01:30] In Part 1, we will cover how to create a GUI for a Pydantic BaseModel, set ranges for numeric widgets, and how to create functions that are invoked on demand.

[00:01:42] In Part 2, we'll dive into customizing the rendering of a function output, specifying widget sizes in DPI-independent units, and using ImPlot for high-performance plotting.

[00:01:55] Part 3 will focus on how to register a specific GUI for a given type.

[00:02:01] In Part 4, we'll explore advanced features like displaying a function's internal state, running functions asynchronously, and creating compositions of functions.

[00:02:12] Part 5 will teach you how to create custom function graphs, add "GUI Only" nodes, and documentation nodes to your graph. 

[00:02:22] Finally, in Part 6, we'll show you how to create a standalone app version of the sort visualization and manage application layouts using ImGui and dockable windows.


## [00:02:33] Intro - Ready-to-Use Sort Algorithms

[00:02:33] Before we dive into the content, let's quickly look at the sort algorithms and how the latency is handled.

[00:02:42] The code for this tutorial is located in "fiatlight/demos/tutorials/sort\_competition". "sort\_algorithms.py" " provides ready to use sort algorithms: bubble sort, quicksort, et cetera. 

[00:03:01] "numbers\_list.py" " provides a numbers list class which behaves like an integer array, but exposes a user settable latency for memory access and memory write.

[00:03:15] "numbers\_generator" provides a "NumbersGenerationOptions" class which describes how to generate a list of unordered numbers. It derives from pydantic's BaseModel : it behaves like a serializable dataclass. "make\_random\_number\_list" will generate the numbers that shall be sorted. ​


## [00:03:35] Part 1 - Add a GUI for the Numbers Generator

[00:03:36] Let's now add a user interface for the number generator. NumbersGenerationOptions" is a pydantic BaseModel. Let's try to use it and display it via Fiatlight: by default it cannot be edited, because we need to register it. we can do it by using "register base model" in our main script. Alternatively, we can place a decorator "base model with gui registration" on top of the class definition.

[00:04:04] In both cases, our data becomes editable with a nice GUI that reflects our class content. We can see the "edit" GUI in the function parameters, and the "present" GUI in its output.

[00:04:18] We can add "fiat attributes", to customize our user interface: here we set the labels, and ranges for the values, and select a knob widget for the seed. These attrributes are faithfully taken into account in the user interface. Refer to the tutorial "GUI for dataclasses and pydantic models" for more information. 

[00:04:41] We can now run "make random number list" via Fiatlight. As you can see, we have added two attributes to this function: "invoke manually" because we want to run it manually, and "invoke always dirty" because we want to be able to run it even if the inputs did not change. As you can see, the user interface works correctly and we have a button to call the function manually. 


## [00:05:08] Part 2 - Renders the numbers as bar chart

[00:05:08] Now, Let's use ImPlot to render our numbers as a bar chart. 

[00:05:13] ImPlot is a fast and capable plotting library. You can see here an extract of the kind of figures it can generate. 

[00:05:21] Let's see how we can change the appearance of the output of the function. First, we import imgui. 

[00:05:29] Then, we wrap our function into a "Function With Gui", 

[00:05:33] and we override the "present" callback of the function's output: this callback receives a data value and should display it. For the moment, it simply displays a string using "imgui text". 

[00:05:47] Finally, we run the application, now using the wrapped function. 

[00:05:52] And we can see that our string is correctly displayed.

[00:05:56] Let's now work on generating the chart. First we import the required libraries. The "draw\_bars" function will draw the bar chart. "plot bars" will plot our values. Each plot should be done between a call to "begin plot" and "end plot". 

[00:06:15] Then, we ensure that the plotted values will always be fully visible, by setting the axis flags. Finally, we specify the plot size in EM units. 1 EM unit is the height of the font.

[00:06:31] Then we can use this function as our "present" callback, 

[00:06:35] and see that we have a nice bar chart in the application. 

[00:06:39] ​

[00:06:39] 


## [00:06:40] Part 3 - Register a GUI to display bar charts

[00:06:40] Fiatlight maintains a GUI registry which associates types to GUI classes.

[00:06:46] First, we create a new GUI class that inherits from "Any Data With Gui". Since we only want to change how it is rendered, it is enough to set its "present" callback. 

[00:06:59] Refer to the video "Fiatlight Architecture" to learn more about the possible callbacks and the numerous presentation options.

[00:07:07] Then, we tell Fiatlight to always present "Numbers List" with this new GUI. 

[00:07:14] And we are done! 

[00:07:15] Let's look at the application, and see that it shows our bar chart. 


## [00:07:20] Part 4 - Animate one sort function

[00:07:20] Next, let's add a wrapper function for the bubble sort algorithm that enables real-time visualization of the sorting process and measures the elapsed time. 

[00:07:31] We start by using the "with\_fiat\_attributes" decorator to add the "invoke\_async' attribute. This ensures that the function will be called asynchronously, allowing the GUI to update while the function runs.

[00:07:46] Inside the function, we start a timer to measure the elapsed time. We make a copy of the numbers to ensure the original set remains unmodified.

[00:07:56] To enable real-time visualization, we create an instance of NumbersListWithGui and assign the copied numbers to its value. This GUI will display the numbers being sorted.

[00:08:09] We add this GUI instance to the "fiat tuning" dictionary. Fiatlight will automatically display the content of this dictionary at each frame, even if the function is running asynchronously. Since the numbers are updated in the background, their evolution will be visible in the user interface!

[00:08:28] Finally, we call the bubble sort function, which sorts the copied numbers in place. We return the elapsed time to complete the function.

[00:08:38] Now, let's run the function composition with Fiatlight to visualize our sorting algorithm in action. 

[00:08:45] First, we need to ensure that the GUI updates as quickly as possible. We start by instantiating runner parameters for Fiatlight's FunctionsGraph.

[00:08:56] Next, we disable idling to make the animations smoother, even when the user is not interacting with the GUI.

[00:09:04] Finally, we run the composition of functions with Fiatlight. This includes our random number generator and the "bubble sort wrapper" function.

[00:09:15] And we have a nice looking user interface, where the numbers being sorted are updated in real time, and the total elapsed time is returned. 


## [00:09:25] Part 5 - Animate all the sorting functions 

[00:09:25] Now, let's extend our initial implementation to create a more comprehensive application that showcases multiple sorting algorithms within an interactive GUI. 

[00:09:36] First, we import additional sorting algorithms, to be able to show them.

[00:09:42] We've added a descriptive docstring at the beginning of the script to explain the purpose of the application and the role of various nodes. This docstring will be displayed in our application, via a markdown renderer.

[00:09:57] Next, we introduce the "make sort function visualizer" function. This higher-order function wraps each sorting algorithm with the same principle as before, adding a Fiat tuning dictionary to visually track the current status of the numbers and return the elapsed time.

[00:10:15] It also makes sure to preserve the original function name and docstring, so that it can be displayed in the graph

[00:10:23] To control the latency of the sorting algorithms, we define the gui\_latency function. This function will be added to the graph as a GUI node, in other words a node that will display the widgets defined by this function. It provides a slider to set the latency and a button to abort or enable sorting. Note that it is needed to call "set next item width" before displaying a slider.

[00:10:51] To manage the execution of our functions, we create a FunctionsGraph. This will enable us to manually link functions in the graph.

[00:11:00] We add the "make random number list" function to the graph.

[00:11:05] Next, we add each sorting algorithm to the graph, linking them to the random numbers generator. This setup allows us to visualize and compare the performance of different sorting algorithms.

[00:11:19] We also add a GUI node to control the latency, and a documentation node to display the docstring of this script.

[00:11:27] Finally, we run the function graph.

[00:11:30] And our function graph application is complete. You can see that it works perfectly. As always withFiatlight, the user inputs and GUI options - nodes locations, etc. - are saved and restored between different executions.


## [00:11:45] Part 6 - Standalone application

[00:11:45] Fiatlight goes beyond displaying Functions Graphs, and can also help you create full standalone applications. In the application shown here, we reuse Fiatlight's powerful GUI to recreate the same workflow, but we are totally free to add any other components and to change the layout. 

