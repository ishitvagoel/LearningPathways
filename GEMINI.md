# GEMINI.md — Project Instruction Manual

This directory is a **GitHub Pages** project for hosting a collection of **Learning Paths** and **Mastery Plans** focused on AI and Software Engineering. The site is built using the [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) theme for a premium, developer-focused UI/UX.

---

## 🏗️ Core Mandate: The GitHub Pages Structure

All documentation and learning paths MUST be stored in the `docs/` directory.

### 1. Directory Structure
Maintain the following structure for optimal site organization:
```text
.
├── docs/                     # Root for all site content
│   ├── index.md              # The Landing Page (Grid-based Navigation)
│   ├── ai-engineering/       # Topic-specific subdirectories
│   │   ├── langchain-path.md
│   │   └── ai-mastery-plan.md
│   └── assets/               # Shared site assets
│       ├── images/
│       └── custom.css        # Extra UI/UX overrides
├── mkdocs.yml                # Main site configuration (Nav, Theme, Plugins)
└── .github/workflows/        # Automated deployment to GitHub Pages
```

### 2. UI/UX & Navigation Standards
*   **List Navigation:** The sidebar MUST automatically reflect the folder structure in `docs/`. Ensure `mkdocs.yml` is configured for hierarchical, expandable sections.
*   **Dark Mode:** The site MUST support a high-contrast dark mode toggle in the header, with "Slate" or "Deep Indigo" as the primary palette.
*   **Frontmatter:** Every Markdown file MUST start with a YAML frontmatter block for metadata:
    ```yaml
    ---
    title: "Path Title"
    description: "Brief summary for the landing page grid"
    icon: material/brain # Optional: Specific icon for the landing page card
    tags:
      - AI
      - Python
    ---
    ```

---

## 📝 Learning Path Style: "First Principles Deep Dive"

When adding new Learning Paths (e.g., from Claude Opus), they MUST follow the established "First Principles" format to ensure consistency across the site.

### Required Sections:
1.  **Instructions for the Teaching Model:** A set of rules for an LLM (like Gemini or Claude) to act as a mentor.
2.  **Learner Profile:** Defines the target audience's background and knowledge gaps.
3.  **Phase-based Curriculum:** A sequential, phased approach starting from "Phase 0: Environment & First Contact."
4.  **🔨 Checkpoint Projects:** Mandatory hands-on tasks at the end of each phase for empirical validation of knowledge.
5.  **What NOT to Teach:** A list of deprecated patterns or outdated libraries to avoid.

---

## 🛠️ Maintenance Workflow

### 1. Adding a New Path
1.  Place the Markdown file in the appropriate `docs/` subdirectory.
2.  Update the YAML frontmatter at the top of the file.
3.  Verify the "First Principles" structure is intact.
4.  (Optional) Add a card for the new path to `docs/index.md`.

### 2. Local Preview
To preview the site before pushing to GitHub:
```bash
pip install mkdocs-material
mkdocs serve
```
Visit `http://127.0.0.1:8000` in your browser.

### 3. Deployment
The site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch via the `.github/workflows/deploy.yml` action.

---

## ⚠️ Safety & Compliance
*   **No Secrets:** Never commit API keys (e.g., `GOOGLE_API_KEY`) or environment variables to this repository.
*   **Static Assets only:** This is a static site. Do not include server-side code or sensitive database files.
