# Python DSA Learning Lab

A documentation-first, beginner-friendly resource for learning data structures and algorithms with Python.

This repository is **not a data-structures package**. It teaches the ideas behind DSA and how to use Python's built-in types and standard-library modules in real programs.

## What you'll find

- Clear explanations of data structures, algorithms, invariants, and Big-O.
- Idiomatic Python examples using list, dict, set, collections, heapq, bisect, and other standard-library tools.
- Exercises with hints, test cases, and separate reference solutions.
- A browser-based Python playground powered by Pyodide. Code runs locally in your browser; no application server is required.
- Practical guidance on choosing the right tool rather than reimplementing one unnecessarily.

## Documentation

The documentation uses MkDocs and its built-in **Read the Docs** theme.

~~~bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
mkdocs serve
~~~

Open the local URL printed by MkDocs. Build a production copy with:

~~~bash
mkdocs build --strict
~~~

## Project principles

1. Use Python's built-ins and standard library for practical solutions.
2. Implement a data structure from scratch only when the exercise is specifically about understanding its internals.
3. Keep exercise code separate from reference solutions.
4. Explain complexity with assumptions and trade-offs, not just labels.
5. Keep the site fast, accessible, and free of unnecessary dependencies.

## Contributing

See CONTRIBUTING.md and the project issues.

## License

MIT. See LICENSE.