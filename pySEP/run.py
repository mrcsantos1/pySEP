from .gui import JanelaMain
from .circuito import Circuito


def run_gui():
    a = JanelaMain()


def circuit_cmd(sBase):
    a = Circuito(sBase=sBase)
