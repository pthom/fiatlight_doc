# Comparison with Jupyter Lab and ipywidgets

This page provides a detailed comparison between Fiatlight and Jupyter Lab + ipywidgets, highlighting the strengths and weaknesses of each framework.

## Summary
1. **Example used for the comparison**:
   *Display multiple Matplotlib figures and an animated sine wave*

2. **Performance and Responsiveness**:
   *Compare the performances of both frameworks on live and static figures.*

3. **Customization, Layout and Extensibility**:
   *Compare how each framework allows customization of widgets and extensibility.*

4. **State Management**:
   *Evaluate how user inputs and application states are managed and restored.*

5. **Algorithmic Pipelines**:
   *Examine the support for chaining functions and visualizing their interactions.*

6. **User Experience**:
   *Discuss the overall user experience, including UI manipulation capabilities.*

7. **Ease of Use and Learning Curve**:
   *Assess the ease of learning and using each framework.*

8. **Deployment and Accessibility**:
   *Compare the deployment capabilities and accessibility, including online execution.*

9. **Community and Support**:
   *Look at the available community support and resources.*

10. **Integration with Data Science Tools**:
    *Analyze how well each framework integrates with popular data science libraries and tools.*

## Detailed Comparison

### 1. Example used for the comparison
This comparison is based on the following example, which includes several Matplotlib figures, along with an animated sine wave.

#### Using Fiatlight

See the code of [figure_with_gui_demo.py](../fiat_kits/fiat_matplotlib/demo_matplotlib.py).

Here it is in action with Fiatlight. The sine wave is animated at 35 FPS (it could be 120 FPS if using ImPlot instead of MatPlotlib).

```python
from fiatlight.fiat_kits.fiat_matplotlib import demo_matplotlib

figure_with_gui_demo.main()
```

#### Using ipywidgets / Jupyter Lab

A similar demo was created using Jupyter Lab and ipywidgets. It is available [in this notebook](comparison_figure_demo_ipywidgets.ipynb).

### 2. Performance and Responsiveness

It is surprisingly difficult to create live figures in Jupyter Lab. Also, while a figure is being updated, widgets will not transmit new values to python.

An animated figure can be created by updating a figure in a loop inside a cell. The refresh rate using Matplotlib is about 1 FPS, and much higher when using `ProgressPlot`. However, the user has to wait until the cell has finished executing.

Fiatlight can update the graph up to 35 FPS when using Matplotlib. If using [ImPlot](https://github.com/epezent/implot) instead of Matplotlib, Fiatlight would reach the artificial limit of 120 FPS. The updates are done asynchronously and all the other widgets remain active.


### 3. Customization, Layout and Extensibility

- **Fiatlight**:
    - Allows deep customization of widgets, including advanced editing types and ranges. Users can define custom widgets and function graphs for extensive flexibility.
    - Supports advanced layout management, including resizing and moving figures. Arranging the functions on the screen is as easy as dragging with the mouse. Since these options are saved, they become part of the final application.
    - The code for the application occupies 135 Python lines.

- **Jupyter / ipywidgets**:
    - Offers a variety of customizable components, including sliders, checkboxes, dropdowns, and text inputs. Users can create interactive widgets that integrate seamlessly with Jupyter notebooks.
    - The layout is limited to what is possible inside a notebook, but you can use `ipywidgets`'s `HBox`, `VBox`, and other layout widgets to organize components. However, it lacks the advanced layout management features like resizing and moving figures within the notebook interface.
    - The code for the application occupies 142 Python lines.


### 4. State Management
- **Fiatlight**:
   - Automatically saves and restores user inputs, widget placements, and settings. Supports saving different configurations and restoring them later.
- **Jupyter / ipywidgets**:
   - State management is manual and typically involves more code to save and restore states across sessions.

### 5. Algorithmic Pipelines
- **Fiatlight**:
   - Supports function graphs, enabling chaining of functions and visualization of their inputs and outputs, simplifying complex workflows.
- **Jupyter / ipywidgets**:
   - Supports sequential and interactive cell execution but lacks a native function graph feature. While users can manually code function linkages and interactions, it does not offer the same visual pipeline management as Fiatlight.

### 6. User Experience
- **Fiatlight**:
   - Offers a rich user experience with the ability to resize and move figures, enhancing usability and flexibility.
- **Jupyter / ipywidgets**:
   - offers a basic user experience for the final user.
  Note: the appearance of the ipywidgets is not restored when reopening a notebook: the user has to re-run the cells to get the widgets back.

### 7. Ease of Use and Learning Curve
- **Fiatlight**:
   - Powerful and flexible, but it might require some initial learning since it is a novel framework. However, the immediate GUI mode is easy to grasp, making it accessible for new users.
- **Jupyter / ipywidgets**:
   - offers a truly great experience for the developer, in terms of ease and speed of development.


### 8. Deployment and Accessibility
- **Fiatlight**:
   - Fiatlight can run inside a Jupyter Notebook, but requires a local environment and lacks web-based deployment capabilities. Efforts with pyodide are underway but still in development.
- **Jupyter / ipywidgets**:
   - deployable locally and on almost any cloud provider (Google Colab, Binder, etc.)

### 9. Community and Support
- **Fiatlight**:
   - May not have as extensive a community or support resources as more established frameworks, but it benefits from the communities of the libraries it builds upon, like Dear ImGui, Hello ImGui, and ImGui Bundle.
- **Jupyter / ipywidgets**:
   - Large and active community, extensive documentation, and support resources, beneficial for new users and those seeking help or examples. Many resources are available for troubleshooting and expanding functionality.

### 10. Integration with Data Science Tools
- **Fiatlight**:
  - Can integrate with data science tools but may require more setup and configuration. Its use of Dear ImGui allows for high-performance graphics and interactive applications, which can be beneficial for certain data science applications.
- **Jupyter / ipywidgets**:
   - Very mature integration with popular data science libraries and tools such as NumPy, pandas, scikit-learn, and more. It is widely used in the data science community, making it a go-to choice for data-driven research and analysis.

### Conclusion

Both Fiatlight and Jupyter Lab with ipywidgets have their unique advantages.

- **Fiatlight** excels in high-performance applications, offering extensive customization, advanced interactive features, and sophisticated state management that includes automatic saving and restoring of user inputs and widget placements. This makes it exceptionally well-suited for rapid prototyping, as users can quickly iterate on their designs without losing their configurations. Its support for function graphs simplifies complex workflows, making it a powerful tool for developing creative applications.

- **Jupyter Lab with ipywidgets** is ideal for users who prioritize ease of use, rapid development, and integration with data science tools. It offers a user-friendly interface that facilitates interactive data analysis and visualization. The extensive community support, along with its deployment capabilities on platforms like Google Colab and Binder, make it highly accessible and powerful for educational and research purposes.

The choice between them depends on the specific needs and preferences of the user or project. Fiatlight offers a more feature-rich environment for those needing advanced GUI capabilities and state management, while Jupyter Lab with ipywidgets provides a robust solution for interactive data science and educational applications.