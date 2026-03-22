import { Link } from "wouter";
import { AlertCircle } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";

export default function NotFound() {
  return (
    <PageWrapper>
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="glass-card p-12 max-w-md w-full text-center">
          <AlertCircle className="w-16 h-16 text-destructive mx-auto mb-6" />
          <h1 className="text-3xl font-bold text-foreground mb-4">区域未解锁</h1>
          <p className="text-muted-foreground mb-8">
            幸存者，你所寻找的坐标并不存在。请检查地图坐标或返回营地。
          </p>
          <Link href="/">
            <button className="px-6 py-3 bg-primary text-primary-foreground rounded-xl font-bold hover:shadow-[0_0_20px_rgba(245,158,11,0.4)] hover:scale-105 transition-all">
              返回安全区 (首页)
            </button>
          </Link>
        </div>
      </div>
    </PageWrapper>
  );
}
