interface HeadingProps {
  children: React.ReactNode;
  className?: string;
}

export default function Heading({ children, className = "" }: HeadingProps) {
  return (
    <h1 className={`font-bold tracking-tight text-slate-900 ${className}`}>
      {children}
    </h1>
  );
}
