# Wireapps AI Program

A FastAPI-based REST API that provides AI-powered question answering using Anthropic's Claude API.

## Overview

This application exposes a simple API endpoint that accepts user questions and returns AI-generated answers using Claude (claude-sonnet-4-5 model). It's built with FastAPI for high performance and uses Pydantic for configuration management.

## Features

- **REST API**: Built with FastAPI framework
- **AI Integration**: Powered by Anthropic's Claude claude-sonnet-4-5 model
- **Environment Configuration**: Uses pydantic-settings for secure configuration management

## Prerequisites

- Python 3.11
- [PDM](https://pdm-project.org/) (Python Dependency Manager)
- Anthropic API key

## Installation

1. **Install PDM** (if not already installed):
   ```bash
   pip install pdm
   ```

2. **Create a virtual environment**:
   ```bash
   pdm venv create
   ```

3. **Activate the virtual environment**:
   ```bash
   eval $(pdm venv activate)
   ```

4. **Install project dependencies**:
   ```bash
   pdm install
   ```

5. **Deactivate the virtual environment** (when done):
   ```bash
   deactivate
   ```

## Configuration

Create a `.env` file in the project root with your Anthropic API key:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

## Running the Application

Start the development server with hot reload:

```bash
pdm run dev
```

The server will start at `http://127.0.0.1:8000`

## API Endpoints

### Health Check
- **GET** `/`
- Returns a simple hello world message

### Ask Question
- **GET** `/ask?question=<your_question>`
- Sends the question to Claude and returns the AI-generated answer

**Example:**
```bash
curl "http://127.0.0.1:8000/ask?question=What%20is%20Python"
```

## Project Structure

```
wireapps-ai-program/
├── app/
│   ├── main.py        # FastAPI application and routes
│   ├── llm.py         # Anthropic Claude integration
│   └── settings.py    # Configuration management
├── pyproject.toml     # Project dependencies and scripts
└── .env               # Environment variables (not committed)
```

## License

MIT
