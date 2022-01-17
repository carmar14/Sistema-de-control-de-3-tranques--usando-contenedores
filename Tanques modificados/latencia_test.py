import matplotlib.pyplot as plt
import numpy as np
import scipy.io
import seaborn as sns


def adjacent_values(vals, q1, q3):
    upper_adjacent_value = q3 + (q3 - q1) * 1.5
    upper_adjacent_value = np.clip(upper_adjacent_value, q3, vals[-1])

    lower_adjacent_value = q1 - (q3 - q1) * 1.5
    lower_adjacent_value = np.clip(lower_adjacent_value, vals[0], q1)
    return lower_adjacent_value, upper_adjacent_value



# -------------------nuevas pruebas-------------------
fig7, axs7 = plt.subplots(nrows=1, ncols=1, figsize=(9, 4))

# -----------------sample time 5ms-----------------
mat = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\cyberattack_ph\control_ph_python\Modulos para contenedores\singu\latencia2.mat')
mat2 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\cyberattack_ph\control_ph_python\Modulos para contenedores\singu\lat_cm_rt.mat')
mat3 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\cyberattack_ph\control_ph_python\Modulos para contenedores\singu\lat_control_slave_rt.mat')
mat4 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\cyberattack_ph\control_ph_python\Modulos para contenedores\singu\lat_proceso_slave_rt.mat')
# -------latencias-------
# lat_ = mat['lat'] * 1000 # .tolist()
lat_ = mat['lat']  # .tolist()
lat_cm_rt = mat2['lat_cm_rt'] * 1000  # .tolist()
lat_cs_rt = mat3['lat_cs_rt'] * 1000
lat_ps_rt = mat4['lat_ps_rt'] * 1000

'''
lat = np.append(lat_, lat_cm_rt, axis=0)
lat = np.append(lat, lat_cs_rt, axis=0)
lat = np.append(lat, lat_ps_rt, axis=0)
'''
lat = np.append(lat_cm_rt, lat_cs_rt, axis=0)
lat = np.append(lat, lat_ps_rt, axis=0)
lat = lat.tolist()

# print(type(lat))
# print(len(lat))


max_ = np.amax(lat_)
min_ = np.amin(lat_)
mu = lat_.mean()
median = np.median(lat_)
sigma = lat_.std()
textstr = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props = dict(boxstyle='round', facecolor='#8B8CDB', alpha=0.5)

cell_text = np.empty((3, 5))
# cell_text[0][0] = mu
# cell_text[0][1] = median
# cell_text[0][2] = sigma
# cell_text[0][3] = max_
# cell_text[0][4] = min_

max_ = np.amax(lat_cm_rt)
min_ = np.amin(lat_cm_rt)
mu = lat_cm_rt.mean()
median = np.median(lat_cm_rt)
sigma = lat_cm_rt.std()
textstr2 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props2 = dict(boxstyle='round', facecolor='#8B1F8A', alpha=0.5)

cell_text[0][0] = mu
cell_text[0][1] = median
cell_text[0][2] = sigma
cell_text[0][3] = max_
cell_text[0][4] = min_

max_ = np.amax(lat_cs_rt)
min_ = np.amin(lat_cs_rt)
mu = lat_cs_rt.mean()
median = np.median(lat_cs_rt)
sigma = lat_cs_rt.std()
textstr3 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props3 = dict(boxstyle='round', facecolor='#FF1F8A', alpha=0.5)

cell_text[1][0] = mu
cell_text[1][1] = median
cell_text[1][2] = sigma
cell_text[1][3] = max_
cell_text[1][4] = min_

max_ = np.amax(lat_ps_rt)
min_ = np.amin(lat_ps_rt)
mu = lat_ps_rt.mean()
median = np.median(lat_ps_rt)
sigma = lat_ps_rt.std()
textstr4 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props4 = dict(boxstyle='round', facecolor='#DF5014', alpha=0.5)

cell_text[2][0] = mu
cell_text[2][1] = median
cell_text[2][2] = sigma
cell_text[2][3] = max_
cell_text[2][4] = min_

# place a text box in upper left in axes coords

# axs7.text(0.12, 0.35, textstr, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props)
axs7.text(0.23, 0.35, textstr2, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props2)
axs7.text(0.53, 0.35, textstr3, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props3)
axs7.text(0.75, 0.35, textstr4, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props4)
# axs7.text(0.57, 0.35, textstr5, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props5)
# axs7.text(0.65, 0.25, textstr6, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props6)
# axs7.text(0.77, 0.25, textstr7, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props7)
# axs7.text(0.9, 0.25, textstr8, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props8)

columns = ('$\mu$', '$\mathrm{Median}$', '$\sigma$', '$Worst$', '$Best$')
rows = ['Singularity Controller Master', 'Singularity Controller Slave', 'Singularity Process Slave']
# rows = ['Singularity Detection system', 'Singularity Controller Master',
#       'Singularity Controller Slave', 'Singularity Process Slave']
# 'Detection system', 'RT-Linux Controller Master', 'RT-Linux Controller Slave',
# 'RT-Linux Process Slave' ]

