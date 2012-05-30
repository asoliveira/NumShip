import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
plt.subplot(311)
t = np.arange(0.01, 10.0, 0.01)
s1 = np.exp(t)
plt.plot(t, s1, 'b-')
plt.xlabel('time (s)')
plt.ylabel('exp')

plt.twinx()
s2 = np.sin(2*np.pi*t)
plt.plot(t, s2, 'r.')
plt.ylabel('sin')
plt.show()
