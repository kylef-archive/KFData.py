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

{% for relationship in entity.to_one_relationships %}
@class {{ relationship.destination_entity_class_name }}{% if kfattribute %}, {{ relationship.destination_entity_class_name }}RelationshipAttribute{% endif %};
{% endfor %}

{% if kfattribute %}
@interface {{ entity.represented_class_name }}RelationshipAttribute : KFAttribute

{% for attribute in entity.attributes %}
/** {{ attribute }} */
- ({{ attribute.attribute_class }} *){{ attribute }};

{% endfor %}
{% for relationship in entity.relationships %}
/** {{ relationship }} */
- ({{ relationship.attribute_class }} *){{ relationship }};

{% endfor %}
@end
{% endif %}

@interface {{ entity.represented_class_name }} : {{ entity.super_class_name }}

+ (NSString *)entityName;

#pragma mark - Properties

{% for attribute in entity.attributes %}
/** {{ attribute.name }} ({% if attribute.is_optional %}optional{% else %}required{% endif %}) */
@property (nonatomic, {% if use_scalar_types and attribute.has_scalar_type %}assign{% else %}retain{% endif %}) {% if use_scalar_types and attribute.has_scalar_type %}{{ attribute.scalar_type }} {% else %}{{ attribute.class_name }}{% endif %}{{ attribute.name }};

{% endfor %}
{% for relationship in entity.relationships %}
/** {{ relationship.name }} ({% if relationship.is_optional %}optional{% else %}required{% endif %}) */
@property (nonatomic, retain) {{ relationship.class_name }}{{ relationship.name }};

{% endfor %}
@end

{% if entity.to_many_relationships %}
@interface {{ entity.represented_class_name }} (CoreDataGeneratedAccessors)

{% for relationship in entity.to_many_relationships %}
- (void)add{{ relationship|capitalize }}Object:(NSManagedObject *)value;
- (void)remove{{ relationship|capitalize }}Object:(NSManagedObject *)value;
- (void)add{{ relationship|capitalize }}:({{ relationship.class_name }})values;
- (void)remove{{ relationship|capitalize }}:({{ relationship.class_name }})values;

{% endfor %}
@end
{% endif %}

{% if kfattribute %}
@interface {{ entity.represented_class_name }} (KFAttribute)

{% for attribute in entity.attributes %}
/** {{ attribute }} */
+ (KFAttribute *){{ attribute }};

{% endfor %}
{% for relationship in entity.relationships %}
/** {{ relationship }} */
+ ({{ relationship.attribute_class }} *){{ relationship }};

{% endfor %}
@end
{% endif %}
