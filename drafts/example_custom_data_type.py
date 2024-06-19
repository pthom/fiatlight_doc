import fiatlight
from fiatlight import AnyDataWithGui
from fiatlight.fiat_widgets import fontawesome_6_ctx, icons_fontawesome_6
from typing import NewType, Any, Dict
from imgui_bundle import imgui, hello_imgui, imgui_ctx, ImVec4


# Our custom type for which we want to create a GUI
Length = NewType("Length", float)


# The specific GUI for our custom type
class LengthWithGui(AnyDataWithGui[Length]):
    use_imperial_units: bool = False

    def __init__(self) -> None:
        super().__init__(Length)
        self.callbacks.edit = self._edit  # A custom callback for editing the data
        self.callbacks.present = self._present  # A custom callback for presenting the data
        self.callbacks.present_str = self._present_str  # A custom callback for presenting the data as a short string
        self.callbacks.default_value_provider = lambda: Length(1.0)  # A custom callback for providing a default value
        # custom callback for saving the GUI options (here, we save the imperial units option)
        self.callbacks.save_gui_options_to_json = self._save_gui_options_to_json
        self.callbacks.load_gui_options_from_json = self._load_gui_options_from_json

    def _edit(self, value: Length) -> tuple[bool, Length]:
        _, self.use_imperial_units = imgui.checkbox("Imperial", self.use_imperial_units)

        format = "%.3g m" if not self.use_imperial_units else "%.3g yd"
        value_unit = value * 1.09361 if self.use_imperial_units else value
        imgui.set_next_item_width(hello_imgui.em_size(10))
        changed, new_value_unit = imgui.slider_float(
            "Value", value_unit, 1e-5, 1e11, format, imgui.SliderFlags_.logarithmic.value
        )
        if changed:
            value = Length(new_value_unit / 1.09361 if self.use_imperial_units else new_value_unit)
        return changed, value

    @staticmethod
    def _present_str(value: Length) -> str:
        return f"Length: {value:.2f} m"

    @staticmethod
    def _present(value: Length) -> None:
        with fontawesome_6_ctx():
            yd = int(Length(value * 1.09361))
            inches = int((Length(value * 1.09361 - yd) * 36))
            bananas = int(value / 0.2)
            imgui.text(f"Length: {yd} yd {inches:.0f} in (aka {bananas}")
            imgui.same_line()
            with imgui_ctx.push_style_color(imgui.Col_.text.value, ImVec4(1, 0.5, 0, 1)):
                imgui.text(icons_fontawesome_6.ICON_FA_CARROT)
            imgui.same_line()
            imgui.text(")")

    def _save_gui_options_to_json(self) -> Dict[str, Any]:
        return {"use_imperial_units": self.use_imperial_units}

    def _load_gui_options_from_json(self, json: Dict[str, Any]) -> None:
        self.use_imperial_units = json.get("use_imperial_units", False)


# A function to register our custom type with its GUI
def register_length_with_gui() -> None:
    # In order to not pollute the module namespace, we import the register_type function here
    from fiatlight import register_type

    register_type(Length, LengthWithGui)


# Call this function at your program's startup
register_length_with_gui()


# A function that uses our custom type
def circle_perimeter(radius: Length) -> Length:
    return Length(2 * 3.14159 * radius)


# Run the function with the GUI
fiatlight.run(circle_perimeter)
