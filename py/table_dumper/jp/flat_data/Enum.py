from enum import IntEnum


class GroundNodeType(IntEnum):
    none = 0
    WalkAble = 1
    JumpAble = 2
    TSSOnly = 3
    NotWalkAble = 2147483647


class BubbleType(IntEnum):
    Idle = 0
    Monologue = 1
    EmoticonNormal = 2
    EmoticonFavorite = 3
    EmoticonReward = 4
    EmoticonGiveGift = 5


class FurnitureCategory(IntEnum):
    Furnitures = 0
    Decorations = 1
    Interiors = 2


class FurnitureSubCategory(IntEnum):
    Table = 0
    Closet = 1
    Chair = 2
    Bed = 3
    FurnitureEtc = 4
    FurnitureSubCategory1 = 5
    Prop = 6
    HomeAppliance = 7
    WallDecoration = 8
    FloorDecoration = 9
    DecorationEtc = 10
    DecorationSubCategory1 = 11
    Floor = 12
    Background = 13
    Wallpaper = 14
    InteriorsSubCategory1 = 15
    All = 16


class FurnitureLocation(IntEnum):
    none = 0
    Inventory = 1
    Floor = 2
    WallLeft = 3
    WallRight = 4


class AcademyMessageConditions(IntEnum):
    none = 0
    FavorRankUp = 1
    AcademySchedule = 2
    Answer = 3
    Feedback = 4


class AcademyMessageTypes(IntEnum):
    none = 0
    Text = 1
    Image = 2


class VoiceEvent(IntEnum):
    OnTSA = 0
    FormationPickUp = 1
    CampaignResultDefeat = 2
    CampaignResultVictory = 3
    CharacterLevelUp = 4
    CharacterTranscendence = 5
    SkillLevelUp = 6
    Formation = 7
    CampaignCharacterSpawn = 8
    BattleStartTimeline = 9
    BattleVictoryTimeline = 10
    CharacterFavor = 11
    BattleMiss = 12
    BattleBlock = 13
    BattleCover = 14
    BattleMove = 15
    BattleMoveToForamtionBeacon = 16
    MGS_GameStart = 17
    MGS_CharacterSelect = 18
    MGS_Attacking = 19
    MGS_GeasGet = 20
    EXSkill = 21
    EXSkillLevel = 22
    EXSkill2 = 23
    EXSkillLevel2 = 24
    EXSkill3 = 25
    EXSkillLevel3 = 26
    EXSkill4 = 27
    EXSkillLevel4 = 28
    PublicSkill01 = 29
    PublicSkill02 = 30
    InteractionPublicSkill01 = 31
    InteractionPublicSkill02 = 32


class UnitType(IntEnum):
    none = 0
    AR = 1
    RF = 2
    HG = 3
    MG = 4
    SMG = 5
    SG = 6
    HZ = 7
    Melee = 8


class AttackType(IntEnum):
    Single = 0
    Splash = 1
    Through = 2
    Heal = 3


class ProjectileType(IntEnum):
    Guided = 0
    Ground = 1
    GuidedExplosion = 2
    GroundConstDistance = 3
    AirConstDistance = 4


class DamageFontColor(IntEnum):
    Blue = 0
    White = 1
    Yellow = 2
    Red = 3
    Green = 4


class TargetingCellType(IntEnum):
    none = 0
    Near = 1
    Far = 2


class TargetingUnitType(IntEnum):
    none = 0
    Near = 1
    Far = 2
    MinHp = 3
    MaxHp = 4
    Random = 5


class ProjectileAction(IntEnum):
    none = 0
    Damage = 1
    Heal = 2


class FontType(IntEnum):
    none = 0
    Damage = 1
    Block = 2
    Heal = 3
    Miss = 4
    Critical = 5
    Skill = 6
    Immune = 7
    DamageResist = 8
    DamageWeak = 9
    CriticalResist = 10
    CriticalWeak = 11
    Effective = 12
    CriticalEffective = 13


class EmoticonEvent(IntEnum):
    CoverEnter = 0
    ShelterEnter = 1
    Panic = 2
    NearlyDead = 3
    Reload = 4
    Found = 5
    GetBeacon = 6
    Warning = 7


class BulletType(IntEnum):
    Normal = 0
    Pierce = 1
    Explosion = 2
    Siege = 3
    Mystic = 4
    none = 5
    Sonic = 6


class ActionType(IntEnum):
    Crush = 0
    Courage = 1
    Tactic = 2


class BuffOverlap(IntEnum):
    Able = 0
    Unable = 1
    Change = 2
    Additive = 3


class ReArrangeTargetType(IntEnum):
    AllySelf = 0
    AllyAll = 1
    AllyUnitType = 2
    AllyGroup = 3


class ArmorType(IntEnum):
    LightArmor = 0
    HeavyArmor = 1
    Unarmed = 2
    Structure = 3
    Normal = 4
    ElasticArmor = 5


class WeaponType(IntEnum):
    none = 0
    SG = 1
    SMG = 2
    AR = 3
    GL = 4
    HG = 5
    RL = 6
    SR = 7
    DSMG = 8
    RG = 9
    DSG = 10
    Vulcan = 11
    Missile = 12
    Cannon = 13
    Taser = 14
    MG = 15
    Binah = 16
    MT = 17
    Relic = 18
    FT = 19


class EntityMaterialType(IntEnum):
    Wood = 0
    Stone = 1
    Flesh = 2
    Metal = 3


class CoverMotionType(IntEnum):
    All = 0
    Kneel = 1


class TargetSortBy(IntEnum):
    DISTANCE = 0
    HP = 1
    DAMAGE_EFFICIENCY = 2
    TARGETED_COUNT = 3
    RANDOM = 4
    FRONT_FORMATION = 5


class PositioningType(IntEnum):
    CloseToObstacle = 0
    CloseToTarget = 1


class DamageType(IntEnum):
    Normal = 0
    Critical = 1
    IgnoreDefence = 2


class FormationLine(IntEnum):
    Students = 0
    TSS = 1


class ExternalBTNodeType(IntEnum):
    Sequence = 0
    Selector = 1
    Instant = 2
    SubNode = 3
    ExecuteAll = 4


class ExternalBTTrigger(IntEnum):
    none = 0
    HPUnder = 1
    ApplySkillEffectCategory = 2
    HaveNextExSkillActiveGauge = 3
    UseNormalSkill = 4
    UseExSkill = 5
    CheckActiveGaugeOver = 6
    CheckPeriod = 7
    CheckSummonCharacterCountOver = 8
    CheckSummonCharacterCountUnder = 9
    ApplyGroggy = 10
    ApplyLogicEffectTemplateId = 11
    OnSpawned = 12
    CheckActiveGaugeBetween = 13
    DestroyParts = 14
    CheckHallucinationCountOver = 15
    CheckHallucinationCountUnder = 16
    UseSkillEndGroupId = 17


class ExternalBehavior(IntEnum):
    UseNextExSkill = 0
    ChangePhase = 1
    ChangeSection = 2
    AddActiveGauge = 3
    UseSelectExSkill = 4
    ClearNormalSkill = 5
    MoveLeft = 6
    MoveRight = 7
    AllUseSelectExSkill = 8
    ConnectCharacterToDummy = 9
    ConnectExSkillToParts = 10
    SetMaxHPToParts = 11
    AlivePartsUseExSkill = 12
    ActivatePart = 13
    AddGroggy = 14
    SelectTargetToUseSkillAlly = 15
    ForceChangePhase = 16
    ClearUseSkillEndGroupId = 17


class TacticEntityType(IntEnum):
    none = 0
    Student = 1
    Minion = 2
    Elite = 4
    Champion = 8
    Boss = 16
    Obstacle = 32
    Servant = 64
    Vehicle = 128
    Summoned = 256
    Hallucination = 512
    DestructibleProjectile = 1024


class BuffIconType(IntEnum):
    none = 0
    Debuff_DyingPenalty = 1
    CC_MindControl = 2
    CC_Inoperative = 3
    CC_Confusion = 4
    CC_Provoke = 5
    CC_Silence = 6
    CC_Blind = 7
    Dot_Damage = 8
    Dot_Heal = 9
    Buff_AttackPower = 10
    Buff_CriticalChance = 11
    Buff_CriticalDamage = 12
    Buff_DefensePower = 13
    Buff_Dodge = 14
    Buff_Hit = 15
    Buff_WeaponRange = 16
    Buff_SightRange = 17
    Buff_MoveSpeed = 18
    Buff_Mind = 19
    Debuf_AttackPower = 20
    Debuff_CriticalChance = 21
    Debuff_CriticalDamage = 22
    Debuff_DefensePower = 23
    Debuff_Dodge = 24
    Debuff_Hit = 25
    Debuff_WeaponRange = 26
    Debuff_SightRange = 27
    Debuff_MoveSpeed = 28
    Debuff_Mind = 29
    Buff_AttackTime = 30
    Debuff_AttackTime = 31
    Buff_MaxHp = 32
    Debuff_MaxHp = 33
    Buff_MaxBulletCount = 34
    Debuff_MaxBulletCount = 35
    Debuff_SuppliesCondition = 36
    Buff_HealEffectivenessRate = 37
    Debuff_HealEffectivenessRate = 38
    Buff_HealPower = 39
    Debuff_HealPower = 40
    Buff_CriticalChanceResistPoint = 41
    Debuff_CriticalChanceResistPoint = 42
    CC_Stunned = 43
    Debuff_ConcentratedTarget = 44
    Buff_Immortal = 45
    Max = 46


class Difficulty(IntEnum):
    Normal = 0
    Hard = 1
    VeryHard = 2
    Hardcore = 3
    Extreme = 4
    Insane = 5
    Torment = 6


class EngageType(IntEnum):
    SearchAndMove = 0
    HoldPosition = 1


class HitEffectPosition(IntEnum):
    Position = 0
    HeadBone = 1
    BodyBone = 2
    Follow = 3


class StageTopography(IntEnum):
    Street = 0
    Outdoor = 1
    Indoor = 2


class TerrainAdaptationStat(IntEnum):
    D = 0
    C = 1
    B = 2
    A = 3
    S = 4
    SS = 5


class SquadType(IntEnum):
    none = 0
    Main = 1
    Support = 2
    TSS = 3


class ObstacleClass(IntEnum):
    MAIN = 0
    SUB = 1


class ObstacleDestroyType(IntEnum):
    Remain = 0
    Remove = 1


class ObstacleHeightType(IntEnum):
    Low = 0
    Middle = 1
    High = 2


class ObstacleCoverType(IntEnum):
    none = 0
    Cover = 1
    Shelter = 2


class SkillCategory(IntEnum):
    none = 0


class LogicEffectCategory(IntEnum):
    none = 0
    Attack = 1
    Heal = 2
    Buff = 3
    Debuff = 4
    CrowdControl = 5
    Boss = 6
    Dummy = 7


class AimIKType(IntEnum):
    none = 0
    OneHandRight = 1
    OneHandLeft = 2
    TwoHandRight = 3
    TwoHandLeft = 4
    Tripod = 5
    Dual = 6
    Max = 7


class DamageAttribute(IntEnum):
    Resist = 0
    Normal = 1
    Weak = 2
    Effective = 3


class SkillPriorityCheckCondition(IntEnum):
    none = 0
    HPRateUnder = 1
    DebuffCountOver = 2
    BuffCountOver = 3
    CrowdControlOver = 4


class SkillPriorityCheckTarget(IntEnum):
    Ally = 0
    Enemy = 1
    All = 2


class StageType(IntEnum):
    Main = 0
    Sub = 1


class OperatorCondition(IntEnum):
    none = 0
    StrategyStart = 1
    StrategyVictory = 2
    StrategyDefeat = 3
    AdventureCombatStart = 4
    AdventureCombatVictory = 5
    AdventureCombatDefeat = 6
    ArenaCombatStart = 7
    ArenaCombatVictory = 8
    ArenaCombatDefeat = 9
    WeekDungeonCombatStart = 10
    WeekDungeonCombatVictory = 11
    WeekDungeonCombatDefeat = 12
    SchoolDungeonCombatStart = 13
    SchoolDungeonCombatVictory = 14
    SchoolDungeonCombatDefeat = 15
    StrategyWarpUnitFromHideTile = 16
    TimeAttackDungeonStart = 17
    TimeAttackDungeonVictory = 18
    TimeAttackDungeonDefeat = 19
    WorldRaidBossSpawn = 20
    WorldRaidBossKill = 21
    WorldRaidBossDamaged = 22
    WorldRaidScenarioBattle = 23
    MinigameTBGThemaOpen = 24
    MinigameTBGThemaComeback = 25
    MinigameTBGAllyRevive = 26
    MinigameTBGItemUse = 27


class KnockbackDirection(IntEnum):
    TargetToCaster = 0
    CasterToTarget = 1
    TargetToHitPosition = 2
    HitPositionToTarget = 3
    CasterToHitPosition = 4
    HitPositionToCaster = 5
    Caster = 6
    Target = 7


class EndCondition(IntEnum):
    Duration = 0
    ReloadCount = 1
    AmmoCount = 2
    AmmoHit = 3
    HitCount = 4
    none = 5
    UseExSkillCount = 6


class LogicEffectSound(IntEnum):
    none = 0
    Damage = 1
    Heal = 2
    Knockback = 3


class EffectBone(IntEnum):
    none = 0
    Shot = 1
    Head = 2
    Body = 3
    Shot2 = 4
    Shot3 = 5
    Extra = 6
    Extra2 = 7
    Extra3 = 8


class ArenaSimulatorServer(IntEnum):
    Preset = 0
    Live = 1
    Dev = 2
    QA = 3


class ClearCheck(IntEnum):
    none = 0
    Success_Play = 1
    Success_Sweep = 2
    Fail_Timeout = 3
    Fail_PlayerGiveUp = 4
    Fail_Annihilation = 5


class BuffType(IntEnum):
    none = 0
    Buff_AttackPower = 1
    Buff_CriticalChance = 2
    Buff_CriticalDamage = 3
    Buff_DefensePower = 4
    Buff_Dodge = 5
    Buff_Hit = 6
    Buff_WeaponRange = 7
    Buff_SightRange = 8
    Buff_MoveSpeed = 9
    Buff_AttackTime = 10
    Buff_MaxHp = 11
    Buff_MaxBulletCount = 12
    DeBuff_AttackPower = 13
    DeBuff_CriticalChance = 14
    DeBuff_CriticalDamage = 15
    DeBuff_DefensePower = 16
    DeBuff_Dodge = 17
    DeBuff_Hit = 18
    DeBuff_WeaponRange = 19
    DeBuff_SightRange = 20
    DeBuff_MoveSpeed = 21
    DeBuff_AttackTime = 22
    DeBuff_MaxHp = 23
    DeBuff_MaxBulletCount = 24


class WorldRaidDifficulty(IntEnum):
    none = 0
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7


class TacticSpeed(IntEnum):
    none = 0
    Slow = 1
    Normal = 2
    Fast = 3


class TacticSkillUse(IntEnum):
    none = 0
    Auto = 1
    Manual = 2


class ShowSkillCutIn(IntEnum):
    none = 0
    Once = 1
    Always = 2


class BattleCalculationStat(IntEnum):
    FinalDamage = 0
    FinalHeal = 1
    FinalDamageRatio = 2
    FinalDamageRatio2 = 3
    FinalCriticalRate = 4


class StatTransType(IntEnum):
    SpecialTransStat = 0
    TSATransStat = 1


class StatLevelUpType(IntEnum):
    Standard = 0
    Premature = 1
    LateBloom = 2
    Obstacle = 3
    TimeAttack = 4


class GrowthCategory(IntEnum):
    none = 0
    LevelUp = 1
    Transcend = 2
    SkillLevelUp = 3


class StatType(IntEnum):
    none = 0
    MaxHP = 1
    AttackPower = 2
    DefensePower = 3
    HealPower = 4
    AccuracyPoint = 5
    AccuracyRate = 6
    DodgePoint = 7
    DodgeRate = 8
    CriticalPoint = 9
    CriticalChanceRate = 10
    CriticalResistChanceRate = 11
    CriticalDamageRate = 12
    MoveSpeed = 13
    SightRange = 14
    ActiveGauge = 15
    StabilityPoint = 16
    StabilityRate = 17
    ReloadTime = 18
    MaxBulletCount = 19
    IgnoreDelayCount = 20
    WeaponRange = 21
    BlockRate = 22
    BodyRadius = 23
    ActionCount = 24
    StrategyMobility = 25
    StrategySightRange = 26
    StreetBattleAdaptation = 27
    OutdoorBattleAdaptation = 28
    IndoorBattleAdaptation = 29
    HealEffectivenessRate = 30
    CriticalChanceResistPoint = 31
    CriticalDamageResistRate = 32
    LifeRecoverOnHit = 33
    NormalAttackSpeed = 34
    AmmoCost = 35
    GroggyGauge = 36
    GroggyTime = 37
    DamageRatio = 38
    DamagedRatio = 39
    OppressionPower = 40
    OppressionResist = 41
    RegenCost = 42
    InitialWeaponRangeRate = 43
    DefensePenetration = 44
    DefensePenetrationResisit = 45
    ExtendBuffDuration = 46
    ExtendDebuffDuration = 47
    ExtendCrowdControlDuration = 48
    EnhanceExplosionRate = 49
    EnhancePierceRate = 50
    EnhanceMysticRate = 51
    EnhanceLightArmorRate = 52
    EnhanceHeavyArmorRate = 53
    EnhanceUnarmedRate = 54
    EnhanceSiegeRate = 55
    EnhanceNormalRate = 56
    EnhanceStructureRate = 57
    EnhanceNormalArmorRate = 58
    DamageRatio2Increase = 59
    DamageRatio2Decrease = 60
    DamagedRatio2Increase = 61
    DamagedRatio2Decrease = 62
    EnhanceSonicRate = 63
    EnhanceElasticArmorRate = 64
    ExDamagedRatioIncrease = 65
    ExDamagedRatioDecrease = 66
    Max = 67


class ProductionStep(IntEnum):
    ToDo = 0
    Doing = 1
    Complete = 2
    Release = 3


class TacticRole(IntEnum):
    none = 0
    DamageDealer = 1
    Tanker = 2
    Supporter = 3
    Healer = 4
    Vehicle = 5


