from PyInquirer import prompt


def get_todos():
    return ['hey', 'hello']


def show_todos(todos):
    print('All my todos 👉')
    for item in todos:
        print(f'🔮 {item}')


def main():
    print("My todos list.")
    questions = {
        'type': 'input',
        'name': 'command',
        'message': 'What you want to do next >>',
    }
    answers = prompt(questions)
    if answers['command'] == 'list':
        todos = get_todos()
        show_todos(todos)


if __name__ == "__main__":
    main()
