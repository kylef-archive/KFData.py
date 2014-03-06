class Attribute(object):
    class_name = 'id '

    def __init__(self, name, is_indexed=False, is_optional=False, is_transient=False):
        self.name = name
        self.is_indexed = is_indexed
        self.is_optional = is_optional
        self.is_transient = is_transient

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Attribute {}>'.format(self.name)

    def __eq__(self, other):
        return isinstance(other, Attribute) and \
                other.name == self.name and \
                other.is_indexed == self.is_indexed and \
                other.is_optional == self.is_optional and \
                other.is_transient == self.is_transient

    @property
    def attribute_class(self):
        return 'KFAttribute'

class DefaultAttribute(Attribute):
    def __init__(self, name, default_value=None, **kwargs):
        super(DefaultAttribute, self).__init__(name, **kwargs)
        self.default_value = default_value

    def __eq__(self, other):
        return isinstance(other, DefaultAttribute) and \
                super(DefaultAttribute, self).__eq__(other) and \
                other.default_value == self.default_value


class StringAttribute(DefaultAttribute):
    class_name = 'NSString *'

    def __init__(self, name, **kwargs):
        if 'default_value' not in kwargs:
            kwargs['default_value'] = ''

        super(StringAttribute, self).__init__(name, **kwargs)


class BooleanAttribute(DefaultAttribute):
    class_name = 'NSNumber *'

    def __init__(self, name, **kwargs):
        if 'default_value' not in kwargs:
            kwargs['default_value'] = False

        super(BooleanAttribute, self).__init__(name, **kwargs)

    def __eq__(self, other):
        return isinstance(other, BooleanAttribute) and \
                super(BooleanAttribute, self).__eq__(other)


class NumberAttribute(DefaultAttribute):
    number_type = int
    class_name = 'NSNumber *'

    def __init__(self, name, minimum_value=None, maximum_value=None, **kwargs):
        if 'default_value' not in kwargs:
            kwargs['default_value'] = 0

        super(NumberAttribute, self).__init__(name, **kwargs)
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value

    def __eq__(self, other):
        return isinstance(other, NumberAttribute) and \
                super(NumberAttribute, self).__eq__(other) and \
                other.minimum_value == self.minimum_value and \
                other.maximum_value == self.maximum_value


class Integer16Attribute(NumberAttribute):
    pass


class Integer32Attribute(NumberAttribute):
    pass


class Integer64Attribute(NumberAttribute):
    pass


class FloatAttribute(NumberAttribute):
    number_type = float


class DecimalAttribute(NumberAttribute):
    number_type = float


class DoubleAttribute(NumberAttribute):
    number_type = float


class DateAttribute(Attribute):
    class_name = 'NSDate *'


class BinaryAttribute(Attribute):
    class_name = 'NSData *'


class TransformerAttribute(Attribute):
    pass
