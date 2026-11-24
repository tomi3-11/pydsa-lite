# Contributing to Python DSA Learning Lab

Thank you for helping make data structures and algorithms easier to understand. This repository is a learning resource and browser playground, not a reusable data-structures package.

## What makes a good contribution?

- Explain the problem before presenting code.
- Prefer Python built-ins and standard-library modules in practical examples.
- Label from-scratch implementations as learning exercises, not production recommendations.
- Explain invariants, time complexity, auxiliary space, and trade-offs.
- Include a worked example and meaningful edge cases.
- Keep exercises separate from hints and reference solutions.
- Keep the documentation beginner-friendly without being inaccurate.

## Development setup

~~~bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
mkdocs serve
~~~

Build the site with strict validation:

~~~bash
mkdocs build --strict
~~~

## Playground contributions

The playground runs client-side with Pyodide. Keep examples short and deterministic. Do not assume filesystem, network, subprocess, or native operating-system access. Explain when a standard-library module behaves differently in WebAssembly.

## Pull requests

Use a focused branch and pull request. Link the related issue, explain the learning objective, and include validation steps. Avoid adding plugins or JavaScript dependencies unless they solve a concrete problem.

## Review checklist

- [ ] The learning objective is clear.
- [ ] Python examples use built-ins or the standard library where practical.
- [ ] Complexity claims and assumptions are accurate.
- [ ] Exercises, hints, and solutions are clearly separated.
- [ ] Playground examples work in the browser.
- [ ] mkdocs build --strict passes.
