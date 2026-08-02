# To-Do List - Aufgabenverwaltungsanwendung

[🇮🇷 نسخه فارسی](README.md) | [🇬🇧 English Version](README_EN.md)

---

## 📋 Projektbeschreibung

Eine Python-basierte To-Do-Listen-Anwendung zur Verwaltung täglicher Aufgaben mit CSV-Datenspeicherung. Diese Befehlszeilenschnittstellen-Anwendung folgt den Prinzipien der objektorientierten Programmierung (OOP) und bietet eine intuitive Schnittstelle für die Aufgabenverwaltung.

---

## ✨ Funktionen

- ✅ **Aufgaben hinzufügen**: Erstellen Sie neue Aufgaben mit Name, Beschreibung und Prioritätsstufe
- ✅ **Aufgaben löschen**: Löschen Sie Aufgaben nach Name
- ✅ **Aufgaben anzeigen**: Zeigen Sie alle Aufgaben in der Liste an
- ✅ **Frist festlegen**: Weisen Sie Aufgaben Fälligkeitstermine zu
- ✅ **Status ändern**: Ändern Sie den Aufgabenstatus (Erledigt/Nicht erledigt)
- ✅ **Auto-Speichern**: Speichern Sie Aufgaben automatisch in einer CSV-Datei
- ✅ **Auto-Laden**: Laden Sie zuvor gespeicherte Aufgaben beim Start der Anwendung
- ✅ **Prioritätsstufen**: Legen Sie die Priorität für jede Aufgabe fest (Hoch/Mittel/Niedrig)

---

## 🛠 Installation und Verwendung

### Anforderungen
- Python 3.6 oder höher

### Erste Schritte

1. **Repository klonen**:
```bash
git clone https://github.com/amirrgn/todo-list.git
cd todo-list
```

2. **Anwendung ausführen**:
```bash
python main.py
```

3. **Menü verwenden**:
```
===== TO DO LIST =====
1. Aufgabe hinzufügen
2. Aufgabe löschen
3. Alle anzeigen
4. Aufgabe als erledigt markieren
5. Speichern
6. Beenden
```

---

## 📁 Projektstruktur

```
todo-list/
├── main.py              # Hauptanwendungsdatei
├── tasks.csv            # Aufgabenspeicherdatei (wird automatisch erstellt)
├── README.md            # Persische Dokumentation
├── README_EN.md         # Englische Dokumentation
└── README_DE.md         # Deutsche Dokumentation
```

---

## 🏗 Code-Architektur

### Klasse `Task`
Stellt eine einzelne Aufgabe mit Eigenschaften dar:
- `name`: Aufgabenname
- `description`: Aufgabenbeschreibung
- `priority`: Prioritätsstufe
- `status`: Aufgabenstatus (Erledigt/Nicht erledigt)
- `deadline`: Fälligkeitsdatum

### Klasse `TODoList`
Verwaltet die Aufgabenliste mit Methoden:
- `add_task(task)`: Neue Aufgabe hinzufügen
- `remove_task(name)`: Aufgabe nach Name löschen
- `display_tasks()`: Alle Aufgaben anzeigen
- `mark_task_done(name)`: Aufgabenstatus ändern
- `save_to_csv()`: Aufgaben in CSV-Datei speichern
- `load_from_csv()`: Aufgaben aus CSV-Datei laden

---

## 📝 Verwendungsbeispiel

```python
# To-Do-Liste erstellen
mylist = TODoList()

# Zuvor gespeicherte Aufgaben laden
mylist.load_from_csv()

# Neue Aufgabe hinzufügen
task = Task("Lebensmittel kaufen", "Zum Frühstück", "Hoch")
task.deadline = "2025-01-15"
mylist.add_task(task)

# Alle Aufgaben anzeigen
mylist.display_tasks()

# Aufgabe als erledigt markieren
mylist.mark_task_done("Lebensmittel kaufen")

# Aufgaben speichern
mylist.save_to_csv()
```

---

## 🎯 Zukünftige Verbesserungen

- [ ] Implementierung einer GUI-Schnittstelle
- [ ] Migration zu einer Datenbank (SQLite)
- [ ] Erweiterte Such- und Filteroptionen
- [ ] Erinnerungsmeldungen hinzufügen
- [ ] Nach Excel exportieren

---

## 👤 Autor

**Amirreza Ghanaatiyan**
- GitHub: [@amirrgn](https://github.com/amirrgn)

---

## 🔗 Links

- [Persische Version](README.md)
- [Englische Version](README_EN.md)
- [Repository](https://github.com/amirrgn/todo-list)

---

**Erstellt mit ❤️ von Amirreza Ghanaatiyan**
