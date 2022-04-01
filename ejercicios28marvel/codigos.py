Tecla1 = "ctrl"
Tecla2 = "alt"
Tecla3 = "Del"

if Tecla1 == 'ctrl':
    if Tecla2 == 'alt':
        action = 'Locks the screen'
    elif Tecla2 == 'D':
        action = 'Show desktop'
    elif Tecla2 == 'A':
        action = 'Shows the application menu'
    elif Tecla2 == 'M':
        action = 'Toggle notification tray'
    elif Tecla2 == 'Tab':
        action = 'Switch between running applications'
    elif Tecla2 == 'Space':
        action = 'Change input keyboard'
    elif Tecla2 == '<arrow>':
        action = 'Snap windows'
elif Tecla1 == 'Alt':
    if Tecla2 == 'F2':
        action = 'Run console'
    if Tecla2 == 'Tab':
        action = 'Switch between running applications'
elif Tecla1 == 'Ctrl':
    if Tecla2 == 'Q':
        action = 'Close an application window'
    elif Tecla2 == 'Alt':
        if Tecla3 == '<arrow>':
            action = 'Move between workspaces'
        elif Tecla3 == 'Del':
            action = 'Log out'
        elif Tecla3 == 'T':
            action = 'Ubuntu terminal shortcut'
        elif Tecla3 == 'L':
            action = 'Locks the screen'
        elif Tecla3 == 'D':
            action = 'Show desktop'

print(action)
