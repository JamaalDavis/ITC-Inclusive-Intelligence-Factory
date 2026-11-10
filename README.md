# ITC Inclusive Intelligence Factory · v0.1

A runnable, dependency-free **reference scaffold** for an inclusive multi-agent editorial workflow. Inspired by the modular `agents / skills / workflows` structure of [tarekcxl/ai-seo-system](https://github.com/tarekcxl/ai-seo-system), but independently authored for Inclusive Tech Club.

## Why this exists

AI-generated outputs can be variable. **Governance doesn't have to be.** The system separates probabilistic content creation from deterministic permission checks, validation, and human publication approval. Accessibility, factual integrity and human agency are product requirements, not post-production decoration.

## What works in v0.1

- Command-line demonstration: `python -m itc_factory.demo` from inside `src` (see exact command below).
- Task context schema validation using Python's standard library (small subset of required fields, with JSON Schema for integration).
- Context selection with task-specific minimization and no private personal records in the output bundle.
- Draft evaluation for missing source support, missing alt-text, human approval and structured output.
- Structured handoff data and a human approval gate.
- Automated unit tests with `python -m unittest discover -s tests -v`.

**Not implemented:** actual LLM providers, live source retrieval, automated visual accessibility scanning, secure distributed authorization, CMS publishing, or real self-improvement. The demo deliberately does not pretend to verify factual claims. Human review is required. Do not use it as a production security boundary.

## Quick start

Requires Python 3.10+; no packages to install.

```bash
cd itc-inclusive-intelligence
PYTHONPATH=src python -m itc_factory.demo
PYTHONPATH=src python -m unittest discover -s tests -v
```

PowerShell:

```powershell
$env:PYTHONPATH="src"
python -m itc_factory.demo
python -m unittest discover -s tests -v
```

This prints an evaluation report and saves a demonstration packet under `workflows/output/`. Publication remains blocked unless both independent review evidence and explicit approval are provided.

## Directory structure

- `CLAUDE.md`: project policy and development instructions
- `agents/`: agent responsibilities, tool limits, and handoff contracts
- `skills/`: reusable focused skill instructions
- `context/`: governance principles, inclusion requirements, and design evolution notes
- `schemas/`: JSON Schema contracts for task input and handoff
- `src/itc_factory/`: runnable illustrative orchestration
- `evaluations/`: scoring rubrics and test cases
- `tests/`: executable checks
- `workflows/`: workflow specifications and generated local outputs
- `examples/`: sample task

## Architecture

`Task → context selection → research packet → editorial draft → evaluation → human review → approved publishing adapter (future)`

**Human approval is not the same as automated evaluation.** Automated checks can flag issues and block missing requirements; editorial judgment, lived-experience review and source verification remain necessary.

## Service design workflow

This proposed service workflow connects community needs, editorial delivery, and learning. It describes the intended service beyond the v0.1 demo: research and drafting currently use fixtures, human review is still required, and publishing is a future integration.

```mermaid
flowchart TD
    A["Discover: listen to community needs and access barriers"] --> B["Define: agree audience, outcome, scope, and authority"]
    B --> C["Prepare: validate brief and select minimal context"]
    C --> D["Develop: gather evidence, draft, and design"]
    D --> E["Evaluate: run checks and apply the rubric"]
    E --> F{"Checks pass?"}
    F -->|No| D
    F -->|Yes| G["Human review: verify sources and accessibility"]
    G --> H{"Review evidence and explicit approval recorded?"}
    H -->|Revisions needed| D
    H -->|Approval withheld| I["Hold: publication remains blocked"]
    H -->|Yes| J["Deliver: restricted publishing adapter - future"]
    J --> K["Learn: collect feedback and outcome metrics"]
    K --> A
```

**Text equivalent:** Discover community needs, define the service outcome, validate the brief, and prepare content with relevant context. Failed checks or requested revisions return to development. Publication stays blocked without human review evidence and explicit approval. After future delivery, feedback informs the next brief.

## Community member journey

This illustrative journey follows a community member requesting an accessible explainer. Satisfaction scores are design hypotheses on a 1–5 scale, not measured research findings. Delivery and feedback stages describe the future service.

```mermaid
journey
    title Requesting an accessible ITC explainer
    section Discover
      Find a relevant topic: 3: Community member
      Share a question and access preferences: 3: Community member
    section Define
      Agree the brief and preferred format: 4: Community member, Editor
    section Develop
      Prepare a source-supported draft: 3: Editor
      Review clarity and accessibility: 3: Editor, Reviewer
    section Approve
      Resolve review findings: 4: Editor, Reviewer
      Record the publication decision: 4: Reviewer
    section Deliver and learn - future
      Read or listen in the preferred format: 5: Community member
      Report a barrier or suggest a correction: 3: Community member, Editor
```

**Text equivalent:** The member finds a topic, shares a question and access preferences, and agrees a brief with an editor. The editor prepares the draft; a human reviewer checks it and records a publication decision. In the future service, the member receives an approved explainer in their preferred format and can report barriers or corrections.

Use interviews and accessibility review to validate this journey before treating it as evidence. Track clarity of the brief, review turnaround, access barriers, and whether members can use the final content.

## Service blueprint

Follow the service from left to right. Each row shows what the community member experiences and what ITC must do to support it. This is a proposed service design, not evidence from a live service.

| Service layer | 1. Request | 2. Agree | 3. Prepare and review | 4. Deliver | 5. Improve |
| --- | --- | --- | --- | --- | --- |
| **Community actions** | Share a question and optional access preferences | Confirm the outcome and format | Clarify the request if needed | Read or listen to the explainer | Report a barrier or request a correction |
| **Visible editorial support** | Acknowledge the request | Confirm scope, format, and next step | Explain progress or a hold | Share approved content in the agreed format | Acknowledge feedback and explain the response |
| **Internal work** | Validate task and authority | Select minimal relevant context | Prepare evidence and draft; evaluate; conduct human source and accessibility review | Obtain explicit approval before requesting publication | Triage feedback; revise content or the next brief |
| **Supporting systems** | Task schema | Context selection rules | Handoff contract and evaluation report | Approval gate; restricted publishing adapter (future) | Feedback records and outcome metrics (future) |
| **Service evidence** | Request summary | Agreed brief | Draft, source packet, review findings | Approval record and accessible explainer | Correction record and updated brief |
| **Failure and recovery** | Missing details: ask a focused question | Unclear scope: agree it before drafting | Failed checks or review: revise; approval missing: hold | Publication failure: retain approved packet and report status | Access barrier: offer an alternative format and review the cause |

**Line of interaction:** between community actions and visible editorial support. **Line of visibility:** between visible editorial support and internal work. Supporting systems enable the service; human reviewers retain editorial judgment and publication authority.

### Review and delivery gate

This diagram highlights the decision that controls delivery. Passing automated checks alone does not authorize publication.

```mermaid
flowchart TD
    A["Agreed brief and access preferences"] --> B["Prepare evidence, draft, and design"]
    B --> C{"Required checks pass?"}
    C -->|No| R["Revise with specific findings"]
    R --> B
    C -->|Yes| D["Human source and accessibility review"]
    D --> E{"Review outcome?"}
    E -->|Revisions requested| R
    E -->|Not approved| H["Hold and explain the next step"]
    E -->|Approved| F{"Review evidence and explicit approval recorded?"}
    F -->|No| H
    F -->|Yes| G["Request delivery through restricted adapter - future"]
    G --> I["Member receives agreed format - future"]
    I --> J["Feedback or correction request - future"]
    J -.->|Next revision| B
```

**Text equivalent:** Prepare content from an agreed brief, run checks, and revise failures. A human then reviews sources and accessibility. Requested changes return to preparation; a refusal or missing approval evidence keeps publication on hold. Only passing checks, recorded review evidence, and explicit approval allow future delivery. Feedback can initiate another revision, which must pass the same gates.

**Implementation boundary:** v0.1 validates tasks, selects context, uses fixtures for research and drafting, and runs a subset of evaluation checks. The demo blocks at human review. Member communications, persistent review records, live publishing, and feedback handling shown here remain future service capabilities. Recovery actions in the table are proposed operating practices.

## First pilot metrics

Source-backed claim rate, critical accessibility defects, time spent correcting drafts, editorial consistency, task success, and run cost. Compare baseline and new workflow using the same briefs and reviewer rubric.

## Reuse and provenance

The reference repository's architecture inspired the directory naming and modular approach; no files from that repository were copied. Do not infer a license grant for upstream code. This scaffold is independently authored and can be adapted by ITC. Add a license only after choosing appropriate publication terms.
