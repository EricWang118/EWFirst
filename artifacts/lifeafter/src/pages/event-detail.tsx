import { useParams, Link } from "wouter";
import { motion } from "framer-motion";
import { ArrowLeft, Info, Zap, Gift, Target } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { GameCard } from "@/components/ui/GameCard";
import { ACTIVITIES, getStatusText, getStatusColor, getPriorityColor } from "@/lib/data";
import NotFound from "./not-found";

export default function EventDetail() {
  const params = useParams();
  const event = ACTIVITIES.find(e => e.id === params.id);

  if (!event) return <NotFound />;

  return (
    <PageWrapper>
      <div className="container mx-auto px-4 max-w-4xl">
        <Link href="/events" className="inline-flex items-center text-muted-foreground hover:text-primary transition-colors mb-6 font-medium">
          <ArrowLeft className="w-4 h-4 mr-2" /> 返回活动列表
        </Link>

        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
          <GameCard className="p-8 md:p-12 mb-8">
            <div className="border-b border-border pb-8 mb-8">
              <div className="flex flex-wrap items-center gap-3 mb-4">
                <h1 className="text-3xl md:text-4xl font-bold text-foreground">{event.name}</h1>
                <span className={`px-3 py-1 rounded-full text-xs font-bold border ${getStatusColor(event.status)}`}>
                  {getStatusText(event.status)}
                </span>
                <span className={`px-2.5 py-1 rounded text-xs font-bold border ${getPriorityColor(event.priority)}`}>
                  优先级: {event.priority}
                </span>
              </div>
              <div className="flex flex-wrap items-center gap-4 text-sm text-muted-foreground">
                <span className="bg-white/5 px-3 py-1.5 rounded-lg border border-white/10 font-mono">{event.date}</span>
                <span className="bg-white/5 px-3 py-1.5 rounded-lg border border-white/10">{event.server}</span>
                <span className="bg-white/5 px-3 py-1.5 rounded-lg border border-white/10">{event.category}</span>
              </div>
              {event.tags.length > 0 && (
                <div className="flex flex-wrap gap-2 mt-4">
                  {event.tags.map(tag => (
                    <span key={tag} className="px-3 py-1 rounded-full text-xs bg-primary/10 text-primary border border-primary/20 font-medium">
                      {tag}
                    </span>
                  ))}
                </div>
              )}
            </div>

            <div className="space-y-8">
              <section>
                <h3 className="text-xl font-bold text-primary mb-3 flex items-center gap-2">
                  <Info className="w-5 h-5" /> 活动简介
                </h3>
                <p className="text-foreground/80 leading-relaxed bg-white/5 p-5 rounded-xl border border-white/5">{event.description}</p>
              </section>

              <section>
                <h3 className="text-xl font-bold text-primary mb-3 flex items-center gap-2">
                  <Zap className="w-5 h-5" /> 参与方式
                </h3>
                <p className="text-foreground/80 leading-relaxed bg-white/5 p-5 rounded-xl border border-white/5">{event.gameplay}</p>
              </section>

              <section>
                <h3 className="text-xl font-bold text-primary mb-3 flex items-center gap-2">
                  <Gift className="w-5 h-5" /> 奖励内容
                </h3>
                <p className="text-foreground/80 leading-relaxed bg-white/5 p-5 rounded-xl border border-white/5">{event.rewards}</p>
              </section>

              <section>
                <h3 className="text-xl font-bold text-amber-400 mb-3 flex items-center gap-2">
                  <Target className="w-5 h-5" /> 攻略建议
                </h3>
                <div className="bg-amber-500/10 p-5 rounded-xl border border-amber-500/20">
                  <p className="text-foreground/90 leading-relaxed">{event.tips}</p>
                </div>
              </section>
            </div>
          </GameCard>
        </motion.div>
      </div>
    </PageWrapper>
  );
}
