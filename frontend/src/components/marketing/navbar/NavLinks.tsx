import Link from "next/link";
import { navigation } from "@/data/navigation";

export default function NavLinks() {
  return (
    <nav className="hidden items-center gap-12 lg:flex">
      {navigation.map((item) => (
        <Link
          key={item.title}
          href={item.href}
          className="text-[15px] font-medium text-slate-600 transition-colors duration-300 hover:text-black"
        >
          {item.title}
        </Link>
      ))}
    </nav>
  );
}
