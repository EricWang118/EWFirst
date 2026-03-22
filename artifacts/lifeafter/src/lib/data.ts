export const GAME_VERSION = "2026年3月22日 · 春日樱花季";

export type ActivityStatus = 'active' | 'upcoming' | 'ending-soon' | 'ended';
export type ServerType = '全服' | '经典服' | '简单生存专服';
export type PlayerTag = '白嫖' | '战力' | '庄园' | '外观' | '回坑' | 'PVP';

export interface Activity {
  id: string;
  name: string;
  status: ActivityStatus;
  date: string;
  server: ServerType;
  description: string;
  gameplay: string;
  rewards: string;
  tips: string;
  tags: PlayerTag[];
  priority: '极高' | '高' | '中' | '低';
  category: '春日福利' | '限时玩法' | '奖池/商城' | '竞技赛事' | '系统优化' | '即将开启' | '已结束/下架';
}

export const ACTIVITIES: Activity[] = [
  {
    id: "sakura-bloom",
    name: "樱花绽放",
    status: "active",
    date: "3月20日 ~ 4月3日 3:00",
    server: "全服",
    description: "种植限时樱花树，收获樱花花瓣后去兑换商店换取奖励。经典服可兑换樱花树种子（可插花版）、樱花树野外基建、樱花系列家具；简单生存专服可兑换樱花树种子（可插花版）、樱花系列家具。",
    gameplay: "种植限时樱花树 → 收获樱花花瓣 → 兑换商店换奖励",
    rewards: "樱花树种子（可插花版）、樱花树野外基建、樱花系列家具",
    tips: "实战重点不是爆肝，而是尽快开种、尽快稳定产出花瓣。早开种 = 多产出。",
    tags: ["白嫖", "庄园"],
    priority: "极高",
    category: "春日福利"
  },
  {
    id: "flower-forest",
    name: "寻觅花林",
    status: "active",
    date: "3月20日 ~ 4月3日 3:00",
    server: "全服",
    description: "前往快乐101、晴空麦田、莱辛港找到移栽的樱花树和林间打卡点，拍照打卡即可获得动态头像框。本质上是轻量级跑图/拍照活动。",
    gameplay: "前往指定地图 → 找到樱花树和打卡点 → 拍照打卡",
    rewards: "动态头像框",
    tips: "成本最低、最不该漏掉的活动。不需要战力门槛，也不需要氪金，所有玩家必做。",
    tags: ["白嫖", "外观"],
    priority: "极高",
    category: "春日福利"
  },
  {
    id: "peach-feather",
    name: "桃羽收集大作战",
    status: "active",
    date: "3月20日 ~ 5月21日 24:00",
    server: "全服",
    description: "与春季农场上新联动：3月20日~5月15日，饲育屋里的矮脚鸡、嘎嘎鸭、咕咕鹅有概率孵化成桃花款小动物，掉落桃花羽毛和桃花蛋，用这些去兑换主题家具。这不是单独活动，而是「春季农场产出 → 桃羽兑换」的完整闭环。",
    gameplay: "春季农场孵化桃花款小动物 → 收集桃花羽毛/桃花蛋 → 兑换家具",
    rewards: "家具·桃花蛋窝、家具·桃花小鸡公仔、家具·桃花小鸭公仔、家具·桃花小鹅公仔等",
    tips: "养成党和庄园党优先级很高。活动周期长，不需要急，但要尽早开始农场产出。",
    tags: ["白嫖", "庄园"],
    priority: "高",
    category: "春日福利"
  },
  {
    id: "april-login",
    name: "4月1日登录福利",
    status: "upcoming",
    date: "4月1日当天",
    server: "全服",
    description: "4月1日当天登录即可领取限定表情包、限定称号、神秘道具。节点性活动，当天别忘记登录。",
    gameplay: "当天登录即可领取",
    rewards: "限定表情包、限定称号、神秘道具",
    tips: "别忘了4月1日登录领取，错过就没了。",
    tags: ["白嫖"],
    priority: "高",
    category: "即将开启"
  },
  {
    id: "mystery-manuscript",
    name: "神秘手稿",
    status: "upcoming",
    date: "4月1日当天",
    server: "全服",
    description: "4月1日当天进行采集、战斗、钓鱼时，有概率掉落张博的手稿。手稿里有恶作剧纸条，也有记录未来会真实发生之事的内容。春日主题彩蛋型掉落活动。",
    gameplay: "采集、战斗、钓鱼 → 概率掉落手稿",
    rewards: "张博的手稿（含彩蛋内容）",
    tips: "做日常的时候顺便就能触发，不用专门刷。",
    tags: ["白嫖"],
    priority: "中",
    category: "即将开启"
  },
  {
    id: "special-combat",
    name: "特战巅峰赛（测试）",
    status: "ending-soon",
    date: "3月20日 ~ 3月22日",
    server: "全服",
    description: "正式开测的竞技赛事，赛程包含海选、小组、淘汰赛。官方明确表示：这次测试的真实对战反馈，会被拿去打磨并确立2026正式比赛规则。有专门的入场方式、组队报名流程、赛程安排。",
    gameplay: "海选 → 小组赛 → 淘汰赛",
    rewards: "赛事奖励（具体数值暂未完整公开）",
    tips: "PVP玩家优先参与！今天(3月22日)是最后一天窗口。普通玩家可当赛事活动参与，优先级低于春日福利但高于纯外观池。",
    tags: ["PVP", "战力"],
    priority: "极高",
    category: "竞技赛事"
  },
  {
    id: "qingsong-season",
    name: "青松季（减负优化）",
    status: "active",
    date: "当前版本持续",
    server: "全服",
    description: "项目组在庄园、养成、日常等多个维度做了深度改革与优化。当前能落到实处的减负项目包括：专属配件箱自动开箱/最高阶开箱、批量分解、经验转移优化、染色分享码、边境农场邀请共耕、核芯预购、南茜市防连控等。",
    gameplay: "自动享受系统减负优化",
    rewards: "节省日常时间、降低养成压力",
    tips: "本质上是「时间价值活动」。对老区养老党、回坑党、新号养成党都很重要，甚至比部分抽奖池更值得关注。回坑玩家最该先看这个——现在回坑没那么肝了。",
    tags: ["白嫖", "回坑"],
    priority: "极高",
    category: "系统优化"
  },
  {
    id: "frozen-snow",
    name: "凛雪危局",
    status: "active",
    date: "3月6日 ~ 4月3日 8:00",
    server: "全服",
    description: "限时回归玩法。前往废弃的捷卡德琳堡搜索物资，在风雪环境里争取收益。适合喜欢跑玩法本体的玩家。",
    gameplay: "前往废弃的捷卡德琳堡 → 搜索物资 → 风雪生存对抗",
    rewards: "搜索物资收益（具体奖励表暂未完整展开）",
    tips: "限时回归玩法，对喜欢生存对抗玩法的玩家来说比纯外观池更有价值。",
    tags: ["白嫖", "战力"],
    priority: "中",
    category: "限时玩法"
  },
  {
    id: "puppet-contract",
    name: "人偶契约",
    status: "ended",
    date: "已于3月12日 3:00下架",
    server: "全服",
    description: "已下架的外观内容。如果你错过了这个皮肤，可以关注后续是否会返场。",
    gameplay: "已结束",
    rewards: "已结束",
    tips: "已下架，等待未来可能的返场。",
    tags: ["外观"],
    priority: "低",
    category: "已结束/下架"
  },
  {
    id: "cloud-away",
    name: "乌云退退退",
    status: "ended",
    date: "已于3月20日 3:00截止",
    server: "全服",
    description: "已结束的限时活动。",
    gameplay: "已结束",
    rewards: "已结束",
    tips: "已结束。",
    tags: [],
    priority: "低",
    category: "已结束/下架"
  },
  {
    id: "return-squad",
    name: "返利小队",
    status: "ended",
    date: "已于3月6日结束",
    server: "全服",
    description: "已结束的返利活动。",
    gameplay: "已结束",
    rewards: "已结束",
    tips: "已结束。",
    tags: [],
    priority: "低",
    category: "已结束/下架"
  }
];

