import Link from "next/link";
import { Button } from "@/components/ui/Button";

export default function NavActions() {
  return (
    <div className="mr-2 hidden items-center gap-4 lg:flex">
      <Button variant="ghost" asChild>
        <Link href="/login">Login</Link>
      </Button>

      <Button asChild>
        <Link href="/">Get Started</Link>
      </Button>
    </div>
  );
}
