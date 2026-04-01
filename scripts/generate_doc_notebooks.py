from fiatlight.fiat_notebook.notebook_utils import (
    save_notebook_from_markdown_file,
)
from pathlib import Path

THIS_DIR = Path(__file__).parent
DOC_DIR = (THIS_DIR / "..").resolve()
FIATLIGHT_DIR = (DOC_DIR / "../src/python/fiatlight").resolve()


def generate_doc_notebooks() -> None:
    def md_source_to_notebook(file_prefix: str) -> None:
        source_md_file = f"{DOC_DIR}/{file_prefix}_source.md"
        notebook_file = f"{DOC_DIR}/{file_prefix}.ipynb"
        save_notebook_from_markdown_file(source_md_file, notebook_file)

    def md_source_list_to_notebooks(file_prefixes: list[str]) -> None:
        for file_prefix in file_prefixes:
            md_source_to_notebook(file_prefix)

    #
    # Introduction & getting started
    #
    md_source_list_to_notebooks([
        "intro",
        "install",
    ])

    #
    # Tutorials
    #
    md_source_list_to_notebooks([
        "manual_first",
        "manual_function",
        "manual_gui_node",
        "manual_tuning",
        "manual_subclass",
        "manual_fiat_attributes",
        "manual_functions_graph",
        "manual_cli",
        "manual_validation",
        "manual_demos",
        "manual_registry",
        "manual_dataclass_models",
        "manual_custom",
        "manual_reuse_widgets",
    ])

    #
    # Rosetta
    #
    md_source_to_notebook("rosetta")

    #
    # API doc / fiat_core
    #
    # FunctionWithGui
    save_notebook_from_markdown_file(
        f"{FIATLIGHT_DIR}/fiat_core/function_with_gui.md",
        f"{DOC_DIR}/api_function_with_gui.ipynb")
    # any_data_gui_callbacks
    save_notebook_from_markdown_file(
        f"{FIATLIGHT_DIR}/fiat_core/any_data_gui_callbacks.md",
        f"{DOC_DIR}/api_any_data_gui_callbacks.ipynb",
    )
    # any_data_with_gui
    save_notebook_from_markdown_file(
        f"{FIATLIGHT_DIR}/fiat_core/any_data_with_gui.md",
        f"{DOC_DIR}/api_any_data_with_gui.ipynb",
    )
    # FunctionsGraph
    save_notebook_from_markdown_file(
        f"{FIATLIGHT_DIR}/fiat_core/functions_graph.md",
        f"{DOC_DIR}/api_functions_graph.ipynb",
    )

    #
    # Doc / Kits
    #
    # fiat_image
    save_notebook_from_markdown_file(
        f"{FIATLIGHT_DIR}/fiat_kits/fiat_kits.md",
        f"{DOC_DIR}/fiat_kits.ipynb",
    )
    save_notebook_from_markdown_file(
        f"{FIATLIGHT_DIR}/fiat_kits/fiat_image/fiat_image.md",
        f"{DOC_DIR}/fiat_image.ipynb",
    )
    save_notebook_from_markdown_file(
        f"{FIATLIGHT_DIR}/fiat_kits/fiat_matplotlib/fiat_matplotlib.md",
        f"{DOC_DIR}/fiat_matplotlib.ipynb",
    )
    save_notebook_from_markdown_file(
        f"{FIATLIGHT_DIR}/fiat_kits/fiat_dataframe/fiat_dataframe.md",
        f"{DOC_DIR}/fiat_dataframe.ipynb",
    )
    save_notebook_from_markdown_file(
        f"{FIATLIGHT_DIR}/fiat_kits/fiat_implot/fiat_implot.md",
        f"{DOC_DIR}/fiat_implot.ipynb",
    )

    #
    # Doc / Comparisons
    #
    md_source_list_to_notebooks([
        "comparison_streamlit",
        "comparison_dash",
        "comparison_ipywidgets",
        "comparison_figure_demo_ipywidgets"
    ])


if __name__ == "__main__":
    generate_doc_notebooks()
