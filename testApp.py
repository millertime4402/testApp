from nicegui import ui

label = ui.label('')

def say_hello():
    label.set_text('hello there')

ui.button('Click Me', on_click=say_hello)

ui.run(host='0.0.0.0', port=8080)