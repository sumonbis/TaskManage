# TeamFlow Lite

TeamFlow Lite is a minimal Python/Flask task tracker starter app for demonstrating AI-assisted feature building in a Software Engineering class.

The app intentionally implements only the homepage and basic task creation. Students can extend it with features such as priority, due dates, task completion, search, filters, tests, refactoring, and a REST API.

## What is included

- Flask homepage
- Task creation form
- SQLite database
- Task listing
- Minimal validation for required task title
- Simple CSS

## Project structure

```text
teamflow_lite/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── styles.css
```

## Mac setup instructions

These instructions assume you are using macOS and running the commands from the VS Code terminal or the macOS Terminal app.

### 1. Open the project folder

Unzip the project folder and open it in VS Code.

Then open a terminal in VS Code:

```text
Terminal → New Terminal
```

Make sure you are inside the project folder:

```bash
cd teamflow_lite
```

### 2. Check that Python is installed

Run:

```bash
python3 --version
```

You should see a Python 3 version, such as:

```text
Python 3.11.x
```

If `python3` is not found, install Python from <https://www.python.org/downloads/> or through Homebrew.

### 3. Create a virtual environment

Run:

```bash
python3 -m venv .venv
```

This creates a local virtual environment folder named `.venv` inside the project.

### 4. Activate the virtual environment

Run:

```bash
source .venv/bin/activate
```

After activation, your terminal prompt should show something like:

```text
(.venv)
```

### 5. Install dependencies

Run:

```bash
pip install -r requirements.txt
```

This installs Flask and any other required packages listed in `requirements.txt`.

### 6. Run the app

Run:

```bash
python app.py
```

You should see output showing that the Flask development server is running.

Open this address in your browser:

```text
http://127.0.0.1:5000
```

### 7. Stop the app

To stop the app, go back to the terminal and press:

```text
Control + C
```

### 8. Deactivate the virtual environment

When you are done working, run:

```bash
deactivate
```

## Quick command summary for Mac

```bash
cd teamflow_lite
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Suggested student feature tasks

1. Add task completion status.
2. Add priority: Low, Medium, High.
3. Add due dates and highlight overdue tasks.
4. Add search and filtering.
5. Add edit and delete actions.
6. Add unit tests with pytest.
7. Refactor database logic into a separate module.
8. Add a JSON API endpoint.

## Example Copilot prompt for students

```text
Add a priority field to each task. Priority should be one of Low, Medium, or High. Update the task creation form, store the priority in SQLite, and show it on the homepage. Keep the code simple and explain any schema changes.
```
