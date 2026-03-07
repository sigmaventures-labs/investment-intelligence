import {
  ArrowRight,
  BarChart3,
  BookOpen,
  ChevronRight,
  ExternalLink,
  Github,
  Grid3X3,
  Mail,
  MessageSquareWarning,
  Network,
  Radar,
  Shield,
  Target,
  Zap,
} from "lucide-react";

const GITHUB_URL = "https://github.com/sigmaventures-labs/investment-intelligence";

const skills = [
  {
    name: "Thematic Screening",
    description:
      "Go from a macro thesis to a ranked list of investable names in minutes \u2014 with the non-obvious second and third-order plays most screens miss.",
    icon: Network,
    example: `${GITHUB_URL}/blob/main/examples/thematic-screening.md`,
  },
  {
    name: "Investment Memo",
    description:
      "Produce an IC-ready memo that argues a position, not just describes a company. Variant perception, key drivers, valuation, risks \u2014 done in one pass.",
    icon: BookOpen,
    example: `${GITHUB_URL}/blob/main/examples/investment-memo.md`,
  },
  {
    name: "CIO/PM Q&A Prep",
    description:
      "Know the 25 hardest questions before you walk into the room. Pre-built answers, supporting evidence, and clear red lines for each.",
    icon: MessageSquareWarning,
    example: `${GITHUB_URL}/blob/main/examples/cio-qa-prep.md`,
  },
  {
    name: "Catalyst Mapping",
    description:
      "See every event that could move your position \u2014 with asymmetry analysis that tells you which catalysts are worth trading around.",
    icon: Target,
    example: `${GITHUB_URL}/blob/main/examples/catalyst-mapping.md`,
  },
  {
    name: "Cross-Asset Signals",
    description:
      "Find out whether rates, credit, FX, commodities, and vol agree with your thesis \u2014 or are quietly contradicting it.",
    icon: Radar,
    example: `${GITHUB_URL}/blob/main/examples/cross-asset-signals.md`,
  },
  {
    name: "Scenario Analysis",
    description:
      "Know your upside, downside, and exactly where the thesis breaks. Probability-weighted returns with sensitivity tables and decision triggers.",
    icon: BarChart3,
    example: `${GITHUB_URL}/blob/main/examples/scenario-analysis.md`,
  },
];

const comparisonRows = [
  { label: "Output", free: "Markdown document", engine: "Structured JSON + formatted PDF" },
  { label: "Numbers", free: "LLM estimates (flagged)", engine: "Computed from valuation models" },
  {
    label: "Sensitivity",
    free: "3\u00d73 table (estimated)",
    engine: "N\u00d7N grid (calculated) + Monte Carlo",
  },
  { label: "Quality", free: "Unchecked", engine: "Scored against explicit criteria" },
  { label: "Data", free: "Training data only", engine: "Live data via MCP connectors" },
  {
    label: "Integration",
    free: "Copy-paste",
    engine: "API, calendar export, JSON for downstream tools",
  },
];

const faqs = [
  {
    q: "Who is this for?",
    a: "Investment professionals who use AI coding tools (Cursor, Claude Code, OpenClaw) for research. The free skills work for anyone. The Engine and institutional services are designed for analysts, emerging managers, small funds, and family offices.",
  },
  {
    q: "Do I need an API key for the free skills?",
    a: "No. The skills run on whatever LLM your IDE provides. No additional API keys, no account required.",
  },
  {
    q: "Are the numbers in the output real?",
    a: "In Surface Mode, market data and estimates come from the LLM\u2019s training data and are flagged with [estimate]. Connect MCP data sources or use the Engine for computed, verified figures.",
  },
  {
    q: "What\u2019s the difference between the free skills and the Engine?",
    a: "The free skills produce structured markdown with estimated numbers. The Engine computes real sensitivity grids, runs Monte Carlo simulations, scores output quality, and returns structured JSON + formatted PDF. The skills are the methodology. The Engine is the math.",
  },
  {
    q: "How is this different from ChatGPT / Claude?",
    a: "ChatGPT and Claude are general-purpose models. Investment Intelligence is a structured decision architecture built specifically for institutional investment analysis. The difference is the same as between a blank spreadsheet and a fully built financial model.",
  },
  {
    q: "Is my data safe?",
    a: "The free skills run entirely locally in your IDE. The Engine API processes inputs server-side \u2014 we do not train on your data, and all data is encrypted in transit and at rest.",
  },
];

