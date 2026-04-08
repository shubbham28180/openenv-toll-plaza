import os
import requests
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("API_BASE_URL")
)
MODEL = os.getenv("MODEL_NAME", "gpt-4o")
ENV_URL = "http://localhost:8080"

def run():
    for task_id in [0, 1, 2]:
        print(f"[START] Task ID: {task_id}")
        
        reset_req = requests.post(f"{ENV_URL}/reset", params={"task_id": task_id})
        obs = reset_req.json()["view"]
        
        total_reward = 0
        
        for _ in range(3):
            action_cmd = "solve"
            step_req = requests.post(f"{ENV_URL}/step", json={"command": action_cmd})
            data = step_req.json()
            
            curr_reward = data["reward"]["value"]
            total_reward += curr_reward
            
            print(f"[STEP] Action: {action_cmd} | Reward: {curr_reward}")
            
            if data["done"]:
                break
                
        success = "True" if total_reward >= 1.0 else "False"
        print(f"[END] Total Reward: {total_reward} | Success: {success}")

if __name__ == "__main__":
    run()