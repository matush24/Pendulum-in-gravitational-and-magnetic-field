import numpy as np
import matplotlib.pyplot as plt

# Interesting values for [Bz, t('stop' if 'start'=0)]: (x and y components of B are 0, q=1, m=1, gz=[0, 0,-9.81], l=1, phi=pi/10)
# [2.3, 2.9], [3.75, 3.5], [4.88, 4], [1.32, 5], [2.62, 15.1], [3.92, 25.1], 

# Setting parameters of pendulum
q = 1
m = 1
g = np.array([0, 0, -9.81])
B = np.array([0, 0, 1.32])
r0 = np.array([0, 0, 0])
l = 1
phi = np.pi/10

start, stop, dt = 0, 5, 0.0002

# preparing variables in t('start') and time
r = np.array([[np.sin(phi), 0, -np.cos(phi)]])
v = np.array([[0, 0, 0]])
aOld = np.array([0, 0, 0])

time = np.arange(start, stop, dt)


for t in time:
    # calculating tension in string
    # firstly, it should compensate parallel components of other forces to the string
    # secondly it should serve as centripetal force
    T = (np.dot((r[-1]-r0)/np.linalg.norm(r[-1]-r0), (m*g+q*np.cross(v[-1], B))) + m*np.dot(v[-1], v[-1])/np.linalg.norm(r0-r[-1]))*(r0-r[-1])
    # calculating acceleration
    a = (T + m*g + q*np.cross(v[-1], B))/m

    # trapezoidal numerical integration
    v = np.append(v, [v[-1] + (a + aOld)*dt/2], axis=0)
    aOld = a
    r = np.append(r, [r[-1] + (v[-1] + v[-2])*dt/2], axis=0)
    
    # checking, if simulation is accurate enought
    if abs(np.linalg.norm(r[-1]-r0)) - l > 0.01*l:
        print(np.linalg.norm(r[-1]-r0))

# Prepare lists of positions for chart
x, y, z = [], [], []
for i in r:
    x.append(i[0])
    y.append(i[1])
    z.append(i[2])

# Create chart
ax = plt.axes(projection='3d')
ax.plot(x, y, z)

# Set labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# show chart
plt.show()
