

une video de demos ou gtp lit la doc (+ fiatlight help) et fait une application
    Rosetta
    Fourier / square signal


# From natural language to naturally understandable applications.

Examples with ChatGPT where someone explains the different functions of a program and it will create it.




```
@gui_specs(
    # name specs
    name__max_length=100,
    name__placeholder="your name...",
    name__single_line=True,
    name__allowed_chars="a-zA-Z -",
    name__widget_type="text_input",
    # age specs
    age__range=(0, 125),
    age__widget_type="slider",
    # output specs
    output__widget_type="text_box",
    # function specs
    function__doc_style="tooltip",
    function__doc_renderer="markdown",
    )
def hello_rosetta(name: str, age: int) -> str:
    """`hello_rosetta`: A function that greets a person by name and age.
    ====================================================================
    Args
    ----
    * `name` (str) : The name of the person
       * Max length: 10 characters.
       * Only non-accentuated latin letters, spaces, and "-" are allowed.
    * `age` (int)  : The age of the person. Should be between 0 and 125
    Returns
    -------
    * `str`        : A greeting message, with a special welcome message for newcomers.
    """
    if age == 0:
        return f"Hello, {name}, welcome to the world!"
    elif age == 1:
        return f"Hello, {name}, you are {age} year old."
    else:
        return f"Hello, {name}, you are {age} years old."

```


# Additional Sections to Consider
## User Contributions
- **How to Contribute**: Guide on contributing to the project (e.g., adding new widgets, improving documentation).
- **Community Guidelines**: Code of conduct and contribution guidelines.

## FAQ and Troubleshooting
- **Common Issues**: Address common issues and their solutions.
- Layout (Vertical, Horizontal, etc)
- Id & Unique Id / push_id
- imgui_ctx-
- popup & state (fire_at_frame_end)

- **Tips and Tricks**: Provide useful tips for getting the most out of Fiatlight.

## Appendix
- **Glossary**: Define key terms and concepts used throughout the documentation.
- **Changelog**: Track changes and updates to the framework.


## License


# Getting started
## Installation
- **Requirements**: List system requirements and dependencies.
- **Installation Steps**: Provide step-by-step instructions for installing Fiatlight on various operating systems (Windows, macOS, Linux).




--------------------

# Done ImGui & the Immediate Mode GUI Paradigm
## ==> Links to intro
- **Introduction to ImGui**: Describe the immediate mode GUI paradigm and its benefits.
- **Comparison with Retained Mode GUIs**: Briefly compare ImGui with traditional retained mode GUIs.
- fiat_widgets: font_awesome, etc.

## Done References and Manuals
- **Official Documentation**: Links to the official ImGui documentation.
- **Community Resources**: Links to tutorials, forums, and other learning resources.



# Done Introduction
## Done What is Fiatlight?
From idea to app in 3 minutes ...
- **Description**: A brief overview highlighting Fiatlight's purpose and key features.
- **Mottos**: Include the mottos you have considered, to set the tone and vision.
- **Key Benefits**: Summarize the primary advantages for different user types (non-technical users, tech-savvy users, and computer scientists).

## Done Examples
... several examples in different domains
- **Overview of Examples**: Briefly describe what kinds of examples are included.
- **Domain-Specific Examples**: Provide a few examples in different domains such as data visualization, audio processing, AI, and educational tools.

-----------

# Done Tutorials and Examples

## Quick Start
- **First Example**: Guide users through creating and running their first Fiatlight application.
- **Basic Concepts**: Introduce basic concepts such as functions, graphs, and GUI elements.

## Beginner Tutorials
- **Creating a Simple App**: Walkthrough for creating a simple application.
- **Using Built-in Widgets**: How to use and customize built-in widgets.

## Intermediate Tutorials
- **Data Visualization**: Creating interactive data visualizations.
- **Integrating Libraries**: How to integrate Fiatlight with other Python libraries (e.g., Matplotlib, Numpy).

## Advanced Tutorials

### Register custom widgets by type
- **Data Types**: Overview of supported data types and how to register custom types.
- **Enums**
- **Dataclasses**
- **Pydantic models**

-----------


# Done High-Level Overview of Fiatlight Framework
## Done Class Diagrams
- **Core Classes**: Visual representation of core classes and their relationships.
- **Example Use Cases**: Diagrams showing typical usage patterns.

## Done Folder Structure
- **Directory Overview**: Explain the purpose of each directory in the Fiatlight codebase.
- **Navigation Tips**: Tips for navigating the codebase effectively.

-----------

# Done fiat_core
## Done FunctionWithGui
- **Overview**: Explain what `FunctionWithGui` is and its role in Fiatlight.
- **Usage Examples**: Detailed examples demonstrating how to use and customize `FunctionWithGui`.

## Done AnyDataWithGui
- **Overview**: Explain what `AnyDataWithGui` is and its role in Fiatlight.
- **Usage Examples**: Detailed examples demonstrating how to use and customize `AnyDataWithGui`.

## Done AnyDataGuiCallbacks

## Done FunctionsGraph

## Done Gui Registry

