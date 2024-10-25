We have developed a simple driver software for L293D chip in combination whith R-Pi. It
should be compatible with most 4 channel stepper motors.
It's  easy to use just open the file in your coding program like Thonny and press run. 
Now you should be able to enter the amount of steps for the motor. 
At the bottom you find the correct wiring to use the program with your Raspberry Pi.
The current of the power source can vary so be sure that the motor has enough power to operate.






Here is a short pin layout explanation. Look for Raspberry Pi and L293D pinout online.
Be carefull with the L293D chip it overheats quite fast you may need a active colling
or some heatsinks. 




```
Raspberry Pi-           -L293D-             	-Power 2 Amp 5v-      	-Motor
Pin 2  +5v             	Vcc 1 (Vss)
Pin 3  GPIO 2           Enable 1,2,3,4
Pin 6  GND              Ground
Pin 5  GPIO 3  black    Input 1
Pin 7  GPIO 4  blue     Input 2
Pin 13 GPIO 27 green    Input 3
Pin 15 GPIO 22 red      Input 4   
			Ground             	"- pole/ground"
			Vcc 2 (Vs)          	"+ pole/ + 5v "
			Output 1 	 				A+ black
			Output 2					A- blue
			Output 3					B+ green
			Output 4					B- red
```

## Feedback

If you have any feedback, please reach out to us at management@torspace.net
