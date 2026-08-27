import ipywe.fileselector
import numpy as np
from PIL import Image
import plotly.express as px
import time
from IPython.display import display
from IPython.core.display import HTML
import os

from ipywidgets import interactive
import ipywidgets as widgets


class Exercise1WithWidgetsPlotly:

    def __init__(self):
        pass

    def input_load_and_visualize_data(self):
        data_folder = ipywe.fileselector.FileSelectorPanel(instruction="Select images",
                                                           filters={'TIFF': ['*.tiff', '*.tif']},
                                                           default_filter='TIFF',
                                                           multiple=True,
                                                           start_dir="data/example1/",
                                                           next=self.load_data)
        data_folder.show()

    def load_data(self, list_files):
        self.images = []
        self.list_files = list_files

        pb = widgets.IntProgress(min=0, max=len(list_files) - 1, description="Loading")
        display(pb)

        for _index, _file in enumerate(list_files):
            _image = np.array(Image.open(_file))
            self.images.append(_image)
            pb.value = _index + 1
            time.sleep(0.15)  # slowing down the load to be able to see the progress bar in action

        pb.description = "Done!"

        self.visualize_data()

    def visualize_data(self):

        def plot(index):
            fig = px.imshow(self.images[index], color_continuous_scale='Viridis')
            fig.update_layout(width=600, height=600)
            fig.show()

        v = interactive(plot,
                        index=widgets.IntSlider(min=0,
                                                max=len(self.images) - 1))
        display(v)

    def crop_data(self):
        [height, width] = np.shape(self.images[0])

        def plot(index, left, right, top, bottom):
            fig = px.imshow(self.images[index], color_continuous_scale='Viridis')
            fig.add_vline(x=left, line_color='blue')
            fig.add_vline(x=right, line_color='blue')
            fig.add_hline(y=top, line_color='red')
            fig.add_hline(y=bottom, line_color='red')
            fig.update_layout(width=600, height=600)
            fig.show()

            return left, right, top, bottom

        self.cropping = interactive(plot,
                               index=widgets.IntSlider(min=0, max=len(self.images) - 1),
                               left=widgets.IntSlider(min=0, max=width - 1, value=0, continuous_update=True),
                               right=widgets.IntSlider(min=0, max=width - 1, value=width - 1, continuous_update=True),
                               top=widgets.IntSlider(min=0, max=height - 1, value=0, continuous_update=True),
                               bottom=widgets.IntSlider(min=0, max=height - 1, value=height - 1,
                                                        continuous_update=True))
        display(self.cropping)

    def visualize_data_cropped(self):

        [left, right, top, bottom] = self.cropping.result

        self.images_cropped = []
        for _image in self.images:
            _image_cropped = _image[top: bottom, left: right]
            self.images_cropped.append(_image_cropped)

        def plot(index):
            fig = px.imshow(self.images_cropped[index], color_continuous_scale='Viridis')
            fig.update_layout(width=600, height=600)
            fig.show()

        vv = interactive(plot,
                         index=widgets.IntSlider(min=0,
                                                 max=len(self.images) - 1))
        display(vv)

    def _export_data(self, output_folder):
        pb = widgets.IntProgress(min=0, max=len(self.list_files) - 1, description="Exporting")
        display(pb)

        for _index, _image in enumerate(self.images_cropped):
            file_name = os.path.join(output_folder, f"cropped_image_{_index}.tiff")
            _image_to_export = Image.fromarray(_image)
            _image_to_export.save(file_name)
            time.sleep(0.15)
            pb.value = _index + 1

        pb.description = "Done!"

    def export_data(self):

        output_folder_ui = ipywe.fileselector.FileSelectorPanel(instruction="Select output folder",
                                                                type='directory',
                                                                multiple=False,
                                                                start_dir="data/output",
                                                                next=self._export_data)
        output_folder_ui.show()
