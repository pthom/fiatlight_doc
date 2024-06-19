from fiatlight.fiat_doc.notebook_utils import (
    save_function_or_class_doc_to_notebook,
    save_notebook_from_markdown_file,
)
import os
import subprocess

THIS_DIR = os.path.dirname(__file__)
DOC_DIR = os.path.realpath(os.path.join(THIS_DIR, ".."))
FIATLIGHT_DIR = os.path.realpath(os.path.join(DOC_DIR, ".."))


def generate_doc_notebooks() -> None:
    from fiatlight.fiat_core import function_with_gui, functions_graph

    #
    # Introduction & getting started
    #
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/intro_source.md", update_existing=True, notebook_filename=f"{DOC_DIR}/intro.ipynb"
    )
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/imgui_tech_stack_source.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/imgui_tech_stack.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/install_source.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/install.ipynb",
    )

    #
    # Tutorials
    #
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/tutorials_source.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/tutorials.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/tutorials_advanced_source.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/tutorials_advanced.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/tutorials_cli_source.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/tutorials_cli.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/tutorials_validation_source.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/tutorials_validation.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/tutorials_demos_source.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/tutorials_demos.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/tutorials_signature_source.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/tutorials_signature.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/tutorials_first_source.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/tutorials_first.ipynb",
    )
    save_notebook_from_markdown_file(
        # Warning, path from the source
        md_filename=f"{FIATLIGHT_DIR}/fiat_kits/fiat_kit_skeleton/fiat_skeleton.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/tutorials_new_widget.ipynb",
    )

    #
    # Rosetta
    #
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/rosetta_source.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/rosetta.ipynb",
    )

    #
    # Doc / fiat_core
    #
    # FunctionWithGui
    save_function_or_class_doc_to_notebook(function_with_gui, update_existing=True)
    # any_data_gui_callbacks
    save_notebook_from_markdown_file(
        md_filename=f"{FIATLIGHT_DIR}/fiat_core/any_data_gui_callbacks.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/any_data_gui_callbacks.ipynb",
    )
    # any_data_with_gui
    save_notebook_from_markdown_file(
        md_filename=f"{FIATLIGHT_DIR}/fiat_core/any_data_with_gui.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/any_data_with_gui.ipynb",
    )
    # FunctionsGraph
    save_function_or_class_doc_to_notebook(functions_graph, update_existing=True)

    #
    # Doc / fiat_togui
    #
    save_notebook_from_markdown_file(
        md_filename=f"{FIATLIGHT_DIR}/fiat_togui/fiat_togui.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/fiat_togui.ipynb",
    )

    #
    # Doc / Kits
    #
    # fiat_image
    save_notebook_from_markdown_file(
        md_filename=f"{FIATLIGHT_DIR}/fiat_kits/fiat_kits.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/fiat_kits.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{FIATLIGHT_DIR}/fiat_kits/fiat_image/fiat_image.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/fiat_image.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{FIATLIGHT_DIR}/fiat_kits/fiat_matplotlib/fiat_matplotlib.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/fiat_matplotlib.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{FIATLIGHT_DIR}/fiat_kits/fiat_dataframe/fiat_dataframe.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/fiat_dataframe.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{FIATLIGHT_DIR}/fiat_kits/fiat_implot/fiat_implot.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/fiat_implot.ipynb",
    )

    #
    # Doc / Comparisons
    #
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/comparison_streamlit.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/comparison_streamlit.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/comparison_dash.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/comparison_dash.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/comparison_ipywidgets.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/comparison_ipywidgets.ipynb",
    )
    save_notebook_from_markdown_file(
        md_filename=f"{DOC_DIR}/figure_demo_ipywidgets.md",
        update_existing=True,
        notebook_filename=f"{DOC_DIR}/figure_demo_ipywidgets.ipynb",
    )


def generate_book() -> None:
    # Generate a single PDF for the complete manual.
    #     pip install pyppeteer
    # subprocess.run(["jupyter-book", "build", DOC_DIR, "--builder", "pdfhtml"])

    # Generate multiple HTML pages for the manual
    subprocess.run(["jupyter-book", "build", DOC_DIR])

    # Copy recursively the _build/html directory to output/
    import shutil
    output_dir = f"{DOC_DIR}/docs/flgt"
    shutil.rmtree(output_dir, ignore_errors=True)
    shutil.copytree(f"{DOC_DIR}/_build/html", output_dir)



if __name__ == "__main__":
    generate_doc_notebooks()
    generate_book()
