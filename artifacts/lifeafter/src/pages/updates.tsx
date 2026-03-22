import { motion } from "framer-motion";
import { Settings, AlertTriangle, Wrench, ArrowRight } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { GameCard } from "@/components/ui/GameCard";
import { SYSTEM_UPDATES } from "@/lib/data";

export default function Updates() {
  return (
    <PageWrapper>
      <div className="container mx-auto px-4 max-w-5xl">
        <div className="mb-10 text-center">
          <h1 className="text-4xl md:text-5xl font-display text-primary mb-4 text-glow">版本动态</h1>
          <p className="text-muted-foreground text-lg">系统更新、减负优化、玩法改动一览</p>
        </div>

        <div className="mb-8 p-6 rounded-xl bg-amber-500/10 border border-amber-500/20">
          <div className="flex items-start gap-3">
            <AlertTriangle className="w-6 h-6 text-amber-400 shrink-0 mt-0.5" />
            <div>
              <h3 className="font-bold text-amber-400 mb-2 text-lg">重要预告：海洋玩法即将封锁</h3>
              <p className="text-foreground/80 leading-relaxed">
                4月17日更新后，海洋探索、骑士委托将被移除，船只回收返还部分金条/补偿，但航海硬币不会回收。
                <span className="text-amber-400 font-bold"> 赶紧把还能做的海洋内容做掉，航海硬币赶紧花掉。</span>
              </p>
            </div>
          </div>
        </div>

        <div className="space-y-6">
          {SYSTEM_UPDATES.map((update, idx) => (
            <motion.div
              key={update.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: idx * 0.05 }}
            >
              <GameCard className="p-6 md:p-8">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 rounded-xl bg-primary/10 border border-primary/20 flex items-center justify-center shrink-0">
                    {update.id === 'qingsong-detail' ? <Settings className="w-6 h-6 text-primary" /> : <Wrench className="w-6 h-6 text-primary" />}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex flex-wrap items-center gap-3 mb-2">
                      <h3 className="text-xl font-bold text-foreground">{update.name}</h3>
                      <span className="px-2 py-0.5 rounded text-xs bg-white/5 text-muted-foreground border border-white/10">
                        {update.server}
                      </span>
                    </div>
                    <p className="text-sm text-muted-foreground font-mono mb-3">{update.date}</p>
                    <p className="text-foreground/70 text-sm mb-4 leading-relaxed">{update.description}</p>
                    <div className="space-y-2">
                      {update.details.map((detail, i) => (
                        <div key={i} className="flex items-start gap-2 text-sm">
                          <ArrowRight className="w-4 h-4 text-primary shrink-0 mt-0.5" />
                          <span className="text-foreground/80">{detail}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              </GameCard>
            </motion.div>
          ))}
        </div>
      </div>
    </PageWrapper>
  );
}
