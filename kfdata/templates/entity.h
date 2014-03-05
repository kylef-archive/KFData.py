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

{% for relationship in entity.relationships %}
{% if relationship.is_to_one %}@class {{ relationship.destination_entity_class_name }}{% if kfattribute %}, {{ relationship.destination_entity_class_name }}RelationshipAttribute{% endif %};{% endif %}
{% endfor %}


{% if kfattribute %}
@interface {{ entity.represented_class_name }}RelationshipAttribute : KFAttribute

{% for attribute in entity.attributes %}
/** {{ attribute }} */
- (KFAttribute *){{ attribute }};

{% endfor %}
{% for relationship in entity.relationships %}
/** {{ relationship }} */
- ({% if relationship.is_to_one %}{{ relationship.destination_entity_class_name }}RelationshipAttribute{% else %}KFAttrbute{% endif %} *){{ relationship }};

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
@property (nonatomic, strong) {% if relationship.is_to_many %}NS{% if relationship.is_ordered %}Ordered{% endif %}Set{% else %}{{ relationship.destination_entity_class_name }}{% endif %} *{{ relationship.name }};

{% endfor %}
@end

{% if kfattribute %}
@implementation (KFAttribute)

{% for attribute in entity.attributes %}
/** {{ attribute }} */
+ (KFAttribute *){{ attribute }};

{% endfor %}
{% for relationship in entity.relationships %}
/** {{ relationship }} */
+ ({% if relationship.is_to_one %}{{ relationship.destination_entity_class_name }}RelationshipAttribute{% else %}KFAttrbute{% endif %} *){{ relationship }};

{% endfor %}
@end
{% endif %}
