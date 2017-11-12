"""
Dendrogram and Heatmap generator
Cluster assigner

@author: Vinicius Alves
"""

import numpy as np
import pandas as pd

import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist, squareform
import pylab

import matplotlib.pyplot as plt
from matplotlib import gridspec


# Parameters
np.set_printoptions(precision=4, suppress=True)

# Open and prepare data
df = pd.read_csv('data_example\\descriptors.csv', sep=',')
X = df.iloc[:100,1:].values
#X = np.memmap(X, dtype='float32', mode='w+', shape=(50000,117))

# Calculate distance matrix for dendrogram
D = pdist(X, 'euclidean')
Dm = squareform(D)


# Dendrogram
fig = plt.figure(figsize=(18,6))
plt.style.use('seaborn-whitegrid')
G = gridspec.GridSpec(1, 3, wspace=0, hspace=0.1,
                      top=0.86, bottom=0.08,
                      left=0.14, right=0.9)
ax0 = plt.subplot(G[0, :-1])
Z = sch.linkage(D, method='complete')
sch.set_link_color_palette(['r', 'b', 'g', 'm', 'y', 'c'])
dn = sch.dendrogram(Z,
                    orientation='left',
                    distance_sort='descending',
                    no_labels=True,
                    above_threshold_color='k',
                    color_threshold=110,
                    )
#plt.xticks(np.arange(0, 1500, 100))
plt.margins(0.5, 0.1)
plt.title('Dendrogram', fontsize=20)
plt.xlabel('Euclidean distance', fontsize=14)
plt.axvline(x=110)


# Generate heatmap
ax1 = plt.subplot(G[0, -1])
idx = dn['leaves']
Dm = Dm[idx,:]
Dm = Dm[:,idx]
cm = pylab.cm.gist_rainbow
im = ax1.imshow(Dm, cmap=cm, alpha=0.9,
                vmin=0, vmax=1000,
                aspect='auto', origin='lower'
                )
plt.colorbar(im, fraction=0.06, pad=0.03)
plt.title('Heatmap', fontsize=20)
ax1.grid(b='off')
ax1.set_yticklabels([])
ax1.set_xticklabels([])

fig.savefig('figure.png', bbox_inches='tight',
            transparent=True, format='png', dpi=300)

C = sch.fcluster(Z, t=16, criterion='maxclust')
C = pd.DataFrame(C, index=None, columns=['clid'])
C.index += 1
C.index.names = ['id']
C.to_csv('list_of_clusters.txt', header=True, index=True, sep='\t')

