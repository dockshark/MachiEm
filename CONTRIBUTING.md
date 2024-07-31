
### Updated `CONTRIBUTING.md`
```markdown
# Contributing to MachiEm

We welcome contributions! Please follow these steps:

1. **Fork the repository**:
    - Click the "Fork" button on the top right of the repository page.
    - Clone your fork to your local machine:
    ```sh
    git clone https://github.com/your-username/MachiEm.git
    cd MachiEm
    ```

2. **Create a new branch**:
    ```sh
    git checkout -b feature-branch
    ```

3. **Make your changes**: Implement your feature or fix a bug.

4. **Commit your changes**:
    ```sh
    git add .
    git commit -m "Description of the changes"
    ```

5. **Push to your fork**:
    ```sh
    git push origin feature-branch
    ```

6. **Create a pull request**: Go to the repository on GitHub and click "New pull request".

## Code of Conduct
Please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) when contributing.

## Development Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/username/MachiEm.git
    cd MachiEm
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the tests** to ensure everything is working correctly:
    ```sh
    pytest
    ```

## Testing
- Ensure that all new features are covered by tests.
- Run the test suite to verify your changes:
    ```sh
    pytest
    ```

## Pull Request Process
1. Ensure your feature or fix is well documented.
2. Ensure all tests pass before submitting.
3. Describe your changes in detail in the pull request.
4. Wait for review and feedback from maintainers.
