# To-Do List - Task Management Application

[🇮🇷 نسخه فارسی](README.md)

---

## 📋 Project Description

A Python-based to-do list application for managing daily tasks with CSV data persistence. This command-line application follows Object-Oriented Programming (OOP) principles and provides an intuitive interface for task management.

---

## ✨ Features

- ✅ **Add Tasks**: Create new tasks with name, description, and priority level
- ✅ **Remove Tasks**: Delete tasks by name
- ✅ **View Tasks**: Display all tasks in the list
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
git clone https://github.com/Amirrezaghanaatiyan/todo-list.git
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
4. Save to CSV
5. Exit
```

---

## 📁 Project Structure

```
todo-list/
├── main.py              # Main application file
├── tasks.csv            # Task storage file (auto-created)
├── README.md            # Persian documentation
└── README_EN.md         # English documentation
```

---

## 🏗 Code Architecture

### `Task` Class
Represents a single task with properties:
- `name`: Task name
- `description`: Task description
- `priority`: Priority level

### `TODoList` Class
Manages the task list with methods:
- `add_task(task)`: Add a new task
- `remove_task(name)`: Remove a task by name
- `display_tasks()`: Show all tasks
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
mylist.add_task(task)

# Display all tasks
mylist.display_tasks()

# Save tasks
mylist.save_to_csv()
```

---

## 🎯 Future Enhancements

- [ ] Add deadline dates
- [ ] Add task completion status (Done/Not Done)
- [ ] Implement GUI interface
- [ ] Migrate to database (SQLite)
- [ ] Add advanced search and filter options

---

## 👤 Author

**Amirreza Ghanaatiyan**
- GitHub: [@Amirrezaghanaatiyan](https://github.com/Amirrezaghanaatiyan)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🔗 Links

- [Persian Version](README.md)
- [Repository](https://github.com/Amirrezaghanaatiyan/todo-list)

---

**Built with ❤️ by Amirreza Ghanaatiyan**
