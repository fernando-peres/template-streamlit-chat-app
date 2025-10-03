# Template: Streamlit chat app

A ready-to-use Streamlit template for chat applications, perfect for fast prototyping.

> It us under construction. Soon it will be ready for use.

<img src="/static/img/uc.png" alt="Project Cover" style="width:100%; max-width:800px;" />


🧰 This template is built using the following tools:
- **Easy setup**: Fast environment provisioning with `uv`
- **Ruff**: Blazing-fast linter and formatter
- **MyPy**: Static type checking for Python
- **pre-commit**: Automated checks before every commit


For more details on Ruff and MyPy, see the Code Standards Guide [/readme/code-standards.md ](/readme/code-standards.md)

---

## 1. Installation

Step 1: Install dependencies

```bash
uv sync --all-groups
```

Step 2: Activate the virtual environment

```bash
source .venv/bin/activate
```

Step 3: Set up pre-commit hooks

```bash
pre-commit install  
```

## 2. Cooments about pre-commit

Check pre-commit hook status

```bash
pre-commit run --all-files
``` 

Whenever you run:

```bash
git commit -m "<message>"
```
💡 When you run `git commit`, ***pre-commit hooks*** will automatically execute and checks  across the entire codebase by sing mypy and ruff.


Happy coding! 🚀
