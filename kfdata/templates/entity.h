// {{ entity }}
//

#import <Foundation/Foundation.h>
{% if entity.parent_entity %}
#import "{{ entity.parent_entity }}.h"
{% else %}
#import <CoreData/CoreData.h>
{% endif %}
{% if kfattribute %}
#import <KFData/KFData.h>
{% endif %}

{{classes}}

{% if kfattribute %}
@interface {{ entity.represented_class_name }}RelationshipAttribute : KFAttribute

{% for attribute in entity.attributes %}
/** {{ attribute }} */
- (KFAttribute *){{ attribute }};

{% endfor %}
@end
{% endif %}

@interface {{ entity.represented_class_name }} : {{ entity.super_class_name }}

+ (NSString *)entityName;

#pragma mark - Properties

{% for attribute in entity.attributes %}
/** {{ attribute.name }} ({% if attribute.is_optional %}optional{% else %}required{% endif %}) */
@property (nonatomic, strong) {{ attribute.attribute_type }}{{ attribute.name }};

{% endfor %}
{% for relationship in entity.relationships %}
/** {{ relationship.name }} ({% if relationship.is_optional %}optional{% else %}required{% endif %}) */
@property (nonatomic, strong) {% if relationship.is_to_many %}NS{% if relationship.is_ordered %}Ordered{% endif %}Set *{% else %}id{% endif %} {{ relationship.name }};

{% endfor %}
@end

{% if kfattribute %}
@implementation (KFAttribute)

{% for attribute in entity.attributes %}
/** {{ attribute }} */
+ (KFAttribute *){{ attribute }};

{% endfor %}
@end
{% endif %}
