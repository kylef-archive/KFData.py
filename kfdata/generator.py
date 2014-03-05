from jinja2 import Environment, PackageLoader

template_loader = PackageLoader('kfdata')
template_environment = Environment(trim_blocks=True, loader=template_loader)

class EntityWriter(object):
    template_name = None

    def __init__(self, entity):
        self.entity = entity

    def context(self):
        return {
            'kfattribute': True,
            'entity': self.entity,
        }

    def write(self, destination_file):
        template = template_environment.get_template(self.template_name)
        output = template.render(self.context())

        with open(destination_file, 'w') as f:
            f.write(output)


class EntityInterfaceWriter(EntityWriter):
    template_name = 'entity.h'

class EntityImplementationWriter(EntityWriter):
    template_name = 'entity.m'

