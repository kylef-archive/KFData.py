// {{ entity }}
//

#import <Foundation/Foundation.h>
{% if entity.parent_entity %}
#import "{{ entity.parent_entity }}.h"
{% else %}
#import <CoreData/CoreData.h>
{% endif %}


{{classes}}

@interface {{ entity.represented_class_name }} : {{ entity.super_class_name }}

+ (NSString *)entityName;

{% if kfattribute %}
#pragma mark - Attributes

{% for attribute in entity.attributes %}
/** {{ attribute }} */
+ (KFAttribute *){{ attribute }};

{% endfor %}
{% endif %}

#pragma mark - Properties

{% for attribute in entity.attributes %}
/** {{ attribute.name }} ({% if attribute.is_optional %}optional{% else %}required{% endif %}) */
@property (nonatomic, strong) {{ attribute.attribute_type }}{{ attribute.name }};

{% endfor %}
@end

