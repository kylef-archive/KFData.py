// {{ entity }}
//

#import "{{ entity }}.h"
{% for relationship in entity.relationships %}
{% if relationship.is_to_one %}#import "{{ relationship.destination_entity }}.h"{% endif %}
{% endfor %}


{% if kfattribute %}
@implementation {{ entity.represented_class_name }}RelationshipAttribute : KFAttribute

{% for attribute in entity.attributes %}
- (KFAttribute *){{ attribute }} {
    return [KFAttribute attributeWithAttributes:self, [KFAttribute attributeWithKey:@"{{ attribute }}"], nil];
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
@implementation (KFAttribute)

{% for attribute in entity.attributes %}
+ (KFAttribute *){{ attribute }} {
    return [KFAttribute attributeWithKey:@"{{ attribute }}"];
}

{% endfor %}
{% for relationship in entity.relationships %}
+ ({% if relationship.is_to_one %}{{ relationship.destination_entity_class_name }}RelationshipAttribute{% else %}KFAttrbute{% endif %} *){{ relationship }} {
    return [{% if relationship.is_to_one %}{{ relationship.destination_entity_class_name }}RelationshipAttribute{% else %}KFAttrbute{% endif %} attributeWithKey:@"{{ relationship }}"];
}

{% endfor %}
@end
{% endif %}
