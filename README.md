# README of this Fork
Temporary Fork to allow the support of 
* the Lego Powered Up Train hub
* the Lego Power Up hub

This fork will be merged later in the main pylgbst branch if the author accepts.

TrainHub might be seen as MoveHub, with less port and less features. To support it, only the hub.py is modified so far, by mostly copy pasting code from MoveHub. For the Train Motor, using the Motor() class is working fine so far.

TechnicHub might be seen as MoveHub, with less port and less features. To support it, only the hub.py is modified so far, by mostly copy pasting code from MoveHub
When initizaling connection with the TechnicHub, I got a messages:

    Have not dedicated class for peripheral type 2e on port 1
    Have not dedicated class for peripheral type 2f on port 3
    Have not dedicated class for peripheral type 3c on port 3d
    Have not dedicated class for peripheral type 3c on port 60
    Have not dedicated class for peripheral type 39 on port 61
    Have not dedicated class for peripheral type 3a on port 62
    Have not dedicated class for peripheral type 3b on port 63
    Have not dedicated class for peripheral type 36 on port 64

This is not preventing some tests apps to control the motor. But because of this message, the Flask server was raising and exception. I commented the line in hub.py:

    log.warning("Have not dedicated class for peripheral type %x on port %x", dev_type, port)

With that the flask server worked fine.

On both Hub, I only tested:
* connection to the hub
* hub creation 
* the start_power() and stop() methods for motors
* disconnection 

Later on, we can manage the TrainHub and TechnicHub by moving common of the code in the Hub class. Bu

There is also in this Fork a test_train_hub.py which contains an example and the ouput script, which works on a Raspberry Pi 3, but with warning messages that I will try to remove.

## Installing this fork on a Jetson Nano

    python3 setup.py install --user

## Using the pygatt on Linux / Jetson Nano
After testing some of the connections alternative :
bluepy requires python 3.7 to run asyncio command
pygatt requires sudo
So i decided to move with gatt

    pip install gatt
    
Examples given are hardcoded with my Technic Hub and Train Hub.
90:84:2B:5F:33:35 as Technic Hub



# Original README below


# Python library to interact with Move Hub / PoweredUp Hubs

