import Container from "@/components/ui/Container";
import HeroContent from "./HeroContent";

export default function Hero() {
  return (
    <section className="min-h-[92vh] flex items-center">
      <Container className="px-12 lg:px-20">
        <div className="grid items-center gap-20 lg:grid-cols-12">
          {/* Left */}

          <div className="lg:col-span-6">
            <HeroContent />
          </div>

          {/* Right */}

          <div className="lg:col-span-6">
            <div className="flex h-[550px] items-center justify-center rounded-[32px] border border-dashed border-slate-300 bg-slate-50">
              <p className="text-slate-400">Knowledge Constellation</p>
            </div>
          </div>
        </div>
      </Container>
    </section>
  );
}
