from environment import TollPlazaEnv
from models import Action
from tasks.easy_task import setup_easy
from tasks.medium_task import setup_medium
from tasks.hard_task import setup_hard
from tasks.graders import get_score

tasks = ["easy", "medium", "hard"]

for task in tasks:
    env = TollPlazaEnv()
    env.reset()

    if task == "easy":
        setup_easy(env)

    elif task == "medium":
        setup_medium(env)

    elif task == "hard":
        setup_hard(env)

    print(f"[START] task={task}")

    done = False

    while not done:
        if env.emergency_vehicle_waiting:
            action = Action(action_type="prioritize_emergency")

        elif env.queue_lengths[0] > 15:
            action = Action(action_type="redirect_traffic")

        else:
            action = Action(action_type="open_lane")

        obs, reward, done, info = env.step(action)

        print(
            f"[STEP] step={obs.step_number} "
            f"action={action.action_type} "
            f"reward={reward.score}"
        )

    score = get_score(task, env)

    print(f"[END] task={task} score={score}")