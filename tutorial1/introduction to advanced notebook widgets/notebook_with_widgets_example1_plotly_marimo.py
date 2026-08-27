import marimo

__generated_with = "0.24.0"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # GOAL

    * load data set from data/example1 (in the *introduction to basic notebook widgets* folder)
    * crop and make sure the sample is within the field of view for all the images
    * export to data/output

    This is the **marimo + plotly** version of `3. notebook_with_widgets_example1_cleaner_version.ipynb`.
    Because marimo is reactive, there is no need for `interactive(...)` callbacks: cells that use a
    slider value automatically re-run when the slider moves.
    """
    )
    return


@app.cell
def _():
    import os

    import numpy as np
    import plotly.express as px
    from PIL import Image

    return Image, np, os, px


@app.cell
def _(mo):
    basic_tutorial_dir = (
        mo.notebook_dir().parent / "introduction to basic notebook widgets"
    )
    data_dir = basic_tutorial_dir / "data" / "example1"
    output_dir = basic_tutorial_dir / "data" / "output"
    return data_dir, output_dir


@app.cell
def _(mo):
    mo.md(r"""# Input, load and visualize data""")
    return


@app.cell
def _(data_dir, mo):
    file_browser = mo.ui.file_browser(
        initial_path=data_dir,
        filetypes=[".tif", ".tiff"],
        multiple=True,
        label="Select images",
    )
    file_browser
    return (file_browser,)


@app.cell
def _(Image, file_browser, mo, np):
    mo.stop(
        not file_browser.value,
        mo.md("*Select one or more TIFF images above to continue!*"),
    )

    list_files = sorted(str(_file.path) for _file in file_browser.value)

    images = []
    for _file_name in mo.status.progress_bar(list_files, title="Loading"):
        images.append(np.array(Image.open(_file_name)))

    [height, width] = np.shape(images[0])
    return height, images, list_files, width


@app.cell
def _(images, mo):
    index = mo.ui.slider(start=0, stop=len(images) - 1, value=0, label="index")
    return (index,)


@app.cell
def _(images, index, mo, px):
    _fig = px.imshow(images[index.value], color_continuous_scale="Viridis")
    _fig.update_layout(width=600, height=600)
    mo.vstack([index, _fig])
    return


@app.cell
def _(mo):
    mo.md(r"""# Crop data""")
    return


@app.cell
def _(height, images, mo, width):
    crop_index = mo.ui.slider(start=0, stop=len(images) - 1, value=0, label="index")
    left = mo.ui.slider(start=0, stop=width - 1, value=0, label="left")
    right = mo.ui.slider(start=0, stop=width - 1, value=width - 1, label="right")
    top = mo.ui.slider(start=0, stop=height - 1, value=0, label="top")
    bottom = mo.ui.slider(start=0, stop=height - 1, value=height - 1, label="bottom")
    return bottom, crop_index, left, right, top


@app.cell
def _(bottom, crop_index, images, left, mo, px, right, top):
    _fig = px.imshow(images[crop_index.value], color_continuous_scale="Viridis")
    _fig.add_vline(x=left.value, line_color="blue")
    _fig.add_vline(x=right.value, line_color="blue")
    _fig.add_hline(y=top.value, line_color="red")
    _fig.add_hline(y=bottom.value, line_color="red")
    _fig.update_layout(width=600, height=600)
    mo.vstack([mo.hstack([crop_index, left, right, top, bottom]), _fig])
    return


@app.cell
def _(mo):
    mo.md(r"""# Visualize data cropped""")
    return


@app.cell
def _(bottom, images, left, right, top):
    images_cropped = [
        _image[top.value : bottom.value, left.value : right.value]
        for _image in images
    ]
    return (images_cropped,)


@app.cell
def _(images_cropped, mo):
    cropped_index = mo.ui.slider(
        start=0, stop=len(images_cropped) - 1, value=0, label="index"
    )
    return (cropped_index,)


@app.cell
def _(cropped_index, images_cropped, mo, px):
    _fig = px.imshow(
        images_cropped[cropped_index.value], color_continuous_scale="Viridis"
    )
    _fig.update_layout(width=600, height=600)
    mo.vstack([cropped_index, _fig])
    return


@app.cell
def _(mo):
    mo.md(r"""# Export data""")
    return


@app.cell
def _(mo, output_dir):
    output_folder = mo.ui.text(
        value=str(output_dir), label="Output folder", full_width=True
    )
    export_button = mo.ui.run_button(label="Export!")
    mo.vstack([output_folder, export_button])
    return export_button, output_folder


@app.cell
def _(Image, export_button, images_cropped, mo, os, output_folder):
    mo.stop(not export_button.value)

    os.makedirs(output_folder.value, exist_ok=True)

    for _index in mo.status.progress_bar(
        range(len(images_cropped)), title="Exporting"
    ):
        _file_name = os.path.join(
            output_folder.value, f"cropped_image_{_index}.tiff"
        )
        Image.fromarray(images_cropped[_index]).save(_file_name)

    mo.md(f"**Done!** {len(images_cropped)} images exported to `{output_folder.value}`")
    return


if __name__ == "__main__":
    app.run()
