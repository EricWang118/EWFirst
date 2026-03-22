import React from "react";
import { Link } from "wouter";
import { motion } from "framer-motion";
import { ArrowRight } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { GameCard } from "@/components/ui/GameCard";
import { ACTIVITIES, getStatusText, getStatusColor, getPriorityColor } from "@/lib/data";

export default function Events() {
  const activeEvents = ACTIVITIES.filter(a => a.status === 'active' || a.status === 'ending-soon');
  const upcomingEvents = ACTIVITIES.filter(a => a.status === 'upcoming');
  const endedEvents = ACTIVITIES.filter(a => a.status === 'ended');

  const renderSection = (title: string, events: typeof ACTIVITIES, showIfEmpty = false) => {
    if (events.length === 0 && !showIfEmpty) return null;
    return (
      <div className="mb-12">
        <h2 className="text-2xl font-bold text-foreground mb-6 border-l-4 border-primary pl-4">{title}</h2>
        <div className="space-y-4">
          {events.map((event, idx) => (
            <motion.div
              key={event.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: idx * 0.05 }}
            >
              <Link href={`/events/${event.id}`}>
                <GameCard glowOnHover className="p-6 md:p-8">
                  <div className="flex flex-col md:flex-row gap-4 md:items-center">
                    <div className="flex-1">
                      <div className="flex flex-wrap items-center gap-3 mb-2">
                        <h3 className="text-xl font-bold text-foreground">{event.name}</h3>
                        <span className={`px-2.5 py-0.5 rounded-full text-xs font-bold border ${getStatusColor(event.status)}`}>
                          {event.status === 'ending-soon' && <span className="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse inline-block mr-1.5" />}
                          {event.status === 'active' && <span className="w-1.5 h-1.5 rounded-full bg-green-400 animate-pulse inline-block mr-1.5" />}
                          {getStatusText(event.status)}
                        </span>
                        <span className={`px-2 py-0.5 rounded text-xs font-bold border ${getPriorityColor(event.priority)}`}>
                          {event.priority}
                        </span>
                        <span className="px-2 py-0.5 rounded text-xs bg-white/5 text-muted-foreground border border-white/10">
                          {event.server}
                        </span>
                      </div>
                      <p className="text-sm text-muted-foreground font-mono mb-2">{event.date}</p>
                      <p className="text-foreground/70 text-sm line-clamp-2">{event.description}</p>
                      {event.tags.length > 0 && (
                        <div className="flex flex-wrap gap-1.5 mt-3">
                          {event.tags.map(tag => (
                            <span key={tag} className="px-2 py-0.5 rounded-full text-xs bg-primary/10 text-primary border border-primary/20">
                              {tag}
                            </span>
                          ))}
                        </div>
                      )}
                    </div>
                    <div className="shrink-0 flex items-center">
                      <span className="text-primary font-medium flex items-center text-sm">
                        查看详情 <ArrowRight className="w-4 h-4 ml-1" />
                      </span>
                    </div>
                  </div>
                </GameCard>
              </Link>
            </motion.div>
          ))}
        </div>
      </div>
    );
  };

  return (
    <PageWrapper>
      <div className="container mx-auto px-4 max-w-5xl">
        <div className="mb-10 text-center">
          <h1 className="text-4xl md:text-5xl font-display text-primary mb-4 text-glow">当前活动</h1>
          <p className="text-muted-foreground text-lg">2026年3月22日 · 春日樱花季版本</p>
        </div>

        {renderSection("进行中 / 即将结束", activeEvents)}
        {renderSection("即将开始", upcomingEvents)}
        {renderSection("已结束 / 已下架", endedEvents)}
      </div>
    </PageWrapper>
  );
}