export default function Home() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <Nav />
      <Hero />
      <Problem />
      <Skills />
      <Engine />
      <Institutional />
      <DataPhilosophy />
      <FAQ />
      <Footer />
    </div>
  );
}

function Nav() {
  return (
    <nav className="fixed top-0 z-50 w-full border-b border-border/50 bg-background/80 backdrop-blur-md">
      <div className="mx-auto flex h-14 max-w-6xl items-center justify-between px-6">
        <a href="#" className="font-mono text-sm font-medium tracking-tight">
          Investment Intelligence
        </a>
        <div className="hidden items-center gap-8 text-sm text-muted md:flex">
          <a href="#skills" className="transition-colors hover:text-foreground">
            Skills
          </a>
          <a href="#engine" className="transition-colors hover:text-foreground">
            Engine
          </a>
          <a href="#teams" className="transition-colors hover:text-foreground">
            For Teams
          </a>
          <a
            href={GITHUB_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="transition-colors hover:text-foreground"
          >
            <Github className="h-4 w-4" />
          </a>
        </div>
        <a
          href={GITHUB_URL}
          target="_blank"
          rel="noopener noreferrer"
          className="hidden rounded-md bg-foreground px-3.5 py-1.5 text-sm font-medium text-background transition-opacity hover:opacity-90 md:block"
        >
          Get Started
        </a>
      </div>
    </nav>
  );
}

function Hero() {
  return (
    <section className="relative flex min-h-[85vh] flex-col items-center justify-center px-6 pt-14">
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--color-accent-muted)_0%,_transparent_70%)] opacity-20" />
      <div className="relative z-10 mx-auto max-w-3xl text-center">
        <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-border px-3 py-1 text-xs text-muted">
          <span className="h-1.5 w-1.5 rounded-full bg-accent" />
          Open-source &middot; MIT license
        </div>
        <h1 className="text-4xl font-semibold leading-tight tracking-tight sm:text-5xl md:text-6xl">
          Citadel-grade research throughput. Without the Citadel-sized headcount.
        </h1>
        <p className="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-muted">
          Six AI workflows that turn hours of analyst grunt work into minutes
          &mdash; thematic screens, investment memos, IC prep, catalyst maps,
          cross-asset checks, and scenario analysis. Institutional-grade output,
          every time.
        </p>
        <p className="mx-auto mt-3 max-w-2xl text-base text-muted/70">
          Coming soon: the <span className="text-foreground font-medium">Engine</span>.
          Numbers you can trust, analysis you can score, deliverables you can
          hand to your PM.
        </p>
        <div className="mt-10 flex flex-col items-center gap-4 sm:flex-row sm:justify-center">
          <a
            href={GITHUB_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 rounded-md bg-foreground px-5 py-2.5 text-sm font-medium text-background transition-opacity hover:opacity-90"
          >
            Install the free skills
            <ArrowRight className="h-4 w-4" />
          </a>
          <a
            href="#engine"
            className="inline-flex items-center gap-2 rounded-md border border-border px-5 py-2.5 text-sm font-medium text-muted transition-colors hover:border-foreground/30 hover:text-foreground"
          >
            Join the Engine waitlist
          </a>
        </div>
        <p className="mt-6 text-xs text-muted/50">
          Works with Cursor, Claude Code, OpenClaw, and Cowork.
        </p>
      </div>
    </section>
  );
}

function Problem() {
  return (
    <section className="border-y border-border bg-surface px-6 py-20">
      <div className="mx-auto max-w-3xl text-center">
        <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl">
          The largest funds already built this internally.
        </h2>
        <p className="mt-6 text-base leading-relaxed text-muted">
          Citadel, Balyasny, and Point72 have deployed AI research assistants
          that compress weeks of analyst work into minutes. Their edge isn&apos;t
          the model &mdash; it&apos;s the structured workflows, data plumbing,
          and quality governance underneath.
        </p>
        <p className="mt-4 text-base font-medium text-foreground">
          You need the same throughput. You don&apos;t have the same headcount.
        </p>
      </div>
    </section>
  );
}

