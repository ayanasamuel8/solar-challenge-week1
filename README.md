# Solar Challenge Week 1

This repository contains the code and resources for the Solar Challenge Week 1 project.

## Project Structure

```
├── .vscode/              # VS Code settings
├── .github/              # GitHub Actions workflows
├── src/                  # Source code
├── notebooks/            # Jupyter notebooks
├── tests/               # Unit tests
└── scripts/             # Utility scripts
```

## Setup Instructions

1. Clone the repository:

```bash
git clone <repository-url>
cd solar-challenge-week1
```

2. Create and activate a virtual environment:

For Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

For Unix/MacOS:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Development

- Code formatting is handled by `black`
- Linting is done with `pylint`
- Tests are written using `pytest`

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Run tests
4. Submit a pull request

## License

[MIT License](LICENSE)
