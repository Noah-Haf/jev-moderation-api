# Jev Moderation API 

Built with FastAPI, using ruff for styling and linting. 

## Development 

1. ``uv venv`` 
2. Activate venv 
3. ``uv sync`` 
4. Copy ``.env.example`` -> ``.env`` and fill values as necessary. 
5. ``uv run fastpai dev``

Format with ``ruff format`` and lint with ``ruff check``.

Would recommend using the ``ty extension`` for type checking. 

## Contributing 

Ensure linters and formatters pass - make sure you have installed pre-commit: 

``pre-commit install`` 