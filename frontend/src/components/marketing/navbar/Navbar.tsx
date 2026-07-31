import Container from "@/components/ui/Container";

import NavLogo from "./NavLogo";
import NavLinks from "./NavLinks";
import NavActions from "./NavActions";
// import MobileMenu from "./MobileMenu";

export default function Navbar() {
  return (
    <header className="fixed inset-x-0 top-6 z-50 flex justify-center">
      <Container className="max-w-7xl">
        <div className="grid h-16 grid-cols-[200px_1fr_200px] items-center rounded-full border border-slate-200/70 bg-white/80 px-8 lg:px-10 shadow-[0_10px_35px_rgba(15,23,42,0.08)] backdrop-blur-xl transition-all duration-300">
          {/* Logo */}
          <div className="justify-self-start">
            <NavLogo />
          </div>

          {/* Navigation */}
          <div className="flex justify-center">
            <NavLinks />
          </div>

          {/* Actions */}
          <div className="justify-self-end">
            <NavActions />
          </div>
        </div>
      </Container>
    </header>
  );
}
