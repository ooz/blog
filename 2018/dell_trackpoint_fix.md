---
title: Dell Trackpoint Fix
date: 2018-02-02T04:00:53Z
---

Alter Dell laptop trackpoint sensitivity under Linux:

```
xinput list
xinput list-props 13
xinput set-prop 13 269 1.0
xinput set-prop 13 269 0.8
xinput set-prop 13 269 0.5
xinput set-prop 13 269 0.1
xinput set-prop 13 268 0.5
xinput set-prop 13 268 0.9
xinput list-props 13
xinput set-prop 13 267 0.9
xinput set-prop 13 267 0.1
xinput set-prop 13 267 2.0
xinput set-prop 13 268 2.0
xinput set-prop 13 268 1.0
xinput set-prop 13 269 0.05
xinput set-prop 13 267 3.0
xinput set-prop 13 267 5.0
xinput set-prop 13 268 2.0
xinput set-prop 13 268 1.5
xinput set-prop 13 267 1.0
xinput set-prop 13 267 2.0
xinput set-prop 13 267 3.0
xinput set-prop 13 267 4.0
xinput set-prop 13 268 2.0
xinput list-props 13
xinput set-prop 13 267 2.5
xinput set-prop 13 268 1.0
xinput set-prop 13 269 12.5
xinput set-prop 13 267 5.0
xinput set-prop 13 267 7.0
xinput set-prop 13 268 2.0
xinput set-prop 13 267 10.0
xinput set-prop 13 268 3.0
xinput set-prop 13 268 5.0
xinput set-prop 13 267 15.0
xinput set-prop 13 267 12.0
xinput set-prop 13 267 11.0

# $ xinput list-props 13
# Device 'AlpsPS/2 ALPS DualPoint Stick':
# 	Device Enabled (140):	1
# 	Coordinate Transformation Matrix (142):	1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 0.000000, 1.000000
# 	Device Accel Profile (266):	0
# 	Device Accel Constant Deceleration (267):	11.000000
# 	Device Accel Adaptive Deceleration (268):	5.000000
# 	Device Accel Velocity Scaling (269):	12.500000
# 	Device Product ID (261):	2, 8
# 	Device Node (262):	"/dev/input/event6"
# 	Evdev Axis Inversion (305):	0, 0
# 	Evdev Axes Swap (307):	0
# 	Axis Labels (308):	"Rel X" (150), "Rel Y" (151)
# 	Button Labels (309):	"Button Left" (143), "Button Middle" (144), "Button Right" (145), "Button Wheel Up" (146), "Button Wheel Down" (147), "Button Horiz Wheel Left" (148), "Button Horiz Wheel Right" (149)
# 	Evdev Scrolling Distance (310):	0, 0, 0
# 	Evdev Middle Button Emulation (311):	1
# 	Evdev Middle Button Timeout (312):	50
# 	Evdev Third Button Emulation (313):	0
# 	Evdev Third Button Emulation Timeout (314):	1000
# 	Evdev Third Button Emulation Button (315):	3
# 	Evdev Third Button Emulation Threshold (316):	20
# 	Evdev Wheel Emulation (317):	1
# 	Evdev Wheel Emulation Axes (318):	6, 7, 4, 5
# 	Evdev Wheel Emulation Inertia (319):	10
# 	Evdev Wheel Emulation Timeout (320):	200
# 	Evdev Wheel Emulation Button (321):	2
# 	Evdev Drag Lock Buttons (322):	0
```
