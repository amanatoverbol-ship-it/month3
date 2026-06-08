import flet as ft

def main(page: ft.Page):
    page.title = 'Title of the page'
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_history=[]

    greeting_text = ft.Text('History of greetings', size=24, color=ft.Colors.BLUE_900)
    text_hello= ft.Text('Hello', color=ft.Colors.BLUE_900, size=48)
    def text_name(e):
        print(text_input.value)
        if text_input.value.strip() == '':
            text_hello.value ='You did not enter your name'
            text_hello.color = ft.Colors.RED
        elif int(text_input.value.isdigit())==True:
            text_hello.value ='Name cannot consist of digits only'
            text_hello.color = ft.Colors.YELLOW
        else:
            if len(text_input.value.split())<2:
                text_hello.value ='Name should consist of at least two letters'
                text_hello.color = ft.Colors.RED
            else:
                if text_input.value in greeting_history:
                    text_hello.value = f"The name is already in the history"
                    text_hello.color = ft.Colors.RED
                else:
                    text_hello.value = f"Welcome, {text_input.value}"
                    text_hello.color = ft.Colors.GREEN
                    if len(greeting_history)>5:
                        greeting_history.pop(0)
                    else:
                        greeting_text.value = "History of greetings: \n " + " \n ".join(greeting_history)
                    greeting_history.append(text_input.value)
                    greeting_text.value = "History of greetings: \n " + " \n ".join(greeting_history)
                
                
                
            page.update()
            text_input.value = ""
        page.update()


    def toggle_theme(e):
        if page.theme_mode== ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode= ft.ThemeMode.LIGHT
    page.update()
    
    button_theme = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=toggle_theme)
    
    text_input= ft.TextField(label='Enter your name', on_submit=text_name, expand = False)
    btn = ft.ElevatedButton('SEND', on_click=text_name)
    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = "History of greetings: \n " + " \n ".join(greeting_history)
        page.update()



    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click = clear_history) 


    main_obj= ft.Column(controls=[text_hello,ft.Row(controls=[text_input, btn], expand=True), greeting_text], alignment = ft.MainAxisAlignment.CENTER)
    text_Row= ft.Row(controls =[button_theme, clear_button], alignment = ft.MainAxisAlignment.SPACE_BETWEEN)


    page.add(text_Row, main_obj)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)