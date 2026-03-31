# Design Spec: Learning Pathways GitHub Pages

**Date:** 2026-03-31
**Status:** Draft
**Topic:** Documentation Hub for AI-powered Learning Paths

---

## 1. Overview
The goal is to transform a collection of Markdown-based Learning Paths into a high-end, visually stunning GitHub Pages site. The site will serve as a central hub for various topics (starting with LangChain), offering a premium "Material Design" experience for learners.

## 2. Architecture & Tech Stack
*   **Engine:** [MkDocs](https://www.mkdocs.org/)
*   **Theme:** [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
*   **Hosting:** GitHub Pages
*   **Automation:** GitHub Actions (`.github/workflows/deploy.yml`)

## 3. UI/UX Design

### 3.1 List Navigation & Structure
*   **Side Navigation:** A sticky, hierarchical sidebar that automatically reflects the `docs/` folder structure.
*   **Landing Page (`index.md`):** A grid-based "Portal" view where each Learning Path is presented as a card with an icon, title, and short description.
*   **Search:** Integrated instant search bar in the header.

### 3.2 Visuals & Dark Mode
*   **Dark Mode:** A manual toggle in the header, with "Automatic" system preference support.
*   **Primary Palette:** Deep Indigo/Slate for a professional developer feel.
*   **Typography:** Inter/Roboto for body text; Fira Code for code blocks.
*   **Interactive Elements:** 
    *   One-click code copy buttons.
    *   Scroll-to-top button.
    *   Navigation progress bar (top of screen).
    *   Admonitions (Notes, Tips, Warnings) for pedagogical highlights.

## 4. Maintenance Workflow

### 4.1 Path Ingestion
1.  **Placement:** New Markdown files from Claude Opus are placed in `docs/`.
2.  **Metadata:** Every file receives YAML frontmatter (Title, Description, Tags).
3.  **Style Check:** Gemini CLI ensures new paths adhere to the "First Principles Deep Dive" format (Learner Profile, Teaching Rules, Checkpoint Projects).

### 4.2 Build & Deploy
*   **Automatic Deploy:** Pushing to the `main` branch triggers a GitHub Action to rebuild the site.
*   **Local Preview:** `mkdocs serve` for local validation.

## 5. Directory Structure
```text
.
├── docs/
│   ├── index.md (Home)
│   ├── ai-engineering/
│   │   ├── langchain-deep-dive.md
│   │   └── ai-developer-mastery-plan.md
│   └── assets/
│       └── images/
├── mkdocs.yml (Config)
├── GEMINI.md (Instruction Manual)
└── .github/
    └── workflows/
        └── deploy.yml
```

## 6. Success Criteria
*   [ ] Site is accessible via GitHub Pages URL.
*   [ ] Dark Mode toggle works flawlessly.
*   [ ] Navigation sidebar is correctly auto-generated.
*   [ ] Search results are accurate and fast.
