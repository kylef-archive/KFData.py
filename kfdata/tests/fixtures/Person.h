// Person
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>
#import <KFData/KFData.h>

@class Country, CountryRelationshipAttribute;

@interface PersonRelationshipAttribute : KFAttribute

/** age */
- (KFAttribute *)age;

/** firstName */
- (KFAttribute *)firstName;

/** lastName */
- (KFAttribute *)lastName;

/** username */
- (KFAttribute *)username;

/** companies */
- (KFAttribute *)companies;

/** country */
- (CountryRelationshipAttribute *)country;

@end

@interface Person : NSManagedObject

+ (NSString *)entityName;

#pragma mark - Properties

/** age (required) */
@property (nonatomic, assign) int32_t age;

/** firstName (optional) */
@property (nonatomic, strong) NSString *firstName;

/** lastName (optional) */
@property (nonatomic, strong) NSString *lastName;

/** username (required) */
@property (nonatomic, strong) NSString *username;

/** companies (optional) */
@property (nonatomic, strong) NSOrderedSet *companies;

/** country (required) */
@property (nonatomic, strong) Country *country;

@end

@implementation Person (CoreDataGeneratedAccessors)

- (void)addCompaniesObject:(NSManagedObject *)value;
- (void)removeCompaniesObject:(NSManagedObject *)value;
- (void)addCompanies:(NSOrderedSet *)values;
- (void)removeCompanies:(NSOrderedSet *)values;

@end

@implementation Person (KFAttribute)

/** age */
+ (KFAttribute *)age;

/** firstName */
+ (KFAttribute *)firstName;

/** lastName */
+ (KFAttribute *)lastName;

/** username */
+ (KFAttribute *)username;

/** companies */
+ (KFAttribute *)companies;

/** country */
+ (CountryRelationshipAttribute *)country;

@end
