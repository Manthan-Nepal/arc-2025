from utility_module import *
# from utility_module import add_task
import utility_module
# from mathoperation import *

task_list = []

utility_module.add_task(task_list, "Buy groceries")
add_task(task_list, "Finish homework")
add_task(task_list, "Walk the dog")



print("\nCurrent Tasks:")
list_tasks(task_list)

remove_task(task_list, "Finish homework")

print("\nTasks after removal:")
list_tasks(task_list)



from contact_book import *
add_contact("bhumika", 12345)
view_contacts()