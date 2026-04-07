from tasks.easy_task import grade_easy
from tasks.medium_task import grade_medium
from tasks.hard_task import grade_hard

def get_score(task_name, env):
    if task_name == "easy":
        return grade_easy(env)

    elif task_name == "medium":
        return grade_medium(env)

    elif task_name == "hard":
        return grade_hard(env)

    return 0.0