export interface PoolItem {
  name: string;
  probability: number;
}

export interface GachaPool {
  id: string;
  name: string;
  type: string;
  date: string;
  server: ServerType;
  description: string;
  highlights: string[];
  items: PoolItem[];
  tips: string;
  tags: PlayerTag[];
}

export const GACHA_POOLS: GachaPool[] = [
  {
    id: "youth-variation",
    name: "青春变奏曲",
    type: "时装返场 + 自选大奖池",
    date: "3月6日 ~ 4月3日 8:00",
    server: "全服",
    description: "青春系列时装返场 + 自选大奖池。大奖方向包括时装·香草回忆、草莓奶霜、葡萄气泡，以及塗装·弧光电磁典藏版、异变核芯·炽热枪膛、异变核芯·冰凌龙息等。",
    highlights: ["时装·香草回忆/草莓奶霜/葡萄气泡", "塗装·弧光电磁典藏版", "异变核芯·炽热枪膛", "异变核芯·冰凌龙息"],
    items: [
      { name: "青春变奏曲自选箱", probability: 1.03 },
      { name: "弧光电磁典藏版", probability: 0.19 },
      { name: "弧光电磁雨战版", probability: 0.26 },
      { name: "弧光电磁雪地版", probability: 0.26 },
      { name: "弧光电磁机枪配方", probability: 1.69 },
      { name: "异变核芯·炽热枪膛", probability: 0.96 },
      { name: "异变核芯·冰凌龙息", probability: 0.96 },
      { name: "彩虹独角兽挂饰礼盒", probability: 0.71 },
      { name: "进化头盔自选箱", probability: 1.12 },
      { name: "磺骨战甲", probability: 0.42 },
      { name: "蔚蓝战甲", probability: 1.61 },
      { name: "深红战甲", probability: 4.28 },
      { name: "青春奏鸣曲高级彩绘板自选箱", probability: 0.86 },
      { name: "青春奏鸣曲彩绘板自选箱", probability: 3.08 },
      { name: "配方残页500", probability: 1.03 },
      { name: "稀有微晶500", probability: 1.03 },
      { name: "1型记忆材料4", probability: 1.57 },
      { name: "稀有微晶80", probability: 1.57 },
      { name: "重构分子50", probability: 6.86 },
      { name: "配方残页20", probability: 6.05 },
      { name: "配方残页10", probability: 12.09 },
      { name: "纳米塑材2 7000", probability: 11.06 },
      { name: "纳米塑材1 15000", probability: 16.12 },
      { name: "技能点8000", probability: 10.08 },
      { name: "新币8000", probability: 15.11 }
    ],
    tips: "适合两类人：一是返场外观收藏党，看重青春系列三套时装；二是想顺手补战力资源的人，因为池内混了核芯、机枪配方、战甲和材料。纯白嫖玩家不建议硬冲。",
    tags: ["外观", "战力"]
  },
  {
    id: "sakura-fox",
    name: "樱灵狐梦",
    type: "限定时装池",
    date: "3月12日 8:00 ~ 3月26日 3:00",
    server: "全服",
    description: "春日主题外观池，风格为古典柔美+未来科幻。可获取完整主题内容包括：时装·樱灵狐梦、再生莲·折樱见春、头饰·心月狐、背包·狐绥绥、背包·梦中樱、头像框&名片框·朝樱衔光、单人动作·捕梦、樱灵狐梦专属彩绘板。获得时装后额外附赠2个高级彩绘板+4个彩绘板。",
    highlights: ["时装·樱灵狐梦", "再生莲·折樱见春", "头饰·心月狐", "背包·狐绥绥/梦中樱", "单人动作·捕梦"],
    items: [
      { name: "樱灵狐梦时装礼包", probability: 0.03 },
      { name: "背包·狐绥绥", probability: 0.14 },
      { name: "头饰·心月狐", probability: 0.34 },
      { name: "梦中樱礼包", probability: 4.09 },
      { name: "能量电池20", probability: 5.11 },
      { name: "配方残页600", probability: 17.04 },
      { name: "稀有微晶300", probability: 11.93 },
      { name: "名片框·朝樱衔光", probability: 27.25 },
      { name: "头像框·朝樱衔光", probability: 34.07 }
    ],
    tips: "纯外观党/拍照党/喜欢樱花赛博风格的人的首选。论实用性不如战力池，但视觉完整度比本期很多内容都更强。注意3月26日就结束。",
    tags: ["外观"]
  },
  {
    id: "cold-blade",
    name: "蓄势寒锋",
    type: "核芯/战斗养成池",
    date: "经典服: 3月20日~4月17日 8:00 | 简单生存专服: 3月20日~4月3日 8:00",
    server: "全服",
    description: "新冷兵器异变核芯「蓄势寒锋」上线。机制：使用冷兵器时提升火力，获得10%概率正面「伤害抵御」；战斗中逐渐充能，触发伤害抵御可额外充能+回护盾；50%能量进入「寒锋」状态切成重刃蓄力高伤斩击，100%能量切成连斩快速连续斩击。5星起命中可触发抵御延长状态，9星每次命中/抵御/格挡叠1%挥砍速度+0.5%移速（最多40层），12星开启寒锋击退变为1秒冰冻。经典服把它和配方、武器外观做成大池；简单生存专服保底方向为「每获得两个极品异变核芯至少包含一个蓄势寒锋」。活动里拿到的武器配方可以分解成数据权杖，再去装备兑换库换本期武器配方和异变核芯。",
    highlights: [
      "冷兵器异变核芯·蓄势寒锋",
      "50%能量: 重刃蓄力高伤斩击",
      "100%能量: 快速连斩+终结斩击",
      "9星: 叠加挥砍速度+移速（最多40层）",
      "12星: 击退→1秒冰冻控制",
      "塗装·蠍尾狙击典藏版",
      "配方·仿生蠍尾狙击枪/破潮弓"
    ],
    items: [
      { name: "塗装·蠍尾狙击典藏版", probability: 0.12 },
      { name: "塗装·破潮弓·血月", probability: 0.12 },
      { name: "蠍尾狙击雪地版", probability: 0.11 },
      { name: "蠍尾狙击雨战版", probability: 0.11 },
      { name: "破潮弓雪地版", probability: 0.11 },
      { name: "破潮弓雨战版", probability: 0.11 },
      { name: "配方·仿生蠍尾狙击枪", probability: 0.70 },
      { name: "配方·破潮弓", probability: 0.70 },
      { name: "萌鸭乐园主题方案", probability: 0.21 },
      { name: "狂鲨号背包", probability: 0.21 },
      { name: "自选极品异变核芯1", probability: 0.90 },
      { name: "自选极品异变核芯2", probability: 0.90 },
      { name: "2型记忆材料4", probability: 0.63 },
      { name: "配方残页600", probability: 0.63 },
      { name: "1型记忆材料5", probability: 2.07 },
      { name: "稀有微晶80", probability: 2.07 },
      { name: "数据权杖10", probability: 3.62 },
      { name: "重构分子30", probability: 9.06 },
      { name: "配方残页20", probability: 9.61 },
      { name: "配方残页10", probability: 19.21 },
      { name: "纳米塑材2 6000", probability: 12.30 },
      { name: "纳米塑材1 15000", probability: 15.37 },
      { name: "技能点8000", probability: 9.61 },
      { name: "新币10000", probability: 11.52 }
    ],
    tips: "武士/冷兵器近战/喜欢冲脸打压制的人的强目标。纯枪械玩家可以放后。核芯机制本身决定了它偏向近战流打法。",
    tags: ["战力", "PVP"]
  },
  {
    id: "chenshi-treasure",
    name: "宸世臻藏",
    type: "高消费返场池",
    date: "3月20日 ~ 4月30日 8:00",
    server: "全服",
    description: "高消费返场池。已确认返场或上新内容：低空滑行背包·铃兰空翼、典藏时装·六时吉祥、幻彩典藏时装·冰渊神典、典藏武器外观·金蟒啸焰、载具·初樱绽放/丹凤飞焰、投影·浮光花丛、典藏武器外观·赤蛇御火、时装·香韵弄樱/冰上恋人。经典服还有蝶影左轮典藏版、无人机塗装·欲火金刚、金龙等返场；简单生存专服另有塗装·极光护卫/青鸾。挂饰·赤焰栖梧进稀世商店。",
    highlights: ["典藏时装·六时吉祥", "幻彩典藏时装·冰渊神典", "低空滑行背包·铃兰空翼", "典藏武器外观·金蟒啸焰", "载具·初樱绽放/丹凤飞焰"],
    items: [
      { name: "宸晶臻石5", probability: 0.04 },
      { name: "地狱火臻藏礼盒", probability: 0.02 },
      { name: "赤龙臻藏礼盒", probability: 0.02 },
      { name: "六时吉祥臻藏礼盒", probability: 0.02 },
      { name: "赤焰风华臻藏礼盒", probability: 0.02 },
      { name: "银骑飞鹰臻藏礼盒", probability: 0.02 },
      { name: "宸晶臻石1", probability: 1.25 },
      { name: "塗装·叶影", probability: 0.18 },
      { name: "塗装·青龙", probability: 0.18 },
      { name: "蝶影左轮雨战版", probability: 0.18 },
      { name: "蝶影左轮雪地版", probability: 0.18 },
      { name: "配方·银甲臂猿", probability: 0.34 },
      { name: "配方·守御灵龙", probability: 0.34 },
      { name: "异变核芯·脉冲闪电", probability: 0.89 },
      { name: "异变核芯·决斗时刻", probability: 0.89 },
      { name: "配方·蝶影左轮手枪", probability: 0.89 },
      { name: "稀世之证8", probability: 4.44 },
      { name: "稀世之证4", probability: 8.88 },
      { name: "配方残页60", probability: 6.81 },
      { name: "配方残页40", probability: 10.21 },
      { name: "配方残页20", probability: 20.42 },
      { name: "纳米塑材自选箱", probability: 10.21 },
      { name: "基础资源大自选箱", probability: 5.23 },
      { name: "基础资源自选箱", probability: 9.07 },
      { name: "技能点6000", probability: 9.07 },
      { name: "新币8000", probability: 10.20 }
    ],
    tips: "偏高消费返场池方向，不是白嫖路线。更像是「我就要经典大件返场」的池。适合长期收藏党。",
    tags: ["外观"]
  },
  {
    id: "spring-furniture-qingliu",
    name: "春苑惠选 · 青柳纸鸢",
    type: "家具池",
    date: "3月20日 ~ 6月12日 8:00",
    server: "全服",
    description: "春季主题家具池之一。江南水乡风格，含氤氲群山灯、燕子风筝、入梦乌篷、江南拱桥小亭、青青柳树等完整主题件。",
    highlights: ["氤氲群山灯", "燕子风筝", "入梦乌篷", "江南拱桥", "江南小亭", "青青柳树"],
    items: [
      { name: "氤氲群山灯", probability: 0.24 },
      { name: "燕子风筝", probability: 0.15 },
      { name: "入梦乌篷", probability: 0.46 },
      { name: "江南拱桥", probability: 0.91 },
      { name: "江南小亭", probability: 0.61 },
      { name: "青青柳树", probability: 0.30 },
      { name: "春燕纷飞灯", probability: 2.43 },
      { name: "金条50000", probability: 10.65 },
      { name: "春草池塘·圆", probability: 6.77 },
      { name: "春草池塘·方", probability: 6.77 },
      { name: "踏青水牛", probability: 6.35 },
      { name: "河边蒲苇", probability: 7.62 },
      { name: "青青河岸", probability: 7.62 },
      { name: "乐居币1", probability: 23.71 },
      { name: "乐居币2", probability: 10.16 },
      { name: "配方残页60", probability: 15.25 }
    ],
    tips: "庄园党/家具党专属。江南水乡主题搭配春季氛围，做庄园展示很合适。",
    tags: ["庄园"]
  },
  {
    id: "spring-furniture-sakura",
    name: "春苑惠选 · 春日暖樱",
    type: "家具池",
    date: "3月20日 ~ 6月12日 8:00",
    server: "全服",
    description: "春季主题家具池之一。樱花野餐主题，含野餐吉他·樱、小熊樱樱、初恋樱花树、粉樱野餐垫、樱花热气球、樱花帐篷等。",
    highlights: ["野餐吉他·樱", "小熊樱樱", "初恋樱花树", "樱花热气球", "樱花帐篷", "樱花双开门冰箱"],
    items: [
      { name: "野餐吉他·樱", probability: 0.09 },
      { name: "小熊樱樱", probability: 0.15 },
      { name: "初恋樱花树", probability: 0.15 },
      { name: "粉樱野餐垫", probability: 0.30 },
      { name: "樱花热气球", probability: 0.30 },
      { name: "野餐烤炉", probability: 0.60 },
      { name: "樱花帐篷", probability: 0.60 },
      { name: "樱花双开门冰箱", probability: 0.60 },
      { name: "樱花配方箱", probability: 0.91 },
      { name: "金条50000", probability: 12.12 },
      { name: "樱花坐垫", probability: 6.07 },
      { name: "樱花壁饰", probability: 6.94 },
      { name: "樱花地毯", probability: 5.21 },
      { name: "野餐篮子", probability: 6.94 },
      { name: "樱花建筑箱", probability: 8.68 },
      { name: "乐居币1", probability: 24.30 },
      { name: "乐居币2", probability: 10.41 },
      { name: "配方残页60", probability: 15.63 }
    ],
    tips: "樱花野餐风格，适合春季庄园布置。拍照党首选主题之一。",
    tags: ["庄园"]
  },
  {
    id: "spring-furniture-oz",
    name: "春苑惠选 · 绿野仙踪",
    type: "家具池（互动型）",
    date: "3月20日 ~ 6月12日 8:00",
    server: "全服",
    description: "本期互动性最强的家具池。仙踪奇境可以让角色变小；仙踪落地钟可以调庄园昼夜；仙踪奇幻茶杯带泡泡浴/沉浸式交互；仙踪栖木枝可控制花灯明灭。另有树洞床、书籍、躺椅、矮几、花灯、书架等完整主题件。同批商城上庆典映墨灯、落英燕舞灯。",
    highlights: [
      "仙踪奇境（角色变小魔法）",
      "仙踪落地钟（调节庄园昼夜）",
      "仙踪奇幻茶杯（泡泡浴交互）",
      "仙踪栖木枝（控制花灯明灭）",
      "仙踪树洞床/书架/花灯/躺椅"
    ],
    items: [
      { name: "仙踪奇境", probability: 0.14 },
      { name: "仙踪落地钟", probability: 0.23 },
      { name: "仙踪奇幻茶杯", probability: 0.29 },
      { name: "仙踪栖木枝", probability: 0.87 },
      { name: "仙踪树洞床", probability: 0.58 },
      { name: "仙踪书架", probability: 1.74 },
      { name: "金条50000", probability: 11.60 },
      { name: "仙踪花灯", probability: 7.35 },
      { name: "仙踪躺椅", probability: 7.35 },
      { name: "仙踪矮几", probability: 8.27 },
      { name: "仙踪书籍", probability: 8.27 },
      { name: "乐居币1", probability: 25.73 },
      { name: "乐居币2", probability: 11.03 },
      { name: "配方残页60", probability: 16.55 }
    ],
    tips: "建筑党/庄园党/拍照党高优先级。绿野仙踪互动性最强，是本期最值得关注的家具池。战力党可以跳过。",
    tags: ["庄园"]
  },
  {
    id: "wasteland-busy",
    name: "废土很忙",
    type: "时装直购",
    date: "3月20日 ~ 4月17日 8:00",
    server: "全服",
    description: "新时装·废土很忙，风格为西部牛仔+废土元素（荒野镖客/双持左轮/宽檐牛仔帽）。购买可得专属动作，有同主题头饰·明日镖客和彩绘板优惠。",
    highlights: ["时装·废土很忙", "专属动作", "头饰·明日镖客", "彩绘板优惠"],
    items: [],
    tips: "标准的外观消费项，不是福利项也不是战力项。适合喜欢西部废土风格的玩家。",
    tags: ["外观"]
  },
  {
    id: "qingling-discount",
    name: "清铃满减补贴",
    type: "直购满减活动",
    date: "3月26日 8:00 ~ 4月9日 3:00",
    server: "全服",
    description: "直购活动，单笔结算最高可减7500信用点。已确认内容包括：时装·清铃漱玉、武器外观·铃兰之约、头饰·玉铃凝香、家具·滑入铃谷（独享板）。",
    highlights: ["时装·清铃漱玉", "武器外观·铃兰之约", "头饰·玉铃凝香", "家具·滑入铃谷", "最高减7500信用点"],
    items: [],
    tips: "铃兰轻奢风格的直购活动，有满减优惠。外观党可以关注。",
    tags: ["外观"]
  }
];

