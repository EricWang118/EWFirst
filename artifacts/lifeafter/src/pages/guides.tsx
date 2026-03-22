import { useParams, Link, useLocation } from "wouter";
import { motion, AnimatePresence } from "framer-motion";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { GameCard } from "@/components/ui/GameCard";
import { PLAYER_GUIDES } from "@/lib/data";
import { ChevronRight, Star } from "lucide-react";
import { clsx } from "clsx";

export default function Guides() {
  const params = useParams();
  const [_, setLocation] = useLocation();
  const activeTab = params.type && PLAYER_GUIDES.some(g => g.id === params.type) ? params.type : "f2p";

  if (params.type && !PLAYER_GUIDES.some(g => g.id === params.type)) {
    setLocation("/guides/f2p");
    return null;
  }

  const activeGuide = PLAYER_GUIDES.find(g => g.id === activeTab)!;

  return (
    <PageWrapper>
      <div className="container mx-auto px-4">
        <div className="mb-10">
          <h1 className="text-4xl md:text-5xl font-display text-primary mb-4 text-glow">玩家攻略</h1>
          <p className="text-muted-foreground text-lg">根据你的玩法风格，找到当前版本的最优先级。</p>
        </div>

        <div className="flex flex-col lg:flex-row gap-8">
          <div className="w-full lg:w-64 shrink-0">
            <div className="flex flex-row lg:flex-col overflow-x-auto lg:overflow-visible gap-2 pb-4 lg:pb-0 hide-scrollbar sticky top-28">
              {PLAYER_GUIDES.map((guide) => {
                const isActive = activeTab === guide.id;
                return (
                  <Link key={guide.id} href={`/guides/${guide.id}`}>
                    <div className={clsx(
                      "flex items-center gap-3 px-5 py-4 rounded-xl cursor-pointer transition-all whitespace-nowrap lg:whitespace-normal group relative",
                      isActive ? "bg-primary text-primary-foreground font-bold shadow-lg shadow-primary/20" : "hover:bg-white/5 text-muted-foreground hover:text-foreground"
                    )}>
                      <span>{guide.title}</span>
                      {isActive && <ChevronRight className="w-4 h-4 ml-auto hidden lg:block" />}
                    </div>
                  </Link>
                );
              })}
            </div>
          </div>

          <div className="flex-1 min-w-0">
            <AnimatePresence mode="wait">
              <motion.div
                key={activeTab}
                initial={{ opacity: 0, x: 20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: -20 }}
                transition={{ duration: 0.3 }}
              >
                <GameCard className="p-6 md:p-10">
                  <div className="mb-8 pb-6 border-b border-border">
                    <h2 className={`text-3xl font-bold mb-2 ${activeGuide.color}`}>{activeGuide.title}</h2>
                    <p className="text-muted-foreground text-lg">{activeGuide.subtitle}</p>
                  </div>

                  <h3 className="text-xl font-bold text-primary mb-6 flex items-center gap-2">
                    <Star className="w-5 h-5" /> 当前版本优先级排序
                  </h3>

                  <div className="space-y-4 mb-8">
                    {activeGuide.priorities.map((item, idx) => (
                      <motion.div
                        key={idx}
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: idx * 0.05 }}
                        className="bg-background/50 p-5 rounded-xl border border-white/5 flex gap-4 items-start"
                      >
                        <div className={`w-10 h-10 rounded-full flex items-center justify-center font-bold text-lg shrink-0 ${idx === 0 ? 'bg-amber-500/20 text-amber-400' : idx < 3 ? 'bg-primary/20 text-primary' : 'bg-white/10 text-muted-foreground'}`}>
                          {idx + 1}
                        </div>
                        <div>
                          <h4 className="font-bold text-foreground mb-1 text-lg">{item.name}</h4>
                          <p className="text-muted-foreground text-sm leading-relaxed">{item.reason}</p>
                        </div>
                      </motion.div>
                    ))}
                  </div>

                  <div className="bg-primary/10 p-6 rounded-xl border border-primary/20">
                    <h4 className="font-bold text-primary mb-3 text-lg">总结</h4>
                    <p className="text-foreground/80 leading-relaxed">{activeGuide.summary}</p>
                  </div>
                </GameCard>
              </motion.div>
            </AnimatePresence>
          </div>
        </div>
      </div>
    </PageWrapper>
  );
}
