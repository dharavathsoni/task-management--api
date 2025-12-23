# Task Management API
# A RESTful API for managing tasks with SQLite database

import sqlite3
import json
from datetime import datetime
from typing import List, Optional, Dict, Any
from enum import Enum


class TaskStatus(Enum):
    """Enum for task status"""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskPriority(Enum):
    """Enum for task priority"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class DatabaseManager:
    """Handles all database operations"""

    def __init__(self, db_name: str = "tasks.db"):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        """Initialize the database with required tables"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'todo',
                    priority TEXT DEFAULT 'medium',
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    due_date TEXT
                )
            """)
            conn.commit()

    def execute_query(self, query: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """Execute a SELECT query and return results as list of dicts"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]

    def execute_update(self, query: str, params: tuple = ()) -> int:
        """Execute an INSERT/UPDATE/DELETE query and return affected rows"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid if cursor.lastrowid else cursor.rowcount


class Task:
    """Task model representing a single task"""

    def __init__(self, title: str, description: str = "",
                 status: str = TaskStatus.TODO.value,
                 priority: str = TaskPriority.MEDIUM.value,
                 due_date: Optional[str] = None,
                 task_id: Optional[int] = None):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        self.due_date = due_date

    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'due_date': self.due_date
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Task':
        """Create task from dictionary"""
        task = Task(
            title=data['title'],
            description=data.get('description', ''),
            status=data.get('status', TaskStatus.TODO.value),
            priority=data.get('priority', TaskPriority.MEDIUM.value),
            due_date=data.get('due_date'),
            task_id=data.get('id')
        )
        if 'created_at' in data:
            task.created_at = data['created_at']
        if 'updated_at' in data:
            task.updated_at = data['updated_at']
        return task


class TaskService:
    """Service layer for task operations"""

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def create_task(self, task: Task) -> int:
        """Create a new task and return its ID"""
        query = """
            INSERT INTO tasks (title, description, status, priority, created_at, updated_at, due_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (task.title, task.description, task.status, task.priority,
                  task.created_at, task.updated_at, task.due_date)
        return self.db.execute_update(query, params)

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by ID"""
        query = "SELECT * FROM tasks WHERE id = ?"
        results = self.db.execute_query(query, (task_id,))
        return Task.from_dict(results[0]) if results else None

    def get_all_tasks(self, status: Optional[str] = None,
                      priority: Optional[str] = None) -> List[Task]:
        """Retrieve all tasks with optional filtering"""
        query = "SELECT * FROM tasks WHERE 1=1"
        params = []

        if status:
            query += " AND status = ?"
            params.append(status)
        if priority:
            query += " AND priority = ?"
            params.append(priority)

        query += " ORDER BY created_at DESC"
        results = self.db.execute_query(query, tuple(params))
        return [Task.from_dict(row) for row in results]

    def update_task(self, task_id: int, updates: Dict[str, Any]) -> bool:
        """Update a task with given values"""
        if not self.get_task(task_id):
            return False

        updates['updated_at'] = datetime.now().isoformat()
        set_clause = ", ".join([f"{k} = ?" for k in updates.keys()])
        query = f"UPDATE tasks SET {set_clause} WHERE id = ?"
        params = tuple(list(updates.values()) + [task_id])

        self.db.execute_update(query, params)
        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID"""
        query = "DELETE FROM tasks WHERE id = ?"
        rows_affected = self.db.execute_update(query, (task_id,))
        return rows_affected > 0

    def get_statistics(self) -> Dict[str, Any]:
        """Get task statistics"""
        all_tasks = self.get_all_tasks()
        return {
            'total': len(all_tasks),
            'by_status': {
                status.value: len([t for t in all_tasks if t.status == status.value])
                for status in TaskStatus
            },
            'by_priority': {
                priority.value: len([t for t in all_tasks if t.priority == priority.value])
                for priority in TaskPriority
            }
        }


class TaskAPI:
    """API interface for task management"""

    def __init__(self):
        self.db_manager = DatabaseManager()
        self.task_service = TaskService(self.db_manager)

    def handle_request(self, method: str, endpoint: str,
                       data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Handle API requests
        Methods: GET, POST, PUT, DELETE
        Endpoints: /tasks, /tasks/{id}, /tasks/stats
        """
        try:
            if endpoint == "/tasks" and method == "POST":
                return self._create_task(data)
            elif endpoint == "/tasks" and method == "GET":
                return self._get_all_tasks(data)
            elif endpoint.startswith("/tasks/") and method == "GET":
                task_id = int(endpoint.split("/")[-1])
                return self._get_task(task_id)
            elif endpoint.startswith("/tasks/") and method == "PUT":
                task_id = int(endpoint.split("/")[-1])
                return self._update_task(task_id, data)
            elif endpoint.startswith("/tasks/") and method == "DELETE":
                task_id = int(endpoint.split("/")[-1])
                return self._delete_task(task_id)
            elif endpoint == "/tasks/stats" and method == "GET":
                return self._get_statistics()
            else:
                return {"error": "Invalid endpoint or method", "status": 404}
        except Exception as e:
            return {"error": str(e), "status": 500}

    def _create_task(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new task"""
        if not data or 'title' not in data:
            return {"error": "Title is required", "status": 400}

        task = Task(
            title=data['title'],
            description=data.get('description', ''),
            status=data.get('status', TaskStatus.TODO.value),
            priority=data.get('priority', TaskPriority.MEDIUM.value),
            due_date=data.get('due_date')
        )
        task_id = self.task_service.create_task(task)
        task.id = task_id
        return {"data": task.to_dict(), "status": 201}

    def _get_task(self, task_id: int) -> Dict[str, Any]:
        """Get a single task"""
        task = self.task_service.get_task(task_id)
        if not task:
            return {"error": "Task not found", "status": 404}
        return {"data": task.to_dict(), "status": 200}

    def _get_all_tasks(self, filters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Get all tasks with optional filters"""
        status = filters.get('status') if filters else None
        priority = filters.get('priority') if filters else None
        tasks = self.task_service.get_all_tasks(status, priority)
        return {"data": [task.to_dict() for task in tasks], "status": 200}

    def _update_task(self, task_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update a task"""
        if not data:
            return {"error": "No update data provided", "status": 400}

        success = self.task_service.update_task(task_id, data)
        if not success:
            return {"error": "Task not found", "status": 404}

        updated_task = self.task_service.get_task(task_id)
        return {"data": updated_task.to_dict(), "status": 200}

    def _delete_task(self, task_id: int) -> Dict[str, Any]:
        """Delete a task"""
        success = self.task_service.delete_task(task_id)
        if not success:
            return {"error": "Task not found", "status": 404}
        return {"message": "Task deleted successfully", "status": 200}

    def _get_statistics(self) -> Dict[str, Any]:
        """Get task statistics"""
        stats = self.task_service.get_statistics()
        return {"data": stats, "status": 200}


# Example usage and testing
if __name__ == "__main__":
    api = TaskAPI()

    # Create tasks
    print("Creating tasks...")
    response1 = api.handle_request("POST", "/tasks", {
        "title": "Implement user authentication",
        "description": "Add JWT-based auth system",
        "priority": "high",
        "due_date": "2025-01-15"
    })
    print(json.dumps(response1, indent=2))

    response2 = api.handle_request("POST", "/tasks", {
        "title": "Write unit tests",
        "description": "Add test coverage for API endpoints",
        "priority": "medium"
    })
    print(json.dumps(response2, indent=2))

    response3 = api.handle_request("POST", "/tasks", {
        "title": "Update documentation",
        "priority": "low"
    })
    print(json.dumps(response3, indent=2))

    # Get all tasks
    print("\nFetching all tasks...")
    response = api.handle_request("GET", "/tasks")
    print(json.dumps(response, indent=2))

    # Update a task
    print("\nUpdating task status...")
    response = api.handle_request("PUT", "/tasks/1", {
        "status": "in_progress"
    })
    print(json.dumps(response, indent=2))

    # Get statistics
    print("\nFetching statistics...")
    response = api.handle_request("GET", "/tasks/stats")
    print(json.dumps(response, indent=2))

    # Filter by status
    print("\nFetching tasks by status...")
    response = api.handle_request("GET", "/tasks", {"status": "todo"})
    print(json.dumps(response, indent=2))
