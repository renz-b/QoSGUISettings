## QoSGUISettings
Automated getting the settings of my router using selenium and show it on a GUI using DearPyGUI. This will save me a few clicks on knowing my router settings and changing them on the GUI.
- Clicks on or off button and turns settings, respectively. No need to re run, buttons work during runtime.

### DearPyGUI
![QoSScreenshot](https://user-images.githubusercontent.com/69705483/103144301-2e0e7a80-4762-11eb-9341-bbca5f1c1e39.png)

#### V 1.0.0:
- Simple GUI with On and Off button

#### To Do:
- Tried radio buttons with an 'Apply' button, failed to get_value of data from radio buttons during runtime. Once the value was set it does not change.
- Failed adding an 'Updated settings changed to:' text. Having a hard time getting values once variables are set. Upon starting, qos is set to 'Off' when changed to on and confirmed using debug, print statements, and manually checking the settings it would still show in the GUI that it is 'Off' not 'On.
