import { useState } from "react";
import { useParams, Link, useLocation } from "wouter";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronRight, Star, AlertTriangle } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { GameCard } from "@/components/ui/GameCard";
import { GACHA_POOLS } from "@/lib/data";
import { clsx } from "clsx";

export default function Pools() {
  const params = useParams();
  const [_, setLocation] = useLocation();
  const activePoolId = params.id && GACHA_POOLS.some(p => p.id === params.id) ? params.id : GACHA_POOLS[0].id;
  const activePool = GACHA_POOLS.find(p => p.id === activePoolId)!;
  const [showAll, setShowAll] = useState(false);

  const displayItems = showAll ? activePool.items : activePool.items.slice(0, 15);
  const hasMore = activePool.items.length > 15;

  return (
    <PageWrapper>
      <div className="container mx-auto px-4">
        <div className="mb-10 text-center">
          <h1 className="text-4xl md:text-5xl font-display text-primary mb-4 text-glow">奖池详情</h1>
          <p className="text-muted-foreground text-lg">完整概率公示 · 实战攻略建议</p>
        </div>

        <div className="flex flex-col lg:flex-row gap-8">
          <div className="w-full lg:w-64 shrink-0">
            <div className="flex flex-row lg:flex-col overflow-x-auto lg:overflow-visible gap-2 pb-4 lg:pb-0 hide-scrollbar sticky top-28">
              {GACHA_POOLS.map((pool) => {
                const isActive = activePoolId === pool.id;
                return (
                  <Link key={pool.id} href={`/pools/${pool.id}`}>
                    <div className={clsx(
                      "flex items-center gap-3 px-4 py-3 rounded-xl cursor-pointer transition-all whitespace-nowrap lg:whitespace-normal group relative",
                      isActive ? "bg-primary text-primary-foreground font-bold shadow-lg shadow-primary/20" : "hover:bg-white/5 text-muted-foreground hover:text-foreground"
                    )}>
                      <span className="text-sm">{pool.name}</span>
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
                key={activePoolId}
                initial={{ opacity: 0, x: 20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: -20 }}
                transition={{ duration: 0.3 }}
                className="space-y-6"
              >
                <GameCard className="p-6 md:p-8">
                  <div className="mb-6">
                    <span className="text-xs font-bold text-accent uppercase tracking-wider mb-1 block">{activePool.type}</span>
                    <h2 className="text-3xl font-bold text-foreground mb-2">{activePool.name}</h2>
                    <p className="text-sm text-muted-foreground font-mono mb-4">{activePool.date}</p>
                    <span className="px-2 py-0.5 rounded text-xs bg-white/5 text-muted-foreground border border-white/10">{activePool.server}</span>
                  </div>

                  <p className="text-foreground/80 leading-relaxed mb-6">{activePool.description}</p>

                  {activePool.highlights.length > 0 && (
                    <div className="mb-6">
                      <h3 className="text-lg font-bold text-primary mb-3 flex items-center gap-2">
                        <Star className="w-4 h-4" /> 核心亮点
                      </h3>
                      <div className="flex flex-wrap gap-2">
                        {activePool.highlights.map((h, i) => (
                          <span key={i} className="px-3 py-1.5 rounded-lg text-sm bg-primary/10 text-primary border border-primary/20 font-medium">
                            {h}
                          </span>
                        ))}
                      </div>
                    </div>
                  )}
                </GameCard>

                {activePool.items.length > 0 && (
                  <GameCard className="p-6 md:p-8">
                    <h3 className="text-xl font-bold text-foreground mb-6 border-b border-border pb-3">
                      概率公示（完整表）
                    </h3>
                    <div className="overflow-x-auto">
                      <table className="w-full text-left border-collapse">
                        <thead>
                          <tr className="border-b border-white/10 text-muted-foreground text-sm">
                            <th className="pb-3 font-medium px-3">道具名称</th>
                            <th className="pb-3 font-medium px-3 text-right w-28">概率</th>
                            <th className="pb-3 font-medium px-3 w-48">概率条</th>
                          </tr>
                        </thead>
                        <tbody>
                          {displayItems.map((item, i) => {
                            const isRare = item.probability < 1;
                            const barWidth = Math.min(item.probability * 3, 100);
                            return (
                              <tr key={i} className="border-b border-white/5 hover:bg-white/5 transition-colors">
                                <td className={clsx("py-3 px-3 font-medium", isRare ? "text-amber-400" : "text-foreground")}>
                                  {item.name}
                                </td>
                                <td className="py-3 px-3 text-right font-mono text-sm">
                                  <span className={isRare ? "text-amber-400 font-bold" : "text-muted-foreground"}>
                                    {item.probability}%
                                  </span>
                                </td>
                                <td className="py-3 px-3">
                                  <div className="h-2 w-full bg-background rounded-full overflow-hidden border border-white/5">
                                    <motion.div
                                      initial={{ width: 0 }}
                                      animate={{ width: `${barWidth}%` }}
                                      transition={{ duration: 0.8, delay: i * 0.02 }}
                                      className={clsx(
                                        "h-full rounded-full",
                                        isRare ? "bg-amber-500 shadow-[0_0_6px_rgba(245,158,11,0.6)]" : "bg-blue-400/60"
                                      )}
                                    />
                                  </div>
                                </td>
                              </tr>
                            );
                          })}
                        </tbody>
                      </table>
                    </div>
                    {hasMore && !showAll && (
                      <button
                        onClick={() => setShowAll(true)}
                        className="mt-4 w-full py-3 rounded-xl bg-white/5 text-muted-foreground hover:text-foreground hover:bg-white/10 transition-colors text-sm font-medium border border-white/10"
                      >
                        展开全部 {activePool.items.length} 项
                      </button>
                    )}
                    <div className="mt-4 text-xs text-muted-foreground text-center bg-black/20 p-3 rounded-lg">
                      * 概率数据来自官方公开公示信息。
                    </div>
                  </GameCard>
                )}

                {activePool.items.length === 0 && (
                  <GameCard className="p-6 md:p-8">
                    <div className="text-center py-8 text-muted-foreground">
                      <AlertTriangle className="w-10 h-10 mx-auto mb-3 opacity-30" />
                      <p>该内容为直购项，无概率抽取机制。</p>
                    </div>
                  </GameCard>
                )}

                <GameCard className="p-6 md:p-8 border-t-4 border-t-amber-500">
                  <h3 className="text-xl font-bold text-amber-400 mb-3">攻略建议</h3>
                  <p className="text-foreground/80 leading-relaxed">{activePool.tips}</p>
                  {activePool.tags.length > 0 && (
                    <div className="flex flex-wrap gap-2 mt-4">
                      {activePool.tags.map(tag => (
                        <span key={tag} className="px-3 py-1 rounded-full text-xs bg-primary/10 text-primary border border-primary/20 font-medium">
                          推荐: {tag}
                        </span>
                      ))}
                    </div>
                  )}
                </GameCard>
              </motion.div>
            </AnimatePresence>
          </div>
        </div>
      </div>
    </PageWrapper>
  );
}
