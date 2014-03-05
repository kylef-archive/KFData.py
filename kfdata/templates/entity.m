// {{ entity }}
//

#import "{{ entity }}.h"

@implementation {{entity.represented_class_name}}

+ (NSString *)entityName {
    return @"{{ entity }}";
}

{% if kfattribute %}
#pragma mark - Attributes

{% for attribute in entity.attributes %}
/** {{ attribute }} */
+ (KFAttribute *){{ attribute }} {
    return [KFAttribute attributeWithKey:@"{{ attribute }}"];
}

{% endfor %}
{% endif %}

{% for attribute in entity.attributes %}
@dynamic {{ attribute }};
{% endfor %}

@end

