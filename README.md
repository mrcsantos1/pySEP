# pySEP

![PyPI](https://img.shields.io/pypi/v/pySEP?style=plastic&logo=PyPi) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pySEP?color=black&logo=python&logoColor=white&style=plastic) ![PyPI - License](https://img.shields.io/pypi/l/pySEP?color=red&style=plastic&logo=apache)  ![PyPI - Status](https://img.shields.io/pypi/status/pySEP?style=plastic) ![PyPI - Downloads](https://img.shields.io/pypi/dd/pySEP?color=blue&style=plastic) ![GitHub followers](https://img.shields.io/github/followers/mrcsantos1?label=Siga-me&logo=github&style=social) 

---

A principal ideia deste pacote é fornecer, em livre licença, uma série de ferramentas capazes de modelar e simular Systemas Elétricos de Potência.  

Para isso, a presente versão possibilita a seguinte operação: 

 - Cálculo do Fluxo de Potência pelo método de Newton-Raphson de um sistema com n barras. 
 
 Uma série de novas ferramentas serão disponibilizadas em novas versões, tais como: 
 
 
 - Cálculo de curto-circuitos entre barras.  
 - Cálculo de curto-circuito em linhas. 
 - Cálculos relacionados a Sistemas de Transmissão.   
 - Cálculos relacionados a Sistemas de Distribuição.   
 
 Entre outras ferramentas.
 
  
This package, pySEP, is a package created to assist in the Electric Power Systems learning, modelling and simulating.   
  
The application of the Newton-Raphson method for the calculation of power flow in electrical power systems is an example of how it works.

---

## Youtube

A playlist was created to show how the code of the Power Flow by Newton-Raphson method was created. It is available in:

![enter image description here](https://i.ytimg.com/vi/wHmq-bpv-Oo/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBOhZPCD5Lupd9udu2juM3BecwPQQ)

[FLUXO DE POTÊNCIA POR NEWTON-RAPHSON EM PYTHON](https://www.youtube.com/playlist?list=PLNOc51Usq3jgqOe4zmCNrXJ71SOBpa-TI)

---

## Getting Started

For the correct working of this library, it is only required that, on the machine where this package is installed, the Python interpreter is also installed, with versions 3.x onwards being recommended.

### Installing

A step-by-step guide on how to install this package is described below.

First, using the python pip, just type the following command.

```
pip install pySEP
```

After that, the package is installed where you configured the installation of it. Therefore, to use the circuit modeling tool to perform the calculations, write this command in the program in which the calculation will be created.

```
import pySEP 
```

It is common to define an abbreviation to shorten the package name. Do this after "asadfdgfg", as in the example below.

```
import pySEP as psp
```
### For example

```
import pySEP.lFlowNR as psp

c = psp.CreateCircuit(100e6)

c.addBus(1, 1, 1.05, 0, 0 + 0 * 1j, 0 + 0 * 1j)
c.addBus(2, 2, 1.00, 0, 256.6e6 + 110.2e6 * 1j, 0 + 0 * 1j)
c.addBus(3, 2, 1.00, 0, 138.6e6 + 45.2e6 * 1j, 0 + 0 * 1j)

c.setSesp()

c.addLine(1, 2, impedancia=0.02 + 0.04j)
c.addLine(1, 3, impedancia=0.01 + 0.03j)
c.addLine(2, 3, impedancia=0.0125 + 0.025j)

c.solveCircuito(iteracoes=20, listTensao=[2, 3], listAng=[2, 3], erro=None, showSubMat=False)

c.powerFlow(printTensao=True, printCorrentes=True)

c.losses()

c.plotData(tensao=True, ang=True)
```

The above example is enough to create a circuit with 3 buses and 4 lines, to calculate the load flow (power flow by newton-raphson method) in it and to show the results with a graphical description. 
 
 
 It is recommended to run the "help ()" method of the "Create Circuit" class to obtain more detailed information about this code.

## Built With

All the code in this package uses only two external packages. These are: 

* [NumPy]([https://numpy.org/](https://numpy.org/)) - NumPy is the fundamental package for scientific computing with Python.
* [MatPlotLib]([https://matplotlib.org/](https://matplotlib.org/)) - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

All others libraries used in this code are Python builtins.



## Versioning

All versions of this package are "committed" and are available on my [GitHub](https://github.com/mrcsantos1/pySEP)

## Author

* **Marcos Alves dos Santos** - [mrcsantos1](https://github.com/mrcsantos1)


## License

This project is licensed under the Apache License - see the [LICENSE.txt](LICENSE.txt) file for details

