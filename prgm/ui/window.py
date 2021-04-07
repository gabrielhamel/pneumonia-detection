import PySimpleGUI as sg

def init_window():
    exit_button = sg.Button("Exit")
    layout = [
        [
            sg.Text("Select image to test"),
            sg.Input(key='uploaded_path', size=(45, 1), disabled=True, enable_events=True),
            sg.FileBrowse('Upload', target='uploaded_path')
        ],
        [
            sg.Text("Result: "),
            sg.Text("", key='result', size=(55, 2))
        ],
        [
            exit_button
        ]
    ]
    window = sg.Window(title="XRay AI", layout=layout)
    return window
