Fiatlight First Steps - Transcript
==================================

# Outline

- Opening goal
  - Set the promise: turn small Python functions and models into interactive apps in minutes; show automatic widgets, persistence, and async without boilerplate.

- Wrap Single function: add(x: int, y: int) -> int
  - Auto-generated widgets for parameters and output; demonstrate Run and Restart
  - Change y to int|None and show how the widget updates to reflect optionality
  - Show how the GUI controls work: reset to default, use current value, set to None
  
- Persistence
   - Save/Load buttons, auto-save on exit, auto-restore on start; reveal the fiat_settings folder and restart to prove state restore .

- Customization via attributes
  - Quick CLI tour (fiatlight)
  - Show how to set the range and labels for the add parameters using fiat_attributes (using either fl.add_fiat_attributes or the @fl.with_fiat_attributes decorator) .
  - Show help, list supported types, list attributes for a type/param, 

- Using fiatlight utility types: 
    - Show type-aware widgets for ImagePath and an Image output preview; mention built-ins and why typing matters .
    - read_image(ImagePath) → Image

- Compose two functions
    - int_source → add; wire outputs to inputs, observe live updates; keep this to a simple, single edge to avoid graph complexity.
    - may be quickly mention a large composition such as demo_word_count?

- Minimal manual override of a parameter's widget
    - Override a single parameter’s widget by hand to show full control exists, then defer to manual/API for patterns .
    - Override function output widget to show custom output rendering

- Async run
    - Enable async for a function with a deliberate delay; show responsive UI, progress/status, and error replay basics already emphasized in the advanced tutorial.

- Close
    - Recap: automatic widgets from types, composition, persistence, quick CLI discovery, light customization, and async; direct viewers to the advanced and dataclass/pydantic videos for deep dives.
  