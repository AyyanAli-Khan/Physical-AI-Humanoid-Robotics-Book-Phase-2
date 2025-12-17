---
id: 1
title: Update Constitution
stage: constitution
date: 2025-12-09
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution,book,physical-ai,humanoid-robotics]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
/sp.constitution

Project: Book on Physical AI & Humanoid Robotics

Core principles:

* Scientific accuracy through verification from primary robotics and AI sources
* Clarity for an academic and engineering audience
* Reproducibility of all technical claims with proper citations
* Rigor grounded in peer-reviewed robotics and AI literature

Key standards:

* All factual statements must be traceable to credible sources
* Citation format: APA style
* Source types: minimum 60% peer-reviewed publications
* Plagiarism check: 0% tolerance before manuscript approval
* Writing clarity: Flesch-Kincaid grade 11–14

Constraints:

* Word count: 40,000–60,000 words
* Minimum 200 sources across all chapters
* Format: EPUB or PDF with embedded citations

Success criteria:

* All claims verified against authoritative sources
* Zero plagiarism detected
* Passes expert technical and fact-checking review
```

## Response snapshot

The constitution file at .specify/memory/constitution.md has been successfully updated with project-specific principles for the Physical AI & Humanoid Robotics book project. The updated constitution includes six core principles: Scientific Accuracy, Clarity for Technical Audience, Rigorous Verification, Citation Standards, Quality Standards, and Academic Integrity. It also includes Technical Standards, Development Workflow, and Governance sections that align with the project requirements.

## Outcome

- ✅ Impact: Updated project constitution with specific principles for Physical AI & Humanoid Robotics book
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md updated with project-specific content
- 🔁 Next prompts: Next steps might include creating feature specifications based on this constitution
- 🧠 Reflection: The constitution now properly reflects the academic and technical nature of the robotics book project

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin creating feature specifications based on the established constitution