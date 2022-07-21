import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dict = {
    'country': ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
    'capital': ['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria'],
    'area': [8.516, 17.10, 3.286, 9.597, 1.221],
    'population': [200.4, 143.5, 1252, 1357, 52.98]
}

print(dict)

brics = pd.DataFrame(dict)
brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']

print(brics)

colors = np.array(['green', 'blue', 'orange', 'red', 'yellow'])
sizes = np.array([dict["population"][0]/dict["area"][0], dict["population"][1]/dict["area"][1]
                     , dict["population"][2]/dict["area"][2], dict["population"][3]/dict["area"][3]
                     , dict["population"][4]/dict["area"][4]])
plt.scatter(dict['area'], dict['population'],c=colors, s=sizes)



plt.xlabel('Area (km²)')
plt.ylabel('Population (M)')
plt.title('Population / Area Rate', color='red')
plt.text(8.516, 200.4, f'Brazil ({dict["population"][0]/dict["area"][0]:.2f})')
plt.text(17.10, 143.5, f'Russia ({dict["population"][1]/dict["area"][1]:.2f})')
plt.text(3.286, 1252, f'India ({dict["population"][2]/dict["area"][2]:.2f})')
plt.text(9.597, 1357, f'China ({dict["population"][3]/dict["area"][3]:.2f})')
plt.text(1.221, 52.98, f'South Africa ({dict["population"][4]/dict["area"][4]:.2f})')
plt.show()