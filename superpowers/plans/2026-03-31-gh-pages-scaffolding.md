# Learning Pathways GitHub Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scaffold a mobile-responsive GitHub Pages site using MkDocs Material to host AI Learning Paths.

**Architecture:** A static documentation site built from Markdown files in the `docs/` directory. Navigation is auto-generated based on the folder structure. Mobile responsiveness is handled natively by the Material for MkDocs theme with specific UI/UX enhancements.

**Tech Stack:** MkDocs, Material for MkDocs theme, GitHub Actions, Python.

---

### Task 1: Project Scaffolding & Initial Configuration

**Files:**
- Create: `mkdocs.yml`
- Create: `docs/index.md`
- Create: `docs/assets/custom.css`

- [ ] **Step 1: Create the base `mkdocs.yml` with Material theme and Mobile settings**

```yaml
site_name: Learning Pathways
site_url: https://ishitva.github.io/LeaningPathways/
theme:
  name: material
  font:
    text: Roboto
    code: Roboto Mono
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - navigation.expand
    - navigation.top
    - navigation.tracking
    - navigation.instant
    - search.suggest
    - search.highlight
    - content.code.copy
    - content.tooltips
  icon:
    logo: material/library-shelves

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - attr_list
  - md_in_html

extra_css:
  - assets/custom.css

nav:
  - Home: index.md
  - AI Engineering:
      - ai-engineering/
```

- [ ] **Step 2: Create the initial landing page `docs/index.md`**

```markdown
---
title: Welcome to Learning Pathways
---

# 📚 Learning Pathways

Welcome to a curated collection of deep-dive learning paths for AI and Software Engineering.

## 🚀 Featured Paths

<div class="grid cards" markdown>

-   :material-language-python: __LangChain Deep Dive__

    ---

    Master LangChain from first principles using Google Gemini.

    [:octicons-arrow-right-24: Start Learning](ai-engineering/langchain-path.md)

-   :material-robot: __AI Developer Mastery__

    ---

    A comprehensive roadmap for becoming a production-grade AI Engineer.

    [:octicons-arrow-right-24: Start Learning](ai-engineering/ai-mastery-plan.md)

</div>
```

- [ ] **Step 3: Create `docs/assets/custom.css` for mobile refinements**

```css
/* Ensure the grid cards look great on mobile */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
}

/* Mobile-specific padding adjustments */
@media screen and (max-width: 76.25em) {
  .md-content {
    padding-top: 0.5rem;
  }
}
```

- [ ] **Step 4: Verify structure and commit**

```bash
ls -R docs/
git add mkdocs.yml docs/index.md docs/assets/custom.css
git commit -m "chore: scaffold initial mkdocs structure and landing page"
```

---

### Task 2: Migrate & Format Existing Paths

**Files:**
- Move: `LangChain Learning Path.md` -> `docs/ai-engineering/langchain-path.md`
- Move: `AI Developer Mastery Plan.md` -> `docs/ai-engineering/ai-mastery-plan.md`

- [ ] **Step 1: Create directory and move LangChain path**

```bash
mkdir -p docs/ai-engineering/
mv "LangChain Learning Path.md" docs/ai-engineering/langchain-path.md
```

- [ ] **Step 2: Add Frontmatter to `langchain-path.md`**

```markdown
---
title: LangChain First Principles
description: A model-guided deep dive into the LangChain ecosystem.
---
```

- [ ] **Step 3: Move AI Mastery Plan and add Frontmatter**

```bash
mv "AI Developer Mastery Plan.md" docs/ai-engineering/ai-mastery-plan.md
```

```markdown
---
title: AI Developer Mastery Plan
description: Strategic roadmap for becoming a senior AI engineer.
---
```

- [ ] **Step 4: Commit migration**

```bash
git add docs/ai-engineering/
git commit -m "feat: migrate and format existing learning paths"
```

---

### Task 3: Setup GitHub Actions Deployment

**Files:**
- Create: `.github/workflows/deploy.yml`

- [ ] **Step 1: Create the deployment workflow**

```yaml
name: ci
on:
  push:
    branches:
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configure Python
        uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc +%V)" >> $GITHUB_ENV
      - uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs-material
      - run: mkdocs gh-deploy --force
```

- [ ] **Step 2: Commit workflow**

```bash
git add .github/workflows/deploy.yml
git commit -m "chore: add github actions deployment workflow"
```

---

### Task 4: Final Validation

- [ ] **Step 1: Verify all files are in the right place**

Run: `find docs/ -maxdepth 2`
Expected: 
```
docs/
docs/index.md
docs/assets
docs/ai-engineering
docs/ai-engineering/langchain-path.md
docs/ai-engineering/ai-mastery-plan.md
```

- [ ] **Step 2: Check for any broken links in `index.md` or `mkdocs.yml`**

- [ ] **Step 3: Final Commit**

```bash
git status
```
