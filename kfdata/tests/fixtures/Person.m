// Person
//

#import "Person.h"

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
@dynamic parent;

@end

@implementation (KFAttribute)

+ (KFAttribute *)firstName {
    return [KFAttribute attributeWithKey:@"firstName"];
}

+ (KFAttribute *)lastName {
    return [KFAttribute attributeWithKey:@"lastName"];
}

+ (KFAttribute *)username {
    return [KFAttribute attributeWithKey:@"username"];
}

@end
