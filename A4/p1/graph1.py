import operator
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from statistics import median
import math


x = [1,2,40,48,51,55,68,76,85,94,98,108,122,127,135,139,146,155,167,191,195,205,210,225,238,253,256,261,266,266,267,283,287,290,311,320,322,323,325,339,341,348,356,357,360,361,383,389,393,395,397,431,434,450,451,457,467,474,482,486,495,510,536,537,561,571,577,579,591,595,627,633,635,643,654,693,705,707,708,748,758,776,821,827,851,907,916,949,984,993,1145,1250,1427,1446,1559,1757,1931,2143,3955]
mean = 538
medium = 395
std = 535.98
anwala = 98

plt.plot(x)
plt.suptitle('Anwala Friends')
plt.plot([62],mean,marker='x',markersize=4, color='red', label = 'Mean = 538')
plt.plot([61],std,marker='x',markersize=4, color='orange', label = 'Std Dev = 535.98')
plt.plot([45],medium,marker='x',markersize=4, color='blue', label = 'median = 395')
plt.plot([10],anwala,marker='x',markersize=4, color='green', label = 'Anwala = 98')
plt.legend()
plt.ylabel('# of Friends')
plt.xlabel('Index of Friends')
plt.show()