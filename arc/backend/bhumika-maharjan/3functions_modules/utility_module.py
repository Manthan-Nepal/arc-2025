
def add_task(task_list,task):
    task_list.append(task)
    return task_list

def remove_task(task_list, task):
    if task in task_list:
        task_list.remove(task)
    return task_list


def list_tasks(task_list):
    for i, task in enumerate(task_list, 1):
        print(f"{i}. {task}")

