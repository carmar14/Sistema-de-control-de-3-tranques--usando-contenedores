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
    r'D:\Acer\Documentos\GitHub\Sistema-de-control-de-3-tranques--usando-contenedores\Tanques modificados\latencias_rt_1s\lat_m_rt.mat')
mat2 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\Sistema-de-control-de-3-tranques--usando-contenedores\Tanques modificados\latencias_rt_1s\lat_c_rt.mat')
mat3 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\Sistema-de-control-de-3-tranques--usando-contenedores\Tanques modificados\latencias_rt_1s\lat_a_rt.mat')
mat4 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\Sistema-de-control-de-3-tranques--usando-contenedores\Tanques modificados\latencias_rt_1s\lat_m_.mat')
mat5 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\Sistema-de-control-de-3-tranques--usando-contenedores\Tanques modificados\latencias_rt_1s\lat_c_.mat')
mat6 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\Sistema-de-control-de-3-tranques--usando-contenedores\Tanques modificados\latencias_rt_1s\lat_a_.mat')

# -------latencias-------
# lat_ = mat['lat'] * 1000 # .tolist()
lat_m_rt = mat['lat_m_rt']
lat_c_rt = mat2['lat_c_rt']
lat_a_rt = mat3['lat_a_rt']
lat_m_ = mat4['lat_m_']
lat_c_ = mat5['lat_c_']
lat_a_ = mat6['lat_a_']

'''
lat = np.append(lat_, lat_m_rt, axis=0)
lat = np.append(lat, lat_c_rt, axis=0)
lat = np.append(lat, lat_m_rt, axis=0)
'''
lat = np.append(lat_m_rt, lat_c_rt, axis=0)
lat = np.append(lat, lat_a_rt, axis=0)
lat = np.append(lat, lat_m_, axis=0)
lat = np.append(lat, lat_c_, axis=0)
lat = np.append(lat, lat_a_, axis=0)
lat = lat.tolist()

# print(type(lat))
print(len(lat))


max_ = np.amax(lat_m_rt)
min_ = np.amin(lat_m_rt)
mu = lat_m_rt.mean()
median = np.median(lat_m_rt)
sigma = lat_m_rt.std()
textstr = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props = dict(boxstyle='round', facecolor='#8B8CDB', alpha=0.5)

cell_text = np.empty((6, 5))
cell_text[0][0] = mu
cell_text[0][1] = median
cell_text[0][2] = sigma
cell_text[0][3] = max_
cell_text[0][4] = min_

max_ = np.amax(lat_c_rt)
min_ = np.amin(lat_c_rt)
mu = lat_c_rt.mean()
median = np.median(lat_c_rt)
sigma = lat_c_rt.std()
textstr2 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props2 = dict(boxstyle='round', facecolor='#8B1F8A', alpha=0.5)

cell_text[1][0] = mu
cell_text[1][1] = median
cell_text[1][2] = sigma
cell_text[1][3] = max_
cell_text[1][4] = min_

max_ = np.amax(lat_a_rt)
min_ = np.amin(lat_a_rt)
mu = lat_a_rt.mean()
median = np.median(lat_a_rt)
sigma = lat_a_rt.std()
textstr3 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props3 = dict(boxstyle='round', facecolor='#FF1F8A', alpha=0.5)

cell_text[2][0] = mu
cell_text[2][1] = median
cell_text[2][2] = sigma
cell_text[2][3] = max_
cell_text[2][4] = min_

max_ = np.amax(lat_m_)
min_ = np.amin(lat_m_)
mu = lat_m_.mean()
median = np.median(lat_m_)
sigma = lat_m_.std()
textstr4 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props4 = dict(boxstyle='round', facecolor='#DF5014', alpha=0.5)

cell_text[3][0] = mu
cell_text[3][1] = median
cell_text[3][2] = sigma
cell_text[3][3] = max_
cell_text[3][4] = min_

max_ = np.amax(lat_c_)
min_ = np.amin(lat_c_)
mu = lat_c_.mean()
median = np.median(lat_c_)
sigma = lat_c_.std()
textstr5 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props5 = dict(boxstyle='round', facecolor='#005714', alpha=0.5)

cell_text[4][0] = mu
cell_text[4][1] = median
cell_text[4][2] = sigma
cell_text[4][3] = max_
cell_text[4][4] = min_

