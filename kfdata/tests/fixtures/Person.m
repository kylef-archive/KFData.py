// Person
//

#import "Person.h"

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
