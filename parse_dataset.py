import json
import urllib.request
from nbtschematic import SchematicFile
import numpy as np
from os import listdir as listdir
from os import join as join


def download_dataset(url_file, output_folder):
    schematic_data = json.load(url_file)

    index = 0
    for schematic in schematic_data:
        url = schematic['downloadLink']
        schematic_file = output_folder + '/' + str(index) + '.schematic'
        urllib.request.urlretrieve(url, schematic_file)
        index += 1


def convert_dataset(schematic_folder, output_folder, transforms):
    for file in listdir(schematic_folder):
        schematic_file = join(schematic_folder, file)
        output_file = join(output_folder, file.replace('schematic', '.npy'))

        sf = SchematicFile.load(schematic_file)

        blocks = sf.blocks
        for transform in transforms:
            blocks = transform(blocks)

        np.save(output_file, blocks)


def array_to_schematic(blocks):
    sf = SchematicFile(blocks.shape)
    sf.blocks = blocks
    return sf


def load_blocks_from_numpy(file):
    return np.load(file)


def save_schematic(sf, file):
    sf.save(file)