max_ = np.amax(lat_a_)
min_ = np.amin(lat_a_)
mu = lat_a_.mean()
median = np.median(lat_a_)
sigma = lat_a_.std()
textstr6 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props6 = dict(boxstyle='round', facecolor='#351554', alpha=0.5)

cell_text[5][0] = mu
cell_text[5][1] = median
cell_text[5][2] = sigma
cell_text[5][3] = max_
cell_text[5][4] = min_

# place a text box in upper left in axes coords

axs7.text(0.12, 0.45, textstr, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props)
axs7.text(0.30, 0.45, textstr2, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props2)
axs7.text(0.46, 0.35, textstr3, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props3)
axs7.text(0.63, 0.45, textstr4, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props4)
axs7.text(0.8, 0.85, textstr5, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props5)
axs7.text(0.78, 0.25, textstr6, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props6)

columns = ('$\mu$', '$\mathrm{Median}$', '$\sigma$', '$Worst$', '$Best$')
rows = ['Medición rt', 'Control rt', 'Actuación rt', 'Medición Singularity', 'Control Singularity', 'Actuación Singularity']


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

    if i == 4:
        pc.set_facecolor('#DF5014')

    if i == 5:
        pc.set_facecolor('#005714')
    if i == 6:
        pc.set_facecolor('#351554')


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
#axs7.set_ylim(0, 4)
axs7.set_xticklabels(['Medición rt', 'Control rt', 'Actuación rt', 'Medición Singularity', 'Control Singularity', 'Actuación Singularity'])

lat_a_ = lat_a_.tolist()
lat_c_rt = lat_c_rt.tolist()
lat_m_rt = lat_m_rt.tolist()
lat_a_rt = lat_a_rt.tolist()
lat_m_ = lat_m_.tolist()
lat_c_ = lat_c_.tolist()


fig, ax = plt.subplots(3, 1)
ax[0].set_xlim(np.amin(lat_m_rt), np.amax(lat_m_rt))
ax[0].yaxis.grid(True)
ax[0].set_ylabel('Número de muestras')
# ax[0, 0].set_xlabel('Tiempo de ejecución de la aplicación(ms)')
ax[0].hist(lat_m_rt,color='blue', alpha=0.75, bins=20, linewidth=0.5, edgecolor="black")
ax[0].hist(lat_m_, color='red', alpha=0.45, bins=20, linewidth=0.5, edgecolor="black")
ax[0].legend(['RT', 'Singularity'])
ax[0].set_title('Distribución de los datos para la aplicación del Medición')

ax[1].set_xlim(np.amin(lat_c_rt), np.amax(lat_c_rt))
ax[1].yaxis.grid(True)
ax[1].set_ylabel('Número de muestras')
# ax[0, 1].set_xlabel('Tiempo de ejecución de la aplicación(ms)')
ax[1].hist(lat_c_rt,color='blue', alpha=0.75, bins=20, linewidth=0.5, edgecolor="black")
ax[1].hist(lat_c_, color='red', alpha=0.45, bins=20, linewidth=0.5, edgecolor="black")
ax[1].legend(['RT', 'Singularity'])
ax[1].set_title('Distribución de los datos para la aplicación del Control')

ax[2].set_xlim(np.amin(lat_a_rt), np.amax(lat_a_rt))
ax[2].yaxis.grid(True)
ax[2].set_ylabel('Número de muestras')
ax[2].set_xlabel('Tiempo de ejecución de la aplicación(ms)')
ax[2].hist(lat_a_rt, color='blue', alpha=0.75, bins=20, linewidth=0.5, edgecolor="black")
ax[2].hist(lat_a_, color='red', alpha=0.45, bins=20, linewidth=0.5, edgecolor="black")
ax[2].legend(['RT', 'Singularity'])
ax[2].set_title('Distribución de los datos para la aplicación de la Actuación')
fig.tight_layout()

# -------------------nuevas pruebas-------------------
fig7, axs7 = plt.subplots(nrows=1, ncols=1, figsize=(9, 4))

# -----------------sample time 5ms-----------------

