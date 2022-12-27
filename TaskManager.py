class Task:
    def __init__(self, id, name, description):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__status = 'in progress'
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_descr(self):
        return self.__description

    def change_status(self, new_status):
        self.__status = new_status


class Subtask(Task):
    # have comlex task id
    def __init__(self, task, parent_id):
        super().__init__(task.get_id(), task.get_name(), task.get_descr())
        self.parent_id = parent_id




class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self, task):
        super().__init__(task.get_id(), task.get_name(), task.get_descr())
        self.subtasks = []

    def new_subtask(self, subtask):
        self.subtasks.append(subtask)

class TaskManager:
    id_series = 0

    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
        self.complex_tasks = {}

    def __get_and_increment_id(self):

        next_id_value = self.id_series
        self.id_series += 1

        return next_id_value

    def create_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_task = Task(current_id, name, description)

        self.tasks[current_id] = new_task

        return new_task

    def create_subtask(self, subtask, parent_id):

        if parent_id not in self.complex_tasks:
            self.create_complex_task(self.tasks[parent_id])

        new_subtask = Subtask(subtask, parent_id)
        self.subtasks[new_subtask.get_id()] = new_subtask


        self.tasks.pop(subtask.get_id())
        self.complex_tasks[parent_id].subtasks.append(new_subtask)

        return new_subtask

    def create_complex_task(self, complex_task):
        new_complex_task = ComplexTask(complex_task)

        self.tasks.pop(complex_task.get_id())
        self.complex_tasks[complex_task.get_id()] = new_complex_task

        return new_complex_task

    def get_tasks(self):
        return self.tasks.values()

    def get_subtasks(self):
        return self.subtasks.values()

    def get_complex_tasks(self):
        return self.tasks.values()

    def get_tasks_by_id(self, id):
        try:
            return self.tasks[id]
        except:
            print('There is no task with such id')


    def get_subtasks_by_id(self, id):
        try:
            return self.subtasks[id]
        except:
            print('There is no task with such id')

    def get_complex_tasks_by_id(self, id):
        try:
            return self.complex_tasks[id]
        except:
            print('There is no task with such id')
    def remove_tasks(self):
        self.tasks = {}

    def remove_subtasks(self):
        self.subtasks = {}
        for el in self.complex_tasks:
            self.complex_tasks[el].subtasks = []
        self.tasks.update(self.complex_tasks)
        self.complex_tasks = {}

    def remove_complex_tasks(self):
        self.complex_tasks = {}
        self.subtasks = {}

    def remove_task_by_id(self, id):
        self.tasks.pop(id)

    def remove_subtask_by_id(self, id):
        self.complex_tasks[self.subtasks[id].parent_id].subtasks.remove(self.subtasks[id])
        self.subtasks.pop(id)

    def remove_complex_task_by_id(self, id):
        for el in self.complex_tasks[id].subtasks:
            self.subtasks.pop(el.get_id())
        self.complex_tasks.pop(id)

    def update_status(self, task, new_status):
        task.change_status(new_status)




