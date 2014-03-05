// Person
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>
#import <KFData/KFData.h>



@interface Person : NSManagedObject

+ (NSString *)entityName;

#pragma mark - Properties

/** firstName (optional) */
@property (nonatomic, strong) firstName;

/** lastName (optional) */
@property (nonatomic, strong) lastName;

/** username (required) */
@property (nonatomic, strong) username;

@end

@implementation (KFAttribute)

/** firstName */
+ (KFAttribute *)firstName;

/** lastName */
+ (KFAttribute *)lastName;

/** username */
+ (KFAttribute *)username;

@end
