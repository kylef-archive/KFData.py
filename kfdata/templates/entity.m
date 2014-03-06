// {{ entity }}
//

#import "{{ entity }}.h"
{% for relationship in entity.relationships %}
{% if relationship.is_to_one %}#import "{{ relationship.destination_entity }}.h"{% endif %}
{% endfor %}


{% if kfattribute %}
@implementation {{ entity.represented_class_name }}RelationshipAttribute : KFAttribute

{% for attribute in entity.attributes %}
- ({{ attribute.attribute_class }} *){{ attribute }} {
    return [KFAttribute attributeWithAttributes:self, [{{ entity.represented_class_name }} {{ attribute }}]], nil];
}

{% endfor %}
{% for relationship in entity.relationships %}
/** {{ relationship }} */
- ({{ relationship.attribute_class }} *){{ relationship }} {
    return [{{ relationship.attribute_class }} attributeWithAttributes:self, [{{ entity.represented_class_name }} {{ relationship }}], nil];
}

{% endfor %}
@end
{% endif %}

@implementation {{ entity.represented_class_name }}

+ (NSString *)entityName {
    return @"{{ entity }}";
}

{% if entity.attributes %}
#pragma mark - Attributes

{% for attribute in entity.attributes %}
@dynamic {{ attribute }};
{% endfor %}
{% endif %}

{% if entity.relationships %}
#pragma mark - Relationships

{% for relationship in entity.relationships %}
@dynamic {{ relationship }};
{% endfor %}
{% endif %}

@end

{% if kfattribute %}
@implementation {{ entity.represented_class_name }} (KFAttribute)

{% for attribute in entity.attributes %}
+ ({{ attribute.attribute_class }} *){{ attribute }} {
    return [KFAttribute attributeWithKey:@"{{ attribute }}"];
}

{% endfor %}
{% for relationship in entity.relationships %}
+ ({{ relationship.attribute_class }} *){{ relationship }} {
    return [{{ relationship.attribute_class }} attributeWithKey:@"{{ relationship }}"];
}

{% endfor %}
@end
{% endif %}
