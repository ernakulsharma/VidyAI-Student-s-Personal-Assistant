import { ReactNode } from "react";
import { cn } from "@/lib/utils";

interface CardProps {
  children: ReactNode;
  className?: string;
}

export default function Card({ children, className }: CardProps) {
  return (
    <div
      className={cn(
        "rounded-[28px] border-2 border-black bg-white p-8 shadow-sm transition-all duration-300 hover:-translate-y-2 hover:shadow-xl",
        className,
      )}
    >
      {children}
    </div>
  );
}
