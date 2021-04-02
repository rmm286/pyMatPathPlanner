#!/usr/local/python

import matlab.engine
from math import pi

x0 = 0
y0 = 0
th0 = pi/2.0
k0 = 0
kDot0 = 0
v0 = 1
vDot0 = 0

start = [x0,y0,th0,k0,kDot0,v0,vDot0]

xf = 1
yf = 0
thf = (-1/2.0)*pi
kf = 0
kDotf = 0
vf = 1
vDotf = 0

goal = [xf, yf, thf, kf, kDotf, vf, vDotf]

eng = matlab.engine.start_matlab()

state, control = eng.PlanPath(start, goal,nargout = 2)

print(state)
print(control)
