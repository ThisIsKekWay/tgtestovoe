from typing import Text

from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from FSM import MainMenu, Tasks
from tasks.dao import TasksDAO

tasks_router = Router()


@tasks_router.message(Command('start'))
async def start(msg: types.Message, state: FSMContext):
    content = Text("Привет, это тестовый бот для записи дел")
    await state.set_state(MainMenu.main_menu)
    await msg.answer(content)


@tasks_router.message(Command('add'), StateFilter(MainMenu.main_menu))
async def add_task(msg: types.Message, state: FSMContext):
    content = Text("Что нужно запомнить")
    await state.set_state(Tasks.add_task_name)
    await msg.answer(content)


@tasks_router.message(Command('tsk'), StateFilter(MainMenu.main_menu))
async def add_task(msg: types.Message, state: FSMContext):
    user_id = str(msg.from_user.id)
    res = await TasksDAO.find_all(user_id=user_id)
    for task in res:
        await msg.answer(task.task_name)


@tasks_router.message(F.text, StateFilter(Tasks.add_task_name))
async def add_task_name(msg: types.Message, state: FSMContext):
    user_id = str(msg.from_user.id)
    task_name = msg.text
    await TasksDAO.add(task_name=task_name, user_id=user_id)
    await msg.answer("Задача добавлена")
    await state.set_state(MainMenu.main_menu)
