from PyInquirer import prompt


todos = ['Learn python', 'Learn JavaScript']


def show_todos():
    print('All my todos 👉')
    for item in todos:
        print(f'🔮 {item}')


def add_new_todo(task):
    todos.append(task)


def show_add_todo_prompt():
    question = {
        'type': 'input',
        'name': 'task',
        'message': 'What is your new task?',
    }
    answer = prompt(question)
    add_new_todo(answer['task'])


def main():
    question = {
        'type': 'input',
        'name': 'command',
        'message': 'What you want to do next (list/add/exit) >>',
    }
    answer = prompt(question)
    if answer['command'] == 'list':
        show_todos()
    elif answer['command'] == 'add':
        show_add_todo_prompt()
        show_todos()
    elif answer['command'] == 'exit':
        exit()
    else:
        print('❗️ You entered unavailable task, please enter again!')
    main()


if __name__ == "__main__":
    print("My todos list.")
    main()