function Skills() {
  return (
    <section id="skills" className="px-6 py-24">
      <div className="mx-auto max-w-6xl">
        <div className="text-center">
          <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl">
            Six workflows. Hours of work, compressed into minutes.
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-base text-muted">
            Each workflow encodes institutional best practices into a repeatable
            decision framework. Free, open-source, and ready to use in your IDE today.
          </p>
        </div>

        <div className="mt-16 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {skills.map((skill) => (
            <div
              key={skill.name}
              className="group rounded-lg border border-border bg-surface-raised p-6 transition-colors hover:border-foreground/20"
            >
              <skill.icon className="h-5 w-5 text-accent" />
              <h3 className="mt-4 text-sm font-semibold">{skill.name}</h3>
              <p className="mt-2 text-sm leading-relaxed text-muted">
                {skill.description}
              </p>
              <a
                href={skill.example}
                target="_blank"
                rel="noopener noreferrer"
                className="mt-4 inline-flex items-center gap-1 text-xs text-accent transition-colors hover:text-accent/80"
              >
                See example output
                <ExternalLink className="h-3 w-3" />
              </a>
            </div>
          ))}
        </div>

        <div className="mt-12 text-center">
          <a
            href={GITHUB_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 rounded-md border border-border px-5 py-2.5 text-sm font-medium text-muted transition-colors hover:border-foreground/30 hover:text-foreground"
          >
            <Github className="h-4 w-4" />
            Get the free skills on GitHub
          </a>
        </div>
      </div>
    </section>
  );
}

function Engine() {
  return (
    <section id="engine" className="border-y border-border bg-surface px-6 py-24">
      <div className="mx-auto max-w-6xl">
        <div className="text-center">
          <div className="mb-4 inline-flex items-center gap-2 rounded-full border border-accent/30 bg-accent/10 px-3 py-1 text-xs text-accent">
            Coming Q2 2026
          </div>
          <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl">
            Stop estimating. Start computing.
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-base text-muted">
            The free skills give you structured analysis with estimated figures.
            The Engine is a paid upgrade that gives you real math &mdash;
            computed sensitivity grids, Monte Carlo simulations, and
            quality-scored output you can hand directly to your PM.
          </p>
        </div>

        <div className="mt-16 overflow-hidden rounded-lg border border-border">
          <div className="grid grid-cols-3 border-b border-border bg-surface-raised text-xs font-medium">
            <div className="p-4" />
            <div className="border-l border-border p-4 text-muted">Free Skills</div>
            <div className="border-l border-border bg-accent/5 p-4 text-accent">
              Engine <span className="text-accent/60">(paid)</span>
            </div>
          </div>
          {comparisonRows.map((row) => (
            <div
              key={row.label}
              className="grid grid-cols-3 border-b border-border last:border-b-0"
            >
              <div className="p-4 text-sm font-medium">{row.label}</div>
              <div className="border-l border-border p-4 text-sm text-muted">
                {row.free}
              </div>
              <div className="border-l border-border bg-accent/5 p-4 text-sm text-foreground">
                {row.engine}
              </div>
            </div>
          ))}
        </div>

        <p className="mx-auto mt-8 max-w-2xl text-center text-xs text-muted/60">
          Every output scored against 162 institutional quality criteria.
          The same evaluation framework that maintains a 96.3% pass rate
          internally now powers the Engine&apos;s user-facing quality scores.
        </p>

        <div className="mt-16 grid gap-8 md:grid-cols-3">
          <div>
            <div className="flex h-10 w-10 items-center justify-center rounded-lg border border-border bg-surface-raised">
              <Grid3X3 className="h-5 w-5 text-accent" />
            </div>
            <h3 className="mt-4 text-sm font-semibold">Trust the numbers.</h3>
            <p className="mt-2 text-sm leading-relaxed text-muted">
              Sensitivity grids calculated from valuation models, not guessed by
              an LLM. Monte Carlo across 1,000 iterations. You see exactly where
              your thesis breaks.
            </p>
          </div>
          <div>
            <div className="flex h-10 w-10 items-center justify-center rounded-lg border border-border bg-surface-raised">
              <Shield className="h-5 w-5 text-accent" />
            </div>
            <h3 className="mt-4 text-sm font-semibold">Know where your analysis is weak.</h3>
            <p className="mt-2 text-sm leading-relaxed text-muted">
              Every output scored against institutional quality criteria. You see
              the per-section breakdown and specific suggestions for what to
              strengthen before IC.
            </p>
          </div>
          <div>
            <div className="flex h-10 w-10 items-center justify-center rounded-lg border border-border bg-surface-raised">
              <Zap className="h-5 w-5 text-accent" />
            </div>
            <h3 className="mt-4 text-sm font-semibold">IC-ready deliverables, not raw text.</h3>
            <p className="mt-2 text-sm leading-relaxed text-muted">
              Formatted PDF, structured JSON, and clean markdown. Hand it to your
              PM, feed it into your models, or pipe it to another tool via API.
            </p>
          </div>
        </div>

        <div className="mx-auto mt-16 max-w-md text-center">
          <p className="text-sm text-muted">
            The Engine launches in Q2 2026 as a Pro subscription. Join the
            waitlist for early access and launch pricing.
          </p>
          <form className="mt-4 flex gap-2" action="#" method="POST">
            <input
              type="email"
              name="email"
              placeholder="you@fund.com"
              required
              className="flex-1 rounded-md border border-border bg-surface px-4 py-2.5 text-sm text-foreground placeholder:text-muted/50 focus:border-accent focus:outline-none focus:ring-1 focus:ring-accent"
            />
            <button
              type="submit"
              className="inline-flex items-center gap-2 rounded-md bg-accent px-5 py-2.5 text-sm font-medium text-white transition-opacity hover:opacity-90"
            >
              Join waitlist
              <ChevronRight className="h-4 w-4" />
            </button>
          </form>
        </div>
      </div>
    </section>
  );
}

