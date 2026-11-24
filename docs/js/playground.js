(() => {
  const root = document.getElementById("python-playground");
  if (!root) return;

  const editor = document.getElementById("python-editor");
  const output = document.getElementById("python-output");
  const status = document.getElementById("python-status");
  const runButton = document.getElementById("python-run");
  const resetButton = document.getElementById("python-reset");
  const starterCode = editor.value;

  let runtimePromise = null;
  let running = false;

  function setStatus(message) {
    status.textContent = message;
  }

  function getRuntime() {
    if (!runtimePromise) {
      if (typeof window.loadPyodide !== "function") {
        throw new Error("Pyodide did not load. Check your network connection and reload.");
      }
      setStatus("Loading Python runtime…");
      runtimePromise = window.loadPyodide();
    }
    return runtimePromise;
  }

  async function runCode() {
    if (running) return;
    running = true;
    runButton.disabled = true;
    output.textContent = "";
    setStatus("Preparing Python…");

    try {
      const pyodide = await getRuntime();
      pyodide.setStdout({
        batched: (text) => {
          output.textContent += text;
        },
      });
      pyodide.setStderr({
        batched: (text) => {
          output.textContent += text;
        },
      });

      setStatus("Running…");
      await pyodide.runPythonAsync(editor.value);
      if (!output.textContent) output.textContent = "(No output)";
      setStatus("Finished.");
    } catch (error) {
      output.textContent += String(error);
      setStatus("Execution failed.");
    } finally {
      running = false;
      runButton.disabled = false;
    }
  }

  runButton.addEventListener("click", runCode);
  resetButton.addEventListener("click", () => {
    editor.value = starterCode;
    output.textContent = "Output will appear here.";
    setStatus("Editor reset.");
  });
})();