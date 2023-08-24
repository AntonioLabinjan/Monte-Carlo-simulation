import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (8, 8)
plt.rcParams['figure.dpi'] = 120

nTrials = int(1E4)
radius = 1

nInside = 0
nDrops = 0

XrandCoords = np.random.default_rng().uniform(-1, 1, (nTrials,))
YrandCoords = np.random.default_rng().uniform(-1, 1, (nTrials,))

fig1 = plt.figure(1)
plt.xlim(-1, 1)
plt.ylim(-1, 1)

fig2 = plt.figure(2)

isFirst1 = True
isFirst2 = True

piValueI = []
nDrops_arr = []

insideX = []
outsideX = []
insideY = []
outsideY = []

for i in range(nTrials):
    x = XrandCoords[i]
    y = YrandCoords[i]
    
    nDrops = nDrops + 1
    
    if x**2 + y**2 <= radius**2:
        nInside = nInside + 1
        insideX.append(x)
        insideY.append(y)
    else:
        outsideX.append(x)
        outsideY.append(y)
    
    if i % 100 == 0:
        plt.figure(1)
        
        if isFirst1:
            plt.scatter(insideX, insideY, c='pink', s=50, label='Drop inside')
            isFirst1 = False
        else:
            plt.scatter(insideX, insideY, c='pink', s=50)
        
        plt.figure(1)
        
        if isFirst2:
            plt.scatter(outsideX, outsideY, c='orange', s=50, label='Drop outside')
            isFirst2 = False
        else:
            plt.scatter(outsideX, outsideY, c='orange', s=50)
            
        area = 4 * nInside / nDrops
        plt.figure(1)
        plt.title('No. of pin drops = ' + str(nDrops) + ';       No. inside circle = ' + str(nInside) +
                  r';  π ≈ $4\frac{N_\mathrm{inside}}{N_\mathrm{total}}=$ ' + str(np.round(area, 6)))
        piValueI.append(area)
        nDrops_arr.append(nDrops)
        
        plt.figure(2)
        plt.axhline(y=np.pi, c='darkseagreen', linewidth=2, alpha=0.5)
        plt.plot(nDrops_arr, piValueI, c='mediumorchid')
        plt.title('π estimate vs no. of pin drops')
        plt.annotate('π', [0, np.pi], fontsize=20)
        
        plt.draw()
        plt.pause(0.1)
        
area = 4 * nInside / nTrials
print("Final estimated value of Pi:", area)

plt.show()
