
Here is a short pin layout explanation. Look for Raspberry Pi and L293D pinout online.
Be carefull with the L293D chip it overheats qiute fast you may need a active colling
or some heat sinks. 




```
Raspberry Pi-           -L293D-             	-Power 2 Amp 5v-      	-Motor
Pin 2  +5v             	Vcc 1 (Vss)
Pin 3  GPIO 2           Enable 1,2,3,4
Pin 6  GND              Ground
Pin 5  GPIO 3  black    Input 1
Pin 7  GPIO 4  blue     Input 2
Pin 13 GPIO 27 green    Input 3
Pin 15 GPIO 22 red      Input 4   
			Ground             	 "- pole/ground"
			Vcc 2 (Vs)          	"+ pole/ + 5v "
			Output 1 	 				A+ black
			Output 2					A- blue
			Output 3					B+ green
			Output 4					B- red
```
