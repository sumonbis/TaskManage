# TeamFlow Lite Tutorial Prompts

**Tutorial:** Teaching Code-Generation Courses with GitHub Copilot: A Hands-On Tutorial Informed by Software Engineering Practice  
**App:** TeamFlow Lite — a minimal Python/Flask task-tracking web app  
**Tool:** VS Code + GitHub Copilot Chat

Use these prompts in order during the hands-on tutorial. The goal is not to blindly accept generated code. For each prompt, inspect Copilot's response, verify the changes, run the app/tests, and be ready to explain what changed.

---

## Prompt 1 — Codebase Exploration

Use this before making any code changes.

```text
Explore this TeamFlow Lite Flask project.

Do not modify code yet.

Return:
1. main files and their roles
2. how a new task is created
3. where tasks are stored
4. how tasks are displayed
5. what validation already exists
6. likely files to modify for task completion, priority, and validation improvements
```

### What to check

- Did Copilot identify the correct Flask routes?
- Did it correctly describe the database/storage layer?
- Did it identify the correct templates?
- Did it avoid modifying code?

---

## Prompt 2 — Feature Planning

Use this to create a small implementation roadmap.

```text
Create a minimal implementation plan for extending TeamFlow Lite.

Feature sequence:
1. task completion
2. task priority
3. validation improvements for whitespace-only and duplicate-looking task titles

Constraints:
- keep the app simple
- use the existing Flask structure
- avoid unnecessary frameworks
- identify database, backend, template, and CSS changes
- do not write code yet
```

### What to check

- Is the plan small enough for a tutorial?
- Does it separate backend, database, template, and CSS changes?
- Does it avoid unnecessary redesign?

---

## Prompt 3 — Task Completion Design

Use this before implementing task completion.

```text
Design the smallest change to add task completion to TeamFlow Lite.

Do not implement yet.

Return:
1. database/schema change
2. route change
3. template change
4. CSS change
5. tests or manual checks needed
6. possible regression risks
```

### What to check

- Does the design store completion state persistently?
- Does it preserve existing task creation?
- Does it avoid adding unnecessary features?

---

## Prompt 4 — Task Completion Implementation

Use this to implement the first feature.

```text
Implement task completion in the smallest safe way.

Requirements:
- add a completed/done field for each task
- show completed tasks differently in the UI
- add a button or form action to mark a task as completed
- keep existing task creation behavior working
- avoid unrelated changes

After editing, summarize exactly which files changed.
```

### Manual checks

- Create a new task.
- Mark the task as completed.
- Refresh the page.
- Confirm the completed state persists.
- Confirm completed tasks are visually distinguished.
- Confirm new task creation still works.

---

## Prompt 5 — Task Priority Planning

Use this before implementing priority.

```text
Plan the smallest change to add priority to TeamFlow Lite.

Requirements:
- priorities are Low, Medium, and High
- new tasks can be created with a priority
- existing tasks should still display safely
- priority should be visible in the task list

Do not implement yet.

Return:
1. files to modify
2. data model change
3. form/template change
4. validation rule
5. test/manual check plan
```

### What to check

- Does Copilot include a default priority for existing tasks?
- Does it mention validation for allowed values?
- Does it keep the UI simple?

---

## Prompt 6 — Task Priority Implementation

Use this to implement priority.

```text
Implement task priority in TeamFlow Lite.

Requirements:
- add priority choices: Low, Medium, High
- store priority with each task
- display priority in the task list
- use Medium as the default if appropriate
- validate that only allowed priority values are accepted
- avoid unrelated refactoring

After implementation, list changed files and how to manually test the feature.
```

### Manual checks

- Create a Low priority task.
- Create a Medium priority task.
- Create a High priority task.
- Refresh the page.
- Confirm each priority persists.
- Confirm the priority is displayed in the task list.
- Confirm invalid priority values are not accepted.

---

## Prompt 7 — Validation Analysis

Use this before fixing validation bugs.

```text
Analyze the current task title validation in TeamFlow Lite.

Do not modify code yet.

Find whether the app currently prevents:
1. empty titles
2. whitespace-only titles
3. duplicate-looking titles with different case or extra spaces

Return:
- current behavior
- likely bug locations
- smallest validation strategy
- tests or manual checks needed
```

### What to check

- Did Copilot distinguish empty titles from whitespace-only titles?
- Did it explain duplicate-looking titles clearly?
- Did it avoid changing code before analysis?

