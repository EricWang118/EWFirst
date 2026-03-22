import { ReactNode } from "react";
import { motion, HTMLMotionProps } from "framer-motion";
import { clsx } from "clsx";

interface GameCardProps extends HTMLMotionProps<"div"> {
  children: ReactNode;
  className?: string;
  glowOnHover?: boolean;
}

export function GameCard({ children, className, glowOnHover = false, ...props }: GameCardProps) {
  return (
    <motion.div
      {...props}
      className={clsx(
        "glass-card rounded-2xl overflow-hidden relative group",
        glowOnHover && "hover:border-primary/50 hover:shadow-[0_0_30px_rgba(245,158,11,0.15)] transition-all duration-300",
        className
      )}
    >
      <div className="absolute inset-0 bg-gradient-to-br from-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none" />
      {children}
    </motion.div>
  );
}
