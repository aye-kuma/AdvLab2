import numpy as np
import matplotlib.pyplot as plt

path1 = "/Users/theo/Desktop/PHYS 471/SpeedOfSound2-23-2023/SoS10.17.12AM.TED-edit.csv"
data1 = np.genfromtxt(path1, delimiter=',', names=['X1','Y1',' ','X2','Y2'])

path2 = "/Users/theo/Desktop/PHYS 471/SpeedOfSound2-23-2023/SoS10.18.19AM.TED-edit.csv"
data2 = np.genfromtxt(path2, delimiter=',', names=['X1','Y1',' ','X2','Y2'])

path3 = "/Users/theo/Desktop/PHYS 471/SpeedOfSound2-23-2023/SoS10.19.13AM.TED-edit.csv"
data3= np.genfromtxt(path3, delimiter=',', names=['X1','Y1',' ','X2','Y2'])

path4 = "/Users/theo/Desktop/PHYS 471/SpeedOfSound2-23-2023/SoS10.20.11AM.TED-edit.csv"
data4 = np.genfromtxt(path4, delimiter=',', names=['X1','Y1',' ','X2','Y2'])

path5 = "/Users/theo/Desktop/PHYS 471/SpeedOfSound2-23-2023/SoS10.21.29AM.TED-edit.csv"
data5 = np.genfromtxt(path5, delimiter=',', names=['X1','Y1',' ','X2','Y2'])

path6 = "/Users/theo/Desktop/PHYS 471/SpeedOfSound2-23-2023/SoS10.22.25AM.TED-edit.csv"
data6 = np.genfromtxt(path6, delimiter=',', names=['X1','Y1',' ','X2','Y2'])

path7 = "/Users/theo/Desktop/PHYS 471/SpeedOfSound2-23-2023/SoS10.23.26AM.TED-edit.csv"
data7 = np.genfromtxt(path7, delimiter=',', names=['X1','Y1',' ','X2','Y2'])

path8 = "/Users/theo/Desktop/PHYS 471/SpeedOfSound2-23-2023/SoS10.24.26AM.TED-edit.csv"
data8 = np.genfromtxt(path8, delimiter=',', names=['X1','Y1',' ','X2','Y2'])


plt.plot(data4['X1'],data4['Y1'], color='blue', label='CH1')
plt.plot(data4['X2'],data4['Y2'], color='red', label='CH2')
plt.xlim(-0.00025,0.001)
plt.ylim(0,6)
plt.xlabel('Time' + '[\u03BC' + 's]' )
plt.ylabel('Voltage [mV]')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.title('Measurement 4')
plt.grid()
plt.legend()
plt.show()

"""avgY1 = []
avgY2 = []

for i in range(0,len(data1['X1'])):
    y1 = data1[i]['Y1'] + data2[i]['Y1'] + data3[i]['Y1'] + data4[i]['Y1'] + data5[i]['Y1'] + data6[i]['Y1'] + data7[i]['Y1'] + data8[i]['Y1']
    y2 = data1[i]['Y2'] + data2[i]['Y2'] + data3[i]['Y2'] + data4[i]['Y2'] + data5[i]['Y2'] + data6[i]['Y2'] + data7[i]['Y2'] + data8[i]['Y2']
    avgy1 = y1 / 8
    avgy2 = y2 / 8
    avgY1.append(avgy1)
    avgY2.append(avgy2)
    i += 1

plt.plot(data1['X1'], avgY1, color='red', label='Average of CH1 measurements')
plt.plot(data1['X2'], avgY2, color='blue',label='Average of CH2 measurements')
plt.xlim(-0.001,0.001)
#plt.ylim(-1,6)
plt.xlabel('Time' + '[\u03BC' + 's]' )
plt.ylabel('Voltage [mV]')
plt.legend()
plt.grid()
plt.show()"""
