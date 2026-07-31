interface TextProps {
  children: React.ReactNode;
  className?: string;
}

export default function Text({ children, className = "" }: TextProps) {
  return <p className={`leading-8 text-slate-600 ${className}`}>{children}</p>;
}
