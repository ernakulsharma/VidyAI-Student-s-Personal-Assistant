import { heroContent } from "@/data/hero";

import Badge from "@/components/typography/Badge";
import Heading from "@/components/typography/Heading";
import Text from "@/components/typography/Text";

import { Button } from "@/components/ui/Button";

export default function HeroContent() {
  return (
    <div className="max-w-xl">
      <Badge>{heroContent.badge}</Badge>

      <Heading className="mt-8 max-w-lg text-5xl leading-tight lg:text-6xl xl:text-7xl">
        {heroContent.title.map((line) => (
          <span key={line} className="block">
            {line}
          </span>
        ))}
      </Heading>

      <Text className="mt-8 text-lg">{heroContent.description}</Text>

      <div className="mt-10 flex flex-wrap gap-4">
        <Button size="lg">{heroContent.primaryCTA}</Button>

        <Button size="lg" variant="outline">
          {heroContent.secondaryCTA}
        </Button>
      </div>

      <div className="mt-12 space-y-4">
        {heroContent.highlights.map((item) => (
          <div key={item} className="flex items-center gap-3">
            <div className="h-2.5 w-2.5 rounded-full bg-green-500" />

            <p className="text-slate-600">{item}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
