import flet as ft
def main(page: ft.Page):
    page.title = 'Welcome to website'
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello= ft.Text('Hello', color=ft.Colors.BLUE_900, size=48)
    def text_age(e):
        print(text_input.value)
        if text_input.value.strip() == '' or int(text_input.value.isdigit())==False:
            text_hello.value ='Enter your age correctly'
            text_hello.color = ft.Colors.YELLOW
        elif int(text_input.value)<18:
            text_hello.value = f"Access dissallowed!"
            text_hello.color = ft.Colors.RED
        else:
            text_hello.value = f"Access allowed!"
            text_hello.color = ft.Colors.GREEN
            text_input.value = ""
        page.update()


    def toggle_theme(e):
        if page.theme_mode== ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode= ft.ThemeMode.LIGHT
    page.update()
    
    button_theme = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=toggle_theme)
    page.add(button_theme)
    
    text_input= ft.TextField(label='Enter your age', on_submit=text_age)
    btn = ft.ElevatedButton('SEND', on_click=text_age)
    page.add(text_hello, text_input, btn)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)