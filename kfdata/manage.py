import sys
import os

from kfdata.parser import ModelParser
from kfdata.generator import *

def filename_for_extension(basepath, filename, extension):
    return os.path.join(basepath, filename + '.' + extension)

def main():
    if len(sys.argv) < 3:
       print('Usage: {} [input model] [output directory]'.format(sys.argv[0]))
       exit(0)

    filename = os.path.abspath(sys.argv[1])
    output_folder = sys.argv[2]

    if os.path.splitext(filename)[1] == '.xcdatamodeld':
        filename = os.path.join(filename, 'Model.xcdatamodel/contents')

    model = ModelParser.parse_file(filename)

    if os.path.isdir(output_folder) is False:
        os.mkdir(output_folder)

    for entity in model.entities:
        name = entity.name

        interface_filename = filename_for_extension(output_folder, name, 'h')
        EntityInterfaceWriter(entity).write(interface_filename)

        implementation_filename = filename_for_extension(output_folder, name, 'm')
        EntityImplementationWriter(entity).write(implementation_filename)


if __name__ == '__main__':
    main()
