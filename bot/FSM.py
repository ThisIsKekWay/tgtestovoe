from aiogram.fsm.state import State, StatesGroup


class Tasks(StatesGroup):
    add_task_name = State()


class MainMenu(StatesGroup):
    main_menu = State()
