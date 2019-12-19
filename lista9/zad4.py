import matplotlib.pyplot as plt
import numpy as np
jezyki = ['Java', 'C', 'Python', 'C++', 'C#', 'Visual Basic .NET', 'JavaScript', 'PHP',
         'SQL', 'Swift']
wartosci = [17.253, 16.086, 10.309, 6.196, 4.801, 4.743, 2.090, 2.048, 1.843, 1.490]

index = np.arange(len(jezyki))
plt.bar(index, wartosci, color='g')
plt.xlabel('Język')
plt.ylabel('Procent')
plt.xticks(index, jezyki, fontsize=8, rotation=90)
plt.title('Popularność języków programowania')
plt.show()
