# Contributing to pydsa-lite

Thank you for considering a contribution. This project helps beginners understand data structures, algorithms, and complexity. Clarity is more important than cleverness.

## Before you start

1. Read the relevant documentation and implementation.
2. Check open issues to avoid duplicate work.
3. For substantial changes, discuss the idea in an issue first.
4. Keep each pull request focused on one logical change.

## Development setup

Clone the repository, create and activate a virtual environment, then install the development extras with: python -m pip install -e ".[dev]".

## Branch and pull request workflow

Use descriptive branches such as feat/stack-queue, feat/binary-search, docs/linked-lists, or fix/empty-graph-traversal. Open pull requests against main, explain the reason for the change, link the related issue, and describe how you tested it.

## Code expectations

- Use type hints and clear, beginner-friendly names.
- Add docstrings to public classes and functions.
- Explain non-obvious steps without narrating every line.
- Validate invalid inputs consistently and document behavior.
- State important invariants and time/space complexity.
- Keep core code dependent on the Python standard library only.
- Include runnable examples and tests for new public behavior.

## Run checks

Run the test suite with python -m pytest. For documentation changes, also run mkdocs build --strict.

## Pull request checklist

- [ ] The change addresses one focused issue.
- [ ] Tests cover normal and relevant edge cases.
- [ ] Documentation and examples are updated.
- [ ] Complexity claims are accurate.
- [ ] The full test suite passes.
- [ ] No unnecessary runtime dependencies were added.
