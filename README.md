# Security-and-Surveillance
IoT based general purpose Security and Surveillance system for home, office, traffic etc.

## Hardware used : 

* [NodeMCU : ](https://github.com/nodemcu/nodemcu-firmware)
An open-source firmware and development kit that helps you to prototype your IOT product easily.The Development Kit based on ESP8266, integates GPIO, PWM, IIC, 1-Wire and ADC all in one board. Power your developement in the fastest way combinating with NodeMCU Firmware.
# <img src="https://github.com/RatulGhosh/Temperature_monitoring_system/blob/master/images/c1s.jpg_450x300.jpg" />



## Working : 
There are two nodes and each node is connected to a temperature sensor. Each node has an Node MCU. The sensors are  placed in different rooms which continuously sends the temperature values to the raspberry pi acting as the server (In order to save space I am storing the temperature after every 2 minutes).The temperature is continuously checked with the threshold temperature and if it crosses that temperature a warning message is sent to the website and the android app,also the control mechanism (a CPU fan in this case) is switched on.  The temperature readings will be displayed on the web page as well as on the android app , also the control mechanism can be operated i.e switched on and  off from the website and the app. Also there is an extended option in the android app to change the threshold temperature.




### License
# <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat" width="80" />
Note that Security-and-Surveillance is distributed under the [MIT License](http://opensource.org/licenses/MIT).

### TODO
* An app can be made 
* Cloud platform can be used to handle size issues
* More accurate camera can be used


Your feedback, ideas, suggestions are most welcome!
