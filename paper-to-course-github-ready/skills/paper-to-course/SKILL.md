---
name: paper-to-course
description: "Turn research papers, PDFs, arXiv links, DOI pages, preprints, manuscripts, or academic articles into beautiful interactive single-page HTML courses. Use this skill whenever someone wants to learn a paper, explain a paper interactively, convert a paper into a course/tutorial/walkthrough, teach a PDF or arXiv paper, break down equations/figures/experiments, make a paper study guide, or create an educational course from scientific writing. Produces a self-contained browser course with paper-claim tracing, figure walkthroughs, equation translations, experiment logic, quizzes, glossary tooltips, and reproduction guidance."
---

# Paper-to-Course

Transform a research paper into an interactive course that teaches the paper's argument, method, evidence, and limitations. The output is a **directory** containing copied course assets, per-module HTML files, and an assembled `index.html` that opens in a browser.

The learner may be technical but not yet fluent in the paper's field. Teach like a sharp labmate: concrete, visual, precise, and honest about what the paper proves versus what it only suggests.

## Intake

Accept any of these inputs:
- Local PDF path
- arXiv URL, DOI URL, publisher page, or GitHub-hosted paper
- Local manuscript source such as `.tex`, `.md`, `.docx`, or extracted text
- A paper title plus permission to look it up

If the input is a PDF and PDF tools are available, use them to extract text and visually inspect important pages/figures. If not, use `scripts/extract_pdf_outline.py` for a first-pass outline and then inspect the PDF with available local tools. For arXiv/DOI/publisher URLs, download or browse the paper first, then work from the actual paper text rather than an abstract-only summary.

## The Core Shift

Do not summarize the paper into slides. Build a course around the paper's reasoning chain:

```
problem -> gap -> claim -> method -> equations/algorithm -> experiments -> limits -> reuse
```

Every module should help the learner do one practical thing better: explain the paper, implement the idea, evaluate the evidence, reproduce a result, or decide whether the method applies to their own problem.

## Phase 1: Paper Analysis

Before writing course HTML, deeply understand the paper. Read `references/paper-analysis.md` before analysis.

Extract:
- Bibliographic identity: title, authors, venue/date if available
- One-sentence thesis: what the paper claims
- Problem and gap: what was hard or missing before this paper
- Contributions: separate real contributions from framing claims
- Method pipeline: inputs, assumptions, transformations, outputs
- Key equations, algorithms, and definitions
- Figures and tables: what each is meant to prove
- Experiments: datasets, baselines, metrics, ablations, negative results
- Limitations: stated, implied, and hidden assumptions
- Reproduction path: code/data availability, dependencies, parameters, missing details

For long or dense papers, create a temporary analysis note in the output directory with section summaries and selected snippets. Do not include this note in the final course unless the user asks.

## Phase 2: Curriculum Design

Design **4-6 modules**. Use fewer modules for short papers, and 6 for dense ML/systems/science papers. Do not ask for approval; build the course, then invite feedback.

Default arc:

| Module | Purpose |
|---|---|
| 1 | Why this paper exists: problem, gap, thesis |
| 2 | The core idea in plain language |
| 3 | Method or algorithm walkthrough |
| 4 | Key equation, figure, or mechanism |
| 5 | Experiments and evidence |
| 6 | Limits, reproduction, and how to reuse the idea |

Adapt the arc to the paper. A theory paper may need more equation modules; an empirical paper may need more experiment logic; a survey may need a map of the field.

Each module must include:
- 3-6 screens
- At least one interactive or strongly visual element
- At least one paper-to-plain-English translation block, such as quote/claim/equation/algorithm on the left and explanation on the right
- At least one quiz that tests application, not memorization
- Glossary tooltips on technical terms at first use in each module

Every course must include at least:
- One **argument flow** or **method flow** animation
- One **figure/table walkthrough** or visual evidence map
- One **equation or algorithm translation** if the paper contains equations or pseudocode
- One **limitations/reproduction** module or screen

## Phase 3: Build the Course

The output is a directory, not a single manually-written file.

Recommended output structure:

```
paper-title-course/
  styles.css       <- copied from assets/styles.css
  main.js          <- copied from assets/main.js
  _base.html       <- customized from assets/_base.html
  _footer.html     <- copied from assets/_footer.html
  build.sh         <- copied from assets/build.sh
  modules/
    01-problem.html
    02-core-idea.html
    ...
  index.html       <- assembled by build.sh
```

Setup:
1. Create the course directory and `modules/`.
2. Copy `assets/styles.css`, `assets/main.js`, `assets/_footer.html`, and `assets/build.sh` verbatim.
3. Customize `assets/_base.html` with exactly:
   - course title
   - accent palette
   - one nav dot per module
4. Write module files containing only `<section class="module" id="module-N">...</section>`.
5. Run `bash build.sh` from the course directory.

Never regenerate `styles.css` or `main.js`; they are the stable course engine. Use `references/interactive-elements.md` for valid HTML patterns and `references/design-system.md` for visual conventions.

## Paper-Specific Teaching Rules

Read only the relevant references as needed:

- `references/paper-analysis.md` — paper decomposition workflow and evidence map
- `references/equation-teaching.md` — equations, algorithms, variables, and math intuition
- `references/figure-reading.md` — figure/table walkthrough patterns
- `references/experiment-logic.md` — baselines, metrics, ablations, and claims
- `references/paper-content-philosophy.md` — course voice, density, honesty, and quizzes
- `references/course-gotchas.md` — inherited HTML course failure checklist
- `references/interactive-elements.md` — HTML patterns for quizzes, flows, chat, cards, tooltips
- `references/design-system.md` — styling tokens and layout patterns

Use short direct excerpts from the paper only when necessary. Prefer paraphrase for copyrighted papers, and keep quotations brief. When quoting, identify the section/page when available.

## Review

After building:
1. Run the build script.
2. Verify the number of modules equals the number of nav dots.
3. Check that every quiz, flow, tooltip, and navigation dot works.
4. Open the course in a browser or serve it locally if direct `file://` access is blocked.
5. Report the final `index.html` path and any limitations, such as missing figures because the source PDF could not be extracted.
