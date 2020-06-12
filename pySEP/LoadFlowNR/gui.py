import tkinter as tk

import gui_janela_config as g_config
import gui_menu as g_menu
import gui_toolbar as g_toolbar
import gui_statusbar as g_statusbar

janela = tk.Tk()

# janela
g_config.set_first(janela_main=janela)

# main menu
g_menu.menus(janela_main=janela)

# toolbar
g_toolbar.set_toolbar(janela_main=janela)

# status bar
g_statusbar.set_statusbar(janela_main=janela)

janela.mainloop()
