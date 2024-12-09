
# Vscode Configs for python project

## Settings.json

```json
{
    "python.pythonPath": "C:\\Users\\shane\\miniconda3\\envs\\django\\python.exe",
    "python.defaultInterpreterPath": "C:\\Users\\shane\\miniconda3\\envs\\django\\python.exe",
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.autoImportCompletions": true,
    "ruff.enable": true,
    "ruff.format.args": ["--line-length=200"],
    "ruff.lint.args": ["--line-length=200"],
    "notebook.formatOnSave.enabled": true,
    "notebook.codeActionsOnSave": {
        "notebook.source.fixAll": "explicit",
        "notebook.source.organizeImports": "explicit"
    },
    "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter":"charliermarsh.ruff",
        "editor.codeActionsOnSave": {
            "source.fixAll.ruff":"explicit",
            "source.organizeImports.ruff":"explicit"
        },
        "editor.rulers": [200],
        "editor.tabSize": 4
    },
    "files.associations": {
        "*.html": "html",
        "*.js": "javascript",
        "*.css": "css"
    },
    "emmet.includeLanguages": {
        "django-html": "html"
    }
}
```

## pyproject.toml

```toml
[tool.ruff]
# Same as Black.
line-length = 200
indent-width = 4

# Assume Python 3.11
target-version = "py311"

[tool.ruff.lint]
# Enable Pyflakes (`F`) and a subset of the pycodestyle (`E`)
select = ["E", "F", "I", "DJ"]
ignore = []

# Allow fix for all enabled rules (when `--fix`) is provided.
fixable = ["ALL"]
unfixable = []

# Django plugin
extend-select = ["DJ"]

[tool.ruff.format]
# Use single quotes for strings.
quote-style = "double"

# Indent with spaces, rather than tabs.
indent-style = "space"

# Respect magic trailing commas.
skip-magic-trailing-comma = false

# Automatically detect the appropriate line ending.
line-ending = "auto" 
```
