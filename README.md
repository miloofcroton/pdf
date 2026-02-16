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

Initiate or reset the database:

```bash
mise run setup
```

Run the services in parallel:

```bash
mise run server ::: worker ::: uploader
```

## Other handy commands

To run the main python server separately:

```bash
mise run server
```

To run the worker separately:

```bash
mise run worker
```

To run the uploader separately:

```bash
mise run worker
```