export interface SystemUpdate {
  id: string;
  name: string;
  date: string;
  server: ServerType;
  description: string;
  details: string[];
}

export const SYSTEM_UPDATES: SystemUpdate[] = [
  {
    id: "spring-farm",
    name: "春季农场上新",
    date: "3月20日 ~ 5月15日",
    server: "全服",
    description: "新鲜花牵牛花可在晴空麦田、银翼基地采集种子，回庄园/边境农场种植。桃花款小动物限时进化。边境农场还开放了邀请好友共耕功能。",
    details: [
      "新鲜花「牵牛花」可在晴空麦田、银翼基地采集到种子",
      "矮脚鸡、嘎嘎鸭、咕咕鹅有概率孵化成桃花款小动物",
      "桃花款小动物掉落桃花羽毛和桃花蛋（用于桃羽收集大作战）",
      "边境农场开放邀请好友共耕功能"
    ]
  },
  {
    id: "dye-share",
    name: "染色功能优化",
    date: "本版本更新",
    server: "全服",
    description: "染色分享码上线，优化了未保存覆盖提示、染色板交互逻辑、预览入口，以及手持武器进入染色界面时的显示问题。",
    details: [
      "染色分享码功能上线",
      "优化未保存覆盖提示",
      "优化染色板交互逻辑和预览入口",
      "修复手持武器进入染色界面的显示问题"
    ]
  },
  {
    id: "farstar-brawl",
    name: "远星乱斗重启",
    date: "本版本更新",
    server: "全服",
    description: "经典服每日18:00-22:00，战斗等级70+，最多4人队，每场最多8支队伍。简单生存专服生存等级60+，按60-69/70-78/79级分段，每场最多10支队伍。玩法核心是轮次淘汰：每轮结束前要收集足够红钻（来源：晶簇、悬赏任务、击败对手）。",
    details: [
      "经典服: 每日18:00-22:00，战斗等级70+，最多4人队，每场8支队伍",
      "简单生存专服: 生存等级60+，按等级分段，每场最多10支队伍",
      "核心玩法: 轮次淘汰，每轮结束前收集足够红钻",
      "红钻来源: 晶簇、悬赏任务、击败对手"
    ]
  },
  {
    id: "ocean-lockdown",
    name: "海洋封锁预告",
    date: "4月17日更新后执行",
    server: "全服",
    description: "官方预告4月17日更新后海洋玩法暂时封锁。海洋探索、骑士委托会被移除，船只回收并返还部分金条/补偿，但航海硬币不会回收。",
    details: [
      "4月17日更新后海洋玩法暂时封锁",
      "海洋探索、骑士委托将被移除",
      "船只回收，返还部分金条/补偿",
      "航海硬币不会回收——赶紧花掉",
      "老玩家注意：赶紧把还能做的海洋内容做掉"
    ]
  },
  {
    id: "core-preorder",
    name: "核芯预购 & 南茜市防连控",
    date: "本版本更新",
    server: "全服",
    description: "新增极品异变核芯预购功能。南茜市/约战-南茜市中新增5秒内不重复吃击倒、击飞的机制，缓解连续受控体验。",
    details: [
      "新增极品异变核芯预购功能",
      "南茜市新增5秒内不重复吃击倒/击飞机制",
      "目的: 缓解PVP连续受控体验"
    ]
  },
  {
    id: "duo-training",
    name: "双人集训与商队集市",
    date: "双人集训: 3月20日~4月2日 | 商队集市: 3月20日~4月3日 8:00",
    server: "简单生存专服",
    description: "简单生存专服专属内容。双人集训可邀请好友完成指定任务拿甜甜蜂蜜和额外支援奖励。商队集市可上架春苑惠选家具，并用集训代币换配方残页、强化血清等。",
    details: [
      "双人集训: 邀请好友完成指定任务",
      "奖励: 甜甜蜂蜜 + 额外支援奖励",
      "商队集市: 上架春苑惠选家具",
      "集训代币可换配方残页、强化血清等"
    ]
  },
  {
    id: "tianju-shop",
    name: "天居商店 / 霓虹车港 / 结构商店",
    date: "天居商店: 3月20日~5月30日",
    server: "全服",
    description: "天居商店通过消费家具活动和商城拿天居积分，提升等级可免费领家具。霓虹车港是科技感车库外观，可全息投影车库等级和车辆数，换上后解锁2个车库位+1个停机坪（需天居商店4级）。结构商店新上玻璃小屋、龙凤千秋主题结构。",
    details: [
      "天居商店: 消费家具活动/商城 → 天居积分 → 提升等级领家具",
      "霓虹车港: 科技感车库外观，解锁2车库位+1停机坪（需4级）",
      "结构商店新上: 玻璃小屋、龙凤千秋主题结构"
    ]
  },
  {
    id: "qingsong-detail",
    name: "青松季减负项目汇总",
    date: "本版本持续优化",
    server: "全服",
    description: "当前已落地的减负项目汇总，覆盖庄园、养成、日常等多个维度。",
    details: [
      "专属配件箱: 自动开箱 / 最高阶开箱",
      "批量分解功能",
      "经验转移优化",
      "染色分享码上线",
      "边境农场邀请共耕",
      "极品异变核芯预购",
      "南茜市防连控（5秒内不重复击倒/击飞）",
      "职业天赋优化",
      "专属配件一键开启、批量分解、经验转移更快捷"
    ]
  }
];

