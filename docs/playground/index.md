# Python playground

Run small Python experiments without leaving the documentation. The playground uses Pyodide, a WebAssembly build of CPython that runs in your browser.

<div class="playground" id="python-playground">
  <div class="playground-toolbar">
    <span id="python-status" role="status">Runtime loads when you first run code.</span>
    <div>
      <button type="button" id="python-reset">Reset</button>
      <button type="button" id="python-run" class="primary">Run code</button>
    </div>
  </div>
  <label for="python-editor">Python editor</label>
  <textarea id="python-editor" spellcheck="false" autocapitalize="off" autocomplete="off">from collections import deque

tasks = deque(["learn", "practice"])
tasks.append("review")

while tasks:
    print(tasks.popleft())</textarea>
  <h2>Output</h2>
  <pre id="python-output" aria-live="polite">Output will appear here.</pre>
</div>

## What it can and cannot do

- Code runs locally in the browser; it is not sent to a project server.
- The initial runtime download can take a few seconds.
- The standard library is available, with some WebAssembly-specific limitations.
- Native extensions and operating-system features may not work exactly as they do on desktop Python.
- Do not paste secrets or sensitive data into a playground.

For full development, debugging, files, and test suites, use a local Python environment. The playground is for short experiments, not a replacement for your editor.