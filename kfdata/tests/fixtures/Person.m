// Person
//

#import "Person.h"
#import "Country.h"

@implementation PersonRelationshipAttribute : KFAttribute

- (KFAttribute *)age {
    return [KFAttribute attributeWithAttributes:self, [Person age], nil];
}

- (KFAttribute *)firstName {
    return [KFAttribute attributeWithAttributes:self, [Person firstName], nil];
}

- (KFAttribute *)lastName {
    return [KFAttribute attributeWithAttributes:self, [Person lastName], nil];
}

- (KFAttribute *)username {
    return [KFAttribute attributeWithAttributes:self, [Person username], nil];
}

/** companies */
- (KFAttribute *)companies {
    return [KFAttribute attributeWithAttributes:self, [Person companies], nil];
}

/** country */
- (CountryRelationshipAttribute *)country {
    return [CountryRelationshipAttribute attributeWithAttributes:self, [Person country], nil];
}

/** camcelCaseRelation */
- (KFAttribute *)camcelCaseRelation {
    return [KFAttribute attributeWithAttributes:self, [Person camcelCaseRelation], nil];
}

@end

@implementation Person

+ (NSString *)entityName {
    return @"Person";
}

#pragma mark - Attributes

@dynamic age;
@dynamic firstName;
@dynamic lastName;
@dynamic username;

#pragma mark - Relationships

@dynamic companies;
@dynamic country;
@dynamic camcelCaseRelation;

@end

@implementation Person (KFAttribute)

+ (KFAttribute *)age {
    return [KFAttribute attributeWithKey:@"age"];
}

+ (KFAttribute *)firstName {
    return [KFAttribute attributeWithKey:@"firstName"];
}

+ (KFAttribute *)lastName {
    return [KFAttribute attributeWithKey:@"lastName"];
}

+ (KFAttribute *)username {
    return [KFAttribute attributeWithKey:@"username"];
}

+ (KFAttribute *)companies {
    return [KFAttribute attributeWithKey:@"companies"];
}

+ (CountryRelationshipAttribute *)country {
    return [CountryRelationshipAttribute attributeWithKey:@"country"];
}

+ (KFAttribute *)camcelCaseRelation {
    return [KFAttribute attributeWithKey:@"camcelCaseRelation"];
}

@end
