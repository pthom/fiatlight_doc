from fiatlight.fiat_notebook.notebook_utils import (
    save_notebook_from_markdown_file,
)
import os
import subprocess

THIS_DIR = os.path.dirname(__file__)
DOC_DIR = os.path.realpath(os.path.join(THIS_DIR, ".."))
FIATLIGHT_DIR = os.path.realpath(os.path.join(DOC_DIR, ".."))


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
        "imgui_tech_stack",
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


def generate_book_html() -> None:
    import shutil

    # Remove the _build directory
    build_dir = f"{DOC_DIR}/_build"
    shutil.rmtree(build_dir, ignore_errors=True)

    # Generate multiple HTML pages for the manual
    command = 'jupyter-book build . 2>&1 | grep -v "_source" | grep -v "copying" | grep -v "reading" | grep -v "writing"'
    #subprocess.run(["jupyter-book", "build", DOC_DIR])
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=DOC_DIR)
    stdout, stderr = process.communicate()
    output = stdout.decode('utf-8')
    print(output)

    # Copy recursively the _build/html directory to output/
    output_dir = f"{DOC_DIR}/docs/flgt"
    shutil.rmtree(output_dir, ignore_errors=True)
    shutil.copytree(f"{DOC_DIR}/_build/html", output_dir)
    # Add nojekyll file
    with open(f"{output_dir}/.nojekyll", "w") as f:
        f.write("")


def generate_book_pdf() -> None:
    import shutil

    # Generate a single PDF for the complete manual.
    #     pip install pyppeteer
    subprocess.run(["jupyter-book", "build", DOC_DIR, "--builder", "pdfhtml"])
    shutil.copy(f"{DOC_DIR}/_build/pdf/book.pdf", f"{DOC_DIR}/docs/flgt.pdf")


if __name__ == "__main__":
    import sys
    gen_pdf = (len(sys.argv) > 1 and sys.argv[1] == "pdf")

    generate_doc_notebooks()
    if gen_pdf:
        print("Generating PDF")
        generate_book_pdf()
    else:
        generate_book_html()
