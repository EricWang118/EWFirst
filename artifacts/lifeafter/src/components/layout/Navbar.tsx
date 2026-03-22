import { useState, useEffect } from "react";
import { Link, useLocation } from "wouter";
import { motion, AnimatePresence } from "framer-motion";
import { Menu, X, ChevronDown, Gamepad2 } from "lucide-react";
import { clsx } from "clsx";

const NAV_LINKS = [
  { href: "/", label: "首页" },
  { href: "/events", label: "当前活动" },
  { 
    href: "/pools", 
    label: "奖池详情",
    subLinks: [
      { href: "/pools/cold-blade", label: "蓄势寒锋" },
      { href: "/pools/youth-variation", label: "青春变奏曲" },
      { href: "/pools/sakura-fox", label: "樱灵狐梦" },
      { href: "/pools/chenshi-treasure", label: "宸世臻藏" },
      { href: "/pools/spring-furniture-oz", label: "绿野仙踪" },
    ]
  },
  { 
    href: "/guides", 
    label: "玩家攻略",
    subLinks: [
      { href: "/guides/f2p", label: "白嫖/平民" },
      { href: "/guides/combat", label: "战力/PVP" },
      { href: "/guides/manor", label: "庄园/建筑" },
      { href: "/guides/fashion", label: "外观/收藏" },
      { href: "/guides/returning", label: "回坑指南" },
    ]
  },
  { href: "/updates", label: "版本动态" }
];

export function Navbar() {
  const [location] = useLocation();
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [openDropdown, setOpenDropdown] = useState<string | null>(null);

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 20);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  useEffect(() => {
    setMobileMenuOpen(false);
    setOpenDropdown(null);
  }, [location]);

  return (
    <header 
      className={clsx(
        "fixed top-0 left-0 right-0 z-50 transition-all duration-300",
        isScrolled ? "bg-background/80 backdrop-blur-xl border-b border-white/5 py-3 shadow-lg" : "bg-transparent py-5"
      )}
    >
      <div className="container mx-auto px-4 md:px-6 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2 group relative z-50">
          <div className="bg-primary p-2 rounded-xl text-primary-foreground group-hover:scale-110 transition-transform">
            <Gamepad2 className="w-5 h-5" />
          </div>
          <span className="font-display text-2xl tracking-widest text-foreground group-hover:text-primary transition-colors">
            明日之后<span className="text-primary opacity-80 text-sm ml-2 font-sans tracking-normal">攻略站</span>
          </span>
        </Link>

        <nav className="hidden md:flex items-center gap-6">
          {NAV_LINKS.map((link) => {
            const isActive = link.href === "/" ? location === "/" : location.startsWith(link.href);
            
            if (link.subLinks) {
              return (
                <div 
                  key={link.href}
                  className="relative group"
                  onMouseEnter={() => setOpenDropdown(link.href)}
                  onMouseLeave={() => setOpenDropdown(null)}
                >
                  <Link 
                    href={link.subLinks[0].href}
                    className={clsx(
                      "flex items-center gap-1 text-sm font-medium transition-colors hover:text-primary py-2",
                      isActive ? "text-primary" : "text-muted-foreground"
                    )}
                  >
                    {link.label}
                    <ChevronDown className={clsx("w-4 h-4 transition-transform", openDropdown === link.href && "rotate-180")} />
                  </Link>
                  
                  <AnimatePresence>
                    {openDropdown === link.href && (
                      <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: 10 }}
                        transition={{ duration: 0.2 }}
                        className="absolute top-full left-1/2 -translate-x-1/2 pt-2 min-w-[160px]"
                      >
                        <div className="glass-panel rounded-xl overflow-hidden py-2 flex flex-col">
                          {link.subLinks.map(sub => (
                            <Link 
                              key={sub.href} 
                              href={sub.href}
                              className={clsx(
                                "px-4 py-2.5 text-sm transition-colors hover:bg-white/5",
                                location === sub.href ? "text-primary bg-primary/10" : "text-foreground"
                              )}
                            >
                              {sub.label}
                            </Link>
                          ))}
                        </div>
                      </motion.div>
                    )}
                  </AnimatePresence>
                </div>
              );
            }

            return (
              <Link 
                key={link.href} 
                href={link.href}
                className={clsx(
                  "text-sm font-medium transition-colors hover:text-primary relative",
                  isActive ? "text-primary" : "text-muted-foreground"
                )}
              >
                {link.label}
                {isActive && (
                  <motion.div 
                    layoutId="desktop-nav-indicator"
                    className="absolute -bottom-1.5 left-0 right-0 h-0.5 bg-primary"
                  />
                )}
              </Link>
            );
          })}
        </nav>

        <button 
          className="md:hidden p-2 text-foreground relative z-50"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
        >
          {mobileMenuOpen ? <X /> : <Menu />}
        </button>

        <AnimatePresence>
          {mobileMenuOpen && (
            <motion.div
              initial={{ opacity: 0, y: -20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="absolute inset-x-0 top-0 pt-24 pb-8 px-6 bg-background/95 backdrop-blur-3xl border-b border-border z-40 md:hidden flex flex-col gap-4 shadow-2xl"
            >
              {NAV_LINKS.map((link) => (
                <div key={link.href} className="flex flex-col">
                  {link.subLinks ? (
                    <>
                      <div className="text-sm font-bold text-muted-foreground mb-2 px-2 uppercase tracking-wider">{link.label}</div>
                      <div className="flex flex-col pl-4 border-l border-white/10 space-y-1">
                        {link.subLinks.map(sub => (
                          <Link 
                            key={sub.href} 
                            href={sub.href}
                            className={clsx(
                              "px-2 py-3 rounded-lg text-lg font-medium transition-colors",
                              location === sub.href ? "bg-primary/20 text-primary" : "text-foreground hover:bg-white/5"
                            )}
                          >
                            {sub.label}
                          </Link>
                        ))}
                      </div>
                    </>
                  ) : (
                    <Link 
                      href={link.href}
                      className={clsx(
                        "px-4 py-3 rounded-xl text-lg font-medium transition-colors",
                        (link.href === "/" ? location === "/" : location.startsWith(link.href))
                          ? "bg-primary text-primary-foreground" 
                          : "text-foreground hover:bg-white/5"
                      )}
                    >
                      {link.label}
                    </Link>
                  )}
                </div>
              ))}
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </header>
  );
}
