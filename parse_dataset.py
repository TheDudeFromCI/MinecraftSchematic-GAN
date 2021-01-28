import json
import urllib.request
from nbtschematic import SchematicFile
import numpy as np


def convert_dataset(url_file, output_folder, temp_folder, transforms):
    schematic_data = json.load(url_file)

    index = 0
    for schematic in schematic_data:
        url = schematic['downloadLink']
        temp_file = temp_folder + '/' + str(index) + '.schematic'
        urllib.request.urlretrieve(url, temp_file)
        sf = SchematicFile.load(temp_file)

        blocks = sf.blocks
        for transform in transforms:
            blocks = transform(blocks)

        save_schematic_as_numpy(blocks, output_folder, index)
        index += 1


def save_schematic_as_numpy(blocks, output_folder, index):
    file_name = output_folder + '/' + str(index) + '.npy'
    np.save(file_name, blocks)


def array_to_schematic(blocks):
    sf = SchematicFile(blocks.shape)
    sf.blocks = blocks
    return sf


def load_blocks_from_numpy(file):
    return np.load(file)


def save_schematic(sf, file):
    sf.save(file)
