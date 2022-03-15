import PySimpleGUI as sg

# getting the END value
def defineEND(load):
    stats = [45.0, 45.0, 45.0, 45.0, 45.0, 45.0, 45.0, 45.0, 46.6, 48.2, 49.8, 51.4, 52.9, 54.5, 56.1, 57.7, 59.3, 60.9, 62.5, 64.1, 65.6, 67.2, 68.8, 70.4, 72.0, 73.0, 74.1, 75.2, 76.4, 77.6, 78.9, 80.2, 81.5, 82.8, 84.1, 85.4, 86.8, 88.1, 89.5, 90.9, 92.3, 93.7, 95.1, 96.5, 97.9, 99.4, 100.8, 102.2, 103.7, 105.2, 106.6, 108.1, 109.6, 111.0, 112.5, 114.0, 115.5, 117.0, 118.5, 120.0, 121.0, 122.1, 123.1, 124.1, 125.1, 126.2, 127.2, 128.2, 129.2, 130.3, 131.3, 132.3, 133.3, 134.4, 135.4, 136.4, 137.4, 138.5, 139.5, 140.5, 141.5, 142.6, 143.6, 144.6, 145.6, 146.7, 147.7, 148.7, 149.7, 150.8, 151.8, 152.8, 153.8, 154.9, 155.9, 156.9, 157.9, 159.0, 160.0]

    for i in range(len(stats)):
        if load < stats[i]:
            return str(i+1) + " ENDURANCE"

    return "OVER 99 ENDURANCE, which is impossible"


# responsible for all the calculations
def calc(equipment_load, load_buff):
    load_buff_fl = (load_buff + 100) / 100

    medium_roll = 0.699
    light_roll = 0.299

    desired_load_light = equipment_load / light_roll
    desired_load_medium = equipment_load / medium_roll

    required_load_light = desired_load_light / load_buff_fl
    required_load_medium = desired_load_medium / load_buff_fl

    toReturn = "[LIGHT ROLL, requires load below 30%]"
    toReturn += "\nThe total equipment load that you need to have is: {:.1f}".format(desired_load_light)
    toReturn += "\nThe equipment load you would need without the {:.1f}% buff is: {:.1f}".format(load_buff, required_load_light)
    toReturn += "\nThen, you would need at least " + defineEND(desired_load_light)

    toReturn += "\n\n[MEDIUM ROLL, reuqires load below 70%]"
    toReturn += "\nThe total equipment load that you need to have is: {:.1f}".format(desired_load_medium)
    toReturn += "\nThe equipment load you would need without the {:.1f}% buff is: {:.1f}".format(load_buff, required_load_medium)
    toReturn += "\nThen, you would need at least " + defineEND(required_load_medium)

    return toReturn


# Checking if both values are of numeric values
def areFloat(val1, val2):
    v1Bool = False

    try:
        float(val1)
        v1Bool = True
    except:
        v1Bool = False

    v2Bool = False

    try:
        float(val2)
        v2Bool = True
    except:
        v2Bool = False

    return v1Bool and v2Bool


# GUI from here
sg.theme('DarkAmber')   # Elden Bling

# Elements
layout = [  [sg.Text('Welcome to the Elden Ring equip load to END calculator!', font='Arial 18')],
            [sg.Text('Input the total weight of your equipments (including talismans):', font='Arial 15', size=(50, 1)), sg.InputText()],
            [sg.Text('Input how much equipment load increase buff you have in total:', font='Arial 15', size=(50, 1)), sg.InputText()],
            [sg.Button('Calculate', font='Arial 11')],
            [sg.Multiline(size=(100, 10), font='Arial 13', key='result', autoscroll=True), sg.VerticalSeparator(pad=None)]]


# Create the Window
window = sg.Window('EquipLoadENDCalc', layout).Finalize()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Close Window'): # if user closes window or clicks cancel
        break

    if areFloat(values[0], values[1]):
        content = calc(float(values[0]), float(values[1]))
        window['result'].update(content)
    else:
        window['result'].update("Invalid input! Please try again")

window.close()