# Pendulum in gravitational and magnetic field

Welcome to the simulation of pendulum in gravitational and magnetic field. Although simulation propably holds for variety of mutal orientations of fields, we are particulary interested in parallel case. Mainly because of the symetri of the whole problem. 

## Forces
The only interesting part of the simulation is the computation of forces acting on the pendulum. 
There are three.

Gravitational: $\vec{F_g} = m\vec{g}$

Magnetic: $\vec{F_m} = q(\vec{v} \times \vec{B})$

And than there force from tension in the string. This one is a bit tricky to express as it is as big as it needs to be. We know it has to compensate for all parts of other forces parallel to the string. Aditionaly, it has to act as a centripetal force. Therefore we calculate it as:

$$T = \left(\left( \frac{\vec{l}}{l} \right) \cdot \left( m\vec{g} + q(\vec{v} \times \vec{B}) \right) + \frac{mv^2}{l} \right)(-\vec{l})$$

Acceleration is then: $$\vec{a} = \frac{\vec{F_g} + \vec{F_m} + \vec{T}}{m}$$

## Integration
Integration is done simply by suming trapezoids.

## Using simulation
Changed should be variables in section `Setting parameters of pendulum`. After changing them, also integration step `dt` should be checked. If there is not a sharp edge at the tips, integration step should be reduced. Feel free to try it out : )

## Conclusions
(Done after playing some time with the simulation.)

Period of the pendulum is not independent of the magnetic field. Therefore making it harder co come up with simple equation for B and t for star with $n$ tips.
