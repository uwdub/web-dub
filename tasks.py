import importlib
import invoke

task_module_names = [
    'base.invoke.tasks.compile',
    'base.invoke.tasks.jekyll',
    'base.invoke.tasks.update',
]

# Create our task collection
tasks = invoke.Collection()

# Populate it with the tasks in each module
for module_name_current in task_module_names:
    module_loaded = importlib.import_module(module_name_current)

    # Add each task from that module
    module_collection = invoke.Collection.from_module(module_loaded)
    for task_name_current in module_collection.task_names.keys():
        tasks.add_task(module_collection[task_name_current], task_name_current)

# Invoke expects the default collection to be named 'ns'
ns = tasks
