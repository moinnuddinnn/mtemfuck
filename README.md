# linuxtermi

Small collection of Python terminal-related scripts.

Files
- `py_shell.py` — a tiny interactive Python shell (uses standard library only).
- `py_vte_terminal.py` — GTK+ / VTE based terminal UI (requires PyGObject and VTE GIR bindings).

Prerequisites
- Python 3.8+
- On Debian/Ubuntu you likely need system packages:

  ```bash
  sudo apt update && sudo apt install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-vte-2.91
  ```

Install Python dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python3 py_shell.py
python3 py_vte_terminal.py
```

Notes
- The `LICENSE` file is MIT with a placeholder author — replace `Your Name` as appropriate.
- `requirements.txt` lists `PyGObject` which may require additional system libraries (see prerequisites).
