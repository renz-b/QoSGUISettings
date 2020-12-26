## QoSGUISettings
Automated getting the settings of my router using selenium and show it on a GUI using DearPyGUI. This will save me a few clicks on knowing my router settings and changing them on the GUI.
- Clicks on or off button and turns settings, respectively. No need to re run, buttons work during runtime.

### DearPyGUI
![QoSScreenshot](https://user-images.githubusercontent.com/69705483/103144411-d83ad200-4763-11eb-84c6-61ae2b49a14a.png)

### Code
![Code](https://user-images.githubusercontent.com/69705483/103144409-d4a74b00-4763-11eb-820b-195bd9cf7b1c.png)
Even though this is a simple project which automates a few clicks, I used different packages and tried out new modules while reading docs. 
Packages and methods used:
- WebDriverWait from selenium that polls the website if its already loaded and executes it if it does. Instead of using time.sleep which would take a constant amount of time and throws errors if the web page does not load in time. 
- dotenv packages, finally got to learn and read about environment variables and how crucial it is to hide information you would not want others to know.
- DearPyGUI, I learned how to use tkinter but it was not pleasing to the eyes.

#### V 1.0.0:
- Simple GUI with On and Off button

#### To Do:
- Tried radio buttons with an 'Apply' button, failed to get_value of data from radio buttons during runtime. Once the value was set it does not change.
