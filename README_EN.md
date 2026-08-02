# To-Do List - Task Management Application

[🇮🇷 نسخه فارسی](README.md) | [🇩🇪 Deutsche Version](README_DE.md)

---

## 📋 Project Description

A Python-based to-do list application for managing daily tasks with CSV data persistence. This command-line application follows Object-Oriented Programming (OOP) principles and provides an intuitive interface for task management.

---

## ✨ Features

- ✅ **Add Tasks**: Create new tasks with name, description, and priority level
- ✅ **Remove Tasks**: Delete tasks by name
- ✅ **View Tasks**: Display all tasks in the list
- ✅ **Set Deadline**: Assign deadline dates to tasks
- ✅ **Mark as Done**: Change task status (Completed/Not Completed)
- ✅ **Auto-Save**: Automatically save tasks to CSV file
- ✅ **Auto-Load**: Load previously saved tasks when starting the application
- ✅ **Priority Levels**: Set priority for each task (High/Medium/Low)

---

## 🛠 Installation & Usage

### Prerequisites
- Python 3.6 or higher

### Getting Started

1. **Clone the Repository**:
```bash
git clone https://github.com/amirrgn/todo-list.git
cd todo-list
```

2. **Run the Application**:
```bash
python main.py
```

3. **Use the Menu**:
```
===== TO DO LIST =====
1. Add Task
2. Remove Task
3. View All
4. Mark Task as Done
5. Save
6. Exit
```

---

## 📁 Project Structure

```
todo-list/
├── main.py              # Main application file
├── tasks.csv            # Task storage file (auto-created)
├── README.md            # Persian documentation
├── README_EN.md         # English documentation
└── README_DE.md         # German documentation
```

---

## 🏗 Code Architecture

### `Task` Class
Represents a single task with properties:
- `name`: Task name
- `description`: Task description
- `priority`: Priority level
- `status`: Task status (Completed/Not Completed)
- `deadline`: Deadline date

### `TODoList` Class
Manages the task list with methods:
- `add_task(task)`: Add a new task
- `remove_task(name)`: Remove a task by name
- `display_tasks()`: Show all tasks
- `mark_task_done(name)`: Change task status
- `save_to_csv()`: Save tasks to CSV file
- `load_from_csv()`: Load tasks from CSV file

---

## 📝 Usage Example

```python
# Create a to-do list
mylist = TODoList()

# Load previously saved tasks
mylist.load_from_csv()

# Add a new task
task = Task("Buy groceries", "For breakfast", "High")
task.deadline = "2025-01-15"
mylist.add_task(task)

# Display all tasks
mylist.display_tasks()

# Mark task as done
mylist.mark_task_done("Buy groceries")

# Save tasks
mylist.save_to_csv()
```

---

## 🎯 Future Enhancements

- [ ] Implement GUI interface
- [ ] Migrate to database (SQLite)
- [ ] Add advanced search and filter options
- [ ] Add reminder notifications
- [ ] Export to Excel

---

## 👤 Author

**Amirreza Ghanaatiyan**
- GitHub: [@amirrgn](https://github.com/amirrgn)

---

## 🔗 Links

- [Persian Version](README.md)
- [German Version](README_DE.md)
- [Repository](https://github.com/amirrgn/todo-list)

---

**Built with ❤️ by Amirreza Ghanaatiyan**