function Institutional() {
  return (
    <section id="teams" className="px-6 py-24">
      <div className="mx-auto max-w-6xl">
        <div className="text-center">
          <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl">
            For funds that want this embedded in their research process.
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-base text-muted">
            We work directly with mid-sized investment firms to integrate
            custom AI workflows into daily research operations &mdash;
            tailored to your process, your data, and your team. Your analysts
            cover more names. Your research process becomes repeatable.
          </p>
        </div>

        <div className="mt-16 grid gap-6 md:grid-cols-2">
          <div className="rounded-lg border border-border bg-surface-raised p-8">
            <div className="text-xs font-medium uppercase tracking-wider text-muted">
              Phase 1
            </div>
            <h3 className="mt-3 text-lg font-semibold">Diagnostic &amp; Workshop</h3>
            <p className="mt-3 text-sm leading-relaxed text-muted">
              We run the system on your coverage universe, map your research
              workflow, identify bottlenecks, and deliver a concrete
              implementation roadmap. You keep everything &mdash; whether or not
              you go further.
            </p>
          </div>

          <div className="rounded-lg border border-border bg-surface-raised p-8">
            <div className="text-xs font-medium uppercase tracking-wider text-muted">
              Phase 2
            </div>
            <h3 className="mt-3 text-lg font-semibold">Custom Implementation</h3>
            <p className="mt-3 text-sm leading-relaxed text-muted">
              Production research flows tailored to your process, wired to your
              data, embedded in your daily tools, with a firm-specific quality
              evaluation suite and ops runbook.
            </p>
          </div>
        </div>

        <div className="mt-10 text-center">
          <a
            href="mailto:contact@investmentintelligence.ai"
            className="inline-flex items-center gap-2 rounded-md bg-foreground px-5 py-2.5 text-sm font-medium text-background transition-opacity hover:opacity-90"
          >
            <Mail className="h-4 w-4" />
            Book a diagnostic call
          </a>
        </div>
      </div>
    </section>
  );
}

