import Link from "next/link";

export default function NavLogo() {
  return (
    <Link
      href="/"
      className="text-2xl font-bold tracking-tight text-slate-900 transition-colors duration-300 hover:text-blue-600"
    >
      VidyAI
    </Link>
  );
}
