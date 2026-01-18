import sys
import json
import os

# 定义存储文件名
DB_FILE = 'tasks.json'

# 初始化 JSON 文件
def init_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump([], f)

def load_tasks():
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DB_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# 核心功能：添加任务
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"任务已添加 (ID: {new_task['id']})")

# 简单的命令行解析
if __name__ == "__main__":
    init_db()
    args = sys.argv[1:]
    
    if not args:
        print("用法: python task_tracker.py [add/list/delete]")
    elif args[0] == "add":
        add_task(args[1])
    # 这里可以继续扩展 list, update, delete 等逻辑