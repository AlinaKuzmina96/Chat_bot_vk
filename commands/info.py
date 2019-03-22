from Chat_bot_vk_2 import command_system

def info():
    message = ''
    for c in command_system.command_list:
        if c.com != "":
            message += c.com + ' - ' + c.description + '\n'
    return message, ''

info_command = command_system.Command()

info_command.keys = ['помощь']
info_command.process = info