cell_text = np.round(cell_text, 4)
# print(cell_text.shape)
figt7, axt7 = plt.subplots()
axt7.set_axis_off()
table = axt7.table(cellText=cell_text, rowLabels=rows, colLabels=columns, rowColours=["grey"] * 10,
                   colColours=["grey"] * 10, cellLoc='center', loc='center', colWidths=[0.1, 0.1, 0.1, 0.1, 0.1])

# plot violin plot
parts = axs7.violinplot(lat, showmeans=False, showmedians=False,
                        showextrema=False)
# parts = axs.violinplot(lat_.tolist(), showmeans=False, showmedians=True)
i = 1
for pc in parts['bodies']:
    if i == 1:
        pc.set_facecolor('#8B8CDB')
    if i == 2:
        pc.set_facecolor('#8B1F8A')
    if i == 3:
        pc.set_facecolor('#FF1F8A')
    '''
    if i == 4:
        pc.set_facecolor('#DF5014')

    if i == 5:
        pc.set_facecolor('#005714')
    if i == 6:
        pc.set_facecolor('#351554')
    if i == 7:
        pc.set_facecolor('#790020')
    if i == 8:
        pc.set_facecolor('#0093AC')
    '''
    pc.set_edgecolor('black')
    pc.set_alpha(1)
    i = i + 1

quartile1, medians, quartile3 = np.percentile(lat, [25, 50, 75], axis=1)
whiskers = np.array([
    adjacent_values(sorted_array, q1, q3)
    for sorted_array, q1, q3 in zip(lat, quartile1, quartile3)])
whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]

inds = np.arange(1, len(medians) + 1)
axs7.scatter(inds, medians, marker='_', color='k', s=30, zorder=3)
axs7.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=1)
axs7.vlines(inds, whiskers_min, whiskers_max, color='k', linestyle='-', lw=1)

# ax = sns.violinplot(data=lat)
axs7.set_title('Test de latencia con un tiempo de muestreo de $ 1s$')
axt7.set_title('Latency test sample time $ 1s$')
# adding horizontal grid lines
axs7.yaxis.grid(True)
axs7.set_xticks([y + 1 for y in range(len(lat))])
axs7.set_xlabel('Tipo de aplicación')
axs7.set_ylabel('Tiempo de ejecución de la aplicación(ms)')
axs7.set_ylim(0, 4)
axs7.set_xticklabels(['Control maestro', 'Control esclavo', 'Medición'])
#                    'Singularity \n Controller Slave', 'Singularity \n Process Slave'])
# axs7.set_xticklabels(['Singularity \n Detection system', 'Singularity \n Controller Master',
#                    'Singularity \n Controller Slave', 'Singularity \n Process Slave'])
# 'Detection \n system', 'RT-Linux \n Controller Master', 'RT-Linux \n Controller Slave',
# 'RT-Linux \n Process Slave'])
# lat_cm_rt = np.append(lat_cm_rt, axis=0)
lat_ = mat['lat'] * 1000
lat_ = lat_.tolist()
lat_cs_rt = lat_cs_rt.tolist()
lat_ps_rt = lat_ps_rt.tolist()
lat_cm_rt = lat_cm_rt.tolist()

fig, ax = plt.subplots(2, 2)
ax[0, 0].set_xlim(np.amin(lat_cm_rt), np.amax(lat_cm_rt))
ax[0, 0].yaxis.grid(True)
ax[0, 0].set_ylabel('Número de muestras')
# ax[0, 0].set_xlabel('Tiempo de ejecución de la aplicación(ms)')
ax[0, 0].hist(lat_cm_rt, bins=137, linewidth=0.5, edgecolor="black")
ax[0, 0].set_title('Distribución de los datos para la aplicación del Control maestro')

ax[0, 1].set_xlim(np.amin(lat_cs_rt), np.amax(lat_cs_rt))
ax[0, 1].yaxis.grid(True)
ax[0, 1].set_ylabel('Número de muestras')
# ax[0, 1].set_xlabel('Tiempo de ejecución de la aplicación(ms)')
ax[0, 1].hist(lat_cs_rt, bins=137, linewidth=0.5, edgecolor="black")
ax[0, 1].set_title('Distribución de los datos para la aplicación del Control esclavo')

ax[1, 0].set_xlim(np.amin(lat_ps_rt), np.amax(lat_ps_rt))
ax[1, 0].yaxis.grid(True)
ax[1, 0].set_ylabel('Número de muestras')
ax[1, 0].set_xlabel('Tiempo de ejecución de la aplicación(ms)')
ax[1, 0].hist(lat_ps_rt, bins=137, linewidth=0.5, edgecolor="black")
ax[1, 0].set_title('Distribución de los datos para la aplicación de la Medición')

ax[1, 1].set_xlim(np.amin(lat_), np.amax(lat_))
ax[1, 1].yaxis.grid(True)
ax[1, 1].set_ylabel('Número de muestras')
ax[1, 1].set_xlabel('Tiempo de ejecución de la aplicación(ms)')
ax[1, 1].hist(lat_, bins=137, linewidth=0.5, edgecolor="black")
ax[1, 1].set_title('Distribución de los datos para la aplicación del Sistema de monitoreo')

plt.show()

