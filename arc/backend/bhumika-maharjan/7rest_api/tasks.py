import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, unquote
import json

class Task:
    TASKS_FILE = 'tasks.json'

    def __init__(self):
        self.task_list = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.TASKS_FILE):
            return []
        with open(self.TASKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_tasks(self):
        with open(self.TASKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.task_list, f, indent=4)

    def add_task(self, task):
        if task in self.task_list:
            return False
        self.task_list.append(task)
        self.save_tasks()
        return True

    def remove_task(self, task):
        if task not in self.task_list:
            return False
        self.task_list.remove(task)
        self.save_tasks()
        return True

    def get_tasks(self):
        return self.task_list


task_manager = Task()

class SimpleTaskHandler(BaseHTTPRequestHandler):

    def _send_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if self.path == '/tasks':
            tasks = task_manager.get_tasks()
            self._send_response(200, {"tasks": tasks})
        else:
            self._send_response(404, {"error": "Not found"})

    def do_POST(self):
        if self.path == '/tasks':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body)
                task = data.get('task')
                if not task:
                    self._send_response(400, {"error": "Missing 'task' field"})
                    return
                success = task_manager.add_task(task)
                if success:
                    self._send_response(201, {"message": "Task added", "tasks": task_manager.get_tasks()})
                else:
                    self._send_response(409, {"error": "Task already exists"})
            except json.JSONDecodeError:
                self._send_response(400, {"error": "Invalid JSON"})
        else:
            self._send_response(404, {"error": "Not found"})
            
    
    def do_PATCH(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path.startswith('/tasks/'):
            old_task = unquote(parsed_path.path.split('/tasks/')[1])
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body)
                new_task = data.get('new_task')
                if not new_task:
                    self._send_response(400, {"error": "Missing 'new_task' field"})
                    return
    
                if old_task not in task_manager.get_tasks():
                    self._send_response(404, {"error": f"Task '{old_task}' not found"})
                    return
    
                if new_task in task_manager.get_tasks():
                    self._send_response(409, {"error": f"Task '{new_task}' already exists"})
                    return
    
                # Perform rename
                task_manager.remove_task(old_task)
                task_manager.add_task(new_task)
                self._send_response(200, {"message": f"Task '{old_task}' renamed to '{new_task}'", "tasks": task_manager.get_tasks()})
    
            except json.JSONDecodeError:
                self._send_response(400, {"error": "Invalid JSON"})
        else:
            self._send_response(404, {"error": "Not found"})

    def do_DELETE(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path.startswith('/tasks/'):
            taskname = unquote(parsed_path.path.split('/tasks/')[1])
            success = task_manager.remove_task(taskname)
            if success:
                self._send_response(200, {"message": "Task removed", "tasks": task_manager.get_tasks()})
            else:
                self._send_response(404, {"error": f"Task '{taskname}' not found"})
        else:
            self._send_response(404, {"error": "Not found"})


def run(server_class=HTTPServer, handler_class=SimpleTaskHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Task server running on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()



