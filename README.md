# Algorithm Container Example

This repository serves as a template for containerizing a Python algorithm using Docker and setting up a robust CI/CD pipeline with GitHub Actions. It includes code quality tools, automated testing, and a workflow for publishing the container image to the GitHub Container Registry (GHCR).

## File Structure

Here is an overview of the key files in this project:

-   `generate_data.py`: A simple Python script that simulates an algorithm's execution by creating a timestamped output file.
-   `Dockerfile`: Instructions to build a Docker image containing the Python script and its environment.
-   `requirements.txt`: Lists the Python dependencies required for the application to run.
-   `requirements-dev.txt`: Lists the Python dependencies needed for development, such as linters and formatters.
-   `pyproject.toml`: Configuration file for Python development tools. In this project, it's used to configure `ruff`.
-   `.github/workflows/`: This directory contains the GitHub Actions workflows.
    -   `ci.yml`: A workflow that runs on every push and pull request to lint and format-check the Python code, ensuring code quality.
    -   `docker-publish.yml`: A workflow that automatically builds the Docker image and publishes it to the GitHub Container Registry (GHCR) whenever changes are pushed to the `main` branch.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   Python 3.11 or later
-   Docker

### Local Development

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/<your-username>/<your-repository>.git
    cd <your-repository>
    ```

2.  **Set up a virtual environment:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    # On Windows, use: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    This installs both application and development dependencies.
    ```sh
    pip install -r requirements.txt -r requirements-dev.txt
    ```

4.  **Run the script:**
    ```sh
    python generate_data.py
    ```

5.  **Lint and Format Code:**
    This project uses `ruff` for fast linting and formatting.
    ```sh
    # Check for linting errors and formatting issues
    ruff check .
    ruff format --check .

    # Automatically fix linting errors and reformat the code
    ruff check . --fix
    ruff format .
    ```

### Building and Running with Docker

1.  **Build the Docker image:**
    ```sh
    docker build -t my-algorithm .
    ```

2.  **Run the Docker container:**
    The script inside the container writes to `/app/output`. To see the output on your local machine, you can mount a local directory to this path.

    ```sh
    # Create an output directory on your host machine
    mkdir -p output

    # Run the container, mounting the local 'output' directory
    docker run --rm -v "$(pwd)/output:/app/output" my-algorithm
    ```
    After the container runs, you will find the `observation_result.txt` file inside your local `output` directory.

## CI/CD Pipeline

This project is configured with two GitHub Actions workflows.

### 1. Continuous Integration (`ci.yml`)

-   **Trigger**: Runs on every `push` and `pull_request` to any branch.
-   **Jobs**:
    -   `lint`: Installs Python and development dependencies.
    -   Runs `ruff check .` and `ruff format --check .` to ensure all code committed to the repository is well-formatted and free of linting errors.

### 2. Publish Docker Image (`docker-publish.yml`)

-   **Trigger**: Runs on every `push` to the `main` branch.
-   **Jobs**:
    -   `push_to_registry`: Logs into the GitHub Container Registry (GHCR), builds the Docker image, and pushes it.
-   **Result**: The container image will be available at `ghcr.io/<your-github-username>/<your-repository-name>`. For example: `ghcr.io/eoxhub/algorithm-container-example`.