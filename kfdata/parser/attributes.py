from kfdata.attributes import Attribute, BooleanAttribute, StringAttribute, NumberAttribute, DefaultAttribute


class AttributeParser(object):
    attribute_class = Attribute

    @classmethod
    def parse(cls, document):
        attribute_type = document.getAttribute('attributeType')
        return cls.attribute_type_parser(attribute_type).parse_attribute(document)

    @classmethod
    def parse_attribute(cls, document):
        name = document.getAttribute('name')
        is_indexed = document.getAttribute('indexed') == 'YES'
        is_optional = document.getAttribute('optional') == 'YES'
        attribute = cls.attribute_class(name, is_indexed=is_indexed,
                                        is_optional=is_optional)
        return attribute

    @classmethod
    def attribute_type_parser(cls, attribute_type):
        attribute_parsers = [
            StringAttributeParser,
            BooleanAttributeParser,
            NumberAttributeParser
        ]

        for parser in attribute_parsers:
            if attribute_type in parser.attribute_types:
                return parser

        return AttributeParser


class DefaultAttributeParser(AttributeParser):
    attribute_class = DefaultAttribute
    attribute_types = []

    @classmethod
    def parse_default_value_string(cls, document):
        return document.getAttribute('defaultValueString')

    @classmethod
    def parse_attribute(cls, document):
        attribute = super(DefaultAttributeParser, cls).parse_attribute(document)
        attribute.default_value = cls.parse_default_value_string(document)
        return attribute

class BooleanAttributeParser(DefaultAttributeParser):
    attribute_class = BooleanAttribute
    attribute_types = ['Boolean']

    @classmethod
    def parse_default_value_string(cls, document):
        return document.getAttribute('defaultValueString') == 'YES'

class StringAttributeParser(DefaultAttributeParser):
    attribute_class = StringAttribute
    attribute_types = ['String']

class NumberAttributeParser(DefaultAttributeParser):
    attribute_class = NumberAttribute
    attribute_types = ['Float', 'Double', 'Decimal', 'Integer 16', 'Integer 32', 'Integer 64']

    @classmethod
    def parse_default_value_string(cls, document):
        attribute_type = document.getAttribute('attributeType')

        classes = {
            'Float': float,
            'Double': float,
            'Decimal': float,
            'Integer 16': int,
            'Integer 32': int,
            'Integer 64': int,
        }

        default_value_string = document.getAttribute('defaultValueString')


        return classes[attribute_type](default_value_string)
