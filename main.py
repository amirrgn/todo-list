import csv

class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
        self.status = "انجام نشده"

    def __str__(self):
        return f"کار: {self.name} | توضیحات: {self.description} | اولویت: {self.priority} | وضعیت: {self.status}"

class TODoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, name):
        self.tasks = [task for task in self.tasks if task.name != name]
        print("تسک حذف شد.")

    def display_tasks(self):
        if not self.tasks:
            print("هیچ کاری در لیست وجود ندارد.")
        else:
            for task in self.tasks:
                print(task)
    def mark_task_done(self, name):
        for task in self.tasks:
            if task.name == name:
                task.status = "انجام شده"
                return
        print("تسک پیدا نشد.")

    def save_to_csv(self, filename="tasks.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Description", "Priority", "Status"])
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority, task.status])
        print("ذخیره شد.")

    def load_from_csv(self, filename="tasks.csv"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.tasks = []
                for row in reader:
                    task = Task(row["Name"], row["Description"], row["Priority"])
                    task.status = row["Status"]
                    self.tasks.append(task)
            print("بارگذاری شد.")
        except FileNotFoundError:
            print("لیست جدید ساخته شد.")

def main():
    mylist = TODoList()
    mylist.load_from_csv()

    while True:
        print("\n===== TO DO LIST =====")
        print("1. افزودن تسک")
        print("2. حذف تسک")
        print("3. مشاهده همه")
        print("4. تغییر وضعیت تسک")
        print("5. ذخیره")
        print("6. خروج")

        choose = input("انتخاب: ")

        if choose == "1":
            name = input("نام: ")
            description = input("توضیحات: ")
            priority = input("اولویت (بالا/متوسط/پایین): ")
            task = Task(name, description, priority)
            mylist.add_task(task)
            print("✅ اضافه شد.")

        elif choose == "2":
            name = input("نام تسک: ")
            mylist.remove_task(name)

        elif choose == "3":
            mylist.display_tasks()

        elif choose == "4":
            name = input("نام تسک: ")
            sure = input("ایا مطمین هستید میخواهید این تسک را پاک کنید ؟(y/n)")
            if sure == "y":
                mylist.mark_task_done(name)
            else:
                print("وضعیت تغییر نکرد/n" \
                "گذینه دیگری انتخاب کنید")
                return
        

        elif choose == "5":
            mylist.save_to_csv()
            break
        # elif

        else:
            print("گزینه نامعتبر.")

if __name__ == "__main__":
    main()