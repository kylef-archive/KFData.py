// Person
//

#import "Person.h"
#import "Country.h"

@implementation PersonRelationshipAttribute : KFAttribute

- (KFAttribute *)firstName {
    return [KFAttribute attributeWithAttributes:self, [KFAttribute attributeWithKey:@"firstName"], nil];
}

- (KFAttribute *)lastName {
    return [KFAttribute attributeWithAttributes:self, [KFAttribute attributeWithKey:@"lastName"], nil];
}

- (KFAttribute *)username {
    return [KFAttribute attributeWithAttributes:self, [KFAttribute attributeWithKey:@"username"], nil];
}

/** companies */
- (KFAttrbute *)companies {
    return [KFAttrbute attributeWithAttributes:self, [KFAttribute attributeWithKey:companies], nil];
}

/** country */
- (CountryRelationshipAttribute *)country {
    return [CountryRelationshipAttribute attributeWithAttributes:self, [KFAttribute attributeWithKey:country], nil];
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

+ (KFAttrbute *)companies {
    return [KFAttrbute attributeWithKey:@"companies"];
}

+ (CountryRelationshipAttribute *)country {
    return [CountryRelationshipAttribute attributeWithKey:@"country"];
}

@end
