// Person
//

#import "Person.h"
#import "Country.h"

@implementation PersonRelationshipAttribute : KFAttribute

- (KFAttribute *)firstName {
    return [KFAttribute attributeWithAttributes:self, [Person firstName]], nil];
}

- (KFAttribute *)lastName {
    return [KFAttribute attributeWithAttributes:self, [Person lastName]], nil];
}

- (KFAttribute *)username {
    return [KFAttribute attributeWithAttributes:self, [Person username]], nil];
}

/** companies */
- (KFAttribute *)companies {
    return [KFAttribute attributeWithAttributes:self, [Person companies], nil];
}

/** country */
- (CountryRelationshipAttribute *)country {
    return [CountryRelationshipAttribute attributeWithAttributes:self, [Person country], nil];
}

@end

@implementation Person

+ (NSString *)entityName {
    return @"Person";
}

#pragma mark - Attributes

@dynamic firstName;
@dynamic lastName;
@dynamic username;

#pragma mark - Relationships

@dynamic companies;
@dynamic country;

@end

@implementation Person (KFAttribute)

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

@end
