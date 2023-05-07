import numpy as np
import matplotlib.pyplot as plt 

Aperture = [0.5, 0.75, 1, 2]
ExpIntensity = [0.2925, 0.6304, 0.6374, 0.7598]
Power = 0.8

Aperture = np.array(Aperture)

TheoryIntensity = Power*Aperture**2

Area = np.pi * (Aperture/2)**2


plt.scatter(Area, ExpIntensity, label='Experimental')
#plt.scatter(Aperture, ExpIntensity, label="Experimental")
plt.plot(Area, TheoryIntensity, label='Theory')
plt.xlabel('Aperture (Area in mm^2)')
#plt.xlabel('Aperture (mm)')
plt.ylabel('Intensity [A.U]')
plt.legend()
plt.show()
