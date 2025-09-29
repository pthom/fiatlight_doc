# Fiatlight for dataclasses and pydantic


## [00:00:00] Automatic GUI for dataclasses and pydantic models

[00:00:00] Let's now look at how to add a GUI to dataclasses and models.

[00:00:05] The "gui\_dataclass\_pydantic" tutorial examples provide a detailed explanation on how to automatically create a GUI for a dataclass or a pydantic model. 

[00:00:16] Note that pydantic models are preferable since Fiatlight will be able to serialize and deserialize them, and thus save user inputs that use them.

[00:00:27] These examples show how to use custom attributes, named "fiat\_attributes", to customize the widgets appearance (label, numeric range, etc.). Each attribute name constitutes of the name of the parameter, followed by a double underscore, followed by the attribute id. 

[00:00:46] These attributes can be added when registering the class, i.e. using "register\_base\_model" for a pydantic model, or "register\_dataclass" for a dataclass. Alternatively a specific decorator for pydantic model and for dataclasses is provided.

[00:01:06] When running, we can see that the name and age widgets effectively use those attributes.

[00:01:13] You can use the "fiatlight" command line tool to know which widgets and which custom attributes are available. Here, we list the available types. Here, we list the available fiat\_attributes for an int value. Here, we list the available fiat\_attributes for a function. 

[00:01:33] These tutorials also show how to use validators, to ensure that the user inputs are correct. Validators can either raise a "ValueError" message with a nice message that will be displayed to the user, or they can modify the user input.

[00:01:50] In the case of Pydantic models, it is also possible to use pydantic validators: here, our validator for the field "name" is implemented with pydantic. If it raises an error, this will be displayed by Fiatlight.

[00:02:06] When fields are annotated with "more than" and "less than", Fiatlight will detect it and adjust the slider range accordingly.

[00:02:15] When running, we can see that those validators are used: any error is nicely displayed, and numbers are changed to multiples of 5.

[00:02:26] You will find these tutorials inside "fiatlight - demos - tutorials - GUI dataclass pydantic ". ...

