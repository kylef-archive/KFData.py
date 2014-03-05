// {{ entity }}
//

#import "{{ entity }}.h"

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
@end
{% endif %}
