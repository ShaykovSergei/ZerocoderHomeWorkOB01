from datetime import date


class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None):
        new_task = {'description': description,'due_date': due_date if isinstance(due_date, date) else None,
            'completed': False
        }
        self.tasks.append(new_task)

    def mark_as_completed(self, task_description):
        for task in self.tasks:
            if task['description'] == task_description:
                task['completed'] = True
                break

    def get_active_tasks(self):
        return [task for task in self.tasks if not task['completed']]


# Пример использования:
if __name__ == "__main__":
    my_tasks = Task()

    # Добавляем новые задачи
    my_tasks.add_task("Написать статью", date.today())
    my_tasks.add_task("Посмотреть фильм")
    my_tasks.add_task("Прочитать книгу", date(2025, 8, 1))

    # Проверяем список активных задач
    print("Активные задачи:")
    active_tasks = my_tasks.get_active_tasks()
    for t in active_tasks:
        print(f"{t['description']} {'(' + str(t['due_date']) + ')' if t['due_date'] else ''}")

    # Отмечаем одну задачу как выполненную
    my_tasks.mark_as_completed("Посмотреть фильм")

    # Еще раз проверяем активные задачи
    print("\nАктивные задачи после завершения одной задачи:")
    active_tasks = my_tasks.get_active_tasks()
    for t in active_tasks:
        print(f"{t['description']} {'(' + str(t['due_date']) + ')' if t['due_date'] else ''}")