function DataPhilosophy() {
  return (
    <section className="border-y border-border bg-surface px-6 py-24">
      <div className="mx-auto max-w-6xl">
        <div className="text-center">
          <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl">
            It works today with public data. It becomes your edge with proprietary data.
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-base text-muted">
            Start getting value immediately with the free skills and public data.
            Connect your licensed research, internal KPIs, or portfolio data
            through the Engine &mdash; and the same workflows produce materially
            sharper output.
          </p>
        </div>

        <div className="mt-16 grid gap-6 md:grid-cols-2">
          <div className="rounded-lg border border-border bg-surface-raised p-8">
            <div className="flex items-center gap-3">
              <div className="h-2 w-2 rounded-full bg-muted" />
              <h3 className="text-sm font-semibold">Surface Mode</h3>
            </div>
            <p className="mt-4 text-sm leading-relaxed text-muted">
              Public filings and AI estimates. Every estimate flagged for
              verification. Structured, useful, ready to build on.
            </p>
          </div>
          <div className="rounded-lg border border-accent/30 bg-accent/5 p-8">
            <div className="flex items-center gap-3">
              <div className="h-2 w-2 rounded-full bg-accent" />
              <h3 className="text-sm font-semibold">Enhanced Mode</h3>
            </div>
            <p className="mt-4 text-sm leading-relaxed text-muted">
              Your licensed data, internal metrics, and proprietary signals.
              Institutional-grade, differentiated output that reflects what you
              actually know.
            </p>
          </div>
        </div>

        <p className="mx-auto mt-10 max-w-2xl text-center text-xs text-muted/70">
          Built on the Model Context Protocol (MCP). FRED macro data is active
          and free.           Paid providers (FactSet, S&amp;P Global, PitchBook,
          Morningstar, etc.) plug in via your existing API keys. Your data stays local
          &mdash; nothing leaves your environment unless you send it to the
          Engine API.
        </p>
      </div>
    </section>
  );
}

function FAQ() {
  return (
    <section className="border-y border-border bg-surface px-6 py-24">
      <div className="mx-auto max-w-3xl">
        <h2 className="text-center text-2xl font-semibold tracking-tight sm:text-3xl">
          Questions
        </h2>
        <div className="mt-12 divide-y divide-border">
          {faqs.map((faq) => (
            <div key={faq.q} className="py-6">
              <h3 className="text-sm font-semibold">{faq.q}</h3>
              <p className="mt-3 text-sm leading-relaxed text-muted">
                {faq.a}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="px-6 py-16">
      <div className="mx-auto max-w-6xl">
        <div className="flex flex-col items-center gap-8 text-center">
          <div>
            <p className="text-sm text-muted">Stay informed. No spam.</p>
            <form className="mt-3 flex gap-2" action="#" method="POST">
              <input
                type="email"
                name="email"
                placeholder="you@fund.com"
                required
                className="w-64 rounded-md border border-border bg-surface px-4 py-2.5 text-sm text-foreground placeholder:text-muted/50 focus:border-accent focus:outline-none focus:ring-1 focus:ring-accent"
              />
              <button
                type="submit"
                className="rounded-md border border-border px-4 py-2.5 text-sm font-medium text-muted transition-colors hover:border-foreground/30 hover:text-foreground"
              >
                Subscribe
              </button>
            </form>
          </div>

          <div className="flex flex-wrap justify-center gap-6 text-xs text-muted">
            <a
              href={GITHUB_URL}
              target="_blank"
              rel="noopener noreferrer"
              className="transition-colors hover:text-foreground"
            >
              GitHub
            </a>
            <a
              href={`${GITHUB_URL}/tree/main/examples`}
              target="_blank"
              rel="noopener noreferrer"
              className="transition-colors hover:text-foreground"
            >
              Examples
            </a>
            <a
              href="mailto:contact@investmentintelligence.ai"
              className="transition-colors hover:text-foreground"
            >
              Contact
            </a>
          </div>

          <div className="max-w-lg text-center">
            <p className="font-mono text-xs text-muted/40">
              Investment Intelligence assists with financial analysis workflows
              but does not provide financial or investing advice. Outputs contain
              AI-generated analysis that should be verified against authoritative
              sources.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}
