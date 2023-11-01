import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# data
labels = ['OCI-M', 'OMI-C', 'OCM-I', 'ICM-O']
CLIP_V = [98.76, 98.89, 97.92, 98.12]
CLIP = [99.13, 98.89, 98.45, 98.12]
CoOp = [99.08, 98.88, 98.52, 98.97]
CFPL_Ours = [99.28, 99.10, 98.41, 99.42]
data = [CLIP_V, CLIP, CoOp, CFPL_Ours]

# data names
data_names = ['CLIP-V', 'CLIP', 'CoOp', 'CFPL_Ours']

# determine scale factors for each value
max_vals = [99.52, 99.73, 99.15, 100]
scale_factors = []
for i, max_val in enumerate(max_vals):
    max_data_at_i = max([d[i] for d in data])
    scale_factor = max_val / max_data_at_i
    scale_factors.append(scale_factor)
print(scale_factors)

# scale the data
scaled_data = []
for d in data:
    scaled_d = [value * scale_factors[i] for i, value in enumerate(d)]
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

# Hide the outer circle
ax.spines['polar'].set_visible(False)

# set y range
ax.set_ylim(95, 100)

# set y ticks
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_yticklabels([])  # Hide the default radial tick labels
# the outer circular boundary
ax.spines['polar'].set_visible(False)

# set custom radial tick labels
actual_ticks_list = [
    [96, 97, 98, 99],
    [96, 97, 98, 99],
    [96, 97, 98, 99],
    [96, 97, 98, 99]
]
# mutiply by scale factor
custom_labels_list = [None] * len(actual_ticks_list)
for i, actual_ticks in enumerate(actual_ticks_list):
    custom_labels_list[i] = [tick * scale_factors[i] for tick in actual_ticks]
# custom_labels_list = [
#     [96.5, 97.5, 98.3, 99.1, 100],
#     [96.1, 97.4, 98.2, 99.3, 99.6],
#     [95.2, 96.7, 97.2, 98.9, 99.7],
#     [95.3, 96.3, 97.3, 98.3, 99]
# ]
print(custom_labels_list)

for angle, actual_ticks, custom_labels in zip(angles[:-1], actual_ticks_list, custom_labels_list):
    for r, label in zip(actual_ticks, custom_labels):
        ax.text(angle, r, '{:.1f}'.format(label), ha='center', va='center', color='black')

# erase the radial tick labels of the outer circle
ax.set_rticks(list(range(96, 100)))

# add legend
ax.legend(handles=ax.lines, labels=data_names, loc='upper right', bbox_to_anchor=(1.1, 1.1))

# create custom handles
handles = [mlines.Line2D([], [], color=color, linewidth=3, label=label) 
           for color, label in zip(colors, labels)]

ax.legend(handles=handles, loc='upper right')

# add title
ax.set_title("The Results of HTER on Protocol 1", fontsize=16, fontweight='bold')

# add x tick labels as bold
for label in ax.get_xticklabels():
    label.set_weight('bold')

# adjust the position of the labels
ax.tick_params(axis='x', which='major', pad=10)

# adjust the position of the labels
labels = ax.get_xticklabels()

# adjust the position of the labels
label1 = labels[1]
label1.set_position((label1.get_position()[0], label1.get_position()[1] + 0.05))
label3 = labels[3]
label3.set_position((label3.get_position()[0], label3.get_position()[1] + 0.04))


plt.show()
