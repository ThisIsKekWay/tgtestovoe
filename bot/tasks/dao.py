from dao.base import BaseDAO
from tasks.models import Tasks


class TasksDAO(BaseDAO):
    model = Tasks
