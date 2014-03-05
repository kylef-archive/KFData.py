import sys
import os

from kfdata.parser import ModelParser
from kfdata.generator import *

def filename_for_extension(basepath, filename, extension):
    return os.path.join(basepath, filename + '.' + extension)

def main():
    filename = sys.argv[1]
    output_folder = sys.argv[2]

    model = ModelParser.parse_file(filename)

    for entity in model.entities:
        name = entity.name

        interface_filename = filename_for_extension(output_folder, name, 'h')
        EntityInterfaceWriter(entity).write(interface_filename)

        implementation_filename = filename_for_extension(output_folder, name, 'm')
        EntityImplementationWriter(entity).write(implementation_filename)


if __name__ == '__main__':
    main()

