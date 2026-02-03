import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

np.random.seed(23685752)
N_points = 10000
n_bins = 20

x = np.random.randn(N_points)
y = 0.8**x + np.random.randn(N_points)+25
legend = ['distribution']

fig, axs = plt.subplots(1,1, figsize=(10,7), tight_layout=True)

for s in ['top', 'bottom', 'left', 'right']:
    axs.spines[s].set_visible(False)

axs.xaxis.set_ticks_position('none')
axs.yaxis.set_ticks_position('none')
axs.xaxis.set_tick_params(pad=5)
axs.yaxis.set_tick_params(pad=10)

axs.grid(visible=True, color='grey', linestyle='-', linewidth=0.5, alpha=0.6)

fig.text(0.9, 0.15, 'Akash Nair', fontsize=12, color='blue', ha='right', va='bottom', alpha=0.7)

N, bins, patches = axs.hist(x, bins=n_bins)

fracs = ((N**(1/5))/N.max())
norm = colors.Normalize(fracs.min(), fracs.max())
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(legend)
plt.title('Histogram with watermark')
plt.show()

plt.show()