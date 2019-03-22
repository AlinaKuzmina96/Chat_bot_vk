from Chat_bot_vk_2 import command_system

def hello():
   message = 'Привет, друг!'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте']
hello_command.description = 'Поприветствую тебя'
hello_command.com = "Напиши приветствие"
hello_command.process = hello