mat = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\Sistema-de-control-de-3-tranques--usando-contenedores\Tanques modificados\latencias_rt_5ms\lat_m_rt.mat')
mat2 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\Sistema-de-control-de-3-tranques--usando-contenedores\Tanques modificados\latencias_rt_5ms\lat_c_rt.mat')
mat3 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\Sistema-de-control-de-3-tranques--usando-contenedores\Tanques modificados\latencias_rt_5ms\lat_a_rt.mat')
mat4 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\Sistema-de-control-de-3-tranques--usando-contenedores\Tanques modificados\latencias_rt_5ms\lat_m_.mat')
mat5 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\Sistema-de-control-de-3-tranques--usando-contenedores\Tanques modificados\latencias_rt_5ms\lat_c_.mat')
mat6 = scipy.io.loadmat(
    r'D:\Acer\Documentos\GitHub\Sistema-de-control-de-3-tranques--usando-contenedores\Tanques modificados\latencias_rt_5ms\lat_a_.mat')

# -------latencias-------
# lat_ = mat['lat'] * 1000 # .tolist()
lat_m_rt = mat['lat_m_rt']
lat_c_rt = mat2['lat_c_rt']
lat_a_rt = mat3['lat_a_rt']
lat_m_ = mat4['lat_m_']
lat_c_ = mat5['lat_c_']
lat_a_ = mat6['lat_a_']

'''
lat = np.append(lat_, lat_m_rt, axis=0)
lat = np.append(lat, lat_c_rt, axis=0)
lat = np.append(lat, lat_m_rt, axis=0)
'''
lat = np.append(lat_m_rt, lat_c_rt, axis=0)
lat = np.append(lat, lat_a_rt, axis=0)
lat = np.append(lat, lat_m_, axis=0)
lat = np.append(lat, lat_c_, axis=0)
lat = np.append(lat, lat_a_, axis=0)
lat = lat.tolist()

# print(type(lat))
print(len(lat))


max_ = np.amax(lat_m_rt)
min_ = np.amin(lat_m_rt)
mu = lat_m_rt.mean()
median = np.median(lat_m_rt)
sigma = lat_m_rt.std()
textstr = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props = dict(boxstyle='round', facecolor='#8B8CDB', alpha=0.5)

cell_text = np.empty((6, 5))
cell_text[0][0] = mu
cell_text[0][1] = median
cell_text[0][2] = sigma
cell_text[0][3] = max_
cell_text[0][4] = min_

max_ = np.amax(lat_c_rt)
min_ = np.amin(lat_c_rt)
mu = lat_c_rt.mean()
median = np.median(lat_c_rt)
sigma = lat_c_rt.std()
textstr2 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props2 = dict(boxstyle='round', facecolor='#8B1F8A', alpha=0.5)

cell_text[1][0] = mu
cell_text[1][1] = median
cell_text[1][2] = sigma
cell_text[1][3] = max_
cell_text[1][4] = min_

max_ = np.amax(lat_a_rt)
min_ = np.amin(lat_a_rt)
mu = lat_a_rt.mean()
median = np.median(lat_a_rt)
sigma = lat_a_rt.std()
textstr3 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props3 = dict(boxstyle='round', facecolor='#FF1F8A', alpha=0.5)

cell_text[2][0] = mu
cell_text[2][1] = median
cell_text[2][2] = sigma
cell_text[2][3] = max_
cell_text[2][4] = min_

max_ = np.amax(lat_m_)
min_ = np.amin(lat_m_)
mu = lat_m_.mean()
median = np.median(lat_m_)
sigma = lat_m_.std()
textstr4 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props4 = dict(boxstyle='round', facecolor='#DF5014', alpha=0.5)

cell_text[3][0] = mu
cell_text[3][1] = median
cell_text[3][2] = sigma
cell_text[3][3] = max_
cell_text[3][4] = min_

max_ = np.amax(lat_c_)
min_ = np.amin(lat_c_)
mu = lat_c_.mean()
median = np.median(lat_c_)
sigma = lat_c_.std()
textstr5 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props5 = dict(boxstyle='round', facecolor='#005714', alpha=0.5)

cell_text[4][0] = mu
cell_text[4][1] = median
cell_text[4][2] = sigma
cell_text[4][3] = max_
cell_text[4][4] = min_

max_ = np.amax(lat_a_)
min_ = np.amin(lat_a_)
mu = lat_a_.mean()
median = np.median(lat_a_)
sigma = lat_a_.std()
textstr6 = '\n'.join((
    r'$\mu=%.4f$' % (mu,),
    r'$\mathrm{median}=%.4f$' % (median,),
    r'$\sigma=%.4f$' % (sigma,),
    r'$Worst=%.4f$' % (max_,),
    r'$Best=%.4f$' % (min_,)))
