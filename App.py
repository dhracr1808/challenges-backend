import sys
from Task import startTasks
from comands.Comand import ComandTask as Comand


options = {
    "add": {"comand": Comand(startTasks.create), "arg": {"min": 3, "max": 3}},
    "update": {"comand": Comand(startTasks.update), "arg": {"min": 4, "max": 4}},
    "delete": {"comand": Comand(startTasks.delete), "arg": {"min": 3, "max": 3}},
    "list": {"comand": Comand(startTasks.list), "arg": {"min": 2, "max": 3}},
    "mark-in-progress": {"comand": Comand(startTasks.mark_in_progress), "arg": {"min": 3, "max": 3}},
    "mark-done": {"comand": Comand(startTasks.mark_done), "arg": {"min": 2, "max": 3}},

}

print("Bienvenidos a tu lista de tareas")
if sys.argv[1] in options:
    arg = options[sys.argv[1]]["arg"]
    if arg["min"] <= len(sys.argv) <= arg["max"]:
        options[sys.argv[1]]["comand"].execute(*sys.argv[2:])
    else:
        print(
            f'\033[31m{sys.argv[1]}\033[0m necesita { arg["min"]-len(sys.argv) } argumentos más...')
else:
    print("Opcion no válida")