_Move Hub is central controller block of [LEGO® Boost Robotics Set](https://www.lego.com/themes/boost)._

In fact, Move Hub is just a Bluetooth hardware piece, and all manipulations with it are made by commands passed through Bluetooth Low Energy (BLE) wireless protocol. One of the ways to issue these commands is to write Python program using this library.

The best way to start is to look into [`demo.py`](examples/demo.py) file, and run it (assuming you have installed library).

If you have Vernie assembled, you might run scripts from [`examples/vernie`](examples/vernie) directory.

## Demonstrational Videos

[![Vernie Programmed](http://img.youtube.com/vi/oqsmgZlVE8I/0.jpg)](http://www.youtube.com/watch?v=oqsmgZlVE8I)
[![Laser Engraver](http://img.youtube.com/vi/ZbKmqVBBMhM/0.jpg)](https://youtu.be/ZbKmqVBBMhM)
[![Color Sorter](http://img.youtube.com/vi/829RKT8v8M0/0.jpg)](https://youtu.be/829RKT8v8M0)
[![Face Tracker](http://img.youtube.com/vi/WUOa3j-6XfI/0.jpg)](https://youtu.be/WUOa3j-6XfI)
[![Color Pin Bot](http://img.youtube.com/vi/QY6nRYXQw_U/0.jpg)](https://youtu.be/QY6nRYXQw_U)
[![BB-8 Joystick](http://img.youtube.com/vi/55kE9I4IQSU/0.jpg)](https://youtu.be/55kE9I4IQSU)


## Features

- auto-detect and connect to [Move Hub](docs/MoveHub.md) device
- auto-detects [peripheral devices](docs/Peripherals.md) connected to Hub
- constant, angled and timed movement for [motors](docs/Motor.md), rotation sensor subscription
- [vision sensor](docs/VisionSensor.md): several modes to measure distance, color and luminosity
- [tilt sensor](docs/TiltSensor.md) subscription: 2 axis, 3 axis, bump detect modes
- [RGB LED](docs/LED.md) color change
- [push button](docs/MoveHub.md#push-button) status subscription
- [battery voltage and current](docs/VoltageCurrent.md) subscription available
- permanent Bluetooth connection server for faster debugging


## Usage

_Please note that this library requires one of Bluetooth backend libraries to be installed, please read section [here](#bluetooth-backend-prerequisites) for details._

Install library like this: 
```bash
pip install -U pylgbst
```

Then instantiate MoveHub object and start invoking its methods. Following is example to just print peripherals detected on Hub:  

```python
from pylgbst.hub import MoveHub

hub = MoveHub()

for device in hub.peripherals:
    print(device)
```

Each peripheral kind has own methods to do actions and/or get sensor data. See [features](#features) list for individual doc pages.

## Bluetooth Backend Prerequisites

You have following options to install as Bluetooth backend (some of them might require `sudo` on Linux):

- `pip install pygatt` - [pygatt](https://github.com/peplin/pygatt) lib, works on both Windows and Linux  
- `pip install gatt` - [gatt](https://github.com/getsenic/gatt-python) lib, supports Linux, does not work on Windows, does not require `sudo`
- `pip install gattlib` - [gattlib](https://bitbucket.org/OscarAcena/pygattlib) - supports Linux, does not work on Windows, requires `sudo`
- `pip install bluepy` - [bluepy](https://github.com/IanHarvey/bluepy) lib, supports Linux, including Raspbian, which allows connection to the hub from the Raspberry PI
- `pip install bleak` - [bleak](https://github.com/hbldh/bleak) lib, supports Linux/Windows/MacOS, requires Python 3.7 for asyncio.run command

Running on Windows requires [Bluegiga BLED112 Bluetooth Smart Dongle](https://www.silabs.com/products/wireless/bluetooth/bluetooth-low-energy-modules/bled112-bluetooth-smart-dongle) hardware piece, because no other hardware currently works on Windows with Python+BLE.

_Please let author know if you have discovered any compatibility/preprequisite details, so we will update this section to help future users_

Depending on backend type, you might need Linux `sudo` to be used when running Python. gatt does not requires sudo.

### Bluetooth Connection Options
There is an optional parameter for `MoveHub` class constructor, accepting instance of `Connection` object. By default, it will try to use whatever `get_connection_auto()` returns. You have several options to manually control that:

- use `get_connection_auto()` to attempt backend auto-detection 
- use `get_connection_bluegiga()` - if you use BlueGiga Adapter (`pygatt` library prerequisite)
- use `get_connection_gatt()` - if you use Gatt Backend on Linux (`gatt` library prerequisite, no sudo)
- use `get_connection_gattool()` - if you use GattTool Backend on Linux (`pygatt` library prerequisite)
- use `get_connection_gattlib()` - if you use GattLib Backend on Linux (`gattlib` library prerequisite)
- use `get_connection_bluepy()` - if you use Bluepy backend on Linux/Raspbian (`bluepy` library prerequisite, Python 3.7 prerequisite for asyncio.run command)
- use `get_connection_bleak()` - if you use Bleak backend (`bleak` library prerequisite, sudo)
- pass instance of `DebugServerConnection` if you are using [Debug Server](#debug-server) (more details below).

All the functions above have optional arguments to specify adapter name and Hub name (or mac address). Please take a look at functions source code for details.

If you want to specify name for Bluetooth interface to use on local computer, you can pass that to class or function of getting a connection. Then pass connection object to `MoveHub` constructor. Like this:
```python
from pylgbst.hub import MoveHub
from pylgbst import get_connection_gatt

conn = get_connection_gatt(hub_mac='AA:BB:CC:DD:EE:FF')
hub = MoveHub(conn)
```


## Debug Server
Running debug server opens permanent BLE connection to Hub and listening on TCP port for communications. This avoids the need to re-start Hub all the time. 

There is `DebugServerConnection` class that you can use with it, instead of `BLEConnection`. 

Starting debug server is done like this (you may need to run it with `sudo`, depending on your BLE backend):
```bash
python -c "import logging; logging.basicConfig(level=logging.DEBUG); \
                import pylgbst; pylgbst.start_debug_server()"
```

Then push green button on MoveHub, so permanent BLE connection will be established.

## Roadmap & TODO

- validate operations with other Hub types (train, PUP etc)
- make connections to detect hub by UUID instead of name
- document all API methods
- make debug server to re-establish BLE connection on loss

## Links

- https://github.com/LEGO/lego-ble-wireless-protocol-docs - true docs for LEGO BLE protocol
- https://github.com/JorgePe/BOOSTreveng - initial source of protocol knowledge
- https://github.com/nathankellenicki/node-poweredup - JavaScript version of library
- https://github.com/spezifisch/sphero-python/blob/master/BB8joyDrive.py - example with another approach to bluetooth libs
- https://github.com/virantha/bricknil - for the lovers of async Python, alternative implementation of library to control PoweredUp Hubs
