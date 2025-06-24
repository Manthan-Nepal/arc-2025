study_tasks = {'read textbook', 'complete assignment', 'attend lecture', 'review notes'}
daily_tasks = {'attend college', 'cook', 'review notes', 'complete assignment'}

common_tasks = study_tasks.intersection(daily_tasks)
# Display common tasks between study and daily tasks

all_tasks = study_tasks.union(daily_tasks)
print("All tasks are:")


if common_tasks:
    print("Common tasks are:")
    
    for task in common_tasks:
        print(task)
else:
    print("No common tasks found.")
