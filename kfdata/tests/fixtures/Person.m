// Person
//

#import "Person.h"

@implementation Person

+ (NSString *)entityName {
    return @"Person";
}

#pragma mark - Attributes

/** firstName */
+ (KFAttribute *)firstName {
    return [KFAttribute attributeWithKey:@"firstName"];
}

/** lastName */
+ (KFAttribute *)lastName {
    return [KFAttribute attributeWithKey:@"lastName"];
}

/** username */
+ (KFAttribute *)username {
    return [KFAttribute attributeWithKey:@"username"];
}


@dynamic firstName;
@dynamic lastName;
@dynamic username;

@end
