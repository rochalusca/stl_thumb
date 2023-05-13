import os
import pyvista as pv

input_folder = 'stl'
output_folder = 'png'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.stl'):
        mesh = pv.read(os.path.join(input_folder, filename))

        plotter = pv.Plotter(off_screen=True)
        plotter.add_mesh(mesh)

        plotter.camera_position = 'iso'
        plotter.camera.zoom(1.2)

        output_filepath = os.path.join(output_folder, filename[:-4] + '.png')
        plotter.show(screenshot=output_filepath)
