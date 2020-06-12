import tkinter as tk

import gui_janela_config as g_config
import gui_menu as g_menu
import gui_toolbar as g_toolbar
import gui_statusbar as g_statusbar


class JanelaMain:
    def __init__(self):
        self.__janela = tk.Tk()
        self.__info_basic = {}

        # janela
        g_config.set_first(janela_main=self.__janela)

        # main menu
        g_menu.menus(janela_main=self.__janela)

        # toolbar
        g_toolbar.set_toolbar(janela_main=self.__janela)

        # status bar
        g_statusbar.set_statusbar(janela_main=self.__janela)

        self.__janela.mainloop()


a = JanelaMain()