export interface PlayerGuide {
  id: string;
  title: string;
  subtitle: string;
  color: string;
  priorities: { name: string; reason: string }[];
  summary: string;
}

export const PLAYER_GUIDES: PlayerGuide[] = [
  {
    id: "f2p",
    title: "白嫖 / 平民玩家",
    subtitle: "不花钱也能高效发展",
    color: "text-green-400",
    priorities: [
      { name: "寻觅花林", reason: "零成本拍照打卡拿动态头像框，最不该漏掉" },
      { name: "樱花绽放", reason: "种樱花树稳定产出花瓣换家具，早种早收" },
      { name: "春季农场/桃羽链条", reason: "农场孵化桃花小动物，长线兑换家具" },
      { name: "凛雪危局", reason: "限时回归搜物资玩法，有额外收益" },
      { name: "4月1日登录/手稿", reason: "当天登录就有，别忘了" },
      { name: "青松季减负", reason: "了解系统优化，省下来的时间就是资源" }
    ],
    summary: "春日福利和减负内容更可能直接提高资源获取效率，纯外观池最后看。优先做登录/预约/日常/采集打怪钓鱼等能顺手完成的项目，再补需要单独跑图的内容。"
  },
  {
    id: "combat",
    title: "战力 / PVP 玩家",
    subtitle: "战斗力提升优先",
    color: "text-red-400",
    priorities: [
      { name: "蓄势寒锋（核芯）", reason: "武士/冷兵器近战的强目标，机制直接影响近战打法" },
      { name: "特战巅峰赛", reason: "竞技赛事，影响2026正式比赛规则，PVP必参与" },
      { name: "青春变奏曲", reason: "混了核芯、机枪配方、战甲和材料，顺便补战力" },
      { name: "远星乱斗", reason: "每日18:00-22:00轮次淘汰玩法，练手+拿奖励" },
      { name: "南茜市防连控", reason: "5秒内不重复吃击倒/击飞，PVP体验优化" }
    ],
    summary: "蓄势寒锋是本期战力核心内容，特战巅峰赛是赛事入口。对纯枪械玩家来说，蓄势寒锋不是第一优先。"
  },
  {
    id: "manor",
    title: "庄园 / 建筑 / 拍照党",
    subtitle: "庄园布置与收藏",
    color: "text-purple-400",
    priorities: [
      { name: "春苑惠选·绿野仙踪", reason: "互动性最强的家具池——角色变小、调昼夜、泡泡浴" },
      { name: "桃羽收集大作战", reason: "农场产出换主题家具，养成党必做" },
      { name: "春苑惠选·青柳纸鸢/春日暖樱", reason: "江南水乡和樱花野餐两大主题家具" },
      { name: "天居商店", reason: "消费家具活动拿天居积分，提升等级领免费家具" },
      { name: "霓虹车港", reason: "科技感车库，解锁额外车库位和停机坪" },
      { name: "樱花季春日氛围内容", reason: "这波视觉主题非常统一，做展示很受欢迎" }
    ],
    summary: "绿野仙踪是本期最值得单独关注的家具池，不仅有概率还有交互功能卖点。这波春季视觉主题非常统一，适合做整套庄园展示。"
  },
  {
    id: "fashion",
    title: "外观 / 收藏党",
    subtitle: "时装与限定外观收集",
    color: "text-pink-400",
    priorities: [
      { name: "樱灵狐梦", reason: "春日赛博古风，视觉完整度最强，3月26日截止" },
      { name: "废土很忙", reason: "西部废土风格，含专属动作" },
      { name: "清铃满减补贴（3/26开）", reason: "铃兰轻奢风，直购满减最高减7500信用点" },
      { name: "宸世臻藏", reason: "大返场藏品池，典藏大件返场" },
      { name: "青春变奏曲", reason: "青春系列三套时装返场" }
    ],
    summary: "如果只买一类：樱灵狐梦=春日赛博古风、废土很忙=西部废土、清铃=铃兰轻奢、宸世臻藏=大返场藏品池。风格完全不同，按个人审美选。"
  },
  {
    id: "returning",
    title: "回坑玩家",
    subtitle: "回来还值不值得玩",
    color: "text-cyan-400",
    priorities: [
      { name: "青松季减负", reason: "最该先看——现在回坑没那么肝了，系统全面减负" },
      { name: "春日樱花季福利", reason: "白嫖向活动多，低门槛稳定拿资源" },
      { name: "新服「百花漫野」", reason: "新服预约有限时学霸榴弹炮加码奖励" },
      { name: "海洋封锁预告", reason: "4月17日后海洋玩法封锁，赶紧做" },
      { name: "核芯预购功能", reason: "新增预购系统，养成路线更清晰" }
    ],
    summary: "回坑最关心的是「现在肝不肝、追不追得上」。答案是：青松季系统性减负后，比以前好很多。春日福利和新服信息是回坑玩家最直接的资源来源。"
  }
];

