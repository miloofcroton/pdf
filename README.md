# PDF Tool

## First Time Setup

Install core dependencies:

```bash
mise activate
mise install
uv install
```

Create a virtual environment:

```bash
uv sync
source .venv/bin/activate
```


To initiate or reset the database:

```bash
mise run setup
```

To run the main python server:

```bash
mise run server
```


To run the worker:

```bash
mise run worker
```

To run the uploader:

```bash
mise run worker
```

To run Redis:

```bash
redis-server
```
