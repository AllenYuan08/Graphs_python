import numpy as np
import matplotlib.pyplot as plt

# data
labels = ['OCI-M', 'OMI-C', 'OCM-I', 'ICM-O']
CLIP_V = [98.76, 98.89, 97.92, 98.12]
CLIP = [99.13, 98.89, 98.45, 98.12]
CoOp = [99.08, 98.88, 98.52, 98.97]
CEPL_Ours = [99.28, 99.10, 98.41, 99.42]
data = [CLIP_V, CLIP, CoOp, CEPL_Ours]

# data names
data_names = ['CLIP-V', 'CLIP', 'CoOp', 'CEPL_Ours']

# zoom
max_vals = [100, 99.5, 99, 98.5]
scaled_data = []
for d, max_val in zip(data, max_vals):
    scale_factor = max_val / max(d)
    scaled_d = [i * scale_factor for i in d]
    scaled_data.append(scaled_d)

# angle
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
# close
for d in scaled_data:
    d.append(d[0])
angles += angles[:1]

# plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
colors = ['red', 'yellow', 'purple', 'blue']

for i, d in enumerate(scaled_data):
    ax.plot(angles, d, color=colors[i], linewidth=2, label=labels[i])
    ax.fill(angles, d, color=colors[i], alpha=0.25)

# set y range
ax.set_ylim(95, 100)

# set y ticks
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_yticklabels([])  # Hide the default radial tick labels
# the outer circular boundary
# ax.spines['polar'].set_visible(False)

# set custom radial tick labels
custom_ticklabels = [
    [96, 97, 98, 99],
    [96.5, 97.5, 98.5],
    [96, 97, 98],
    [96.2, 97.2, 98.2, 99.2]
]

for angle, ticklabels in zip(angles, custom_ticklabels + [custom_ticklabels[0]]):
    for r in ticklabels:
        # if r != 95 and 95.5 and 95.2 and 96:
        ax.text(angle, r, '{:.1f}'.format(r), ha='center', va='center')


# add legend
ax.legend(handles=ax.lines, labels=data_names, loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.show()
