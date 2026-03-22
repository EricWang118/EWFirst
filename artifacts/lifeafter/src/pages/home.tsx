import { Link } from "wouter";
import { motion, type Variants } from "framer-motion";
import { ArrowRight, Flame, Swords, Calendar, TrendingUp, ShieldAlert, Clock } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { GameCard } from "@/components/ui/GameCard";
import { GAME_VERSION, ACTIVITIES, MARCH_TIMELINE } from "@/lib/data";

const SECTIONS = [
  {
    id: "events",
    title: "当前活动",
    desc: "春日樱花季、特战巅峰赛、青松季减负等核心活动一览",
    icon: Calendar,
    color: "from-green-500/20 to-green-600/5",
    iconColor: "text-green-400",
    href: "/events"
  },
  {
    id: "pools",
    title: "奖池详情",
    desc: "蓄势寒锋、青春变奏曲、樱灵狐梦等全概率表公示",
    icon: Flame,
    color: "from-amber-500/20 to-amber-600/5",
    iconColor: "text-amber-400",
    href: "/pools/cold-blade"
  },
  {
    id: "guides",
    title: "玩家攻略",
    desc: "白嫖/战力/庄园/外观/回坑——不同玩家的最优先级",
    icon: TrendingUp,
    color: "from-purple-500/20 to-purple-600/5",
    iconColor: "text-purple-400",
    href: "/guides/f2p"
  },
  {
    id: "updates",
    title: "版本动态",
    desc: "青松季减负、远星乱斗、海洋封锁预告等系统更新",
    icon: Swords,
    color: "from-blue-500/20 to-blue-600/5",
    iconColor: "text-blue-400",
    href: "/updates"
  }
];

const containerVariants: Variants = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.1 }
  }
};

const itemVariants: Variants = {
  hidden: { opacity: 0, y: 30 },
  show: { opacity: 1, y: 0, transition: { type: "spring" as const, stiffness: 300, damping: 24 } }
};

const hotActivities = ACTIVITIES.filter(a => a.status !== 'ended' && a.priority === '极高').slice(0, 4);

export default function Home() {
  return (
    <PageWrapper className="pt-0">
      <section className="relative min-h-[70vh] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 z-0">
          <img 
            src={`${import.meta.env.BASE_URL}images/hero-bg.png`} 
            alt="Hero Background" 
            className="w-full h-full object-cover opacity-60"
          />
          <div className="absolute inset-0 bg-gradient-to-b from-background/40 via-background/80 to-background" />
          <div className="absolute inset-0 bg-gradient-to-r from-background/80 via-transparent to-background/80" />
        </div>

        <div className="container mx-auto px-4 relative z-10 text-center mt-20">
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
          >
            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full glass-panel mb-6 border-primary/30">
              <ShieldAlert className="w-4 h-4 text-primary animate-pulse" />
              <span className="text-sm font-medium text-primary-foreground/90">{GAME_VERSION}</span>
            </div>
            
            <h1 className="font-display text-6xl md:text-8xl lg:text-9xl mb-6 text-transparent bg-clip-text bg-gradient-to-b from-white to-white/60 drop-shadow-2xl">
              明日之后<span className="text-primary">攻略站</span>
            </h1>
            
            <p className="text-lg md:text-2xl text-muted-foreground max-w-2xl mx-auto mb-10 leading-relaxed font-light">
              实时活动攻略 · 完整概率公示 · 分类玩家指南
            </p>
          </motion.div>
        </div>
      </section>

      <section className="container mx-auto px-4 -mt-20 relative z-20">
        <motion.div 
          variants={containerVariants}
          initial="hidden"
          animate="show"
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6"
        >
          {SECTIONS.map((section) => {
            const Icon = section.icon;
            return (
              <motion.div key={section.id} variants={itemVariants}>
                <Link href={section.href}>
                  <div className="glass-card h-full p-8 group cursor-pointer hover:-translate-y-2 transition-transform duration-300 relative">
                    <div className={`w-16 h-16 rounded-2xl mb-6 flex items-center justify-center bg-gradient-to-br ${section.color} border border-white/10 group-hover:scale-110 transition-transform duration-500`}>
                      <Icon className={`w-8 h-8 ${section.iconColor}`} />
                    </div>
                    <h3 className="text-2xl font-bold mb-3 text-foreground group-hover:text-primary transition-colors">{section.title}</h3>
                    <p className="text-muted-foreground mb-8 line-clamp-2">{section.desc}</p>
                    <div className="absolute bottom-6 left-8 flex items-center text-sm font-medium text-white/50 group-hover:text-primary transition-colors">
                      进入板块 <ArrowRight className="w-4 h-4 ml-1 opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0 transition-all" />
                    </div>
                  </div>
                </Link>
              </motion.div>
            );
          })}
        </motion.div>
      </section>

      <section className="container mx-auto px-4 mt-16">
        <h2 className="text-3xl font-bold text-primary mb-6 font-display text-glow">当前必做</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {hotActivities.map((act, idx) => (
            <motion.div
              key={act.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 + idx * 0.1 }}
            >
              <Link href={`/events/${act.id}`}>
                <GameCard glowOnHover className="p-6 h-full">
                  <div className="flex items-center gap-3 mb-3">
                    <h3 className="text-xl font-bold text-foreground">{act.name}</h3>
                    <span className={`px-2 py-0.5 rounded-full text-xs font-bold border ${act.status === 'ending-soon' ? 'bg-amber-500/20 text-amber-400 border-amber-500/30' : 'bg-green-500/20 text-green-400 border-green-500/30'}`}>
                      {act.status === 'ending-soon' ? '即将结束' : '进行中'}
                    </span>
                    <span className="px-2 py-0.5 rounded text-xs font-bold bg-red-500/20 text-red-400 border border-red-500/30">
                      {act.priority}优先
                    </span>
                  </div>
                  <p className="text-muted-foreground text-sm mb-2">{act.date}</p>
                  <p className="text-foreground/70 text-sm line-clamp-2">{act.tips}</p>
                </GameCard>
              </Link>
            </motion.div>
          ))}
        </div>
      </section>

      <section className="container mx-auto px-4 mt-16 pb-16">
        <h2 className="text-3xl font-bold text-primary mb-6 font-display text-glow">3月活动时间线</h2>
        <GameCard className="p-6 md:p-8">
          <div className="space-y-0">
            {MARCH_TIMELINE.map((item, idx) => (
              <motion.div
                key={idx}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.1 * idx }}
                className="flex gap-4 pb-6 last:pb-0 relative"
              >
                <div className="flex flex-col items-center">
                  <div className="w-3 h-3 rounded-full bg-primary shrink-0 mt-1.5" />
                  {idx < MARCH_TIMELINE.length - 1 && <div className="w-0.5 flex-1 bg-white/10 mt-1" />}
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-3 mb-1">
                    <Clock className="w-4 h-4 text-primary shrink-0" />
                    <span className="font-mono font-bold text-primary text-sm">{item.date}</span>
                  </div>
                  <p className="text-foreground/80 text-sm leading-relaxed">{item.content}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </GameCard>
      </section>
    </PageWrapper>
  );
}
