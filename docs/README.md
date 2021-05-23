# <img src="https://github.com/PEQUI-MEC/PY-VSSS-INF/blob/master/docs/images/pyfromhell.jpeg" width="50" height="50"/> Pequi Very Small Size Soccer Team
[![travis build](https://img.shields.io/travis/PEQUI-MEC/VSSS-INF/master.svg)](https://travis-ci.org/PEQUI-MEC/PY-VSSS-INF) ![](https://img.shields.io/github/stars/PEQUI-MEC/PY-VSSS-INF.svg) ![](https://img.shields.io/github/contributors/PEQUI-MEC/PY-VSSS-INF.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/PEQUI-MEC/PY-VSSS-INF/blob/master/docs/LICENSE)

Hi! This is the development repo of [Pequi Mecânico](https://www.facebook.com/NucleoPMec/) - INF's **Very Small Size Soccer Team**. Our team comprises several courses (Electrical Engineering, Computer Engineering, Software Engineering and Computer Science), all from Federal University of Goiás - [UFG](https://www.ufg.br/) - Goiânia. Our repository is open because we understand that our greatest job is to add our research and knowledge to the academic and industrial world.

You can find our Team Description Paper [here](https://github.com/bryanoliveira/PY-VSSS-INF/blob/master/docs/TDP%20VSSS%20INF%202018.pdf). We are open to answer any questions and suggestions through our email pequimecanicoufg@gmail.com.

## Features

- Isolated modules for vision, strategy, control, communication, and interface
- High-fidelity simulator made with MuJoCo
- Qt interface

<div align="center">
<a href="https://www.youtube.com/watch?v=JQVrX5h7u_8">
<img src="https://github.com/bryanoliveira/PY-VSSS-INF/blob/master/docs/images/Simulator.gif" width="550"/>
</a>
</div>

> Our simulator running two instances of the same control system. Green arrows indicate the robot's movement direction (given by the vector field), and blue, yellow, and red arrows indicate goalie, defender and attacker's targets. 

## Usage

### Dependencies

Our code runs on all Python3-supported OS's (we recommend Python 3.4). To start using our software, you must install all requirements described on our requirements.txt file. You can easily do that by running:

`pip install -r requirements.txt`

We use MuJoCo as our simulation engine. Unfortunately, as MuJoCo is not free software, you must grab your license [here](https://www.roboti.us/license.html) to run our simulator.

### Executing

To open the GUI we use on our competitions, run:

`python afrodite.py`

To open our simulator, run:

`python aether.py`

<div align="center">
<a href="https://www.youtube.com/watch?v=UBV4qlAJ-sc">
<img src="https://github.com/bryanoliveira/PY-VSSS-INF/blob/master/docs/images/Kick.gif" width="600"/>
</a>
</div>

> A kick motion performed by the robot control system using univector fields and simulated with MuJoCo. 

## Social networks

Our activities and events always have updates. Follow us and get updated :D

- [Instagram](https://www.instagram.com/pequimecanico/)
- [Facebook](https://www.facebook.com/NucleoPMec)