class TacticRange(IntEnum):
    Back = 0
    Front = 1
    Middle = 2


class CVCollectionType(IntEnum):
    CVNormal = 0
    CVEvent = 1
    CVEtc = 2


class CVPrintType(IntEnum):
    CharacterOverwrite = 0
    PrefabOverwrite = 1
    Add = 2


class CVExceptionTarget(IntEnum):
    CharacterId = 0
    SquadType = 1


class PotentialStatBonusRateType(IntEnum):
    none = 0
    MaxHP = 1
    AttackPower = 2
    HealPower = 3


class ClanSocialGrade(IntEnum):
    none = 0
    President = 1
    Manager = 2
    Member = 3
    Applicant = 4
    Refused = 5
    Kicked = 6
    Quit = 7
    VicePredisident = 8


class ClanJoinOption(IntEnum):
    Free = 0
    Permission = 1
    All = 2


class ClanSearchOption(IntEnum):
    Name = 0
    Id = 1


class ClanRewardType(IntEnum):
    none = 0
    AssistTerm = 1
    AssistRent = 2
    Attendance = 3


class ConquestEnemyType(IntEnum):
    none = 0
    Normal = 1
    MiddleBoss = 2
    Boss = 3
    UnexpectedEvent = 4
    Challenge = 5
    IndividualErosion = 6
    MassErosion = 7


class ConquestTeamType(IntEnum):
    none = 0
    Team1 = 1
    Team2 = 2
    Team3 = 3


class ConquestTileType(IntEnum):
    none = 0
    Start = 1
    Normal = 2
    Battle = 3
    Base = 4


class ConquestObjectType(IntEnum):
    none = 0
    ParcelOneTimePerAccount = 1


class ConquestItemType(IntEnum):
    none = 0
    EventPoint = 1
    EventToken1 = 2
    EventToken2 = 3
    EventToken3 = 4
    EventToken4 = 5
    EventToken5 = 6


class ConquestProgressType(IntEnum):
    none = 0
    Upgrade = 1
    Manage = 2


class TileState(IntEnum):
    none = 0
    PartiallyConquested = 1
    FullyConquested = 2


class ConquestEventType(IntEnum):
    none = 0
    Event01 = 1
    Event02 = 2


class ConquestConditionType(IntEnum):
    none = 0
    OpenDateOffset = 1
    ItemAcquire = 2
    ParcelUse = 3
    KillUnit = 4


class ConquestErosionType(IntEnum):
    none = 0
    IndividualErosion = 1
    MassErosion = 2


class ContentType(IntEnum):
    none = 0
    CampaignMainStage = 1
    CampaignSubStage = 2
    WeekDungeon = 3
    EventContentMainStage = 4
    EventContentSubStage = 5
    CampaignTutorialStage = 6
    EventContentMainGroundStage = 7
    SchoolDungeon = 8
    TimeAttackDungeon = 9
    Raid = 10
    Conquest = 11
    EventContentStoryStage = 12
    CampaignExtraStage = 13
    StoryStrategyStage = 14
    ScenarioMode = 15
    EventContent = 16
    WorldRaid = 17
    EliminateRaid = 18
    Chaser = 19
    FieldContentStage = 20
    MultiFloorRaid = 21


class EventContentType(IntEnum):
    Stage = 0
    Gacha = 1
    Mission = 2
    Shop = 3
    Raid = 4
    Arena = 5
    BoxGacha = 6
    Collection = 7
    Recollection = 8
    MiniGameRhythm = 9
    CardShop = 10
    EventLocation = 11
    MinigameRhythmEvent = 12
    FortuneGachaShop = 13
    SubEvent = 14
    EventMeetup = 15
    BoxGachaResult = 16
    Conquest = 17
    WorldRaid = 18
    DiceRace = 19
    MiniGameRhythmMission = 20
    WorldRaidEntrance = 21
    MiniEvent = 22
    MiniGameShooting = 23
    MiniGameShootingMission = 24
    MiniGameTBG = 25
    TimeAttackDungeon = 26
    EliminateRaid = 27
    Treasure = 28
    Field = 29
    MultiFloorRaid = 30
    MinigameDreamMaker = 31


class OpenCondition(IntEnum):
    Hide = 0
    Lock = 1
    Open = 2


class ResetContentType(IntEnum):
    none = 0
    HardStagePlay = 1
    StarategyMapHeal = 2
    ShopRefresh = 3
    ArenaDefenseVictoryReward = 4
    WeeklyMasterCoin = 5
    WorldRaidGemEnterCount = 6
    ConquestDailyErosionCheck = 7
    MiniEventToken = 8


class WeekDungeonType(IntEnum):
    none = 0
    ChaserA = 1
    ChaserB = 2
    ChaserC = 3
    FindGift = 4
    Blood = 5


class StarGoalType(IntEnum):
    none = 0
    AllAlive = 1
    Clear = 2
    GetBoxes = 3
    ClearTimeInSec = 4


class OpenConditionContent(IntEnum):
    Shop = 0
    Gacha = 1
    LobbyIllust = 2
    Raid = 3
    Cafe = 4
    Unit_Growth_Skill = 5
    Unit_Growth_LevelUp = 6
    Unit_Growth_Transcendence = 7
    Arena = 8
    Academy = 9
    Equip = 10
    Item = 11
    Favor = 12
    Prologue = 13
    Mission = 14
    WeekDungeon_Chase = 15
    __Deprecated_WeekDungeon_FindGift = 16
    __Deprecated_WeekDungeon_Blood = 17
    Story_Sub = 18
    Story_Replay = 19
    WeekDungeon = 20
    none = 21
    Shop_Gem = 22
    Craft = 23
    Student = 24
    GuideMission = 25
    Clan = 26
    Echelon = 27
    Campaign = 28
    EventContent = 29
    Guild = 30
    EventStage_1 = 31
    EventStage_2 = 32
    Talk = 33
    Billing = 34
    Schedule = 35
    Story = 36
    Tactic_Speed = 37
    Cafe_Invite = 38
    EventMiniGame_1 = 39
    SchoolDungeon = 40
    TimeAttackDungeon = 41
    ShiftingCraft = 42
    WorldRaid = 43
    Tactic_Skip = 44
    Mulligan = 45
    EventPermanent = 46
    Main_L_1_2 = 47
    Main_L_1_3 = 48
    Main_L_1_4 = 49
    EliminateRaid = 50
    Cafe_2 = 51
    Cafe_Invite_2 = 52
    MultiFloorRaid = 53
    StrategySkip = 54
    MinigameDreamMaker = 55


class ContentLockType(IntEnum):
    none = 0
    NotUseControlledByOtherSetting = 1
    Academy = 2
    MultiFloorRaid = 3
    EventContent = 4
    EventNotice = 5
    GuideMission = 6
    Campaign = 7
    Story = 8
    WeekDungeon_Chase = 9
    WeekDungeon = 10
    SchoolDungeon = 11
    Raid = 12
    EliminateRaid = 13
    TimeAttackDungeon = 14
    Arena = 15
    Cafe = 16
    GemShop = 17
    Gacha = 18
    Craft = 19
    MomoTalk = 20


class TutorialFailureContentType(IntEnum):
    none = 0
    Campaign = 1
    WeekDungeon = 2
    Raid = 3
    TimeAttackDungeon = 4
    WorldRaid = 5
    Conquest = 6
    EliminateRaid = 7
    MultiFloorRaid = 8


class FeverBattleType(IntEnum):
    Campaign = 0
    Raid = 1
    WeekDungeon = 2
    Arena = 3


class EventContentScenarioConditionType(IntEnum):
    none = 0
    DayAfter = 1
    EventPoint = 2


class EventTargetType(IntEnum):
    WeekDungeon = 0
    Chaser = 1
    Campaign_Normal = 2
    Campaign_Hard = 3
    SchoolDungeon = 4
    AcademySchedule = 5
    TimeAttackDungeon = 6
    AccountLevelExpIncrease = 7
    Raid = 8
    EliminateRaid = 9


class ContentResultType(IntEnum):
    Failure = 0
    Success = 1


class EventContentItemType(IntEnum):
    EventPoint = 0
    EventToken1 = 1
    EventToken2 = 2
    EventToken3 = 3
    EventToken4 = 4
    EventToken5 = 5
    EventMeetUpTicket = 6


class RaidSeasonType(IntEnum):
    none = 0
    Open = 1
    Close = 2
    Settlement = 3


class BuffConditionType(IntEnum):
    All = 0
    Character = 1
    School = 2
    Weapon = 3


class EventCollectionUnlockType(IntEnum):
    none = 0
    ClearSpecificEventStage = 1
    ClearSpecificEventScenario = 2
    ClearSpecificEventMission = 3
    PurchaseSpecificItemCount = 4
    SpecificEventLocationRank = 5
    DiceRaceConsumeDiceCount = 6
    MinigameTBGThemaClear = 7
    MinigameEnter = 8
    MinigameDreamMakerParameter = 9


class ShortcutContentType(IntEnum):
    none = 0
    CampaignStage = 1
    EventStage = 2
    Blood = 3
    WeekDungeon = 4
    Arena = 5
    Raid = 6
    Shop = 7
    ItemInventory = 8
    Craft = 9
    SchoolDungeon = 10
    Academy = 11
    Mission = 12
    MultiFloorRaid = 13


class JudgeGrade(IntEnum):
    none = 0
    Miss = 1
    Attack = 2
    Critical = 3


class SchoolDungeonType(IntEnum):
    SchoolA = 0
    SchoolB = 1
    SchoolC = 2
    none = 3


class EventContentBuffFindRule(IntEnum):
    none = 0
    WeaponType = 1
    SquadType = 2
    StreetBattleAdaptation = 3
    OutdoorBattleAdaptation = 4
    IndoorBattleAdaptation = 5
    BulletType = 6
    School = 7
    TacticRange = 8


class TimeAttackDungeonRewardType(IntEnum):
    Fixed = 0
    TimeWeight = 1


class TimeAttackDungeonType(IntEnum):
    none = 0
    Defense = 1
    Shooting = 2
    Destruction = 3
    Escort = 4


class SuddenMissionContentType(IntEnum):
    OrdinaryState = 0
    CampaignNormalStage = 1
    CampaignHardStage = 2
    EventStage = 3
    WeekDungeon = 4
    Chaser = 5
    SchoolDungeon = 6
    TimeAttackDungeon = 7
    Raid = 8


class ContentsChangeType(IntEnum):
    none = 0
    WorldRaidBossDamageRatio = 1
    WorldRaidBossGroupDate = 2


class EventNotifyType(IntEnum):
    RewardIncreaseEvent = 0
    AccountExpIncreaseEvent = 1
    RaidSeasonManager = 2
    TimeAttackDungeonSeasonManage = 3
    EliminateRaidSeasonManage = 4


class EventContentDiceRaceResultType(IntEnum):
    DiceResult1 = 0
    DiceResult2 = 1
    DiceResult3 = 2
    DiceResult4 = 3
    DiceResult5 = 4
    DiceResult6 = 5
    MoveForward = 6
    LapFinish = 7
    EventOccur = 8
    DiceResultFixed1 = 9
    DiceResultFixed2 = 10
    DiceResultFixed3 = 11
    DiceResultFixed4 = 12
    DiceResultFixed5 = 13
    DiceResultFixed6 = 14
    SpecialReward = 15


class EventContentDiceRaceNodeType(IntEnum):
    StartNode = 0
    RewardNode = 1
    MoveForwardNode = 2
    SpecialRewardNode = 3


class MeetupConditionType(IntEnum):
    none = 0
    EventContentStageClear = 1
    ScenarioClear = 2


class MeetupConditionPrintType(IntEnum):
    none = 0
    Lock = 1
    Hide = 2


class GuideMissionTabType(IntEnum):
    none = 0
    Daily = 1
    StageClear = 2


class RankingSearchType(IntEnum):
    none = 0
    Rank = 1
    Score = 2


class EventContentReleaseType(IntEnum):
    none = 0
    Permanent = 1
    MainStory = 2
    PermanentSpecialOperate = 3


class CraftSlotIndex(IntEnum):
    Slot00 = 0
    Slot01 = 1
    Slot02 = 2
    Max = 3


class CraftNodeTier(IntEnum):
    Base = 0
    Node01 = 1
    Node02 = 2
    Node03 = 3
    Max = 4


class SubEventType(IntEnum):
    none = 0
    SubEvent = 1
    SubEventPermanent = 2


class EquipmentCategory(IntEnum):
    Unable = 0
    Exp = 1
    Bag = 2
    Hat = 3
    Gloves = 4
    Shoes = 5
    Badge = 6
    Hairpin = 7
    Charm = 8
    Watch = 9
    Necklace = 10
    WeaponExpGrowthA = 11
    WeaponExpGrowthB = 12
    WeaponExpGrowthC = 13
    WeaponExpGrowthZ = 14


class EquipmentOptionType(IntEnum):
    none = 0
    MaxHP_Base = 1
    MaxHP_Coefficient = 2
    AttackPower_Base = 3
    AttackPower_Coefficient = 4
    DefensePower_Base = 5
    DefensePower_Coefficient = 6
    HealPower_Base = 7
    HealPower_Coefficient = 8
    CriticalPoint_Base = 9
    CriticalPoint_Coefficient = 10
    CriticalChanceRate_Base = 11
    CriticalDamageRate_Base = 12
    CriticalDamageRate_Coefficient = 13
    SightRange_Base = 14
    SightRange_Coefficient = 15
    MaxBulletCount_Base = 16
    MaxBulletCount_Coefficient = 17
    HPRecoverOnKill_Base = 18
    HPRecoverOnKill_Coefficient = 19
    StreetBattleAdaptation_Base = 20
    OutdoorBattleAdaptation_Base = 21
    IndoorBattleAdaptation_Base = 22
    HealEffectivenessRate_Base = 23
    HealEffectivenessRate_Coefficient = 24
    CriticalChanceResistPoint_Base = 25
    CriticalChanceResistPoint_Coefficient = 26
    CriticalDamageResistRate_Base = 27
    CriticalDamageResistRate_Coefficient = 28
    ExSkillUpgrade = 29
    OppressionPower_Base = 30
    OppressionPower_Coefficient = 31
    OppressionResist_Base = 32
    OppressionResist_Coefficient = 33
    StabilityPoint_Base = 34
    StabilityPoint_Coefficient = 35
    AccuracyPoint_Base = 36
    AccuracyPoint_Coefficient = 37
    DodgePoint_Base = 38
    DodgePoint_Coefficient = 39
    MoveSpeed_Base = 40
    MoveSpeed_Coefficient = 41
    Max = 42
    NormalAttackSpeed_Base = 43
    NormalAttackSpeed_Coefficient = 44
    DefensePenetration_Base = 45
    DefensePenetrationResisit_Base = 46
    ExtendBuffDuration_Base = 47
    ExtendDebuffDuration_Base = 48
    ExtendCrowdControlDuration_Base = 49
    EnhanceExplosionRate_Base = 50
    EnhanceExplosionRate_Coefficient = 51
    EnhancePierceRate_Base = 52
    EnhancePierceRate_Coefficient = 53
    EnhanceMysticRate_Base = 54
    EnhanceMysticRate_Coefficient = 55
    EnhanceLightArmorRate_Base = 56
    EnhanceLightArmorRate_Coefficient = 57
    EnhanceHeavyArmorRate_Base = 58
    EnhanceHeavyArmorRate_Coefficient = 59
    EnhanceUnarmedRate_Base = 60
    EnhanceUnarmedRate_Coefficient = 61
    EnhanceSiegeRate_Base = 62
    EnhanceSiegeRate_Coefficient = 63
    EnhanceNormalRate_Base = 64
    EnhanceNormalRate_Coefficient = 65
    EnhanceStructureRate_Base = 66
    EnhanceStructureRate_Coefficient = 67
    EnhanceNormalArmorRate_Base = 68
    EnhanceNormalArmorRate_Coefficient = 69
    DamageRatio2Increase_Base = 70
    DamageRatio2Increase_Coefficient = 71
    DamageRatio2Decrease_Base = 72
    DamageRatio2Decrease_Coefficient = 73
    DamagedRatio2Increase_Base = 74
    DamagedRatio2Increase_Coefficient = 75
    DamagedRatio2Decrease_Base = 76
    DamagedRatio2Decrease_Coefficient = 77
    EnhanceSonicRate_Base = 78
    EnhanceSonicRate_Coefficient = 79
    EnhanceElasticArmorRate_Base = 80
    EnhanceElasticArmorRate_Coefficient = 81
    IgnoreDelayCount_Base = 82
    WeaponRange_Base = 83
    BlockRate_Base = 84
    BlockRate_Coefficient = 85
    AmmoCost_Base = 86
    RegenCost_Base = 87
    RegenCost_Coefficient = 88


class MultipleConditionCheckType(IntEnum):
    And = 0
    Or = 1


class Language(IntEnum):
    Kr = 0
    Jp = 1
    Th = 2
    Tw = 3
    En = 4


class SoundType(IntEnum):
    UI = 0
    BGM = 1
    FX = 2


