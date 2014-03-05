// {{ entity }}
//

#import "{{ entity }}.h"

@implementation {{ entity.represented_class_name }}

+ (NSString *)entityName {
    return @"{{ entity }}";
}

#pragma mark - Attributes

{% for attribute in entity.attributes %}
@dynamic {{ attribute }};
{% endfor %}

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
