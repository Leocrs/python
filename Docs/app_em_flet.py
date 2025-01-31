import flet as ft
def main(pagina: ft.Page):
    pagina.title = "Meu primeiro app em Flet"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    def diminuir(e):
        caixa_texto.value = str(int(caixa_texto.value) - 1)
        pagina.update()
    def aumentar(e):
        caixa_texto.value = str(int(caixa_texto.value) + 1)
        pagina.update()
# Criar os itens do APP
    botao_menos = ft.IconButton(ft.icons.REMOVE, on_click=diminuir)  
    caixa_texto = ft.TextField(value="0",width=100, text_align=ft.TextAlign.CENTER)
    botao_mais = ft.IconButton(ft.icons.ADD, on_click=aumentar)
# Adicionar os itens a página
    pagina.add(ft.Row([caixa_texto, botao_mais, botao_menos], alignment=ft.MainAxisAlignment.CENTER))
  
ft.app(target=main, view=ft.WEB_BROWSER)

