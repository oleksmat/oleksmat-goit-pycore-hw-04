def hello_command(_: any):
    print('How can I help you?')

hello = (
    ['hello'],
    0,
    ' -- hello\n' +
    '    Prints hello statement',
    hello_command
)
