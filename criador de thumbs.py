import os
import time
import pywinauto
import pywinauto.mouse
import pywinauto.keyboard
import win32api

class criador_de_thumbs():
    # Variáveis e constântes
    gimp = pywinauto.application.Application()
    TITULO_THUMB = input("Insira o título da thumb: ")
    BAIXO_THUMB = input("Insira a parte de baixo da thumb: ")
    X_TEXTO = 310
    Y_TEXTO = 500
    FONTE = "Burbank Big Condensed, Semi-Bold"
    TAMANHO_FONTE = "200"
    def main(self):
        self.abrir_gimp()
        self.abrir_template_de_thumbs()
        self.editar_texto()



    def abrir_gimp(self):
        # Abre o gimp
        self.gimp.start("C:\\Program Files\\GIMP 2\\bin\\gimp-2.10.exe")
        time.sleep(1)


    def abrir_template_de_thumbs(self):
        # Abre o template para a criação de novas miniaturas
        os.startfile("C:\\Users\\Luis Felipe\\Documents\\Audiolivros template 2.xcf")
        time.sleep(2)

    def editar_texto(self):
        # Função principal para a edição do texto dentro da miniatura.
        self.gimp.window()
        if self.gimp.top_window():
            self.gimp.active()
            pywinauto.mouse.click("left", (170, 110))
            self.digitar_texto(0, 100, False)
            if self.BAIXO_THUMB != "":
                # Chama três funções complementares uma para cada processo no segundo texto.
                self.digitar_texto(100, 0, True)
                self.configurar_texto()
                self.mover_texto_baixo()

            self.selecionar_texto_por_cor()
            self.fazer_degrade_no_texto()
            self.adicionar_sombra()
            self.inclinar_texto()
            pywinauto.mouse.click("left", (1760, 627))
            self.adicionar_sombra()

    def digitar_texto(self, y, y2, texto_baixo):
        if not texto_baixo:
            pywinauto.mouse.click("left", (self.X_TEXTO, self.Y_TEXTO + y))
            pywinauto.mouse.click("left", (self.X_TEXTO, self.Y_TEXTO + y2))
            pywinauto.keyboard.send_keys("^a")
            pywinauto.keyboard.send_keys(self.TITULO_THUMB.upper(), False, True)
        else:
            self.posicao_texto_baixo_x = self.X_TEXTO
            self.posicao_texto_baixo_y = self.Y_TEXTO + y
            pywinauto.mouse.click("left", (self.X_TEXTO, self.Y_TEXTO + y))
            pywinauto.keyboard.send_keys("^a")
            pywinauto.keyboard.send_keys(self.BAIXO_THUMB.upper(), False, True)

    def configurar_texto(self):
        # Configura a fonte
        pywinauto.keyboard.send_keys("^a")
        pywinauto.mouse.click("left", (self.X_TEXTO + 15, self.Y_TEXTO + 40))
        pywinauto.keyboard.send_keys("^a" f"{self.FONTE}" "~")
        # Configura o tamanho da fonte
        pywinauto.mouse.click("left", (self.X_TEXTO + 225, self.Y_TEXTO + 40))
        pywinauto.keyboard.send_keys("^a")
        pywinauto.keyboard.send_keys(self.TAMANHO_FONTE)
        # Configura a cor do texto
        pywinauto.mouse.click("left", (604, 573))
        pywinauto.mouse.double_click("left", (724, 642))
        pywinauto.keyboard.send_keys("ffffff")
        pywinauto.keyboard.send_keys("~")
        pywinauto.mouse.click("left", (667, 746))
        pywinauto.mouse.click("left", (1900, self.Y_TEXTO + 130))

    def mover_texto_baixo(self):
        print("Entrei na função")
        pywinauto.keyboard.send_keys("+t")
        pywinauto.mouse.press("left", coords=(self.posicao_texto_baixo_x + 15, self.posicao_texto_baixo_y + 25))
        pywinauto.mouse.release("left", coords=(self.posicao_texto_baixo_x + 50, self.posicao_texto_baixo_y - 70))
        pywinauto.keyboard.send_keys("~")

    def selecionar_texto_por_cor(self):
        pywinauto.mouse.click("left", (1900, self.Y_TEXTO + 160))
        time.sleep(0.5)
        pywinauto.keyboard.send_keys("{ESC}" "{ESC}" "+t")
        pywinauto.mouse.press("left", (self.X_TEXTO, self.Y_TEXTO))
        pywinauto.mouse.release("left", (self.X_TEXTO + 50, self.Y_TEXTO + 25))
        pywinauto.keyboard.send_keys("~" "+o down" "+o up")

    def fazer_degrade_no_texto(self):
        x_letra = 310
        pywinauto.mouse.click("left", (x_letra, self.Y_TEXTO - 120))
        pywinauto.keyboard.send_keys("{g down}" "{g up}")
        pywinauto.mouse.press("left", (x_letra, self.Y_TEXTO - 120))
        pywinauto.mouse.release("left", (x_letra + 125, self.Y_TEXTO))
        pywinauto.keyboard.send_keys("~")

    def adicionar_sombra(self):
        time.sleep(1)
        pywinauto.keyboard.send_keys("{r down}" "{r up}")
        self.clicar_em_local_vazio()
        pywinauto.keyboard.send_keys("^%s")
        self.mudar_opacidade_da_sombra()
        self.mudar_grow_radius_da_sombra()
        self.mudar_x_e_y_da_sombra()
        pywinauto.mouse.click("left", (687, 776))

    def mudar_opacidade_da_sombra(self):
        pywinauto.mouse.double_click("left", (556, 652))
        pywinauto.keyboard.send_keys("2")

    def mudar_grow_radius_da_sombra(self):
        pywinauto.mouse.double_click("left", (633, 600))
        pywinauto.keyboard.send_keys("10")

    def mudar_x_e_y_da_sombra(self):
        pywinauto.mouse.double_click("left", (581, 503))
        pywinauto.keyboard.send_keys("10")
        pywinauto.mouse.double_click("left", (615, 523))
        pywinauto.keyboard.send_keys("10")

    def inclinar_texto(self):
        pywinauto.keyboard.send_keys("+h")
        pywinauto.mouse.click("left", (615, 523))
        pywinauto.mouse.double_click("left", (1529, 150))
        pywinauto.keyboard.send_keys("-25")
        time.sleep(0.5)
        pywinauto.mouse.click("left", (1580, 207))
        pywinauto.mouse.click("left", (615, 523))
        pywinauto.mouse.double_click("left", (1545, 168))
        pywinauto.keyboard.send_keys("-15")
        time.sleep(0.5)
        pywinauto.mouse.click("left", (1580, 207))

    def pegaPosicaoMouse(self):
        time.sleep(2)
        mouse_x, mouse_y = win32api.GetCursorPos()
        print(f"X: {mouse_x}")
        print(f"Y: {mouse_y}")

    def clicar_em_local_vazio(self):
        pywinauto.mouse.click("left", (self.X_TEXTO, self.Y_TEXTO + 450))


thumb = criador_de_thumbs()
thumb.main()
#thumb.pegaPosicaoMouse()
