from setuptools import setup

setup(
    name='pySEP',
    version='1.0.0',
    author='Marcos Alves dos Santos',
    author_email='mrcsantos1@outlook.com',
    packages=['pySEP'],

    description='Pacote Open Source desenvolvido no Brasil para modelar e simular Sistemas Elétricos de Potência. '
                'Open Source Package developed in Brazil to model and simulate Electric Power Systems',

    long_description="\nA principal ideia deste pacote é fornecer, em livre licença, uma série de ferramentas capazes de modelar e simular Systemas Elétricos de Potência. "
                     "\nPara isso, a presente versão possibilita a seguinte operação: "
                     "\n\t*\tCálculo do Fluxo de Potência pelo método de Newton-Raphson de um sistema com n barras. "
                     "\nUma série de novas ferramentas serão disponibilizadas em novas versões, tais como: "
                     "\n\t*\tCálculo de curto-circuitos entre barras. "
                     "\n\t*\tCálculo de curto-circuito em linhas. "
                     "\n\t*\tCálculos relacionados a Sistemas de Transmissão. "
                     "\n\t*\tCálculos relacionados a Sistemas de Distribuição "
                     "\n\tEntre outras ferramentas.",

    url='https://github.com/mrcsantos1/pySEP',

    project_urls={
        'Source Code': 'https://github.com/mrcsantos1/pySEP',
        'Download': 'https://github.com/mrcsantos1/pySEP/archive/master.zip'
    },

    license='Apache License',

    keywords=['Load Flow', 'Power Flow', 'Newton-Raphson', 'Fluxo de Potência', 'Python', 'Electrical Engineering',
              'Engenharia Elétrica'],

    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: Console',
        'Framework :: Matplotlib',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Adaptive Technologies',
        'Topic :: Education',
        'Topic :: Education :: Computer Aided Instruction (CAI)',
        'Topic :: Education :: Testing',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',

    ]
)