class WeekDay(IntEnum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    All = 7


class EchelonType(IntEnum):
    none = 0
    Adventure = 1
    Raid = 2
    ArenaAttack = 3
    ArenaDefence = 4
    WeekDungeonChaserA = 5
    Scenario = 6
    WeekDungeonBlood = 7
    WeekDungeonChaserB = 8
    WeekDungeonChaserC = 9
    WeekDungeonFindGift = 10
    EventContent = 11
    SchoolDungeonA = 12
    SchoolDungeonB = 13
    SchoolDungeonC = 14
    TimeAttack = 15
    WorldRaid = 16
    Conquest = 17
    ConquestManage = 18
    StoryStrategyStage = 19
    EliminateRaid01 = 20
    EliminateRaid02 = 21
    EliminateRaid03 = 22
    Field = 23
    MultiFloorRaid = 24


class EchelonExtensionType(IntEnum):
    Base = 0
    Extension = 1


class NoticeType(IntEnum):
    none = 0
    Notice = 1
    Event = 2


class RewardTag(IntEnum):
    Default = 0
    FirstClear = 1
    StrategyObject = 2
    Event = 3
    ThreeStar = 4
    ProductMonthly = 5
    Rare = 6
    EventBonus = 7
    TimeWeight = 8
    ProductWeekly = 9
    ProductBiweekly = 10
    EventPermanentReward = 11
    ConquestManageEvent = 12
    ConquestManageDefault = 13
    ConquestCalculateDefault = 14
    ConquestCalculateLevel2 = 15
    ConquestCalculateLevel3 = 16
    ConquestFootholdUpgrade2 = 17
    ConquestFootholdUpgrade3 = 18
    ConquestErosionPenalty = 19
    GemBonus = 20
    GemPaid = 21


class ArenaRewardType(IntEnum):
    none = 0
    Time = 1
    Daily = 2
    SeasonRecord = 3
    OverallRecord = 4
    SeasonClose = 5
    AttackVictory = 6
    DefenseVictory = 7
    RankIcon = 8


class ServiceActionType(IntEnum):
    ClanCreate = 0
    HardAdventurePlayCountRecover = 1


class RaidStatus(IntEnum):
    none = 0
    Playing = 1
    Clear = 2
    Close = 3


class WebAPIErrorLevel(IntEnum):
    none = 0
    Warning = 1
    Error = 2


class GachaTicketType(IntEnum):
    none = 0
    PackageThreeStar = 1
    ThreeStar = 2
    TwoStar = 3
    Normal = 4
    NormalOnce = 5
    SelectRecruit = 6
    PackagePropertyThreeStar = 7
    Temp_1 = 8
    PackageAcademyThreeStar = 9


class EventChangeType(IntEnum):
    MainSub = 0
    SubMain = 1


class CafeCharacterState(IntEnum):
    none = 0
    Idle = 1
    Walk = 2
    Reaction = 3
    Interaction = 4
    Max = 5


class FurnitureFunctionType(IntEnum):
    none = 0
    EventCollection = 1
    VideoPlay = 2
    TrophyCollection = 3
    InteractionBGMPlay = 4


class NotificationEventReddot(IntEnum):
    StagePointReward = 0
    MissionComplete = 1
    MiniGameMissionComplete = 2
    WorldRaidReward = 3
    ConquestCalculateReward = 4
    DiceRaceLapReward = 5


class EmblemCategory(IntEnum):
    none = 0
    Default = 1
    Mission = 2
    GroupStory = 3
    Event = 4
    MainStory = 5
    Favor = 6
    Boss = 7
    Etc = 8
    Etc_Anniversary = 9
    MultiFloorRaid = 10
    Potential = 11


class EmblemDisplayType(IntEnum):
    Always = 0
    Time = 1
    Favor = 2
    Potential = 3


class EmblemCheckPassType(IntEnum):
    none = 0
    Default = 1
    Favor = 2
    Story = 3
    Potential = 4


class StickerGetConditionType(IntEnum):
    none = 0
    StickerCheckPass = 1
    GetStickerCondition = 2


class Nation(IntEnum):
    none = 0
    All = 1
    JP = 2
    GL = 3
    KR = 4


class FilterCategory(IntEnum):
    Character = 0
    Equipment = 1
    Item = 2
    Craft = 3
    ShiftCraft = 4
    Shop = 5
    MemoryLobby = 6
    Trophy = 7
    Emblem = 8


class FilterIcon(IntEnum):
    TextOnly = 0
    TextWithIcon = 1
    Pin = 2
    Role = 3
    CharacterStar = 4
    WeaponStar = 5
    Attack = 6
    Defense = 7
    Range = 8
    MemoryLobby = 9


class FieldConditionType(IntEnum):
    Invalid = 0
    Interaction = 1
    QuestInProgress = 2
    QuestClear = 3
    Date = 4
    StageClear = 5
    HasKeyword = 6
    HasEvidence = 7
    OpenDate = 8
    OpenDateAfter = 9


class FieldInteractionType(IntEnum):
    none = 0
    Scenario = 1
    Reward = 2
    Dialog = 3
    Stage = 4
    KeywordFound = 5
    EvidenceFound = 6
    SceneChange = 7
    Timeline = 8
    ActionTrigger = 9
    Interplay = 10


class FieldConditionClass(IntEnum):
    AndOr = 0
    OrAnd = 1
    Multi = 2


class FieldDialogType(IntEnum):
    none = 0
    Talk = 1
    Think = 2
    Exclaim = 3
    Question = 4
    Upset = 5
    Surprise = 6
    Bulb = 7
    Heart = 8
    Sweat = 9
    Angry = 10
    Music = 11
    Dot = 12
    Momotalk = 13
    Phone = 14
    Keyword = 15
    Evidence = 16


class FieldTutorialType(IntEnum):
    none = 0
    MasteryHUD = 1
    QuestHUD = 2
    WorldMapHUD = 3


class FriendSearchLevelOption(IntEnum):
    Recommend = 0
    All = 1
    Level1To30 = 2
    Level31To40 = 3
    Level41To50 = 4
    Level51To60 = 5
    Level61To70 = 6
    Level71To80 = 7
    Level81To90 = 8
    Level91To100 = 9


class ItemCategory(IntEnum):
    Coin = 0
    CharacterExpGrowth = 1
    SecretStone = 2
    Material = 3
    Consumable = 4
    Collectible = 5
    Favor = 6
    RecruitCoin = 7
    InvisibleToken = 8


class MailType(IntEnum):
    System = 0
    Attendance = 1
    Event = 2
    MassTrade = 3
    InventoryFull = 4
    ArenaDefenseVictory = 5
    CouponUsageReward = 6
    ArenaSeasonClose = 7
    ProductReward = 8
    MonthlyProductReward = 9
    ExpiryChangeItem = 10
    ClanAttendance = 11
    AccountLink = 12
    NewUserBonus = 13
    LeftClanAssistReward = 14
    AttendanceImmediately = 15
    WeeklyProductReward = 16
    BiweeklyProductReward = 17
    Temp_1 = 18
    Temp_2 = 19
    Temp_3 = 20
    CouponCompleteReward = 21
    BirthdayMail = 22


class AttendanceType(IntEnum):
    Basic = 0
    Event = 1
    Newbie = 2
    EventCountDown = 3
    Event20Days = 4


class AttendanceCountRule(IntEnum):
    Accumulation = 0
    Date = 1


class AttendanceResetType(IntEnum):
    User = 0
    Server = 1


class DreamMakerMultiplierCondition(IntEnum):
    none = 0
    Round = 1
    CollectionCount = 2
    EndingCount = 3


class DreamMakerParameterType(IntEnum):
    none = 0
    Param01 = 1
    Param02 = 2
    Param03 = 3
    Param04 = 4


class DreamMakerResult(IntEnum):
    none = 0
    Fail = 1
    Success = 2
    Perfect = 3


class DreamMakerParamOperationType(IntEnum):
    none = 0
    GrowUpHigh = 1
    GrowUp = 2
    GrowDownHigh = 3
    GrowDown = 4


class DreamMakerEndingCondition(IntEnum):
    none = 0
    Param01 = 1
    Param02 = 2
    Param03 = 3
    Param04 = 4
    Round = 5
    CollectionCount = 6


class DreamMakerVoiceCondition(IntEnum):
    none = 0
    Fail = 1
    Success = 2
    Perfect = 3
    DailyResult = 4


class DreamMakerEndingType(IntEnum):
    none = 0
    Normal = 1
    Special = 2


class DreamMakerEndingRewardType(IntEnum):
    none = 0
    FirstEndingReward = 1
    LoopEndingReward = 2


class Geas(IntEnum):
    ForwardProjectile = 0
    DiagonalProjectile = 1
    SideProjectile = 2
    Pierce = 3
    Reflect = 4
    Burn = 5
    Chill = 6
    AttackPower = 7
    AttackSpeed = 8
    Critical = 9
    Heal = 10


class TBGObjectType(IntEnum):
    none = 0
    EnemyBoss = 1
    EnemyMinion = 2
    Random = 3
    Facility = 4
    TreasureBox = 5
    Start = 6
    Portal = 7


class TBGOptionSuccessType(IntEnum):
    none = 0
    TBGItemAcquire = 1
    ItemAcquire = 2
    TBGDiceAcquire = 3
    Portal = 4


class TBGItemType(IntEnum):
    none = 0
    Dice = 1
    Heal = 2
    HealExpansion = 3
    Defence = 4
    Guide = 5
    DiceResultValue = 6
    DefenceCritical = 7
    DiceResultConfirm = 8


class TBGItemEffectType(IntEnum):
    none = 0
    PermanentContinuity = 1
    TemporaryContinuation = 2
    Immediately = 3


class TBGTileType(IntEnum):
    none = 0
    Start = 1
    Movable = 2
    UnMovable = 3


class TBGThemaType(IntEnum):
    none = 0
    Normal = 1
    Hidden = 2


class TBGPortalCondition(IntEnum):
    none = 0
    ObjectAllEncounter = 1
    Round = 2


class TBGProbModifyCondition(IntEnum):
    none = 0
    AllyRevive = 1
    DicePlayFail = 2


class TBGVoiceCondition(IntEnum):
    none = 0
    DiceResultSuccess = 1
    DiceResultFailBattle = 2
    DiceResultFailRandom = 3
    EnemyDie = 4
    TreasureBoxNormal = 5
    TreasureBoxSpecial = 6
    FacilityResult = 7


class MiniGameTBGThemaRewardType(IntEnum):
    TreasureReward = 0
    EmptyTreasureReward = 1
    HiddenThemaTreasureReward = 2


class MissionCategory(IntEnum):
    Challenge = 0
    Daily = 1
    Weekly = 2
    Achievement = 3
    GuideMission = 4
    All = 5
    MiniGameScore = 6
    MiniGameEvent = 7
    EventAchievement = 8
    DailySudden = 9
    DailyFixed = 10
    EventFixed = 11


class MissionResetType(IntEnum):
    none = 0
    Daily = 1
    Weekly = 2
    Limit = 3


class MissionCompleteConditionType(IntEnum):
    none = 0
    Reset_DailyLogin = 1
    Reset_DailyLoginCount = 2
    Reset_CompleteMission = 3
    Achieve_EquipmentLevelUpCount = 4
    Achieve_EquipmentTierUpCount = 5
    Achieve_CharacterLevelUpCount = 6
    Reset_CharacterTranscendenceCount = 7
    Reset_ClearTaticBattleCount = 8
    Achieve_ClearCampaignStageCount = 9
    Reset_KillSpecificEnemyCount = 10
    Reset_KillEnemyWithTagCount = 11
    Reset_GetCharacterCount = 12
    Reset_GetCharacterWithTagCount = 13
    Reset_GetSpecificCharacterCount = 14
    Reset_AccountLevelUp = 15
    Reset_GetEquipmentCount = 16
    Reset_GachaCount = 17
    Reset_UseGem = 18
    Reset_GetGem = 19
    Reset_GetGemPaid = 20
    Achieve_GetGold = 21
    Achieve_GetItem = 22
    Reset_GetFavorLevel = 23
    Reset___Deprecated_EquipmentAtSpecificLevelCount = 24
    Reset_EquipmentAtSpecificTierUpCount = 25
    Reset_CharacterAtSpecificLevelCount = 26
    Reset_CharacterAtSpecificTranscendenceCount = 27
    Achieve_CharacterSkillLevelUpCount = 28
    Reset_CharacterAtSpecificSkillLevelCount = 29
    Reset_CompleteScheduleCount = 30
    Reset_CompleteScheduleGroupCount = 31
    Reset_AcademyLocationRankSum = 32
    Reset_CraftCount = 33
    Achieve_GetComfortPoint = 34
    Achieve_GetWeaponCount = 35
    Reset_EquipWeaponCount_Obsolete = 36
    Reset_CompleteScheduleWithSpecificCharacter = 37
    Reset_CafeInteractionCount = 38
    Reset_SpecificCharacterAtSpecificLevel = 39
    Reset_SpecificCharacterAtSpecificTranscendence = 40
    Reset_LobbyInteraction = 41
    Achieve_ClearFindGiftAndBloodDungeonCount = 42
    Reset_ClearSpecificFindGiftAndBloodDungeonCount = 43
    Achieve_JoinRaidCount = 44
    Reset_JoinSpecificRaidCount = 45
    Achieve_JoinArenaCount = 46
    Reset_ArenaVictoryCount = 47
    Reset_RaidDamageAmountOnOneBattle = 48
    Reset_ClearEventStageCount = 49
    Reset_UseSpecificCharacterCount = 50
    Achieve_UseGold = 51
    Reset_UseTiket = 52
    Reset_ShopBuyCount = 53
    Reset_ShopBuyActionPointCount = 54
    Reset_SpecificCharacterAtSpecificFavorRank = 55
    Reset_ClearSpecificScenario = 56
    Reset_GetSpecificItemCount = 57
    Achieve_TotalGetClearStarCount = 58
    Reset_CompleteCampaignStageMinimumTurn = 59
    Achieve_TotalLoginCount = 60
    Reset_LoginAtSpecificTime = 61
    Reset_CompleteFavorSchedule = 62
    Reset_CompleteFavorScheduleAtSpecificCharacter = 63
    Reset_GetMemoryLobbyCount = 64
    Reset_GetFurnitureGroupCount = 65
    Reset_AcademyLocationAtSpecificRank = 66
    Reset_ClearCampaignStageDifficultyNormal = 67
    Reset_ClearCampaignStageDifficultyHard = 68
    Achieve_ClearChaserDungeonCount = 69
    Reset_ClearSpecificChaserDungeonCount = 70
    Reset_GetCafeRank = 71
    Reset_SpecificStarCharacterCount = 72
    Reset_EventClearCampaignStageCount = 73
    Reset_EventClearSpecificCampaignStageCount = 74
    Reset_EventCompleteCampaignStageMinimumTurn = 75
    Reset_EventClearCampaignStageDifficultyNormal = 76
    Reset_EventClearCampaignStageDifficultyHard = 77
    Reset_ClearSpecificCampaignStageCount = 78
    Reset_GetItemWithTagCount = 79
    Reset_GetFurnitureWithTagCount = 80
    Reset_GetEquipmentWithTagCount = 81
    Reset_ClearCampaignStageTimeLimitFromSecond = 82
    Reset_ClearEventStageTimeLimitFromSecond = 83
    Reset_ClearRaidTimeLimitFromSecond = 84
    Reset_ClearBattleWithTagCount = 85
    Reset_ClearFindGiftAndBloodDungeonTimeLimitFromSecond = 86
    Reset_CompleteScheduleWithTagCount = 87
    Reset_ClearChaserDungeonTimeLimitFromSecond = 88
    Reset_GetTotalScoreRhythm = 89
    Reset_GetBestScoreRhythm = 90
    Reset_GetSpecificScoreRhythm = 91
    Reset_ClearStageRhythm = 92
    Reset_GetComboCountRhythm = 93
    Reset_GetFullComboRhythm = 94
    Reset_GetFeverCountRhythm = 95
    Reset_UseActionPoint = 96
    Achieve_ClearSchoolDungeonCount = 97
    Reset_ClearSchoolDungeonTimeLimitFromSecond = 98
    Reset_ClearSpecificSchoolDungeonCount = 99
    Reset_GetCriticalCountRhythm = 100
    Achieve_WeaponTranscendenceCount = 101
    Achieve_WeaponLevelUpCount = 102
    Reset_WeaponAtSpecificTranscendenceCount = 103
    Reset_WeaponAtSpecificLevelUpCount = 104
    Reset_BuyShopGoods = 105
    Reset_ClanLogin = 106
    Reset_AssistCharacterSetting = 107
    Reset_DailyMissionFulfill = 108
    Reset_SelectedMissionFulfill = 109
    Reset_TotalDamageToWorldRaid = 110
    Reset_JoinWorldRaidTypeNumber = 111
    Reset_JoinWorldRaidBattleWithTagCount = 112
    Reset_ClearWorldRaidTimeLimitFromSecond = 113
    Achieve_KillEnemyWithDecagrammatonSPOTagCount = 114
    Reset_ConquerTileCount = 115
    Reset_ConquerSpecificStepTileCount = 116
    Reset_ConquerSpecificStepTileAll = 117
    Reset_UpgradeConquestBaseTileCount = 118
    Reset_KillConquestBoss = 119
    Reset_ClearEventConquestTileTimeLimitFromSecond = 120
    Reset_DiceRaceUseDiceCount = 121
    Reset_DiceRaceFinishLapCount = 122
    Reset_FortuneGachaCount = 123
    Reset_FortuneGachaCountByGrade = 124
    Reset_ClearCountShooting = 125
    Reset_ClearSpecificStageShooting = 126
    Reset_ClearSpecificCharacterShooting = 127
    Reset_ClearSpecificSectionShooting = 128
    Achieve_JoinEliminateRaidCount = 129
    Reset_TBGCompleteRoundCount = 130
    Reset_CompleteStage = 131
    Reset_TBGClearSpecificThema = 132
    Reset_ClearGeneralChaserDungeonCount = 133
    Reset_ClearGeneralFindGiftAndBloodDungeonCount = 134
    Reset_ClearGeneralSchoolDungeonCount = 135
    Reset_JoinArenaCount = 136
    Reset_GetCafe2ndRank = 137
    Achieve_GetComfort2ndPoint = 138
    Reset_ClearSpecificTimeAttackDungeonCount = 139
    Reset_GetScoreTimeAttackDungeon = 140
    Reset_GetTotalScoreTimeAttackDungeon = 141
    Reset_JoinRaidCount = 142
    Reset_ClearTimeAttackDungeonCount = 143
    Reset_JoinEliminateRaidCount = 144
    Reset_FieldClearSpecificDate = 145
    Reset_FieldGetEvidenceCount = 146
    Reset_FieldMasteryLevel = 147
    Reset_TreasureCheckedCellCount = 148
    Reset_TreasureGetTreasureCount = 149
    Reset_TreasureRoundRefreshCount = 150
    Achieve_UseTicketCount = 151
    Reset_ClearMultiFloorRaidStage = 152
    Achieve_CharacterPotentialUpCount = 153
    Reset_CharacterPotentialUpCount = 154
    Reset_CharacterAtSpecificPotentialCount = 155
    Reset_PotentialAttackPowerAtSpecificLevel = 156
    Reset_PotentialMaxHPAtSpecificLevel = 157
    Reset_PotentialHealPowerAtSpecificLevel = 158
    Reset_DreamGetSpecificParameter = 159
    Reset_DreamGetSpecificScheduleCount = 160
    Reset_DreamGetScheduleCount = 161
    Reset_DreamGetEndingCount = 162
    Reset_DreamGetSpecificEndingCount = 163
    Reset_DreamGetCollectionScenarioCount = 164


class AccountAchievementType(IntEnum):
    TotalLoginCount = 0
    TotalGetClearStarCount = 1
    TotalCharacterLevelUpCount = 2
    TotalCharacterSkillLevelUpCount = 3
    TotalClearCampaignStageCount = 4
    TotalClearChaserDungeonCount = 5
    TotalClearFindGiftAndBloodDungeonCount = 6
    TotalEquipmentLevelUpCount = 7
    TotalEquipmentTierUpCount = 8
    MaxComfortPoint = 9
    TotalGetGold = 10
    TotalUseGold = 11
    TotalJoinArenaCount = 12
    TotalJoinRaidCount = 13
    TotalClearSchoolDungeonCount = 14
    TotalGetWeaponCount = 15
    TotalWeaponLevelUpCount = 16
    TotalWeaponTranscendenceCount = 17
    KillEnemyWithDecagrammatonSPOTagCount = 18
    EventPoint = 19
    ConquestCalculateReward = 20
    TotalJoinEliminateRaidCount = 21
    Cafe2MaxComfortPoint = 22
    TotalRaidTicketUseCount = 23
    TotalEliminateTicketUseCount = 24
    TotalCharacterPotentialUpCount = 25


class MissionToastDisplayConditionType(IntEnum):
    Always = 0
    Complete = 1
    Never = 2


class GetStickerConditionType(IntEnum):
    none = 0
    Reset_StikcerGetCondition_AccountLevel = 1
    Reset_StickerGetCondition_ScenarioModeId = 2
    Reset_StickerGetCondition_EnemyKillCount = 3
    Reset_StickerGetCondition_GetItemCount = 4
    Reset_StickerGetCondition_BuyItemCount = 5
    Reset_StickerGetCondition_ScheduleRank = 6
    Reset_StickerGetCondition_Change_LobbyCharacter = 7
    Reset_StickerGetCondition_Cafe_Character_Visit_Count = 8
    Reset_StickerGetCondition_Cafe_Chracter_Invite_Count = 9
    Reset_StickerGetCondition_GetChracterCount = 10
    Reset_StickerGetCondition_Cafe_Furniture_Interaction = 11
    Reset_StickerGetCondition_GetFurniture = 12
    Reset_StickerGetCondition_SetFurniture = 13
    Reset_StickerGetCondition_GivePresentChracterCount = 14
    Reset_StickerGetCondition_GivePresentCount = 15
    Reset_StickerGetCondition_MomotalkStudentCount = 16
    Reset_StickerGetCondition_CombatwithCharacterCount = 17
    Reset_StickerGetCondition_GachaCharacterCount = 18
    Reset_StickerGetCondition_TouchLobbyCharacter = 19
    Reset_StickerGetCondition_UseCircleEmoticonCount = 20
    Reset_StickerGetCondition_CraftCount = 21
    Reset_StickerGetCondition_NormalStageClear = 22
    Reset_StickerGetCondition_NormalStageClear3Star = 23
    Reset_StickerGetCondition_HardStageClear = 24
    Reset_StickerGetCondition_HardStageClear3Star = 25
    Achieve_StikcerGetCondition_AccountLevel = 26
    Achieve_StickerGetCondition_ClearStageId = 27
    Achieve_StickerGetCondition_ScenarioModeId = 28
    Achieve_StickerGetCondition_EnemyKillCount = 29
    Achieve_StickerGetCondition_GetItemCount = 30
    Achieve_StickerGetCondition_BuyItemCount = 31
    Achieve_StickerGetCondition_ScheduleRank = 32
    Achieve_StickerGetCondition_Change_LobbyCharacter = 33
    Achieve_StickerGetCondition_Cafe_Character_Visit_Count = 34
    Achieve_StickerGetCondition_Cafe_Chracter_Invite_Count = 35
    Achieve_StickerGetCondition_GetChracterCount = 36
    Achieve_StickerGetCondition_Cafe_Furniture_Interaction = 37
    Achieve_StickerGetCondition_GetFurniture = 38
    Achieve_StickerGetCondition_SetFurniture = 39
    Achieve_StickerGetCondition_GivePresentChracterCount = 40
    Achieve_StickerGetCondition_GivePresentCount = 41
    Achieve_StickerGetCondition_MomotalkStudentCount = 42
    Achieve_StickerGetCondition_CombatwithCharacterCount = 43
    Achieve_StickerGetCondition_GachaCharacterCount = 44
    Achieve_StickerGetCondition_TouchLobbyCharacter = 45
    Achieve_StickerGetCondition_UseCircleEmoticonCount = 46
    Achieve_StickerGetCondition_CraftCount = 47
    Achieve_StickerGetCondition_NormalStageClear = 48
    Achieve_StickerGetCondition_NormalStageClear3Star = 49
    Achieve_StickerGetCondition_HardStageClear = 50
    Achieve_StickerGetCondition_HardStageClear3Star = 51
    Reset_StickerGetCondition_EnemyKillCountbyTag = 52
    Reset_StickerGetCondition_GetItemCountbyTag = 53
    Reset_StickerGetCondition_ClearCampaignOrEventStageCount = 54
    Reset_StickerGetCondition_CompleteCampaignStageMinimumTurn = 55
    Reset_StickerGetCondition_ClearCampaignStageDifficultyNormal = 56
    Reset_StickerGetCondition_ClearCampaignStageDifficultyHard = 57
    Reset_StickerGetCondition_EventClearCampaignStageCount = 58
    Reset_StickerGetCondition_EventClearSpecificCampaignStageCount = 59
    Reset_StickerGetCondition_EventCompleteCampaignStageMinimumTurn = 60
    Reset_StickerGetCondition_EventClearCampaignStageDifficultyNormal = 61
    Reset_StickerGetCondition_EventClearCampaignStageDifficultyHard = 62
    Reset_StickerGetCondition_ClearSpecificCampaignStageCount = 63
    Reset_StickerGetCondition_ClearCampaignStageTimeLimitFromSecond = 64
    Reset_StickerGetCondition_ClearEventStageTimeLimitFromSecond = 65
    Reset_StickerGetCondition_ClearStageRhythm = 66
    Reset_StickerGetCondition_ClearSpecificStageShooting = 67
    Reset_StickerGetCondition_CompleteStage = 68
    Achieve_StickerGetCondition_ClearCampaignStageCount = 69
    Achieve_StickerGetCondition_ClearChaserDungeonCount = 70
    Reset_StickerGetCondition_ClearSpecificChaserDungeonCount = 71
    Achieve_StickerGetCondition_ClearSchoolDungeonCount = 72
    Reset_StickerGetCondition_ClearSpecificSchoolDungeonCount = 73
    Reset_StickerGetCondition_ClearSpecificWeekDungeonCount = 74
    Achieve_StickerGetCondition_ClearFindGiftAndBloodDungeonCount = 75


class StickerCheckPassType(IntEnum):
    none = 0
    ClearScenarioModeId = 1
    ClearCampaignStageId = 2


class ParcelType(IntEnum):
    none = 0
    Character = 1
    Currency = 2
    Equipment = 3
    Item = 4
    GachaGroup = 5
    Product = 6
    Shop = 7
    MemoryLobby = 8
    AccountExp = 9
    CharacterExp = 10
    FavorExp = 11
    TSS = 12
    Furniture = 13
    ShopRefresh = 14
    LocationExp = 15
    Recipe = 16
    CharacterWeapon = 17
    CharacterGear = 18
    IdCardBackground = 19
    Emblem = 20
    Sticker = 21
    Costume = 22


class Rarity(IntEnum):
    N = 0
    R = 1
    SR = 2
    SSR = 3


class Tier(IntEnum):
    T1 = 0
    T2 = 1
    T3 = 2
    T4 = 3


class CurrencyTypes(IntEnum):
    Invalid = 0
    Gold = 1
    GemPaid = 2
    GemBonus = 3
    Gem = 4
    ActionPoint = 5
    AcademyTicket = 6
    ArenaTicket = 7
    RaidTicket = 8
    WeekDungeonChaserATicket = 9
    WeekDungeonFindGiftTicket = 10
    WeekDungeonBloodTicket = 11
    WeekDungeonChaserBTicket = 12
    WeekDungeonChaserCTicket = 13
    SchoolDungeonATicket = 14
    SchoolDungeonBTicket = 15
    SchoolDungeonCTicket = 16
    TimeAttackDungeonTicket = 17
    MasterCoin = 18
    WorldRaidTicketA = 19
    WorldRaidTicketB = 20
    WorldRaidTicketC = 21
    ChaserTotalTicket = 22
    SchoolDungeonTotalTicket = 23
    EliminateTicketA = 24
    EliminateTicketB = 25
    EliminateTicketC = 26
    EliminateTicketD = 27
    Max = 28


class SortingTarget(IntEnum):
    none = 0
    Rarity = 1
    Level = 2
    StarGrade = 3
    Tier = 4


class CurrencyOverChargeType(IntEnum):
    CanNotCharge = 0
    FitToLimit = 1
    ChargeOverLimit = 2


class CurrencyAdditionalChargeType(IntEnum):
    EnableAutoChargeOverLimit = 0
    DisableAutoChargeOverLimit = 1


class RecipeType(IntEnum):
    none = 0
    Craft = 1
    SkillLevelUp = 2
    CharacterTranscendence = 3
    EquipmentTierUp = 4
    CafeRankUp = 5
    SelectionItem = 6
    WeaponTranscendence = 7
    SelectRecruit = 8
    CharacterPotential = 9


class GachaGroupType(IntEnum):
    none = 0
    Reward_General = 1
    System_Craft = 2
    Reward_Pack = 3


class ParcelChangeReason(IntEnum):
    none = 0
    Acquire_NewAccount = 1
    Acquire_PlayReward = 2
    Acquire_ChapterReward = 3
    Acquire_LoginReward = 4
    Acquire_EventReward = 5
    Acquire_GMPush = 6
    Acquire_ShopBuy = 7
    Acquire_GachaBuy = 8
    Acquire_CurrencyBuy = 9
    Equipment_Equip = 10
    Equipment_Unequip = 11
    Equipment_Levelup = 12
    Equipment_LimitBreak = 13
    Equipment_Transcendence = 14
    Equipment_Enchant = 15
    Item_Use = 16
    Item_Lock = 17
    Item_CharacterGrowthMaterial = 18
    Item_Change = 19
    Item_Delete = 20
    Item_Consume = 21
    Item_SelectTicket = 22
    Character_ExpGrowth = 23
    Character_Transcendence = 24
    Character_SkillLevelUp = 25
    Character_FavorGrowth = 26
    Furniture_CafeSet = 27
    Furniture_CafeRecall = 28
    Academy_AttendSchedule = 29
    Academy_MessageList = 30
    Adventure_EnterMainStage = 31
    Adventure_EnterSubStage = 32
    Adventure_MainStageBattleResult = 33
    Adventure_SubStageBattleResult = 34
    Adventure_ChapterClearReward = 35
    Adventure_Retreat = 36
    Adventure_PurchasePlayCountHardStage = 37
    Adventure_TutorialStage = 38
    Adventure_TutorialStageBattleResult = 39
    ContentSweep_Sweep = 40
    Arena_TimeReward = 41
    Arena_DailyReward = 42
    Arena_EnterBattle = 43
    Arena_BattleResult = 44
    Cafe_Interact = 45
    Cafe_Production = 46
    Cafe_RankUp = 47
    Cafe_GiveGift = 48
    WeekDungeon_BattleResult = 49
    WeekDungeon_EnterBattle = 50
    WeekDungeon_Retreat = 51
    Mission_Clear = 52
    Shop_Refresh = 53
    Shop_BuyEligma = 54
    Shop_BuyMerchandise = 55
    Shop_BuyGacha = 56
    Scenario_Clear = 57
    Recipe_Craft = 58
    Raid_Failed = 59
    Raid_Reward = 60
    Raid_SeasonReward = 61
    Raid_CreateBattle = 62
    CumulativeTimeReward_Reward = 63
    Mail_Receive = 64
    MomoTalk_FavorSchedule = 65
    WeekDungeon_EnterBlood = 66
    WeekDungeon_EnterGift = 67
    Acquire_ActionPoint = 68
    Acquire_ArenaTicket = 69
    EventContent_TotalReward = 70
    Craft_UpdateNode = 71
    Craft_CompleteProcess = 72
    Craft_Reward = 73
    EventContent_BattleResult = 74
    Adventure_Sweep = 75
    EventContent_Sweep = 76
    WeekDungeon_Sweep = 77
    Acquire_MonthlyProduct = 78
    Acquire_DailyReward = 79
    Billing_PurchaseProduct = 80
    EventContent_EnterMainStage = 81
    EventContent_EnterSubStage = 82
    EventContent_MainStageResult = 83
    EventContent_SubStageResult = 84
    EventContent_Retreat = 85
    WeekDungeon_BloodResult = 86
    WeekDungeon_GiftResult = 87
    WeekDungeon_EnterChaserA = 88
    WeekDungeon_EnterChaserB = 89
    WeekDungeon_EnterChaserC = 90
    WeekDungeon_ChaserAResult = 91
    WeekDungeon_ChaserBResult = 92
    WeekDungeon_ChaserCResult = 93
    EventContent_BoxGacha = 94
    Raid_Sweep = 95
    Clan_AssistReward = 96
    EventContent_CardShop = 97
    CharacterWeapon_ExpGrowth = 98
    CharacterWeapon_Transcendence = 99
    MiniGameMission_Clear = 100
    SchoolDungeon_EnterSchoolA = 101
    SchoolDungeon_EnterSchoolB = 102
    SchoolDungeon_EnterSchoolC = 103
    SchoolDungeon_SchoolAResult = 104
    SchoolDungeon_SchoolBResult = 105
    SchoolDungeon_SchoolCResult = 106
    TimeAttackDungeon_CreateBattle = 107
    TimeAttackDungeon_EndBattle = 108
    TimeAttackDungeon_Reward = 109
    Clan_Create = 110
    Arena_SeasonReward = 111
    Arena_OverallReward = 112
    EventContent_AttendSchedule = 113
    EventContent_BuyFortuneGacha = 114
    Equipment_BatchGrowth = 115
    EventContent_EnterStoryStage = 116
    EventContent_StoryStageResult = 117
    WorldRaid_EndBattle = 118
    WorldRaid_Reward = 119
    Conquest_EnterBattle = 120
    Conquest_EnterUnExpectBattle = 121
    Conquest_BattleResult = 122
    Conquest_UnExpectBattleResult = 123
    Conquest_UpgradeBase = 124
    Conquest_ManageBase = 125
    Conquest_CalculatedReward = 126
    Conquest_TakeEventBoxObject = 127
    Conquest_ConquerNormalTile = 128
    Item_SelectRecruit = 129
    Adventure_EnterExtraStage = 130
    Adventure_ExtraStageBattleResult = 131
    Scenario_EnterMainStage = 132
    Scenario_MainStageResult = 133
    Scenario_RetreatMainStage = 134
    EventContent_DiceRaceRollReward = 135
    EventContent_DiceRaceLapReward = 136
    ShiftingCraft_BeginProcess = 137
    ShiftingCraft_CompleteProcess = 138
    ShiftingCraft_Reward = 139
    MiniGame_ShootingBattleResult = 140
    MiniGame_ShootingSweep = 141
    EliminateRaid_Failed = 142
    EliminateRaid_Reward = 143
    EliminateRaid_SeasonReward = 144
    EliminateRaid_CreateBattle = 145
    EliminateRaid_Sweep = 146
    Item_AutoSynth = 147
    ContentSweep_MultiSweep = 148
    Emblem_Acquire = 149
    MiniGame_TBGMove = 150
    MiniGame_TBGEncounterInput = 151
    MiniGame_TBGResurrect = 152
    MiniGame_TBGSweep = 153
    Shop_BeforehandGacha = 154
    EliminateRaid_LimitedReward = 155
    Craft_AutoBeginProcess = 156
    Craft_CompleteProcessAll = 157
    Craft_RewardAll = 158
    ShiftingCraft_CompleteProcessAll = 159
    ShiftingCraft_RewardAll = 160
    Temp_1 = 161
    Temp_2 = 162
    Temp_3 = 163
    Temp_4 = 164
    EventContent_Treasure = 165
    Field_EnterStage = 166
    Field_StageResult = 167
    Field_Interaction = 168
    Field_Quest = 169
    Character_PotentialGrowth = 170
    MultiFloorRaid_EndBattle = 171
    MultiFloorRaid_Reward = 172
    MiniGame_DreamSchedule = 173
    MiniGame_DreamDailyClosing = 174
    MiniGame_DreamEnding = 175


class ConsumeCondition(IntEnum):
    And = 0
    Or = 1


class DailyRefillType(IntEnum):
    none = 0
    Default = 1
    Login = 2


class ScenarioBGType(IntEnum):
    none = 0
    Image = 1
    BlurRT = 2
    Spine = 3
    Hide = 4


class ScenarioType(IntEnum):
    none = 0
    Title = 1
    Place = 2


class ScenarioTypes(IntEnum):
    none = 0
    Title = 1
    Place = 2


class ScenarioCharacterAction(IntEnum):
    Idle = 0
    Shake = 1
    Greeting = 2
    FalldownLeft = 3
    FalldownRight = 4
    Stiff = 5
    Hophop = 6
    Jump = 7


class ScenarioCharacterBehaviors(IntEnum):
    none = 0
    Appear = 1
    Disappear = 2
    AppearToLeft = 3
    ApperToRight = 4
    DisappearToLeft = 5
    DisappearToRight = 6
    MoveToTarget = 7


class ScenarioCharacterShapes(IntEnum):
    none = 0
    Signal = 1
    BlackSilhouette = 2
    Closeup = 4
    Highlight = 8
    WhiteSilhouette = 16


class ScenarioBGScroll(IntEnum):
    none = 0
    Vertical = 1
    Horizontal = 2


class DialogCategory(IntEnum):
    Cafe = 0
    Echelon = 1
    CharacterSSRNew = 2
    CharacterGet = 3
    Birthday = 4
    Dating = 5
    Title = 6
    UILobby = 7
    UILobbySpecial = 8
    UIShop = 9
    UIGacha = 10
    UIRaidLobby = 11
    UIWork = 12
    UITitle = 13
    UIWeekDungeon = 14
    UIAcademyLobby = 15
    UIRaidLobbySeasonOff = 16
    UIRaidLobbySeasonOn = 17
    UIWorkAronaSit = 18
    UIWorkAronaSleep = 19
    UIWorkAronaWatch = 20
    UIGuideMission = 21
    UILobby2 = 22
    UIClanSearchList = 23
    UIAttendance = 24
    UIAttendanceEvent01 = 25
    UIEventLobby = 26
    UIEventShop = 27
    UIEventBoxGachaShop = 28
    UIAttendanceEvent02 = 29
    UIAttendanceEvent03 = 30
    UIEventCardShop = 31
    UISchoolDungeon = 32
    UIAttendanceEvent = 33
    UISpecialOperationLobby = 34
    WeaponGet = 35
    UIAttendanceEvent04 = 36
    UIEventFortuneGachaShop = 37
    UIAttendanceEvent05 = 38
    UIAttendanceEvent06 = 39
    UIMission = 40
    UIEventMission = 41
    UIAttendanceEvent08 = 42
    UIAttendanceEvent07 = 43
    UIEventMiniGameMission = 44
    UIAttendanceEvent09 = 45
    UIAttendanceEvent10 = 46
    UIAttendanceEvent11 = 47
    UIWorkPlanaSit = 48
    UIWorkPlanaUmbrella = 49
    UIWorkPlanaCabinet = 50
    UIWorkCoexist_AronaSleepSit = 51
    UIWorkCoexist_PlanaWatchSky = 52
    UIWorkCoexist_PlanaSitPeek = 53
    UIWorkCoexist_AronaSleepPeek = 54
    UIEventArchive = 55
    UIAttendanceEvent12 = 56
    UIAttendanceEvent13 = 57
    UIAttendanceEvent14 = 58
    Temp_1 = 59
    Temp_2 = 60
    Temp_3 = 61
    Temp_4 = 62
    Temp_5 = 63
    UIAttendanceEvent15 = 64
    UILobbySpecial2 = 65
    UIAttendanceEvent16 = 66
    UIEventTreasure = 67
    UIMultiFloorRaid = 68
    UIEventMiniGameDreamMaker = 69


class DialogCondition(IntEnum):
    Idle = 0
    Enter = 1
    Exit = 2
    Buy = 3
    SoldOut = 4
    BoxGachaNormal = 5
    BoxGachaPrize = 6
    Prize0 = 7
    Prize1 = 8
    Prize2 = 9
    Prize3 = 10
    Interaction = 11
    Luck0 = 12
    Luck1 = 13
    Luck2 = 14
    Luck3 = 15
    Luck4 = 16
    Luck5 = 17
    StoryOpen = 18
    CollectionOpen = 19
    BoxGachaFinish = 20
    FindTreasure = 21
    GetTreasure = 22
    RoundRenewal = 23
    MiniGameDreamMakerEnough01 = 24
    MiniGameDreamMakerEnough02 = 25
    MiniGameDreamMakerEnough03 = 26
    MiniGameDreamMakerEnough04 = 27
    MiniGameDreamMakerDefault = 28


class DialogConditionDetail(IntEnum):
    none = 0
    Day = 1
    Close = 2
    MiniGameDreamMakerDay = 3


class DialogType(IntEnum):
    Talk = 0
    Think = 1
    UITalk = 2


class Anniversary(IntEnum):
    none = 0
    UserBDay = 1
    StudentBDay = 2


class School(IntEnum):
    none = 0
    Hyakkiyako = 1
    RedWinter = 2
    Trinity = 3
    Gehenna = 4
    Abydos = 5
    Millennium = 6
    Arius = 7
    Shanhaijing = 8
    Valkyrie = 9
    WildHunt = 10
    SRT = 11
    SCHALE = 12
    ETC = 13
    Tokiwadai = 14
    Sakugawa = 15


class EtcSchool(IntEnum):
    none = 0
    ETC = 1
    Tokiwadai = 2
    Sakugawa = 3
    Max = 4


class StoryCondition(IntEnum):
    Open = 0
    Locked = 1
    ComingSoon = 2
    Hide = 3


class EmojiEvent(IntEnum):
    EnterConver = 0
    EnterShelter = 1
    SignalLeader = 2
    Nice = 3
    Reload = 4
    Blind = 5
    Panic = 6
    Silence = 7
    NearyDead = 8
    Run = 9
    TerrainAdaptionS = 10
    TerrainAdaptionA = 11
    TerrainAdaptionB = 12
    TerrainAdaptionC = 13
    TerrainAdaptionD = 14
    TerrainAdaptionSS = 15
    Dot = 16
    Angry = 17
    Bulb = 18
    Exclaim = 19
    Surprise = 20
    Sad = 21
    Sigh = 22
    Steam = 23
    Upset = 24
    Respond = 25
    Question = 26
    Sweat = 27
    Music = 28
    Chat = 29
    Twinkle = 30
    Zzz = 31
    Tear = 32
    Heart = 33
    Shy = 34
    Think = 35


class ScenarioModeTypes(IntEnum):
    none = 0
    Main = 1
    Sub = 2
    Replay = 3
    Mini = 4


class ScenarioModeSubTypes(IntEnum):
    none = 0
    Club = 1
    TSS = 2


class ScenarioModeReplayTypes(IntEnum):
    none = 0
    Event = 1
    Favor = 2
    Work = 3
    EventMeetup = 4


class ScenarioEffectDepth(IntEnum):
    none = 0
    AboveBg = 1
    AboveCharacter = 2
    AboveAll = 3


class ScenarioZoomAnchors(IntEnum):
    Center = 0
    LeftTop = 1
    LeftBottom = 2
    RightTop = 3
    RightBottom = 4


class ScenarioZoomType(IntEnum):
    Instant = 0
    Slide = 1


class ScenarioContentType(IntEnum):
    Prologue = 0
    WeekDungeon = 1
    Raid = 2
    Arena = 3
    Favor = 4
    Shop = 5
    EventContent = 6
    Craft = 7
    Chaser = 8
    EventContentMeetup = 9
    TimeAttack = 10
    Mission = 11
    EventContentPermanentPrologue = 12
    EventContentReturnSeason = 13
    MiniEvent = 14
    EliminateRaid = 15
    MultiFloorRaid = 16


class MemoryLobbyCategory(IntEnum):
    none = 0
    UILobbySpecial = 1
    UILobbySpecial2 = 2


class PurchaseCountResetType(IntEnum):
    none = 0
    Day = 1
    Week = 2
    Month = 3


class ShopCategoryType(IntEnum):
    General = 0
    SecretStone = 1
    Raid = 2
    Gold = 3
    Ap = 4
    PickupGacha = 5
    NormalGacha = 6
    PointGacha = 7
    EventGacha = 8
    ArenaTicket = 9
    Arena = 10
    TutoGacha = 11
    RecruitSellection = 12
    EventContent_0 = 13
    EventContent_1 = 14
    EventContent_2 = 15
    EventContent_3 = 16
    EventContent_4 = 17
    _Obsolete = 18
    LimitedGacha = 19
    MasterCoin = 20
    SecretStoneGrowth = 21
    TicketGacha = 22
    DirectPayGacha = 23
    FesGacha = 24
    TimeAttack = 25
    Chaser = 26
    ChaserTicket = 27
    SchoolDungeonTicket = 28
    AcademyTicket = 29
    Special = 30
    Care = 31
    BeforehandGacha = 32
    EliminateRaid = 33
    GlobalSpecialGacha = 34


class PurchaseServerTag(IntEnum):
    Audit = 0
    PreAudit = 1
    Production = 2
    Hotfix = 3
    Standby2 = 4
    Standby1 = 5
    Major = 6
    Minor = 7
    Temp = 8
    Test = 9
    TestIn = 10


class PurchaseStatusCode(IntEnum):
    none = 0
    Start = 1
    PublishSuccess = 2
    End = 3
    Error = 4
    DuplicateOrder = 5
    Refund = 6


class StoreType(IntEnum):
    none = 0
    GooglePlay = 1
    AppStore = 2
    OneStore = 3
    MicrosoftStore = 4
    GalaxyStore = 5


class PurchasePeriodType(IntEnum):
    none = 0
    Day = 1
    Week = 2
    Month = 3


class PurchaseSourceType(IntEnum):
    none = 0
    Product = 1
    ProductMonthly = 2


class ProductCategory(IntEnum):
    none = 0
    Gem = 1
    Monthly = 2
    Package = 3
    GachaDirect = 4
    TimeLimit = 5


class ProductDisplayTag(IntEnum):
    none = 0
    New = 1
    Hot = 2
    Sale = 3


class ProductTagType(IntEnum):
    Monthly = 0
    Weekly = 1
    Biweekly = 2


class BillingTransactionEndType(IntEnum):
    none = 0
    Success = 1
    Cancel = 2


class GachaRewardType(IntEnum):
    none = 0
    Eligma = 1
    Eleph = 2


class ShopFreeRecruitType(IntEnum):
    none = 0
    Accumulation = 1
    Reset = 2


class GachaDisplayTag(IntEnum):
    none = 0
    Limited = 1
    TwoStar = 2
    ThreeStar = 3
    Free = 4
    New = 5
    Fes = 6
    SelectRecruit = 7


class ShopFilterType(IntEnum):
    GachaTicket = 0
    SecretStone = 1
    SecretStone_1 = 2
    SkillBook_Ultimate = 3
    ExSkill = 4
    SkillBook = 5
    Craft = 6
    AP = 7
    CharacterExpItem = 8
    Equip = 9
    Material = 10
    Creddit = 11
    Furniture = 12
    SelectItem = 13
    Currency = 14
    Hyakkiyako = 15
    RedWinter = 16
    Trinity = 17
    Gehenna = 18
    Abydos = 19
    Millennium = 20
    Arius = 21
    Shanhaijing = 22
    Valkyrie = 23
    SRT = 24
    Event = 25
    ChaserTotalTicket = 26
    SchoolTotalTicket = 27
    ShopFilterDUMMY_1 = 28
    ShopFilterDUMMY_2 = 29
    ShopFilterDUMMY_3 = 30
    ShopFilterDUMMY_4 = 31
    ShopFilterDUMMY_5 = 32
    ShopFilterDUMMY_6 = 33
    ShopFilterDUMMY_7 = 34
    ETC = 35
    Bundle = 36


class SocialMode(IntEnum):
    TITLE = 0
    LOBBY = 1
    FORMATION = 2
    STAGE_SELECT = 3
    BATTLE = 4
    POPUP = 5
    BATTLE_RESULT = 6
    BATTLE_RESULT_VICTORY = 7
    BATTLE_RESULT_DEFEAT = 8
    INVALID = 9
    TACTIC = 10
    STRATEGY = 11
    ACCONT = 12
    CAMPAIGN_STORY = 13
    CAMPAIGN_STAGE = 14
    TACTICREADY = 15


class AccountState(IntEnum):
    WaitingSignIn = 0
    Normal = 1
    Dormant = 2
    Comeback = 3
    Newbie = 4


class MessagePopupLayout(IntEnum):
    TextOnly = 0
    ImageBig = 1
    ImageSmall = 2
    UnlockCondition = 3


class MessagePopupImagePositionType(IntEnum):
    ImageFirst = 0
    TextFirst = 1


class MessagePopupButtonType(IntEnum):
    Accept = 0
    Cancel = 1
    Command = 2


class ToastType(IntEnum):
    none = 0
    Tactic_Left = 1
    Tactic_Right = 2
    Social_Center = 3
    Social_Mission = 4
    Social_Right = 5
    Notice_Center = 6


class StrategyAIType(IntEnum):
    none = 0
    Guard = 1
    Pursuit = 2


class StageDifficulty(IntEnum):
    none = 0
    Normal = 1
    Hard = 2
    VeryHard = 3
    VeryHard_Ex = 4


class HexaUnitGrade(IntEnum):
    Grade1 = 0
    Grade2 = 1
    Grade3 = 2
    Boss = 3


class TacticEnvironment(IntEnum):
    none = 0
    WarFog = 1


class StrategyObjectType(IntEnum):
    none = 0
    Start = 1
    Heal = 2
    Skill = 3
    StatBuff = 4
    Parcel = 5
    ParcelOneTimePerAccount = 6
    Portal = 7
    PortalOneWayEnterance = 8
    PortalOneWayExit = 9
    Observatory = 10
    Beacon = 11
    BeaconOneTime = 12
    EnemySpawn = 13
    SwitchToggle = 14
    SwitchMovableWhenToggleOff = 15
    SwitchMovableWhenToggleOn = 16
    FixedStart01 = 17
    FixedStart02 = 18
    FixedStart03 = 19
    FixedStart04 = 20


class StrategyEnvironment(IntEnum):
    none = 0
    MapFog = 1


class Tag(IntEnum):
    A = 0
    a = 1
    B = 2
    b = 3
    C = 4
    c = 5
    D = 6
    d = 7
    E = 8
    e = 9
    F = 10
    f = 11
    G = 12
    g = 13
    H = 14
    h = 15
    I = 16
    i = 17
    J = 18
    j = 19
    K = 20
    k = 21
    L = 22
    l = 23
    M = 24
    m = 25
    N = 26
    n = 27
    O = 28
    o = 29
    P = 30
    p = 31
    Q = 32
    q = 33
    R = 34
    r = 35
    S = 36
    s = 37
    T = 38
    t = 39
    U = 40
    u = 41
    V = 42
    v = 43
    W = 44
    w = 45
    X = 46
    x = 47
    Y = 48
    y = 49
    Z = 50
    z = 51
    aA = 52
    aa = 53
    aB = 54
    ab = 55
    aC = 56
    ac = 57
    aD = 58
    ad = 59
    aE = 60
    ae = 61
    aF = 62
    af = 63
    aG = 64
    ag = 65
    aH = 66
    ah = 67
    aI = 68
    ai = 69
    aJ = 70
    aj = 71
    aK = 72
    ak = 73
    aL = 74
    al = 75
    aM = 76
    am = 77
    aN = 78
    an = 79
    aO = 80
    ao = 81
    aP = 82
    ap = 83
    aQ = 84
    aq = 85
    aR = 86
    ar = 87
    aS = 88
    # as = 89
    aT = 90
    at = 91
    aU = 92
    au = 93
    aV = 94
    av = 95
    aW = 96
    aw = 97
    aX = 98
    ax = 99
    aY = 100
    ay = 101
    aZ = 102
    az = 103
    BA = 104
    Ba = 105
    BB = 106
    Bb = 107
    BC = 108
    Bc = 109
    BD = 110
    Bd = 111
    BE = 112
    Be = 113
    BF = 114
    Bf = 115
    BG = 116
    Bg = 117
    BH = 118
    Bh = 119
    BI = 120
    Bi = 121
    BJ = 122
    Bj = 123
    BK = 124
    Bk = 125
    BL = 126
    Bl = 127
    BM = 128
    Bm = 129
    BN = 130
    Bn = 131
    BO = 132
    Bo = 133
    BP = 134
    Bp = 135
    BQ = 136
    Bq = 137
    BR = 138
    Br = 139
    BS = 140
    Bs = 141
    BT = 142
    Bt = 143
    BU = 144
    Bu = 145
    BV = 146
    Bv = 147
    BW = 148
    Bw = 149
    BX = 150
    Bx = 151
    BY = 152
    By = 153
    BZ = 154
    Bz = 155
    bA = 156
    ba = 157
    bB = 158
    bb = 159
    bC = 160
    bc = 161
    bD = 162
    bd = 163
    bE = 164
    be = 165
    bF = 166
    bf = 167
    bG = 168
    bg = 169
    bH = 170
    bh = 171
    bI = 172
    bi = 173
    bJ = 174
    bj = 175
    bK = 176
    bk = 177
    bL = 178
    bl = 179
    bM = 180
    bm = 181
    bN = 182
    bn = 183
    bO = 184
    bo = 185
    bP = 186
    bp = 187
    bQ = 188
    bq = 189
    bR = 190
    br = 191
    bS = 192
    bs = 193
    bT = 194
    bt = 195
    bU = 196
    bu = 197
    bV = 198
    bv = 199
    bW = 200
    bw = 201
    bX = 202
    bx = 203
    bY = 204
    by = 205
    bZ = 206
    bz = 207
    CA = 208
    Ca = 209
    CB = 210
    Cb = 211
    CC = 212
    Cc = 213
    CD = 214
    Cd = 215
    CE = 216
    Ce = 217
    CF = 218
    Cf = 219
    CG = 220
    Cg = 221
    CH = 222
    Ch = 223
    CI = 224
    Ci = 225
    CJ = 226
    Cj = 227
    CK = 228
    Ck = 229
    CL = 230
    Cl = 231
    CM = 232
    Cm = 233
    CN = 234
    Cn = 235
    CO = 236
    Co = 237
    CP = 238
    Cp = 239
    CQ = 240
    Cq = 241
    CR = 242
    Cr = 243
    CS = 244
    Cs = 245
    CT = 246
    Ct = 247
    CU = 248
    Cu = 249
    CV = 250
    Cv = 251
    CW = 252
    Cw = 253
    CX = 254
    Cx = 255
    CY = 256
    Cy = 257
    CZ = 258
    Cz = 259
    cA = 260
    ca = 261
    cB = 262
    cb = 263
    cC = 264
    cc = 265
    cD = 266
    cd = 267
    cE = 268
    ce = 269
    cF = 270
    cf = 271
    cG = 272
    cg = 273
    cH = 274
    ch = 275
    cI = 276
    ci = 277
    cJ = 278
    cj = 279
    cK = 280
    ck = 281
    cL = 282
    cl = 283
    cM = 284
    cm = 285
    cN = 286
    cn = 287
    cO = 288
    co = 289
    cP = 290
    cp = 291
    cQ = 292
    cq = 293
    cR = 294
    cr = 295
    cS = 296
    cs = 297
    cT = 298
    ct = 299
    cU = 300
    cu = 301
    cV = 302
    cv = 303
    cW = 304
    cw = 305
    cX = 306
    cx = 307
    cY = 308
    cy = 309
    cZ = 310
    cz = 311
    DA = 312
    Da = 313
    DB = 314
    Db = 315
    DC = 316
    Dc = 317
    DD = 318
    Dd = 319
    DE = 320
    De = 321
    DF = 322
    Df = 323
    DG = 324
    Dg = 325
    DH = 326
    Dh = 327
    DI = 328
    Di = 329
    DJ = 330
    Dj = 331
    DK = 332
    Dk = 333
    DL = 334
    Dl = 335
    DM = 336
    Dm = 337
    DN = 338
    Dn = 339
    DO = 340
    Do = 341
    DP = 342
    Dp = 343
    DQ = 344
    Dq = 345
    DR = 346
    Dr = 347
    DS = 348
    Ds = 349
    DT = 350
    Dt = 351
    DU = 352
    Du = 353
    DV = 354
    Dv = 355
    DW = 356
    Dw = 357
    DX = 358
    Dx = 359
    DY = 360
    Dy = 361
    DZ = 362
    Dz = 363
    dA = 364
    da = 365
    dB = 366
    db = 367
    dC = 368
    dc = 369
    dD = 370
    dd = 371
    dE = 372
    de = 373
    dF = 374
    df = 375
    dG = 376
    dg = 377
    dH = 378
    dh = 379
    dI = 380
    di = 381
    dJ = 382
    dj = 383
    dK = 384
    dk = 385
    dL = 386
    dl = 387
    dM = 388
    dm = 389
    dN = 390
    dn = 391
    dO = 392
    do = 393
    dP = 394
    dp = 395
    dQ = 396
    dq = 397
    dR = 398
    dr = 399
    dS = 400
    ds = 401
    dT = 402
    dt = 403
    dU = 404
    du = 405
    dV = 406
    dv = 407
    dW = 408
    dw = 409
    dX = 410
    dx = 411
    dY = 412
    dy = 413
    dZ = 414
    dz = 415
    EA = 416
    Ea = 417
    EB = 418
    Eb = 419
    EC = 420
    Ec = 421
    ED = 422
    Ed = 423
    EE = 424
    Ee = 425
    EF = 426
    Ef = 427
    EG = 428
    Eg = 429
    EH = 430
    Eh = 431
    EI = 432
    Ei = 433
    EJ = 434
    Ej = 435
    EK = 436
    Ek = 437
    EL = 438
    El = 439
    EM = 440
    Em = 441
    EN = 442
    En = 443
    EO = 444
    Eo = 445
    EP = 446
    Ep = 447
    EQ = 448
    Eq = 449
    ER = 450
    Er = 451
    ES = 452
    Es = 453
    ET = 454
    Et = 455
    EU = 456
    Eu = 457
    EV = 458
    Ev = 459
    EW = 460
    Ew = 461
    EX = 462
    Ex = 463
    EY = 464
    Ey = 465
    EZ = 466
    Ez = 467
    eA = 468
    ea = 469
    eB = 470
    eb = 471
    eC = 472
    ec = 473
    eD = 474
    ed = 475
    eE = 476
    ee = 477
    eF = 478
    ef = 479
    eG = 480
    eg = 481
    eH = 482
    eh = 483
    eI = 484
    ei = 485
    eJ = 486
    ej = 487
    eK = 488
    ek = 489
    eL = 490
    el = 491
    eM = 492
    em = 493
    eN = 494
    en = 495
    eO = 496
    eo = 497
    eP = 498
    ep = 499
    eQ = 500
    eq = 501
    eR = 502
    er = 503
    eS = 504
    es = 505
    eT = 506
    et = 507
    eU = 508
    eu = 509
    eV = 510
    ev = 511
    eW = 512
    ew = 513
    eX = 514
    ex = 515
    eY = 516
    ey = 517
    eZ = 518
    ez = 519
    FA = 520
    Fa = 521
    FB = 522
    Fb = 523
    FC = 524
    Fc = 525
    FD = 526
    Fd = 527
    FE = 528
    Fe = 529
    FF = 530
    Ff = 531
    FG = 532
    Fg = 533
    FH = 534
    Fh = 535
    FI = 536
    Fi = 537
    FJ = 538
    Fj = 539
    FK = 540
    Fk = 541
    FL = 542
    Fl = 543
    FM = 544
    Fm = 545
    FN = 546
    Fn = 547
    FO = 548
    Fo = 549
    FP = 550
    Fp = 551
    FQ = 552
    Fq = 553
    FR = 554
    Fr = 555
    FS = 556
    Fs = 557
    FT = 558
    Ft = 559
    FU = 560
    Fu = 561
    FV = 562
    Fv = 563
    FW = 564
    Fw = 565
    FX = 566
    Fx = 567
    FY = 568
    Fy = 569
    FZ = 570
    Fz = 571
    fA = 572
    fa = 573
    fB = 574
    fb = 575
    fC = 576
    fc = 577
    fD = 578
    fd = 579
    fE = 580
    fe = 581
    fF = 582
    ff = 583
    fG = 584
    fg = 585
    fH = 586
    fh = 587
    fI = 588
    fi = 589
    fJ = 590
    fj = 591
    fK = 592
    fk = 593
    fL = 594
    fl = 595
    fM = 596
    fm = 597
    fN = 598
    fn = 599
    fO = 600
    fo = 601
    fP = 602
    fp = 603
    fQ = 604
    fq = 605
    fR = 606
    fr = 607
    fS = 608
    fs = 609
    fT = 610
    ft = 611
    fU = 612
    fu = 613
    fV = 614
    fv = 615
    fW = 616
    fw = 617
    fX = 618
    fx = 619
    fY = 620
    fy = 621
    fZ = 622
    fz = 623
    GA = 624
    Ga = 625
    GB = 626
    Gb = 627
    GC = 628
    Gc = 629
    GD = 630
    Gd = 631
    GE = 632
    Ge = 633
    GF = 634
    Gf = 635
    GG = 636
    Gg = 637
    GH = 638
    Gh = 639
    GI = 640
    Gi = 641
    GJ = 642
    Gj = 643
    GK = 644
    Gk = 645
    GL = 646
    Gl = 647
    GM = 648
    Gm = 649
    GN = 650
    Gn = 651
    GO = 652
    Go = 653
    GP = 654
    Gp = 655
    GQ = 656
    Gq = 657
    GR = 658
    Gr = 659
    GS = 660
    Gs = 661
    GT = 662
    Gt = 663
    GU = 664
    Gu = 665
    GV = 666
    Gv = 667
    GW = 668
    Gw = 669
    GX = 670
    Gx = 671
    GY = 672
    Gy = 673
    GZ = 674
    Gz = 675
    gA = 676
    ga = 677
    gB = 678
    gb = 679
    gC = 680
    gc = 681
    gD = 682
    gd = 683
    gE = 684
    ge = 685
    gF = 686
    gf = 687
    gG = 688
    gg = 689
    gH = 690
    gh = 691
    gI = 692
    gi = 693
    gJ = 694
    gj = 695
    gK = 696
    gk = 697
    gL = 698
    gl = 699
    gM = 700
    gm = 701
    gN = 702
    gn = 703
    gO = 704
    go = 705
    gP = 706
    gp = 707
    gQ = 708
    gq = 709
    gR = 710
    gr = 711
    gS = 712
    gs = 713
    gT = 714
    gt = 715
    gU = 716
    gu = 717
    gV = 718
    gv = 719
    gW = 720
    gw = 721
    gX = 722
    gx = 723
    gY = 724
    gy = 725
    gZ = 726
    gz = 727
    HA = 728
    Ha = 729
    HB = 730
    Hb = 731
    HC = 732
    Hc = 733
    HD = 734
    Hd = 735
    HE = 736
    He = 737
    HF = 738
    Hf = 739
    HG = 740
    Hg = 741
    HH = 742
    Hh = 743
    HI = 744
    Hi = 745
    HJ = 746
    Hj = 747
    HK = 748
    Hk = 749
    HL = 750
    Hl = 751
    HM = 752
    Hm = 753
    HN = 754
    Hn = 755
    HO = 756
    Ho = 757
    HP = 758
    Hp = 759
    HQ = 760
    Hq = 761
    HR = 762
    Hr = 763
    HS = 764
    Hs = 765
    HT = 766
    Ht = 767
    HU = 768
    Hu = 769
    HV = 770
    Hv = 771
    HW = 772
    Hw = 773
    HX = 774
    Hx = 775
    HY = 776
    Hy = 777
    HZ = 778
    Hz = 779
    hA = 780
    ha = 781
    hB = 782
    hb = 783
    hC = 784
    hc = 785
    hD = 786
    hd = 787
    hE = 788
    he = 789
    hF = 790
    hf = 791
    hG = 792
    hg = 793
    hH = 794
    hh = 795
    hI = 796
    hi = 797
    hJ = 798
    hj = 799
    hK = 800
    hk = 801
    hL = 802
    hl = 803
    hM = 804
    hm = 805
    hN = 806
    hn = 807
    hO = 808
    ho = 809
    hP = 810
    hp = 811
    hQ = 812
    hq = 813
    hR = 814
    hr = 815
    hS = 816
    hs = 817
    hT = 818
    ht = 819
    hU = 820
    hu = 821
    hV = 822
    hv = 823
    hW = 824
    hw = 825
    hX = 826
    hx = 827
    hY = 828
    hy = 829
    hZ = 830
    hz = 831
    IA = 832
    Ia = 833
    IB = 834
    Ib = 835
    IC = 836
    Ic = 837
    ID = 838
    Id = 839
    IE = 840
    Ie = 841
    IF = 842
    If = 843
    IG = 844
    Ig = 845
    IH = 846
    Ih = 847
    II = 848
    Ii = 849
    IJ = 850
    Ij = 851
    IK = 852
    Ik = 853
    IL = 854
    Il = 855
    IM = 856
    Im = 857
    IN = 858
    In = 859
    IO = 860
    Io = 861
    IP = 862
    Ip = 863
    IQ = 864
    Iq = 865
    IR = 866
    Ir = 867
    IS = 868
    Is = 869
    IT = 870
    It = 871
    IU = 872
    Iu = 873
    IV = 874
    Iv = 875
    IW = 876
    Iw = 877
    IX = 878
    Ix = 879
    IY = 880
    Iy = 881
    IZ = 882
    Iz = 883
    iA = 884
    ia = 885
    iB = 886
    ib = 887
    iC = 888
    ic = 889
    iD = 890
    id = 891
    iE = 892
    ie = 893
    iF = 894
    # if = 895
    iG = 896
    ig = 897
    iH = 898
    ih = 899
    iI = 900
    ii = 901
    iJ = 902
    ij = 903
    iK = 904
    ik = 905
    iL = 906
    il = 907
    iM = 908
    im = 909
    iN = 910
    # in = 911
    iO = 912
    io = 913
    iP = 914
    ip = 915
    iQ = 916
    iq = 917
    iR = 918
    ir = 919
    iS = 920
    # is = 921
    iT = 922
    it = 923
    iU = 924
    iu = 925
    iV = 926
    iv = 927
    iW = 928
    iw = 929
    iX = 930
    ix = 931
    iY = 932
    iy = 933
    iZ = 934
    iz = 935
    JA = 936
    Ja = 937
    JB = 938
    Jb = 939
    JC = 940
    Jc = 941
    JD = 942
    Jd = 943
    JE = 944
    Je = 945
    JF = 946
    Jf = 947
    JG = 948
    Jg = 949
    JH = 950
    Jh = 951
    JI = 952
    Ji = 953
    JJ = 954
    Jj = 955
    JK = 956
    Jk = 957
    JL = 958
    Jl = 959
    JM = 960
    Jm = 961
    JN = 962
    Jn = 963
    JO = 964
    Jo = 965
    JP = 966
    Jp = 967
    JQ = 968
    Jq = 969
    JR = 970
    Jr = 971
    JS = 972
    Js = 973
    JT = 974
    Jt = 975
    JU = 976
    Ju = 977
    JV = 978
    Jv = 979
    JW = 980
    Jw = 981
    JX = 982
    Jx = 983
    JY = 984
    Jy = 985
    JZ = 986
    Jz = 987
    jA = 988
    ja = 989
    jB = 990
    jb = 991
    jC = 992
    jc = 993
    jD = 994
    jd = 995
    jE = 996
    je = 997
    jF = 998
    jf = 999
    jG = 1000
    jg = 1001
    jH = 1002
    jh = 1003
    jI = 1004
    ji = 1005
    jJ = 1006
    jj = 1007
    jK = 1008
    jk = 1009
    jL = 1010
    jl = 1011
    jM = 1012
    jm = 1013
    jN = 1014
    jn = 1015
    jO = 1016
    jo = 1017
    jP = 1018
    jp = 1019
    jQ = 1020
    jq = 1021
    jR = 1022
    jr = 1023
    jS = 1024
    js = 1025
    jT = 1026
    jt = 1027
    jU = 1028
    ju = 1029
    jV = 1030
    jv = 1031
    jW = 1032
    jw = 1033
    jX = 1034
    jx = 1035
    jY = 1036
    jy = 1037
    jZ = 1038
    jz = 1039
    KA = 1040
    Ka = 1041
    KB = 1042
    Kb = 1043
    KC = 1044
    Kc = 1045
    KD = 1046
    Kd = 1047
    KE = 1048
    Ke = 1049
    KF = 1050
    Kf = 1051
    KG = 1052
    Kg = 1053
    KH = 1054
    Kh = 1055
    KI = 1056
    Ki = 1057
    KJ = 1058
    Kj = 1059
    KK = 1060
    Kk = 1061
    KL = 1062
    Kl = 1063
    KM = 1064
    Km = 1065
    KN = 1066
    Kn = 1067
    KO = 1068
    Ko = 1069
    KP = 1070
    Kp = 1071
    KQ = 1072
    Kq = 1073
    KR = 1074
    Kr = 1075
    KS = 1076
    Ks = 1077
    KT = 1078
    Kt = 1079
    KU = 1080
    Ku = 1081
    KV = 1082
    Kv = 1083
    KW = 1084
    Kw = 1085
    KX = 1086
    Kx = 1087
    KY = 1088
    Ky = 1089
    KZ = 1090
    Kz = 1091
    kA = 1092
    ka = 1093
    kB = 1094
    kb = 1095
    kC = 1096
    kc = 1097
    kD = 1098
    kd = 1099
    kE = 1100
    ke = 1101
    kF = 1102
    kf = 1103
    kG = 1104
    kg = 1105
    kH = 1106
    kh = 1107
    kI = 1108
    ki = 1109
    kJ = 1110
    kj = 1111
    kK = 1112
    kk = 1113
    kL = 1114
    kl = 1115
    kM = 1116
    km = 1117
    kN = 1118
    kn = 1119
    kO = 1120
    ko = 1121
    kP = 1122
    kp = 1123
    kQ = 1124
    kq = 1125
    kR = 1126
    kr = 1127
    kS = 1128
    ks = 1129
    kT = 1130
    kt = 1131
    kU = 1132
    ku = 1133
    kV = 1134
    kv = 1135
    kW = 1136
    kw = 1137
    kX = 1138
    kx = 1139
    kY = 1140
    ky = 1141
    kZ = 1142
    kz = 1143
    LA = 1144
    La = 1145
    LB = 1146
    Lb = 1147
    LC = 1148
    Lc = 1149
    LD = 1150
    Ld = 1151
    LE = 1152
    Le = 1153
    LF = 1154
    Lf = 1155
    LG = 1156
    Lg = 1157
    LH = 1158
    Lh = 1159
    LI = 1160
    Li = 1161
    LJ = 1162
    Lj = 1163
    LK = 1164
    Lk = 1165
    LL = 1166
    Ll = 1167
    LM = 1168
    Lm = 1169
    LN = 1170
    Ln = 1171
    LO = 1172
    Lo = 1173
    LP = 1174
    Lp = 1175
    LQ = 1176
    Lq = 1177
    LR = 1178
    Lr = 1179
    LS = 1180
    Ls = 1181
    LT = 1182
    Lt = 1183
    LU = 1184
    Lu = 1185
    LV = 1186
    Lv = 1187
    LW = 1188
    Lw = 1189
    LX = 1190
    Lx = 1191
    LY = 1192
    Ly = 1193
    LZ = 1194
    Lz = 1195
    lA = 1196
    la = 1197
    lB = 1198
    lb = 1199
    lC = 1200
    lc = 1201
    lD = 1202
    ld = 1203
    lE = 1204
    le = 1205
    lF = 1206
    lf = 1207
    lG = 1208
    lg = 1209
    lH = 1210
    lh = 1211
    lI = 1212
    li = 1213
    lJ = 1214
    lj = 1215
    lK = 1216
    lk = 1217
    lL = 1218
    ll = 1219
    lM = 1220
    lm = 1221
    lN = 1222
    ln = 1223
    lO = 1224
    lo = 1225
    lP = 1226
    lp = 1227
    lQ = 1228
    lq = 1229
    lR = 1230
    lr = 1231
    lS = 1232
    ls = 1233
    lT = 1234
    lt = 1235
    lU = 1236
    lu = 1237
    lV = 1238
    lv = 1239
    lW = 1240
    lw = 1241
    lX = 1242
    lx = 1243
    lY = 1244
    ly = 1245
    lZ = 1246
    lz = 1247
    MA = 1248
    Ma = 1249
    MB = 1250
    Mb = 1251
    MC = 1252
    Mc = 1253
    MD = 1254
    Md = 1255
    ME = 1256
    Me = 1257
    MF = 1258
    Mf = 1259
    MG = 1260
    Mg = 1261
    MH = 1262
    Mh = 1263
    MI = 1264
    Mi = 1265
    MJ = 1266
    Mj = 1267
    MK = 1268
    Mk = 1269
    ML = 1270
    Ml = 1271
    MM = 1272
    Mm = 1273
    MN = 1274
    Mn = 1275
    MO = 1276
    Mo = 1277
    MP = 1278
    Mp = 1279
    MQ = 1280
    Mq = 1281
    MR = 1282
    Mr = 1283
    MS = 1284
    Ms = 1285
    MT = 1286
    Mt = 1287
    MU = 1288
    Mu = 1289
    MV = 1290
    Mv = 1291
    MW = 1292
    Mw = 1293
    MX = 1294
    Mx = 1295
    MY = 1296
    My = 1297
    MZ = 1298
    Mz = 1299
    mA = 1300
    ma = 1301
    mB = 1302
    mb = 1303
    mC = 1304
    mc = 1305
    mD = 1306
    md = 1307
    mE = 1308
    me = 1309
    mF = 1310
    mf = 1311
    mG = 1312
    mg = 1313
    mH = 1314
    mh = 1315
    mI = 1316
    mi = 1317
    mJ = 1318
    mj = 1319
    mK = 1320
    mk = 1321
    mL = 1322
    ml = 1323
    mM = 1324
    mm = 1325
    mN = 1326
    mn = 1327
    mO = 1328
    mo = 1329
    mP = 1330
    mp = 1331
    mQ = 1332
    mq = 1333
    mR = 1334
    mr = 1335
    mS = 1336
    ms = 1337
    mT = 1338
    mt = 1339
    mU = 1340
    mu = 1341
    mV = 1342
    mv = 1343
    mW = 1344
    mw = 1345
    mX = 1346
    mx = 1347
    mY = 1348
    my = 1349
    mZ = 1350
    mz = 1351
    NA = 1352
    Na = 1353
    NB = 1354
    Nb = 1355
    NC = 1356
    Nc = 1357
    ND = 1358
    Nd = 1359
    NE = 1360
    Ne = 1361
    NF = 1362
    Nf = 1363
    NG = 1364
    Ng = 1365
    NH = 1366
    Nh = 1367
    NI = 1368
    Ni = 1369
    NJ = 1370
    Nj = 1371
    NK = 1372
    Nk = 1373
    NL = 1374
    Nl = 1375
    NM = 1376
    Nm = 1377
    NN = 1378
    Nn = 1379
    NO = 1380
    No = 1381
    NP = 1382
    Np = 1383
    NQ = 1384
    Nq = 1385
    NR = 1386
    Nr = 1387
    NS = 1388
    Ns = 1389
    NT = 1390
    Nt = 1391
    NU = 1392
    Nu = 1393
    NV = 1394
    Nv = 1395
    NW = 1396
    Nw = 1397
    NX = 1398
    Nx = 1399
    NY = 1400
    Ny = 1401
    NZ = 1402
    Nz = 1403
    nA = 1404
    na = 1405
    nB = 1406
    nb = 1407
    nC = 1408
    nc = 1409
    nD = 1410
    nd = 1411
    nE = 1412
    ne = 1413
    nF = 1414
    nf = 1415
    nG = 1416
    ng = 1417
    nH = 1418
    nh = 1419
    nI = 1420
    ni = 1421
    nJ = 1422
    nj = 1423
    nK = 1424
    nk = 1425
    nL = 1426
    nl = 1427
    nM = 1428
    nm = 1429
    nN = 1430
    nn = 1431
    nO = 1432
    no = 1433
    nP = 1434
    np = 1435
    nQ = 1436
    nq = 1437
    nR = 1438
    nr = 1439
    nS = 1440
    ns = 1441
    nT = 1442
    nt = 1443
    nU = 1444
    nu = 1445
    nV = 1446
    nv = 1447
    nW = 1448
    nw = 1449
    nX = 1450
    nx = 1451
    nY = 1452
    ny = 1453
    nZ = 1454
    nz = 1455
    OA = 1456
    Oa = 1457
    OB = 1458
    Ob = 1459
    OC = 1460
    Oc = 1461
    OD = 1462
    Od = 1463
    OE = 1464
    Oe = 1465
    OF = 1466
    Of = 1467
    OG = 1468
    Og = 1469
    OH = 1470
    Oh = 1471
    OI = 1472
    Oi = 1473
    OJ = 1474
    Oj = 1475
    OK = 1476
    Ok = 1477
    OL = 1478
    Ol = 1479
    OM = 1480
    Om = 1481
    ON = 1482
    On = 1483
    OO = 1484
    Oo = 1485
    OP = 1486
    Op = 1487
    OQ = 1488
    Oq = 1489
    OR = 1490
    Or = 1491
    OS = 1492
    Os = 1493
    OT = 1494
    Ot = 1495
    OU = 1496
    Ou = 1497
    OV = 1498
    Ov = 1499
    OW = 1500
    Ow = 1501
    OX = 1502
    Ox = 1503
    OY = 1504
    Oy = 1505
    OZ = 1506
    Oz = 1507
    oA = 1508
    oa = 1509
    oB = 1510
    ob = 1511
    oC = 1512
    oc = 1513
    oD = 1514
    od = 1515
    oE = 1516
    oe = 1517
    oF = 1518
    of = 1519
    oG = 1520
    og = 1521
    oH = 1522
    oh = 1523
    oI = 1524
    oi = 1525
    oJ = 1526
    oj = 1527
    oK = 1528
    ok = 1529
    oL = 1530
    ol = 1531
    oM = 1532
    om = 1533
    oN = 1534
    on = 1535
    oO = 1536
    oo = 1537
    oP = 1538
    op = 1539
    oQ = 1540
    oq = 1541
    oR = 1542
    # or = 1543
    oS = 1544
    os = 1545
    oT = 1546
    ot = 1547
    oU = 1548
    ou = 1549
    oV = 1550
    ov = 1551
    oW = 1552
    ow = 1553
    oX = 1554
    ox = 1555
    oY = 1556
    oy = 1557
    oZ = 1558
    oz = 1559
    PA = 1560
    Pa = 1561
    PB = 1562
    Pb = 1563
    PC = 1564
    Pc = 1565
    PD = 1566
    Pd = 1567
    PE = 1568
    Pe = 1569
    PF = 1570
    Pf = 1571
    PG = 1572
    Pg = 1573
    PH = 1574
    Ph = 1575
    PI = 1576
    Pi = 1577
    PJ = 1578
    Pj = 1579
    PK = 1580
    Pk = 1581
    PL = 1582
    Pl = 1583
    PM = 1584
    Pm = 1585
    PN = 1586
    Pn = 1587
    PO = 1588
    Po = 1589
    PP = 1590
    Pp = 1591
    PQ = 1592
    Pq = 1593
    PR = 1594
    Pr = 1595
    PS = 1596
    Ps = 1597
    PT = 1598
    Pt = 1599
    PU = 1600
    Pu = 1601
    PV = 1602
    Pv = 1603
    PW = 1604
    Pw = 1605
    PX = 1606
    Px = 1607
    PY = 1608
    Py = 1609
    PZ = 1610
    Pz = 1611
    pA = 1612
    pa = 1613
    pB = 1614
    pb = 1615
    pC = 1616
    pc = 1617
    pD = 1618
    pd = 1619
    pE = 1620
    pe = 1621
    pF = 1622
    pf = 1623
    pG = 1624
    pg = 1625
    pH = 1626
    ph = 1627
    pI = 1628
    pi = 1629
    pJ = 1630
    pj = 1631
    pK = 1632
    pk = 1633
    pL = 1634
    pl = 1635
    pM = 1636
    pm = 1637
    pN = 1638
    pn = 1639
    pO = 1640
    po = 1641
    pP = 1642
    pp = 1643
    pQ = 1644
    pq = 1645
    pR = 1646
    pr = 1647
    pS = 1648
    ps = 1649
    pT = 1650
    pt = 1651
    pU = 1652
    pu = 1653
    pV = 1654
    pv = 1655
    pW = 1656
    pw = 1657
    pX = 1658
    px = 1659
    pY = 1660
    py = 1661
    pZ = 1662
    pz = 1663
    QA = 1664
    Qa = 1665
    QB = 1666
    Qb = 1667
    QC = 1668
    Qc = 1669
    QD = 1670
    Qd = 1671
    QE = 1672
    Qe = 1673
    QF = 1674
    Qf = 1675
    QG = 1676
    Qg = 1677
    QH = 1678
    Qh = 1679
    QI = 1680
    Qi = 1681
    QJ = 1682
    Qj = 1683
    QK = 1684
    Qk = 1685
    QL = 1686
    Ql = 1687
    QM = 1688
    Qm = 1689
    QN = 1690
    Qn = 1691
    QO = 1692
    Qo = 1693
    QP = 1694
    Qp = 1695
    QQ = 1696
    Qq = 1697
    QR = 1698
    Qr = 1699
    QS = 1700
    Qs = 1701
    QT = 1702
    Qt = 1703
    QU = 1704
    Qu = 1705
    QV = 1706
    Qv = 1707
    QW = 1708
    Qw = 1709
    QX = 1710
    Qx = 1711
    QY = 1712
    Qy = 1713
    QZ = 1714
    Qz = 1715
    qA = 1716
    qa = 1717
    qB = 1718
    qb = 1719
    qC = 1720
    qc = 1721
    qD = 1722
    qd = 1723
    qE = 1724
    qe = 1725
    qF = 1726
    qf = 1727
    qG = 1728
    qg = 1729
    qH = 1730
    qh = 1731
    qI = 1732
    qi = 1733
    qJ = 1734
    qj = 1735
    qK = 1736
    qk = 1737
    qL = 1738
    ql = 1739
    qM = 1740
    qm = 1741
    qN = 1742
    qn = 1743
    qO = 1744
    qo = 1745
    qP = 1746
    qp = 1747
    qQ = 1748
    qq = 1749
    qR = 1750
    qr = 1751
    qS = 1752
    qs = 1753
    qT = 1754
    qt = 1755
    qU = 1756
    qu = 1757
    qV = 1758
    qv = 1759
    qW = 1760
    qw = 1761
    qX = 1762
    qx = 1763
    qY = 1764
    qy = 1765
    qZ = 1766
    qz = 1767
    RA = 1768
    Ra = 1769
    RB = 1770
    Rb = 1771
    RC = 1772
    Rc = 1773
    RD = 1774
    Rd = 1775
    RE = 1776
    Re = 1777
    RF = 1778
    Rf = 1779
    RG = 1780
    Rg = 1781
    RH = 1782
    Rh = 1783
    RI = 1784
    Ri = 1785
    RJ = 1786
    Rj = 1787
    RK = 1788
    Rk = 1789
    RL = 1790
    Rl = 1791
    RM = 1792
    Rm = 1793
    RN = 1794
    Rn = 1795
    RO = 1796
    Ro = 1797
    RP = 1798
    Rp = 1799
    RQ = 1800
    Rq = 1801
    RR = 1802
    Rr = 1803
    RS = 1804
    Rs = 1805
    RT = 1806
    Rt = 1807
    RU = 1808
    Ru = 1809
    RV = 1810
    Rv = 1811
    RW = 1812
    Rw = 1813
    RX = 1814
    Rx = 1815
    RY = 1816
    Ry = 1817
    RZ = 1818
    Rz = 1819
    rA = 1820
    ra = 1821
    rB = 1822
    rb = 1823
    rC = 1824
    rc = 1825
    rD = 1826
    rd = 1827
    rE = 1828
    re = 1829
    rF = 1830
    rf = 1831
    rG = 1832
    rg = 1833
    rH = 1834
    rh = 1835
    rI = 1836
    ri = 1837
    rJ = 1838
    rj = 1839
    rK = 1840
    rk = 1841
    rL = 1842
    rl = 1843
    rM = 1844
    rm = 1845
    rN = 1846
    rn = 1847
    rO = 1848
    ro = 1849
    rP = 1850
    rp = 1851
    rQ = 1852
    rq = 1853
    rR = 1854
    rr = 1855
    rS = 1856
    rs = 1857
    rT = 1858
    rt = 1859
    rU = 1860
    ru = 1861
    rV = 1862
    rv = 1863
    rW = 1864
    rw = 1865
    rX = 1866
    rx = 1867
    rY = 1868
    ry = 1869
    rZ = 1870
    rz = 1871
    SA = 1872
    Sa = 1873
    SB = 1874
    Sb = 1875
    SC = 1876
    Sc = 1877
    SD = 1878
    Sd = 1879
    SE = 1880
    Se = 1881
    SF = 1882
    Sf = 1883
    SG = 1884
    Sg = 1885
    SH = 1886
    Sh = 1887
    SI = 1888
    Si = 1889
    SJ = 1890
    Sj = 1891
    SK = 1892
    Sk = 1893
    SL = 1894
    Sl = 1895
    SM = 1896
    Sm = 1897
    SN = 1898
    Sn = 1899
    SO = 1900
    So = 1901
    SP = 1902
    Sp = 1903
    SQ = 1904
    Sq = 1905
    SR = 1906
    Sr = 1907
    SS = 1908
    Ss = 1909
    ST = 1910
    St = 1911
    SU = 1912
    Su = 1913
    SV = 1914
    Sv = 1915
    SW = 1916
    Sw = 1917
    SX = 1918
    Sx = 1919
    SY = 1920
    Sy = 1921
    SZ = 1922
    Sz = 1923
    sA = 1924
    sa = 1925
    sB = 1926
    sb = 1927
    sC = 1928
    sc = 1929
    sD = 1930
    sd = 1931
    sE = 1932
    se = 1933
    sF = 1934
    sf = 1935
    sG = 1936
    sg = 1937
    sH = 1938
    sh = 1939
    sI = 1940
    si = 1941
    sJ = 1942
    sj = 1943
    sK = 1944
    sk = 1945
    sL = 1946
    sl = 1947
    sM = 1948
    sm = 1949
    sN = 1950
    sn = 1951
    sO = 1952
    so = 1953
    sP = 1954
    sp = 1955
    sQ = 1956
    sq = 1957
    sR = 1958
    sr = 1959
    sS = 1960
    ss = 1961
    sT = 1962
    st = 1963
    sU = 1964
    su = 1965
    sV = 1966
    sv = 1967
    sW = 1968
    sw = 1969
    sX = 1970
    sx = 1971
    sY = 1972
    sy = 1973
    sZ = 1974
    sz = 1975
    TA = 1976
    Ta = 1977
    TB = 1978
    Tb = 1979
    TC = 1980
    Tc = 1981
    TD = 1982
    Td = 1983
    TE = 1984
    Te = 1985
    TF = 1986
    Tf = 1987
    TG = 1988
    Tg = 1989
    TH = 1990
    Th = 1991
    TI = 1992
    Ti = 1993
    TJ = 1994
    Tj = 1995
    TK = 1996
    Tk = 1997
    TL = 1998
    Tl = 1999
    TM = 2000
    Tm = 2001
    TN = 2002
    Tn = 2003
    TO = 2004
    To = 2005
    TP = 2006
    Tp = 2007
    TQ = 2008
    Tq = 2009
    TR = 2010
    Tr = 2011
    TS = 2012
    Ts = 2013
    TT = 2014
    Tt = 2015
    TU = 2016
    Tu = 2017
    TV = 2018
    Tv = 2019
    TW = 2020
    Tw = 2021
    TX = 2022
    Tx = 2023
    TY = 2024
    Ty = 2025
    TZ = 2026
    Tz = 2027
    tA = 2028
    ta = 2029
    tB = 2030
    tb = 2031
    tC = 2032
    tc = 2033
    tD = 2034
    td = 2035
    tE = 2036
    te = 2037
    tF = 2038
    tf = 2039
    tG = 2040
    tg = 2041
    tH = 2042
    th = 2043
    tI = 2044
    ti = 2045
    tJ = 2046
    tj = 2047
    tK = 2048
    tk = 2049
    tL = 2050
    tl = 2051
    tM = 2052
    tm = 2053
    tN = 2054
    tn = 2055
    tO = 2056
    to = 2057
    tP = 2058
    tp = 2059
    tQ = 2060
    tq = 2061
    tR = 2062
    tr = 2063
    tS = 2064
    ts = 2065
    tT = 2066
    tt = 2067
    tU = 2068
    tu = 2069
    tV = 2070
    tv = 2071
    tW = 2072
    tw = 2073
    tX = 2074
    tx = 2075
    tY = 2076
    ty = 2077
    tZ = 2078
    tz = 2079
    UA = 2080
    Ua = 2081
    UB = 2082
    Ub = 2083
    UC = 2084
    Uc = 2085
    UD = 2086
    Ud = 2087
    UE = 2088
    Ue = 2089
    UF = 2090
    Uf = 2091
    UG = 2092
    Ug = 2093
    UH = 2094
    Uh = 2095
    UI = 2096
    Ui = 2097
    UJ = 2098
    Uj = 2099
    UK = 2100
    Uk = 2101
    UL = 2102
    Ul = 2103
    UM = 2104
    Um = 2105
    UN = 2106
    Un = 2107
    UO = 2108
    Uo = 2109
    UP = 2110
    Up = 2111
    UQ = 2112
    Uq = 2113
    UR = 2114
    Ur = 2115
    US = 2116
    Us = 2117
    UT = 2118
    Ut = 2119
    UU = 2120
    Uu = 2121
    UV = 2122
    Uv = 2123
    UW = 2124
    Uw = 2125
    UX = 2126
    Ux = 2127
    UY = 2128
    Uy = 2129
    UZ = 2130
    Uz = 2131
    uA = 2132
    ua = 2133
    uB = 2134
    ub = 2135
    uC = 2136
    uc = 2137
    uD = 2138
    ud = 2139
    uE = 2140
    ue = 2141
    uF = 2142
    uf = 2143
    uG = 2144
    ug = 2145
    uH = 2146
    uh = 2147
    uI = 2148
    ui = 2149
    uJ = 2150
    uj = 2151
    uK = 2152
    uk = 2153
    uL = 2154
    ul = 2155
    uM = 2156
    um = 2157
    uN = 2158
    un = 2159
    uO = 2160
    uo = 2161
    uP = 2162
    up = 2163
    uQ = 2164
    uq = 2165
    uR = 2166
    ur = 2167
    uS = 2168
    us = 2169
    uT = 2170
    ut = 2171
    uU = 2172
    uu = 2173
    uV = 2174
    uv = 2175
    uW = 2176
    uw = 2177
    uX = 2178
    ux = 2179
    uY = 2180
    uy = 2181
    uZ = 2182
    uz = 2183
    VA = 2184
    Va = 2185
    VB = 2186
    Vb = 2187
    VC = 2188
    Vc = 2189
    VD = 2190
    Vd = 2191
    VE = 2192
    Ve = 2193
    VF = 2194
    Vf = 2195
    VG = 2196
    Vg = 2197
    VH = 2198
    Vh = 2199
    VI = 2200
    Vi = 2201
    VJ = 2202
    Vj = 2203
    VK = 2204
    Vk = 2205
    VL = 2206
    Vl = 2207
    VM = 2208
    Vm = 2209
    VN = 2210
    Vn = 2211
    VO = 2212
    Vo = 2213
    VP = 2214
    Vp = 2215
    VQ = 2216
    Vq = 2217
    VR = 2218
    Vr = 2219
    VS = 2220
    Vs = 2221
    VT = 2222
    Vt = 2223
    VU = 2224
    Vu = 2225
    VV = 2226
    Vv = 2227
    VW = 2228
    Vw = 2229
    VX = 2230
    Vx = 2231
    VY = 2232
    Vy = 2233
    VZ = 2234
    Vz = 2235
    vA = 2236
    va = 2237
    vB = 2238
    vb = 2239
    vC = 2240
    vc = 2241
    vD = 2242
    vd = 2243
    vE = 2244
    ve = 2245
    vF = 2246
    vf = 2247
    vG = 2248
    vg = 2249
    vH = 2250
    vh = 2251
    vI = 2252
    vi = 2253
    vJ = 2254
    vj = 2255
    vK = 2256
    vk = 2257
    vL = 2258
    vl = 2259
    vM = 2260
    vm = 2261
    vN = 2262
    vn = 2263
    vO = 2264
    vo = 2265
    vP = 2266
    vp = 2267
    vQ = 2268
    vq = 2269
    vR = 2270
    vr = 2271
    vS = 2272
    vs = 2273
    vT = 2274
    vt = 2275
    vU = 2276
    vu = 2277
    vV = 2278
    vv = 2279
    vW = 2280
    vw = 2281
    vX = 2282
    vx = 2283
    vY = 2284
    vy = 2285
    vZ = 2286
    vz = 2287
    WA = 2288
    Wa = 2289
    WB = 2290
    Wb = 2291
    WC = 2292
    Wc = 2293
    WD = 2294
    Wd = 2295
    WE = 2296
    We = 2297
    WF = 2298
    Wf = 2299
    WG = 2300
    Wg = 2301
    WH = 2302
    Wh = 2303
    WI = 2304
    Wi = 2305
    WJ = 2306
    Wj = 2307
    WK = 2308
    Wk = 2309
    WL = 2310
    Wl = 2311
    WM = 2312
    Wm = 2313
    WN = 2314
    Wn = 2315
    WO = 2316
    Wo = 2317
    WP = 2318
    Wp = 2319
    WQ = 2320
    Wq = 2321
    WR = 2322
    Wr = 2323
    WS = 2324
    Ws = 2325
    WT = 2326
    Wt = 2327
    WU = 2328
    Wu = 2329
    WV = 2330
    Wv = 2331
    WW = 2332
    Ww = 2333
    WX = 2334
    Wx = 2335
    WY = 2336
    Wy = 2337
    WZ = 2338
    Wz = 2339
    wA = 2340
    wa = 2341
    wB = 2342
    wb = 2343
    wC = 2344
    wc = 2345
    wD = 2346
    wd = 2347
    wE = 2348
    we = 2349
    wF = 2350
    wf = 2351
    wG = 2352
    wg = 2353
    wH = 2354
    wh = 2355
    wI = 2356
    wi = 2357
    wJ = 2358
    wj = 2359
    wK = 2360
    wk = 2361
    wL = 2362
    wl = 2363
    wM = 2364
    wm = 2365
    wN = 2366
    wn = 2367
    wO = 2368
    wo = 2369
    wP = 2370
    wp = 2371
    wQ = 2372
    wq = 2373
    wR = 2374
    wr = 2375
    wS = 2376
    ws = 2377
    wT = 2378
    wt = 2379
    wU = 2380
    wu = 2381
    wV = 2382
    wv = 2383
    wW = 2384
    ww = 2385
    wX = 2386
    wx = 2387
    wY = 2388
    wy = 2389
    wZ = 2390
    wz = 2391
    XA = 2392
    Xa = 2393
    XB = 2394
    Xb = 2395
    XC = 2396
    Xc = 2397
    XD = 2398
    Xd = 2399
    XE = 2400
    Xe = 2401
    XF = 2402
    Xf = 2403
    XG = 2404
    Xg = 2405
    XH = 2406
    Xh = 2407
    XI = 2408
    Xi = 2409
    XJ = 2410
    Xj = 2411
    XK = 2412
    Xk = 2413
    XL = 2414
    Xl = 2415
    XM = 2416
    Xm = 2417
    XN = 2418
    Xn = 2419
    XO = 2420
    Xo = 2421
    XP = 2422
    Xp = 2423
    XQ = 2424
    Xq = 2425
    XR = 2426
    Xr = 2427
    XS = 2428
    Xs = 2429
    XT = 2430
    Xt = 2431
    XU = 2432
    Xu = 2433
    XV = 2434
    Xv = 2435
    XW = 2436
    Xw = 2437
    XX = 2438
    Xx = 2439
    XY = 2440
    Xy = 2441
    XZ = 2442
    Xz = 2443
    xA = 2444
    xa = 2445
    xB = 2446
    xb = 2447
    xC = 2448
    xc = 2449
    xD = 2450
    xd = 2451
    xE = 2452
    xe = 2453
    xF = 2454
    xf = 2455
    xG = 2456
    xg = 2457
    xH = 2458
    xh = 2459
    xI = 2460
    xi = 2461
    xJ = 2462
    xj = 2463
    xK = 2464
    xk = 2465
    xL = 2466
    xl = 2467
    xM = 2468
    xm = 2469
    xN = 2470
    xn = 2471
    xO = 2472
    xo = 2473
    xP = 2474
    xp = 2475
    xQ = 2476
    xq = 2477
    xR = 2478
    xr = 2479
    xS = 2480
    xs = 2481
    xT = 2482
    xt = 2483
    xU = 2484
    xu = 2485
    xV = 2486
    xv = 2487
    xW = 2488
    xw = 2489
    xX = 2490
    xx = 2491
    xY = 2492
    xy = 2493
    xZ = 2494
    xz = 2495
    YA = 2496
    Ya = 2497
    YB = 2498
    Yb = 2499
    YC = 2500
    Yc = 2501
    YD = 2502
    Yd = 2503
    YE = 2504
    Ye = 2505
    YF = 2506
    Yf = 2507
    YG = 2508
    Yg = 2509
    YH = 2510
    Yh = 2511
    YI = 2512
    Yi = 2513
    YJ = 2514
    Yj = 2515
    YK = 2516
    Yk = 2517
    YL = 2518
    Yl = 2519
    YM = 2520
    Ym = 2521
    YN = 2522
    Yn = 2523
    YO = 2524
    Yo = 2525
    YP = 2526
    Yp = 2527
    YQ = 2528
    Yq = 2529
    YR = 2530
    Yr = 2531
    YS = 2532
    Ys = 2533
    YT = 2534
    Yt = 2535
    YU = 2536
    Yu = 2537
    YV = 2538
    Yv = 2539
    YW = 2540
    Yw = 2541
    YX = 2542
    Yx = 2543
    YY = 2544
    Yy = 2545
    YZ = 2546
    Yz = 2547
    yA = 2548
    ya = 2549
    yB = 2550
    yb = 2551
    yC = 2552
    yc = 2553
    yD = 2554
    yd = 2555
    yE = 2556
    ye = 2557
    yF = 2558
    yf = 2559
    yG = 2560
    yg = 2561
    yH = 2562
    yh = 2563
    yI = 2564
    yi = 2565
    yJ = 2566
    yj = 2567
    yK = 2568
    yk = 2569
    yL = 2570
    yl = 2571
    yM = 2572
    ym = 2573
    yN = 2574
    yn = 2575
    yO = 2576
    yo = 2577
    yP = 2578
    yp = 2579
    yQ = 2580
    yq = 2581
    yR = 2582
    yr = 2583
    yS = 2584
    ys = 2585
    yT = 2586
    yt = 2587
    yU = 2588
    yu = 2589
    yV = 2590
    yv = 2591
    yW = 2592
    yw = 2593
    yX = 2594
    yx = 2595
    yY = 2596
    yy = 2597
    yZ = 2598
    yz = 2599
    ZA = 2600
    Za = 2601
    ZB = 2602
    Zb = 2603
    ZC = 2604
    Zc = 2605
    ZD = 2606
    Zd = 2607
    ZE = 2608
    Ze = 2609
    ZF = 2610
    Zf = 2611
    ZG = 2612
    Zg = 2613
    ZH = 2614
    Zh = 2615
    ZI = 2616
    Zi = 2617
    ZJ = 2618
    Zj = 2619
    ZK = 2620
    Zk = 2621
    ZL = 2622
    Zl = 2623
    ZM = 2624
    Zm = 2625
    ZN = 2626
    Zn = 2627
    ZO = 2628
    Zo = 2629
    ZP = 2630
    Zp = 2631
    ZQ = 2632
    Zq = 2633
    ZR = 2634
    Zr = 2635
    ZS = 2636
    Zs = 2637
    ZT = 2638
    Zt = 2639
    ZU = 2640
    Zu = 2641
    ZV = 2642
    Zv = 2643
    ZW = 2644
    Zw = 2645
    ZX = 2646
    Zx = 2647
    ZY = 2648
    Zy = 2649
    ZZ = 2650
    Zz = 2651
    zA = 2652
    za = 2653
    zB = 2654
    zb = 2655
    zC = 2656
    zc = 2657
    zD = 2658
    zd = 2659
    zE = 2660
    ze = 2661
    zF = 2662
    zf = 2663
    zG = 2664
    zg = 2665
    zH = 2666
    zh = 2667
    zI = 2668
    zi = 2669
    zJ = 2670
    zj = 2671
    zK = 2672
    zk = 2673
    zL = 2674
    zl = 2675
    zM = 2676
    zm = 2677
    zN = 2678
    zn = 2679
    zO = 2680
    zo = 2681
    zP = 2682
    zp = 2683
    zQ = 2684
    zq = 2685
    zR = 2686
    zr = 2687
    zS = 2688
    zs = 2689
    zT = 2690
    zt = 2691
    zU = 2692
    zu = 2693
    zV = 2694
    zv = 2695
    zW = 2696
    zw = 2697
    zX = 2698
    zx = 2699
    zY = 2700
    zy = 2701
    zZ = 2702
    zz = 2703
    aAA = 2704
    aAa = 2705
    aAB = 2706
    aAb = 2707
    aAC = 2708
    aAc = 2709
    aAD = 2710
    aAd = 2711
    aAE = 2712
    aAe = 2713
    aAF = 2714
    aAf = 2715
    aAG = 2716
    aAg = 2717
    aAH = 2718
    aAh = 2719
    aAI = 2720
    aAi = 2721
    aAJ = 2722
    aAj = 2723
    aAK = 2724
    aAk = 2725
    aAL = 2726
    aAl = 2727
    aAM = 2728
    aAm = 2729
    aAN = 2730
    aAn = 2731
    aAO = 2732
    aAo = 2733
    aAP = 2734
    aAp = 2735
    aAQ = 2736
    aAq = 2737
    aAR = 2738
    aAr = 2739
    aAS = 2740
    aAs = 2741
    aAT = 2742
    aAt = 2743
    aAU = 2744
    aAu = 2745
    aAV = 2746
    aAv = 2747
    aAW = 2748
    aAw = 2749
    aAX = 2750
    aAx = 2751
    aAY = 2752
    aAy = 2753
    aAZ = 2754
    aAz = 2755
    aaA = 2756
    aaa = 2757
    aaB = 2758
    aab = 2759
    aaC = 2760
    aac = 2761
    aaD = 2762
    aad = 2763
    aaE = 2764
    aae = 2765
    aaF = 2766
    aaf = 2767
    aaG = 2768
    aag = 2769
    aaH = 2770
    aah = 2771
    aaI = 2772
    aai = 2773
    aaJ = 2774
    aaj = 2775
    aaK = 2776
    aak = 2777
    aaL = 2778
    aal = 2779
    aaM = 2780
    aam = 2781
    aaN = 2782
    aan = 2783
    aaO = 2784
    aao = 2785
    aaP = 2786
    aap = 2787
    aaQ = 2788
    aaq = 2789
    aaR = 2790
    aar = 2791
    aaS = 2792
    aas = 2793
    aaT = 2794
    aat = 2795
    aaU = 2796
    aau = 2797
    aaV = 2798
    aav = 2799
    aaW = 2800
    aaw = 2801
    aaX = 2802
    aax = 2803
    aaY = 2804
    aay = 2805
    aaZ = 2806
    aaz = 2807
    aBA = 2808
    aBa = 2809
    aBB = 2810
    aBb = 2811
    aBC = 2812
    aBc = 2813
    aBD = 2814
    aBd = 2815
    aBE = 2816
    aBe = 2817
    aBF = 2818
    aBf = 2819
    aBG = 2820
    aBg = 2821
    aBH = 2822
    aBh = 2823
    aBI = 2824
    aBi = 2825
    aBJ = 2826
    aBj = 2827
    aBK = 2828
    aBk = 2829
    aBL = 2830
    aBl = 2831
    aBM = 2832
    aBm = 2833
    aBN = 2834
    aBn = 2835
    aBO = 2836
    aBo = 2837
    aBP = 2838
    aBp = 2839
    aBQ = 2840
    aBq = 2841
    aBR = 2842
    aBr = 2843
    aBS = 2844
    aBs = 2845
    aBT = 2846
    aBt = 2847
    aBU = 2848
    aBu = 2849
    aBV = 2850
    aBv = 2851
    aBW = 2852
    aBw = 2853
    aBX = 2854
    aBx = 2855
    aBY = 2856
    aBy = 2857
    aBZ = 2858
    aBz = 2859
    abA = 2860
    aba = 2861
    abB = 2862
    abb = 2863
    abC = 2864
    abc = 2865
    abD = 2866
    abd = 2867
    abE = 2868
    abe = 2869
    abF = 2870
    abf = 2871
    abG = 2872
    abg = 2873
    abH = 2874
    abh = 2875
    abI = 2876
    abi = 2877
    abJ = 2878
    abj = 2879
    abK = 2880
    abk = 2881
    abL = 2882
    abl = 2883
    abM = 2884
    abm = 2885
    abN = 2886
    abn = 2887
    abO = 2888
    abo = 2889
    abP = 2890
    abp = 2891
    abQ = 2892
    abq = 2893
    abR = 2894
    abr = 2895
    abS = 2896
    abs = 2897
    abT = 2898
    abt = 2899
    abU = 2900
    abu = 2901
    abV = 2902
    abv = 2903
    abW = 2904
    abw = 2905
    abX = 2906
    abx = 2907
    abY = 2908
    aby = 2909
    abZ = 2910
    abz = 2911
    aCA = 2912
    aCa = 2913
    aCB = 2914
    aCb = 2915
    aCC = 2916
    aCc = 2917
    aCD = 2918
    aCd = 2919
    aCE = 2920
    aCe = 2921
    aCF = 2922
    aCf = 2923
    aCG = 2924
    aCg = 2925
    aCH = 2926
    aCh = 2927
    aCI = 2928
    aCi = 2929
    aCJ = 2930
    aCj = 2931
    aCK = 2932
    aCk = 2933
    aCL = 2934
    aCl = 2935
    aCM = 2936
    aCm = 2937
    aCN = 2938
    aCn = 2939
    aCO = 2940
    aCo = 2941
    aCP = 2942
    aCp = 2943
    aCQ = 2944
    aCq = 2945
    aCR = 2946
    aCr = 2947
    aCS = 2948
    aCs = 2949
    aCT = 2950
    aCt = 2951
    aCU = 2952
    aCu = 2953
    aCV = 2954
    aCv = 2955
    aCW = 2956
    aCw = 2957
    aCX = 2958
    aCx = 2959
    aCY = 2960
    aCy = 2961
    aCZ = 2962
    aCz = 2963
    acA = 2964
    aca = 2965
    acB = 2966
    acb = 2967
    acC = 2968
    acc = 2969
    acD = 2970
    acd = 2971
    acE = 2972
    ace = 2973
    acF = 2974
    acf = 2975
    acG = 2976
    acg = 2977
    acH = 2978
    ach = 2979
    acI = 2980
    aci = 2981
    acJ = 2982
    acj = 2983
    acK = 2984
    ack = 2985
    acL = 2986
    acl = 2987
    acM = 2988
    acm = 2989
    acN = 2990
    acn = 2991
    acO = 2992
    aco = 2993
    acP = 2994
    acp = 2995
    acQ = 2996
    acq = 2997
    acR = 2998
    acr = 2999
    acS = 3000
    acs = 3001
    acT = 3002
    act = 3003


class Club(IntEnum):
    none = 0
    Engineer = 1
    CleanNClearing = 2
    KnightsHospitaller = 3
    IndeGEHENNA = 4
    IndeMILLENNIUM = 5
    IndeHyakkiyako = 6
    IndeShanhaijing = 7
    IndeTrinity = 8
    FoodService = 9
    Countermeasure = 10
    BookClub = 11
    MatsuriOffice = 12
    GourmetClub = 13
    HoukagoDessert = 14
    RedwinterSecretary = 15
    Schale = 16
    TheSeminar = 17
    AriusSqud = 18
    Justice = 19
    Fuuki = 20
    Kohshinjo68 = 21
    Meihuayuan = 22
    SisterHood = 23
    GameDev = 24
    anzenkyoku = 25
    RemedialClass = 26
    SPTF = 27
    TrinityVigilance = 28
    Veritas = 29
    TrainingClub = 30
    Onmyobu = 31
    Shugyobu = 32
    Endanbou = 33
    NinpoKenkyubu = 34
    Class227 = 35
    EmptyClub = 36
    Emergentology = 37
    RabbitPlatoon = 38
    PandemoniumSociety = 39
    HotSpringsDepartment = 40
    TeaParty = 41
    PublicPeaceBureau = 42
    Genryumon = 43
    BlackTortoisePromenade = 44
    LaborParty = 45
    KnowledgeLiberationFront = 46
    Hyakkayouran = 47
    ShinySparkleSociety = 48