---

## Prompt 8 — Validation Fix

Use this to fix title validation and duplicate-looking tasks.

```text
Fix task title validation in TeamFlow Lite.

Requirements:
- reject empty titles
- reject whitespace-only titles
- normalize titles before checking duplicates
- prevent duplicate-looking tasks such as different case or extra spaces
- show a clear error message
- do not change unrelated behavior

After editing, explain the normalization rule used.
```

### Manual checks

Try creating each of the following tasks:

```text

```

```text
     
```

```text
Write report
```

```text
 write report 
```

```text
WRITE REPORT
```

```text
Write   report
```

Expected behavior: only one meaningful version of `Write report` should be accepted. Duplicate-looking versions should be rejected.

---

## Prompt 9 — Structured Debugging

Use this if a test or manual check fails.

```text
A validation test or manual check is failing.

Debug systematically.

Return:
1. likely root cause
2. exact file and code region
3. smallest fix
4. why the fix works
5. what regression test or manual check confirms it

Do not make unrelated edits.
```

### What to check

- Did Copilot identify the exact code region?
- Did it avoid broad rewrites?
- Did it explain why the fix works?
- Did you rerun the failing check?

---

## Prompt 10 — Small Safe Refactor

Use this only after the features work.

```text
Suggest one small safe refactor for TeamFlow Lite.

Constraints:
- preserve current behavior
- do not add new features
- keep the Flask app beginner-friendly
- explain why the refactor improves maintainability

Apply only one refactor.
```

### What to check

- Did the refactor preserve behavior?
- Is the code easier to understand?
- Did Copilot avoid adding new features?
- Did all manual checks still pass?

---

## Prompt 11 — Code Review

Use this to review the final changes.

```text
Review the recent TeamFlow Lite changes for correctness, maintainability, and possible bugs.

Focus on:
- task completion
- priority handling
- validation and duplicate detection
- database compatibility
- template logic

Return actionable comments only.
```

### What to check

- Which comments are useful?
- Which comments are vague?
- Did Copilot miss any issue?
- Did Copilot suggest unnecessary work?

---

## Prompt 12 — AI-Use Reflection

Use this at the end to prepare a short submission note.

```text
Help me write a short AI-use reflection for my TeamFlow Lite work.

Use this structure:
1. What I asked Copilot to help with
2. Which suggestions I accepted
3. Which suggestions I rejected or modified
4. How I verified the final behavior
5. What I understand well enough to explain without Copilot

Keep it concise and specific to this project.
```

---

# Final Manual Validation Checklist

After completing the tutorial, verify the following:

## Baseline behavior

- [ ] The app starts successfully.
- [ ] The homepage loads.
- [ ] A normal task can be created.
- [ ] Tasks are listed after creation.

## Task completion

- [ ] A task can be marked completed.
- [ ] Completed tasks are visually distinguished.
- [ ] Completion state persists after refresh.
- [ ] Existing task creation still works.

## Task priority

- [ ] A task can be created with Low priority.
- [ ] A task can be created with Medium priority.
- [ ] A task can be created with High priority.
- [ ] Priority is displayed in the task list.
- [ ] Priority persists after refresh.
- [ ] Invalid priority values are rejected or safely handled.

## Validation and duplicate prevention

- [ ] Empty task titles are rejected.
- [ ] Whitespace-only task titles are rejected.
- [ ] Duplicate-looking task titles are rejected.
- [ ] Case differences do not bypass duplicate detection.
- [ ] Extra spaces do not bypass duplicate detection.
- [ ] Error messages are clear.

## Code quality

- [ ] Changes are small and understandable.
- [ ] No unrelated features were added.
- [ ] The code can be explained by the student.
- [ ] Any AI-generated code was inspected and verified.

---

# Suggested Commit Sequence

Use small commits so the AI-assisted development process is visible.

```bash
git add .
git commit -m "Understand baseline TeamFlow Lite app"

git add .
git commit -m "Add task completion feature"

git add .
git commit -m "Add task priority field"

git add .
git commit -m "Improve task title validation"

git add .
git commit -m "Refactor and review TeamFlow Lite changes"
```

---

# Instructor Discussion Questions

1. Which Copilot suggestion was most useful?
2. Which suggestion required the most human correction?
3. What validation check caught the most important issue?
4. How would you grade this work in a software engineering course?
5. What evidence proves that the student understood the code?