props6 = dict(boxstyle='round', facecolor='#351554', alpha=0.5)

cell_text[5][0] = mu
cell_text[5][1] = median
cell_text[5][2] = sigma
cell_text[5][3] = max_
cell_text[5][4] = min_

# place a text box in upper left in axes coords

axs7.text(0.12, 0.45, textstr, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props)
axs7.text(0.30, 0.45, textstr2, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props2)
axs7.text(0.46, 0.35, textstr3, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props3)
axs7.text(0.63, 0.45, textstr4, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props4)
axs7.text(0.8, 0.85, textstr5, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props5)
axs7.text(0.78, 0.25, textstr6, transform=axs7.transAxes, fontsize=7, verticalalignment='top', bbox=props6)

columns = ('$\mu$', '$\mathrm{Median}$', '$\sigma$', '$Worst$', '$Best$')
rows = ['Medición rt', 'Control rt', 'Actuación rt', 'Medición Singularity', 'Control Singularity', 'Actuación Singularity']


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

    if i == 4:
        pc.set_facecolor('#DF5014')

    if i == 5:
        pc.set_facecolor('#005714')
    if i == 6:
        pc.set_facecolor('#351554')


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
axs7.set_title('Test de latencia con un tiempo de muestreo de $ 5ms$')
axt7.set_title('Latency test sample time $ 5ms$')
# adding horizontal grid lines
axs7.yaxis.grid(True)
axs7.set_xticks([y + 1 for y in range(len(lat))])
axs7.set_xlabel('Tipo de aplicación')
axs7.set_ylabel('Tiempo de ejecución de la aplicación(ms)')
#axs7.set_ylim(0, 4)
axs7.set_xticklabels(['Medición rt', 'Control rt', 'Actuación rt', 'Medición Singularity', 'Control Singularity', 'Actuación Singularity'])

lat_a_ = lat_a_.tolist()
lat_c_rt = lat_c_rt.tolist()
lat_m_rt = lat_m_rt.tolist()
lat_a_rt = lat_a_rt.tolist()
lat_m_ = lat_m_.tolist()
lat_c_ = lat_c_.tolist()


fig, ax = plt.subplots(3, 1)
ax[0].set_xlim(np.amin(lat_m_rt), np.amax(lat_m_rt))
ax[0].yaxis.grid(True)
ax[0].set_ylabel('Número de muestras')
# ax[0, 0].set_xlabel('Tiempo de ejecución de la aplicación(ms)')
ax[0].hist(lat_m_rt,color='blue', alpha=0.75, bins=20, linewidth=0.5, edgecolor="black")
ax[0].hist(lat_m_, color='red', alpha=0.45, bins=20, linewidth=0.5, edgecolor="black")
ax[0].set_xlim(1, 6)
ax[0].legend(['RT', 'Singularity'])
ax[0].set_title('Distribución de los datos para la aplicación del Medición')

ax[1].set_xlim(np.amin(lat_c_rt), np.amax(lat_c_rt))
ax[1].yaxis.grid(True)
ax[1].set_ylabel('Número de muestras')
# ax[0, 1].set_xlabel('Tiempo de ejecución de la aplicación(ms)')
ax[1].hist(lat_c_rt, color='blue', alpha=0.75, bins=20, linewidth=0.5, edgecolor="black")
ax[1].hist(lat_c_, color='red', alpha=0.45, bins=20, linewidth=0.5, edgecolor="black")
ax[1].set_xlim(2, 8.3)
ax[1].legend(['RT', 'Singularity'])
ax[1].set_title('Distribución de los datos para la aplicación del Control')

ax[2].set_xlim(np.amin(lat_a_rt), np.amax(lat_a_rt))
ax[2].yaxis.grid(True)
ax[2].set_ylabel('Número de muestras')
ax[2].set_xlabel('Tiempo de ejecución de la aplicación(ms)')
ax[2].hist(lat_a_rt, color='blue', alpha=0.75, bins=20, linewidth=0.5, edgecolor="black")
ax[2].hist(lat_a_, color='red', alpha=0.45, bins=20, linewidth=0.5, edgecolor="black")
ax[2].set_xlim(0.2, 7)
ax[2].legend(['RT', 'Singularity'])
ax[2].set_title('Distribución de los datos para la aplicación de la Actuación')
fig.tight_layout()

plt.show()