export const MARCH_TIMELINE = [
  { date: "3月4日", content: "经典服/专服更新：春日福利解锁暗号、家具自选箱、青春变奏曲、樱灵狐梦上线、凛雪危局回归、拟态能力赛季更新、职业天赋优化、1元月卡回归、多种登录领奖（性别转换卡、专研材料自选箱等）" },
  { date: "3月6日", content: "青春变奏曲、凛雪危局正式开放；返利小队开启" },
  { date: "3月12日", content: "樱灵狐梦上线；人偶契约下架" },
  { date: "3月18-19日", content: "经典服/专服春日大更新：废土春日主活动上线，含樱花绽放、寻觅花林、桃羽收集大作战" },
  { date: "3月20日", content: "蓄势寒锋、宸世臻藏、春苑惠选、废土很忙上线；特战巅峰赛开测；远星乱斗重启；新服百花漫野预约" },
  { date: "3月21日", content: "冷兵器异变核芯「蓄势寒锋」上线" },
  { date: "3月22日", content: "特战巅峰赛测试最后一天" },
  { date: "3月26日", content: "樱灵狐梦结束；清铃满减补贴开启" },
  { date: "4月1日", content: "限定登录福利 + 神秘手稿掉落" },
  { date: "4月3日", content: "樱花绽放/寻觅花林/凛雪危局/青春变奏曲结束" },
  { date: "4月17日", content: "海洋玩法封锁；蓄势寒锋(经典服)结束；废土很忙结束" }
];

export const getStatusText = (status: ActivityStatus): string => {
  switch (status) {
    case 'active': return '进行中';
    case 'upcoming': return '即将开始';
    case 'ending-soon': return '即将结束';
    case 'ended': return '已结束';
  }
};

export const getStatusColor = (status: ActivityStatus): string => {
  switch (status) {
    case 'active': return 'bg-green-500/20 text-green-400 border-green-500/30';
    case 'upcoming': return 'bg-blue-500/20 text-blue-400 border-blue-500/30';
    case 'ending-soon': return 'bg-amber-500/20 text-amber-400 border-amber-500/30';
    case 'ended': return 'bg-gray-500/20 text-gray-400 border-gray-500/30';
  }
};

export const getPriorityColor = (priority: string): string => {
  switch (priority) {
    case '极高': return 'bg-red-500/20 text-red-400 border-red-500/30';
    case '高': return 'bg-amber-500/20 text-amber-400 border-amber-500/30';
    case '中': return 'bg-blue-500/20 text-blue-400 border-blue-500/30';
    case '低': return 'bg-gray-500/20 text-gray-400 border-gray-500/30';
    default: return 'bg-gray-500/20 text-gray-400 border-gray-500/30';
  }
};
