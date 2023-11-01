import numpy as np
import matplotlib.pyplot as plt

# data
labels = ['OCI-M', 'OMI-C', 'OCM-I', 'ICM-O']
CLIP_V = [98.76, 98.89, 97.92, 98.12]
CLIP = [99.13, 98.89, 98.45, 98.12]
CoOp = [99.08, 98.88, 98.52, 98.97]
CFPL_Ours = [99.28, 99.10, 98.41, 99.42]
data = [CLIP_V, CLIP, CoOp, CFPL_Ours]

data_names = ['CLIP-V', 'CLIP', 'CoOp', 'CFPL_Ours']

# angle
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

# close
for d in data:
    d.append(d[0])

angles += angles[:1]

# draw
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
colors = ['blue', 'yellow', 'purple', 'red']

for i, d in enumerate(data):
    ax.plot(angles, d, color=colors[i], linewidth=2, label=labels[i])
    ax.fill(angles, d, color=colors[i], alpha=0.25)

# set y range
ax.set_ylim(97, 99.5)
ax.set_yticks(np.arange(97, 100, 0.5))

# the outer circular boundary
ax.spines['polar'].set_visible(False)

# set labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

ax.set_yticklabels([])  # Hide the default radial tick labels
# the outer circular boundary
ax.spines['polar'].set_visible(False)

# set custom radial tick labels
custom_ticklabels = [
    [97.1, 98.1, 99.1],
    [97.5, 98.3, 99,1],
    [97.6, 98.2, 98.8],
    [97.2, 98.2, 99.2]
]

for angle, ticklabels in zip(angles, custom_ticklabels + [custom_ticklabels[0]]):
    for r in ticklabels:
        # if r != 95 and 95.5 and 95.2 and 96:
        ax.text(angle, r, '{:.1f}'.format(r), ha='center', va='center')

# set custom radial tick labels
ax.legend(handles=ax.lines, labels=data_names, loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.show()
