import csv


class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"کار: {self.name} | توضیحات: {self.description} | اولویت: {self.priority}"


class TODoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print("تسک حذف شد.")
                return

        print("تسکی با این نام پیدا نشد.")

    def get_tasks(self):
        return self.tasks

    def display_tasks(self):
        if not self.tasks:
            print("هیچ کاری در لیست وجود ندارد.")
        else:
            for task in self.tasks:
                print(task)

    def save_to_csv(self, filename="tasks.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["Name", "Description", "Priority"])

            for task in self.tasks:
                writer.writerow([
                    task.name,
                    task.description,
                    task.priority
                ])

        print("اطلاعات با موفقیت ذخیره شد.")

    def load_from_csv(self, filename="tasks.csv"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                self.tasks = []

                for row in reader:
                    task = Task(
                        row["Name"],
                        row["Description"],
                        row["Priority"]
                    )

                    self.tasks.append(task)

            print("اطلاعات از فایل بارگذاری شد.")

        except FileNotFoundError:
            print("فایل CSV پیدا نشد. لیست جدید ساخته شد.")


def main():
    mylist = TODoList()
    mylist.load_from_csv()

    while True:
        print("\n===== TO DO LIST =====")
        print("1. افزودن تسک")
        print("2. حذف تسک")
        print("3. مشاهده همه")
        print("4. ذخیره در CSV")
        print("5. خروج")

        choose = input("انتخاب خود را وارد کنید: ")

        if choose == "1":
            name = input("نام تسک: ")
            description = input("توضیحات: ")
            priority = input("اولویت (بالا/متوسط/پایین): ")

            task = Task(name, description, priority)
            mylist.add_task(task)

            print("✅ تسک اضافه شد.")

        elif choose == "2":
            name = input("نام تسکی که می‌خواهید حذف شود: ")
            mylist.remove_task(name)

        elif choose == "3":
            mylist.display_tasks()

        elif choose == "4":
            mylist.save_to_csv()

        elif choose == "5":
            mylist.save_to_csv()
            print("خروج از برنامه...")
            break

        else:
            print("گزینه نامعتبر است.")


if __name__ == "__main__":
    main()
