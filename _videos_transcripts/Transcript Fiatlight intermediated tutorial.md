# Fiatlight - Intermediate tutorial


## [00:00:00] Handle exceptions in a function

[00:00:00] Let's see how to handle exceptions within fiatlight.

[00:00:03] In this example, we continue from the previous image example.

[00:00:07] We added an integer "aperture size" parameter to the "detect edges" function. However, the Open CV documentation for Canny specifies that the only valid values for this parameter are 3, 5, and 7.

[00:00:22] Thus, if we run our app, the user could enter any integer value, which can lead to an error at runtime, for example if the user enters 4.

[00:00:33] As you can see, Fiatlight is able to catch this error, and to display the exception in the user interface. 

[00:00:40] Fiatlight even provides a button to "Debug this exception": let's click on it.

[00:00:46] The exception is replayed, and we see that the call to "cv2 Canny" fails because the aperture size is invalid.

[00:00:54] This is a very nice way to replay errors "post-mortem", and to debug them.


## [00:01:00] Use validators to check function parameters

[00:01:00] Let's see how to use validators to check function parameters.

[00:01:04] In this part, we will solve the issue with the aperture size parameter by writing a validator function for this parameter.

[00:01:12] A validator function behaves like a pydantic validator i.e.

[00:01:17] - it receives the current value

[00:01:19] - it raises a "Value Error" if the value is not valid

[00:01:23] - it returns a possibly modified value

[00:01:26] Here, we will implement two possible behaviors:

[00:01:29] - Option 1: raise a ValueError if the value is not valid

[00:01:34] - Option 2: return a possibly modified value, using the closest valid value.

[00:01:41] Then, we will register this validator function for the aperture size parameter using fiatlight's "add fiat attributes" function.

[00:01:50] When running the app, we can see that if we enter an invalid value (for example 4)

[00:01:56] either we get a clear error message indicating that the value is not valid, if we are using Option 1.

[00:02:03] or the value is automatically changed to the closest valid value, if we are using Option 2.


## [00:02:10] Manually write the GUI for a parameter

[00:02:10] Let's see how to manually write the interface for a function parameter.

[00:02:14] In this part, we will solve the issue with the aperture size parameter by manually writing the interface for this parameter,  using radio buttons, so that the user can only select one of the valid values.

[00:02:28] In order to create our custom widget, we will write a custom edition callback for this parameter.

[00:02:34] It accepts the current value, and returns a tuple containing a bool indicating if the value was changed and the new value. 

[00:02:43] We will be using the Immediate Mode GUI paradigm (with Dear ImGui Bundle).

[00:02:48] Refer to the section "Immediate Mode GUI with Python" of the manual for more info about this paradigm and about Dear ImGui.

[00:02:57] Here our function simply presents a radio button for each valid value, and returns a tuple "changed, selected value".

[00:03:06] Then, we transform the "detect edges" function into a "Function With Gui", and we set its edit callback for the "aperture size" parameter to our custom function.

[00:03:17] There are many more callbacks. Refer to the documentation for more details.

[00:03:22] Then, we run the app with our two functions (using the customized "detect edges gui").

[00:03:29] And we can see that our custom GUI for this parameter works !


## [00:03:33] Fiat tuning: visually debug the internal state of your function

[00:03:33] Let's see how to visually debug the internal state of your functions.

[00:03:37] In this example, we apply this to a toon-edges effect where contour detection is sensitive to thresholds and blur radius.

[00:03:46] The "fiat tuning" collapsible panel of the function node shows  intermediate images and timing metrics, making it easy to adjust parameters and see their impact in real time.

[00:03:58] In the code, to achieve this, we slightly modified the function "add toon edges". 

[00:04:04] We added a "fiat tuning" dict. This dictionary can contain raw values, like numbers for the durations of each step, and GUI widgets - for example, "Image With Gui" for intermediate images.

[00:04:17] Now, when we tweak the thresholds, the edges, and other intermediate steps all refresh instantly, making the search for good values obvious rather than guesswork!

[00:04:28] This mechanism isn’t limited to images and numbers; in this sorting visualizer, a plot is placed in the fiat tuning dict and animates while the functions are running!


## [00:04:39] A more complex function graph

[00:04:39] Let's see how we can create more complex function graphs.

[00:04:43] In this example, we will create an application which uses and displays the Titanic dataset, together with some plots to visualize the data.

[00:04:52] For this, we will create a function graph with three functions:

[00:04:57] A function to create a filterable DataFrame, with several filter options for which we specify the GUI using fiat attributes.

[00:05:05] A GUI function to display a pie chart, based on the filtered DataFrame: this function does not return anything, it just displays a pie chart. As such, it is really a "GUI function", which uses ImGui and ImPlot widgets to display its interface. 

[00:05:22] A second GUI function displays a histogram, based on the filtered DataFrame.

[00:05:28] We then create a function graph, to which we add the filterable DataFrame function and the two GUI functions.

[00:05:35] Then, we create links between the functions, using the "add link" method, to specify the data flow: the output of the filterable DataFrame function will be linked to the input of the two GUI functions.

[00:05:49] Finally, we run our graph.

[00:05:51] And we can see that passengers in the 1st class had a much higher survival rate than those in the 2nd and 3rd class.

