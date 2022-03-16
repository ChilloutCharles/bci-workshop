## README

This is my fork of the workshop code that sends relaxation and focus metrics to vrchat avatar paramaters via OSC

**Demos** 
- [VRCHAT OSC MAGIC! (Last 30 seconds)](https://twitter.com/kentrl_z/status/1497020472046800897)
- [Old version of Brain Controlled Ears](https://www.youtube.com/watch?v=WjWc51xNgKg)

**Instructions**
1. See the document `INSTRUCTIONS.md` for instructions on how to prepare your pc hardware, bluetooth, and install the base packages. Specifically: the intro, sections A1 and A2. Don't worry about muse-lsl. We'll replace that with the next step.
3. Instead of following section A3, download the *Experimental* version of [Petal Metrics App](https://petal.tech/downloads).
4. Install [python-osc](https://pypi.org/project/python-osc/)
5. Turn on your Muse headset and click on Stream in the Petal App. The headset will connect automatically and stream data via LSL
6. Run the script `python\osc_multichannel.py`. That will start sending OSC messages to set Avatar Parameters

**OSC Avatar Parameters**

Avatar parameters being sent are floats that range from -1.0 to 1.0. Negative and Positive values correspond to low and high focus/relaxation. Left and right sides of the brain are measured and can be recieved by VRC seperately. Update your avatar paramaters as needed to influnece animations and the like. Have fun!

- `/avatar/parameters/osc_relax_left`
- `/avatar/parameters/osc_relax_right`
- `/avatar/parameters/osc_focus_left`
- `/avatar/parameters/osc_focus_right`

Adjusting sensitivity per OSC path can be done by having float parameters in your avatar that are prefixes of the paramater name + '_tune'.
This will allow you to adjust how reactive the metrics are on the fly from your radial menu.
For example, having a parameters named `osc_relax_tune` will adjust the sensitivity for the paramaters:

- `/avatar/parameters/osc_relax_left`
- `/avatar/parameters/osc_relax_right`
- `/avatar/parameters/osc_relax_avg`

While having a parameter named `osc_relax_left_tune` will only adjust `/avatar/parameters/osc_relax_left`

**Interplay with other OSC programs**

Considering that sensitivity adjustment requires receiving data back from vrchat, other OSC programs might fight over port `9001`. The server part of this code has been changed so that it will forward vrchat messages on port `9002` by default. You can also change the receive, send, and forward ports in the OSC threads section of `python/osc_multichannel.py` (line 87)

**Deprecated OSC Avatar Parameters**

These paramaters have been deprecated. They will always report the left channels since taking the average of each side of the brain averages the noise as well:

- `/avatar/parameters/osc_relax_avg`
- `/avatar/parameters/osc_focus_avg`


## License
[MIT](http://opensource.org/licenses/MIT).



