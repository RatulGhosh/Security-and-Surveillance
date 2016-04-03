# Security-and-Surveillance
IoT based general purpose Security and Surveillance system for home, office, traffic etc.
The application continuously records videos and if there is any motion a signal is sent to the Node Mcu which in turn triggers a buzzer. There is an extended application of integrating with the Dropbox API so that the system can automatically upload security photos to our personal Dropbox account.

## Hardware used : 

* [NodeMCU : ](https://github.com/nodemcu/nodemcu-firmware)
An open-source firmware and development kit that helps you to prototype your IOT product easily.The Development Kit based on ESP8266, integates GPIO, PWM, IIC, 1-Wire and ADC all in one board. Power your developement in the fastest way combinating with NodeMCU Firmware.

<img src="https://github.com/RatulGhosh/Temperature_monitoring_system/blob/master/images/c1s.jpg_450x300.jpg" width="264"/>

* [Buzzer : ](https://en.wikipedia.org/wiki/Buzzer)
 Buzzer or beeper is an audio signalling device, which may be mechanical, electromechanical, or piezoelectric. Typical uses of buzzers and beepers include alarm devices, timers and confirmation of user input such as a mouse click or keystroke.

<img src="https://raw.githubusercontent.com/RatulGhosh/Security-and-Surveillance/master/images/buzzer.jpg" width="264" />



## Working : 
The application continuously records videos and if there is any motion a signal is sent to the Node Mcu which in turn triggers a buzzer. We take the difference of the current frame from the initial frame(the weighted average from the current frame). We then find regions of our image that contain substantial difference from the background model — these regions thus correspond to motion in the video stream. We ingore the difference if it is below a threshold value and if the current image pass the thresholding test we upload that to our dropbox folder.


### Screenshot

<p align="center">
  <img src="https://raw.githubusercontent.com/RatulGhosh/Security-and-Surveillance/master/images/vlcsnap-2016-04-03-10h56m53s340.png" width="264" alt="Screenshot"/>
  <img src="https://raw.githubusercontent.com/RatulGhosh/Security-and-Surveillance/master/images/vlcsnap-2016-04-03-10h56m54s280.png" width="264" alt="Screenshot"/>
  <img src="https://raw.githubusercontent.com/RatulGhosh/Security-and-Surveillance/master/images/vlcsnap-2016-04-03-10h57m03s146.png"
  width="264" alt="Screenshot"/>
<img src="https://raw.githubusercontent.com/RatulGhosh/Security-and-Surveillance/master/images/Capture.PNG"
 alt="Screenshot"/>
 <img src="https://raw.githubusercontent.com/RatulGhosh/Security-and-Surveillance/master/images/giphy.gif"  alt="Screenshot"/> 
  
</p>




### License
# <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat" width="80" />
Note that Security-and-Surveillance is distributed under the [MIT License](http://opensource.org/licenses/MIT).

### TODO
* An app can be made 
* Cloud platform can be used to handle size issues
* More accurate camera can be used


Your feedback, ideas, suggestions are most welcome!
