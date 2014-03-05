// Person
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>




@interface Person : NSManagedObject

+ (NSString *)entityName;

#pragma mark - Attributes

/** firstName */
+ (KFAttribute *)firstName;

/** lastName */
+ (KFAttribute *)lastName;

/** username */
+ (KFAttribute *)username;


#pragma mark - Properties

/** firstName (optional) */
@property (nonatomic, strong) firstName;

/** lastName (optional) */
@property (nonatomic, strong) lastName;

/** username (required) */
@property (nonatomic, strong) username;

@end
