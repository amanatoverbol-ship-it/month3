import flet as ft
def main(page: ft.Page):
    count =0
    page.title = "Title of the page"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    text_hello = ft.Text(f"Clicked {count} times", size=52)
    def on_click():
        nonlocal count 
        count += 1
        text_hello.value = f"Clicked {count} times"
        page.update()
    btn = ft.ElevatedButton('SEND', on_click=on_click)
    page.add(text_hello, btn)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)