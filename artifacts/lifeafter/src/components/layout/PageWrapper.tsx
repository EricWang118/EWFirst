import { ReactNode } from "react";
import { motion } from "framer-motion";
import { Navbar } from "./Navbar";

export function PageWrapper({ children, className = "" }: { children: ReactNode, className?: string }) {
  return (
    <div className="min-h-screen flex flex-col relative">
      {/* Global Background Element */}
      <div 
        className="fixed inset-0 z-[-1] opacity-20 pointer-events-none"
        style={{
          backgroundImage: `url(${import.meta.env.BASE_URL}images/grid-bg.png)`,
          backgroundSize: '400px 400px',
          backgroundRepeat: 'repeat',
        }}
      />
      
      <Navbar />
      
      <motion.main 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -20 }}
        transition={{ duration: 0.4, ease: "easeOut" }}
        className={`flex-grow pt-24 pb-16 ${className}`}
      >
        {children}
      </motion.main>
    </div>
  );
}
