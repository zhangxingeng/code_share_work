# Setup GraphRAG without Poetry Step by Step


## initial setup
- create folder `msr_graphrag/` as root (`./`)
- `git clone https://github.com/microsoft/graphrag.git`
- Do conda in command prompt so we can use the `where` command later
    - `conda create -n graphrag python=3.11`
    - `conda activate graphrag`
    - `where python` find the one with `graphrag\python.exe` copy full path
    - in vscode set python.pythonPath to this full path. windows swap `\` with `\\`
    - `ctrl-shift-p` type `reload window` to make sure vscode see the update
    - Now `ctrl-~` open terminal will set conda env as default
    - `pyproject.toml` find `[tool.poe.tasks]` which contains all commands for different tasks defined my MSR
    - We wanna do the index one: `python -m graphrag index`
    - create requirements.txt at root (`./`)
    ```text
    typer
    devtools
    pydantic
    datashaper
    azure-identity
    azure-search-documents
    lancedb
    networkx
    tiktoken
    openai
    tenacity
    aiolimiter
    json-repair
    matplotlib
    pyyaml
    pyaml-env
    environs
    azure-storage-blob
    aiofiles
    nltk
    graspologic
    future
    ```
    - `pip install -r requirements.txt`
    - `python -m graphrag init --root ./ragtest` this will create a folder at root that we can setup a new project using graphrag Check [graphrag-doc-get-started](https://github.com/microsoft/graphrag/blob/main/docs/get_started.md) for details
    - find the `./ragtest/.env` file paste your openai key after `GRAPHRAG_API_KEY`
    - (Optional) Before indexing, if you want to visualize the graph after indexing, follow [Visualization Document](https://github.com/microsoft/graphrag/blob/main/docs/visualization_guide.md) to enable output `graphml` (standard visualization format)
    - Start indexing: `python -m graphrag index --root ./ragtest`
