from services.base_service import get

#fetch todos by userid
def get_todos_by_user(user_id):
    return get(f'todos?userId={user_id}')

#calculate the todo complete task from the list of todos provided
def completed_task_percentage(todos):
    total_tasks = len(todos)
    if total_tasks == 0:
        return 0
    
    #get the length of tasks for which completed is marked as true
    completed_task = len([task for task in todos if task['completed']])
    return (completed_task / total_tasks ) * 100