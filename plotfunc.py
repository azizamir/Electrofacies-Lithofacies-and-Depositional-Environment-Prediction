import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable

# modified from Brendon Hall Github

# lithofacies classifier plot
def lithoplot_data(df, well):
    df = df[df['Well'] == well]

    # lithofacies color map
    # color order = [0, 1, 2, 3, ...]
    litho_colors = ['mediumseagreen', 'orange', 'yellow', 'saddlebrown', 'grey', 'cyan']
    cmap_litho = colors.ListedColormap(litho_colors)  # make color into colormap

    cluster = np.repeat(np.expand_dims(df.Facies, 1), 100, 1)

    # Set the top and bottom of depth
    top = df['Depth'].max()
    bottom = df['Depth'].min()

    # plotting
    fig, ax = plt.subplots(1, 7, figsize=(20, 12))

    # tops
    fm_tops = dict(df[['Formation', 'Depth']].dropna().values.tolist())

    ax[0].set_xlabel('Tops ', fontsize = '12' )
    ax[0].set_ylabel('Measured Depth (m) ', fontsize = '12' )
    ax[0].set_xticklabels([])
    ax[0].set_xticks([])
    ax[0].set_facecolor('#ffffed')
    ax[0].set_ylim(df.Depth.min(), df.Depth.max())
    ax[0].xaxis.set_label_position("top")
    ax[0].invert_yaxis()
    for Top in fm_tops.values() :
        ax[0].axhline(y = float(Top), color = 'k', lw = 1, ls = '-',    
                            alpha = 0.9, xmin = 0.06, xmax = 0.95 )
    for Top, MD in fm_tops.items():
        ax[0].text(x = 0.45,  y = float(MD), s = Top , fontsize = '9', 
                horizontalalignment = 'center', verticalalignment = 'bottom')

    # GR
    ax[1].plot(df.GR, df.Depth, c='g')
    ax[1].set_xlabel('Gamma Ray (API)')
    ax[1].set_ylim(top, bottom)
    ax[1].set_xlim(df.GR.min(), df.GR.max())
    ax[1].grid()
    ax[1].xaxis.set_label_position('top')
    ax[1].xaxis.set_ticks_position('top')
    ax[1].set_yticklabels([])

    # RHOB
    ax[2].plot(df.RHOB, df.Depth, c='r')
    ax[2].set_xlabel('Density (g/cc)')
    ax[2].set_ylim(top, bottom)
    ax[2].set_xlim(df.RHOB.min(), df.RHOB.max())
    ax[2].grid()
    ax[2].xaxis.set_label_position('top')
    ax[2].xaxis.set_ticks_position('top')
    ax[2].set_yticklabels([])

    # NPHI
    ax[3].plot(df.NPHI, df.Depth, c='black')
    ax[3].set_xlabel('NPHI (.pu)')
    ax[3].set_ylim(top, bottom)
    ax[3].set_xlim(df.NPHI.min(), df.NPHI.max())
    ax[3].grid()
    ax[3].xaxis.set_label_position('top')
    ax[3].xaxis.set_ticks_position('top')
    ax[3].set_yticklabels([])

    # DTCO
    ax[4].plot(df.DTCO, df.Depth, c='blue')
    ax[4].set_xlabel('DTCO (us/f)')
    ax[4].set_ylim(top, bottom)
    ax[4].set_xlim(df.DTCO.min(), df.DTCO.max())
    ax[4].grid()
    ax[4].xaxis.set_label_position('top')
    ax[4].xaxis.set_ticks_position('top')
    ax[4].set_yticklabels([])

    # DTSM
    ax[5].plot(df.DTSM, df.Depth, c='red')
    ax[5].set_xlabel('DTSM (us/f)')
    ax[5].set_ylim(top, bottom)
    ax[5].set_xlim(df.DTSM.min(), df.DTSM.max())
    ax[5].grid()
    ax[5].xaxis.set_label_position('top')
    ax[5].xaxis.set_ticks_position('top')
    ax[5].set_yticklabels([])

    # lithofacies
    im = ax[6].imshow(cluster, interpolation='none', aspect='auto',
                      cmap=cmap_litho, vmin=0, vmax=6)
    ax[6].set_xlabel('Lithofacies')
    ax[6].xaxis.set_label_position('top')
    ax[6].xaxis.set_ticks_position('top')
    ax[6].set_xticks([])
    ax[6].set_yticklabels([])

    # color bar
    divider = make_axes_locatable(ax[6])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax=cax)
    cbar.set_label((30 * ' ').join(['Si ', 'VSiS', 'SiSs',
                                    'SiCl', 'Cl', 'SiSsCt']))
    cbar.set_ticks(range(0, 1));
    cbar.set_ticklabels('')

    # title
    fig.suptitle('%s Well' % df['Well'].iloc[0], fontsize=14)

    plt.show()


def lithoplot_val(df, well):
    df = df[df['Well'] == well]

    # lithofacies color map
    litho_colors = ['mediumseagreen', 'orange', 'yellow', 'saddlebrown', 'grey', 'cyan']
    cmap_litho = colors.ListedColormap(litho_colors)  # make color into colormap

    cluster1 = np.repeat(np.expand_dims(df.Facies, 1), 100, 1)
    cluster2 = np.repeat(np.expand_dims(df.Facies_pred, 1), 100, 1)

    # Set the top and bottom of depth
    top = df['Depth'].max()
    bottom = df['Depth'].min()

    # plotting
    fig, ax = plt.subplots(1, 8, figsize=(20, 12))

    # tops
    fm_tops = dict(df[['Formation', 'Depth']].dropna().values.tolist())

    ax[0].set_xlabel('Tops ', fontsize = '12' )
    ax[0].set_ylabel('Measured Depth (m) ', fontsize = '12' )
    ax[0].set_xticklabels([])
    ax[0].set_xticks([])
    ax[0].set_facecolor('#ffffed')
    ax[0].set_ylim(df.Depth.min(), df.Depth.max())
    ax[0].xaxis.set_label_position("top")
    ax[0].invert_yaxis()
    for Top in fm_tops.values() :
        ax[0].axhline(y = float(Top), color = 'k', lw = 1, ls = '-',    
                            alpha = 0.9, xmin = 0.06, xmax = 0.95 )
    for Top, MD in fm_tops.items():
        ax[0].text(x = 0.45,  y = float(MD), s = Top , fontsize = '9', 
                horizontalalignment = 'center', verticalalignment = 'bottom')

    # GR
    ax[1].plot(df.GR, df.Depth, c='g')
    ax[1].set_xlabel('Gamma Ray (API)')
    ax[1].set_ylim(top, bottom)
    ax[1].set_xlim(df.GR.min(), df.GR.max())
    ax[1].grid()
    ax[1].xaxis.set_label_position('top')
    ax[1].xaxis.set_ticks_position('top')
    ax[1].set_yticklabels([])

    # RHOB
    ax[2].plot(df.RHOB, df.Depth, c='r')
    ax[2].set_xlabel('Density (g/cc)')
    ax[2].set_ylim(top, bottom)
    ax[2].set_xlim(df.RHOB.min(), df.RHOB.max())
    ax[2].grid()
    ax[2].xaxis.set_label_position('top')
    ax[2].xaxis.set_ticks_position('top')
    ax[2].set_yticklabels([])

    # NPHI
    ax[3].plot(df.NPHI, df.Depth, c='black')
    ax[3].set_xlabel('NPHI (.pu)')
    ax[3].set_ylim(top, bottom)
    ax[3].set_xlim(df.NPHI.min(), df.NPHI.max())
    ax[3].grid()
    ax[3].xaxis.set_label_position('top')
    ax[3].xaxis.set_ticks_position('top')
    ax[3].set_yticklabels([])

    # DTCO
    ax[4].plot(df.DTCO, df.Depth, c='blue')
    ax[4].set_xlabel('DTCO (us/f)')
    ax[4].set_ylim(top, bottom)
    ax[4].set_xlim(df.DTCO.min(), df.DTCO.max())
    ax[4].grid()
    ax[4].xaxis.set_label_position('top')
    ax[4].xaxis.set_ticks_position('top')
    ax[4].set_yticklabels([])

    # DTSM
    ax[5].plot(df.DTSM, df.Depth, c='red')
    ax[5].set_xlabel('DTSM (us/f)')
    ax[5].set_ylim(top, bottom)
    ax[5].set_xlim(df.DTSM.min(), df.DTSM.max())
    ax[5].grid()
    ax[5].xaxis.set_label_position('top')
    ax[5].xaxis.set_ticks_position('top')
    ax[5].set_yticklabels([])

    # actual lithofacies
    im = ax[6].imshow(cluster1, interpolation='none', aspect='auto',
                      cmap=cmap_litho, vmin=0, vmax=6)
    ax[6].set_xlabel('Actual Lithofacies')
    ax[6].xaxis.set_label_position('top')
    ax[6].xaxis.set_ticks_position('top')
    ax[6].set_xticks([])
    ax[6].set_yticklabels([])

    # predicted lithofacies
    im = ax[7].imshow(cluster2, interpolation='none', aspect='auto',
                      cmap=cmap_litho, vmin=0, vmax=6)
    ax[7].set_xlabel('Predicted Lithofacies')
    ax[7].xaxis.set_label_position('top')
    ax[7].xaxis.set_ticks_position('top')
    ax[7].set_xticks([])
    ax[7].set_yticklabels([])

    # color bar
    divider = make_axes_locatable(ax[7])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax=cax)
    cbar.set_label((30 * ' ').join(['Si ', 'VSiS', 'SiSs',
                                    'SiCl', 'Cl', 'SiSsCt']))
    cbar.set_ticks(range(0, 1));
    cbar.set_ticklabels('')

    # title
    fig.suptitle('%s Well' % df['Well'].iloc[0], fontsize=14)

    plt.savefig('%s Litho Validation' % df['Well'].iloc[0])

    plt.show()


def lithoplot_test(df, well):
    df = df[df['Well'] == well]

    # lithofacies color map
    litho_colors = ['mediumseagreen', 'orange', 'yellow', 'saddlebrown', 'grey', 'cyan']
    cmap_litho = colors.ListedColormap(litho_colors)  # make color into colormap

    cluster = np.repeat(np.expand_dims(df.Facies_pred, 1), 100, 1)

    # Set the top and bottom of depth
    top = df['Depth'].max()
    bottom = df['Depth'].min()

    # plotting
    fig, ax = plt.subplots(1, 5, figsize=(8, 12))

    # GR
    ax[0].plot(df.GR, df.Depth, c='g')
    ax[0].set_ylabel('Depth (m)')
    ax[0].set_xlabel('Gamma Ray (API)')
    ax[0].set_ylim(top, bottom)
    ax[0].set_xlim(df.GR.min(), df.GR.max())
    ax[0].grid()
    ax[0].xaxis.set_label_position('top')
    ax[0].xaxis.set_ticks_position('top')

    # RHOB
    ax[1].plot(df.RHOB, df.Depth, c='r')
    ax[1].set_xlabel('Density (g/cc)')
    ax[1].set_ylim(top, bottom)
    ax[1].set_xlim(df.RHOB.min(), df.RHOB.max())
    ax[1].grid()
    ax[1].xaxis.set_label_position('top')
    ax[1].xaxis.set_ticks_position('top')
    ax[1].set_yticklabels([])

    # NPHI
    ax[2].plot(df.NPHI, df.Depth, c='black')
    ax[2].set_xlabel('NPHI (.pu)')
    ax[2].set_ylim(top, bottom)
    ax[2].set_xlim(df.NPHI.min(), df.NPHI.max())
    ax[2].grid()
    ax[2].xaxis.set_label_position('top')
    ax[2].xaxis.set_ticks_position('top')
    ax[2].set_yticklabels([])

    # DTCO
    ax[3].plot(df.DTCO, df.Depth, c='blue')
    ax[3].set_xlabel('DTCO (us/f)')
    ax[3].set_ylim(top, bottom)
    ax[3].set_xlim(df.DTCO.min(), df.DTCO.max())
    ax[3].grid()
    ax[3].xaxis.set_label_position('top')
    ax[3].xaxis.set_ticks_position('top')
    ax[3].set_yticklabels([])

    # lithofacies
    im = ax[4].imshow(cluster, interpolation='none', aspect='auto',
                      cmap=cmap_litho, vmin=0, vmax=6)
    ax[4].set_xlabel('Lithofacies')
    ax[4].xaxis.set_label_position('top')
    ax[4].xaxis.set_ticks_position('top')
    ax[4].set_xticks([])
    ax[4].set_yticklabels([])

    # color bar
    divider = make_axes_locatable(ax[4])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax=cax)
    cbar.set_label((30 * ' ').join(['Si ', 'VSiS', 'SiSs',
                                    'SiCl', 'Cl', 'SiSsCt']))
    cbar.set_ticks(range(0, 1));
    cbar.set_ticklabels('')

    # title
    fig.suptitle('%s Well' % df['Well'].iloc[0], fontsize=14)

    plt.show()


# electrofacies classifier plot
def efplot_data(df, well):
    df = df[df['Well'] == well]

    # electrofacies color map
    # color order = [0, 1, 2, 3]
    ef_colors = ['red', 'green', 'blue', 'yellow', 'cyan'] 
    cmap_ef = colors.ListedColormap(ef_colors) # make color into colormap

    cluster = np.repeat(np.expand_dims(df.Electrofacies, 1), 100, 1)

    # Set the top and bottom of depth
    top = df['Depth'].max()
    bottom = df['Depth'].min()

    # plotting
    fig, ax = plt.subplots(1, 7, figsize = (20, 12))

    # tops
    fm_tops = dict(df[['Formation', 'Depth']].dropna().values.tolist())

    ax[0].set_xlabel('Tops ', fontsize = '12' )
    ax[0].set_ylabel('Measured Depth (m) ', fontsize = '12' )
    ax[0].set_xticklabels([])
    ax[0].set_xticks([])
    ax[0].set_facecolor('#ffffed')
    ax[0].set_ylim(df.Depth.min(), df.Depth.max())
    ax[0].xaxis.set_label_position("top")
    ax[0].invert_yaxis()
    for Top in fm_tops.values() :
        ax[0].axhline(y = float(Top), color = 'k', lw = 1, ls = '-',    
                            alpha = 0.9, xmin = 0.06, xmax = 0.95 )
    for Top, MD in fm_tops.items():
        ax[0].text(x = 0.45,  y = float(MD), s = Top , fontsize = '9', 
                horizontalalignment = 'center', verticalalignment = 'bottom')

    # GR
    ax[1].plot(df.GR, df.Depth, c='g')
    ax[1].set_xlabel('Gamma Ray (API)')
    ax[1].set_ylim(top, bottom)
    ax[1].set_xlim(df.GR.min(), df.GR.max())
    ax[1].grid()
    ax[1].xaxis.set_label_position('top')
    ax[1].xaxis.set_ticks_position('top')
    ax[1].set_yticklabels([])

    # RHOB
    ax[2].plot(df.RHOB, df.Depth, c='r')
    ax[2].set_xlabel('Density (g/cc)')
    ax[2].set_ylim(top, bottom)
    ax[2].set_xlim(df.RHOB.min(), df.RHOB.max())
    ax[2].grid()
    ax[2].xaxis.set_label_position('top')
    ax[2].xaxis.set_ticks_position('top')
    ax[2].set_yticklabels([])

    # NPHI
    ax[3].plot(df.NPHI, df.Depth, c='black')
    ax[3].set_xlabel('NPHI (.pu)')
    ax[3].set_ylim(top, bottom)
    ax[3].set_xlim(df.NPHI.min(), df.NPHI.max())
    ax[3].grid()
    ax[3].xaxis.set_label_position('top')
    ax[3].xaxis.set_ticks_position('top')
    ax[3].set_yticklabels([])

    # DTCO
    ax[4].plot(df.DTCO, df.Depth, c='blue')
    ax[4].set_xlabel('DTCO (us/f)')
    ax[4].set_ylim(top, bottom)
    ax[4].set_xlim(df.DTCO.min(), df.DTCO.max())
    ax[4].grid()
    ax[4].xaxis.set_label_position('top')
    ax[4].xaxis.set_ticks_position('top')
    ax[4].set_yticklabels([])

    # DTSM
    ax[5].plot(df.DTSM, df.Depth, c='red')
    ax[5].set_xlabel('DTSM (us/f)')
    ax[5].set_ylim(top, bottom)
    ax[5].set_xlim(df.DTSM.min(), df.DTSM.max())
    ax[5].grid()
    ax[5].xaxis.set_label_position('top')
    ax[5].xaxis.set_ticks_position('top')
    ax[5].set_yticklabels([])
  
    # electrofacies
    im = ax[6].imshow(cluster, interpolation='none', aspect='auto',
                    cmap = cmap_ef, vmin=0, vmax=4)
    ax[6].set_xlabel('Electrofacies')
    ax[6].xaxis.set_label_position('top')
    ax[6].xaxis.set_ticks_position('top')
    ax[6].set_xticks([])
    ax[6].set_yticklabels([])

    # color bar
    divider = make_axes_locatable(ax[6])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax = cax)
    cbar.set_label((40*' ').join(['Cy', 'Fu', 'Be', 'SI', 'Sy']))
    cbar.set_ticks(range(0,1)); cbar.set_ticklabels('')

    # title
    fig.suptitle('%s Well'%df['Well'].iloc[0], fontsize = 14)

    plt.show()


def efplot_val(df, well):
    df = df[df['Well'] == well]

    # electrofacies color map
    ef_colors = ['red', 'green', 'blue', 'yellow', 'cyan'] 
    cmap_ef = colors.ListedColormap(ef_colors) # make color into colormap

    cluster1 = np.repeat(np.expand_dims(df.Electrofacies, 1), 100, 1)
    cluster2 = np.repeat(np.expand_dims(df.Ef_pred, 1), 100, 1)

    # Set the top and bottom of depth
    top = df['Depth'].max()
    bottom = df['Depth'].min()

    # plotting
    fig, ax = plt.subplots(1, 8, figsize = (20, 12))

    # tops
    fm_tops = dict(df[['Formation', 'Depth']].dropna().values.tolist())

    ax[0].set_xlabel('Tops ', fontsize = '12' )
    ax[0].set_ylabel('Measured Depth (m) ', fontsize = '12' )
    ax[0].set_xticklabels([])
    ax[0].set_xticks([])
    ax[0].set_facecolor('#ffffed')
    ax[0].set_ylim(df.Depth.min(), df.Depth.max())
    ax[0].xaxis.set_label_position("top")
    ax[0].invert_yaxis()
    for Top in fm_tops.values() :
        ax[0].axhline(y = float(Top), color = 'k', lw = 1, ls = '-',    
                            alpha = 0.9, xmin = 0.06, xmax = 0.95 )
    for Top, MD in fm_tops.items():
        ax[0].text(x = 0.45,  y = float(MD), s = Top , fontsize = '9', 
                horizontalalignment = 'center', verticalalignment = 'bottom')

    # GR
    ax[1].plot(df.GR, df.Depth, c='g')
    ax[1].set_xlabel('Gamma Ray (API)')
    ax[1].set_ylim(top, bottom)
    ax[1].set_xlim(df.GR.min(), df.GR.max())
    ax[1].grid()
    ax[1].xaxis.set_label_position('top')
    ax[1].xaxis.set_ticks_position('top')
    ax[1].set_yticklabels([])

    # RHOB
    ax[2].plot(df.RHOB, df.Depth, c='r')
    ax[2].set_xlabel('Density (g/cc)')
    ax[2].set_ylim(top, bottom)
    ax[2].set_xlim(df.RHOB.min(), df.RHOB.max())
    ax[2].grid()
    ax[2].xaxis.set_label_position('top')
    ax[2].xaxis.set_ticks_position('top')
    ax[2].set_yticklabels([])

    # NPHI
    ax[3].plot(df.NPHI, df.Depth, c='black')
    ax[3].set_xlabel('NPHI (.pu)')
    ax[3].set_ylim(top, bottom)
    ax[3].set_xlim(df.NPHI.min(), df.NPHI.max())
    ax[3].grid()
    ax[3].xaxis.set_label_position('top')
    ax[3].xaxis.set_ticks_position('top')
    ax[3].set_yticklabels([])

    # DTCO
    ax[4].plot(df.DTCO, df.Depth, c='blue')
    ax[4].set_xlabel('DTCO (us/f)')
    ax[4].set_ylim(top, bottom)
    ax[4].set_xlim(df.DTCO.min(), df.DTCO.max())
    ax[4].grid()
    ax[4].xaxis.set_label_position('top')
    ax[4].xaxis.set_ticks_position('top')
    ax[4].set_yticklabels([])

    # DTSM
    ax[5].plot(df.DTSM, df.Depth, c='red')
    ax[5].set_xlabel('DTSM (us/f)')
    ax[5].set_ylim(top, bottom)
    ax[5].set_xlim(df.DTSM.min(), df.DTSM.max())
    ax[5].grid()
    ax[5].xaxis.set_label_position('top')
    ax[5].xaxis.set_ticks_position('top')
    ax[5].set_yticklabels([])
  
    # actual pattern
    im = ax[6].imshow(cluster1, interpolation='none', aspect='auto',
                    cmap = cmap_ef, vmin=0, vmax=4)
    ax[6].set_xlabel('Actual Pattern')
    ax[6].xaxis.set_label_position('top')
    ax[6].xaxis.set_ticks_position('top')
    ax[6].set_xticks([])
    ax[6].set_yticklabels([])

    # predicted pattern
    im = ax[7].imshow(cluster2, interpolation='none', aspect='auto',
                    cmap = cmap_ef, vmin=0, vmax=4)
    ax[7].set_xlabel('Predicted Pattern')
    ax[7].xaxis.set_label_position('top')
    ax[7].xaxis.set_ticks_position('top')
    ax[7].set_xticks([])
    ax[7].set_yticklabels([])

    # color bar
    divider = make_axes_locatable(ax[7])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax = cax)
    cbar.set_label((40*' ').join(['Cy', 'Fu', 'Be', 'SI', 'Sy']))
    cbar.set_ticks(range(0,1)); cbar.set_ticklabels('')

    # title
    fig.suptitle('%s Well'%df['Well'].iloc[0], fontsize = 14)

    plt.savefig('%s Electrofacies Validation' %df['Well'].iloc[0])

    plt.show()


def efplot_test(df, well):
    df = df[df['Well'] == well]

    # electrofacies color map
    ef_colors = ['red', 'green', 'blue', 'yellow', 'cyan']  
    cmap_ef = colors.ListedColormap(ef_colors) # make color into colormap

    cluster = np.repeat(np.expand_dims(df.Ef_pred, 1), 100, 1)

    # Set the top and bottom of depth
    top = df['Depth'].max()
    bottom = df['Depth'].min()

    # plotting
    fig, ax = plt.subplots(1, 5, figsize = (8, 12))

    # GR
    ax[0].plot(df.GR, df.Depth, c = 'g')
    ax[0].set_ylabel('Depth (m)')
    ax[0].set_xlabel('Gamma Ray (API)')
    ax[0].set_ylim(top, bottom)
    ax[0].set_xlim(df.GR.min(),df.GR.max())
    ax[0].grid()
    ax[0].xaxis.set_label_position('top')
    ax[0].xaxis.set_ticks_position('top')

    # RHOB
    ax[1].plot(df.RHOB, df.Depth, c = 'r')
    ax[1].set_xlabel('Density (g/cc)')
    ax[1].set_ylim(top, bottom)
    ax[1].set_xlim(df.RHOB.min(),df.RHOB.max())
    ax[1].grid()
    ax[1].xaxis.set_label_position('top')
    ax[1].xaxis.set_ticks_position('top')
    ax[1].set_yticklabels([])

    # NPHI
    ax[2].plot(df.NPHI, df.Depth, c = 'black')
    ax[2].set_xlabel('NPHI (.pu)')
    ax[2].set_ylim(top, bottom)
    ax[2].set_xlim(df.NPHI.min(),df.NPHI.max())
    ax[2].grid()
    ax[2].xaxis.set_label_position('top')
    ax[2].xaxis.set_ticks_position('top')
    ax[2].set_yticklabels([])

    # DTCO
    ax[3].plot(df.DTCO, df.Depth, c = 'blue')
    ax[3].set_xlabel('DTCO (us/f)')
    ax[3].set_ylim(top, bottom)
    ax[3].set_xlim(df.DTCO.min(),df.DTCO.max())
    ax[3].grid()
    ax[3].xaxis.set_label_position('top')
    ax[3].xaxis.set_ticks_position('top')
    ax[3].set_yticklabels([])
  
 
    # electrofacies
    im = ax[4].imshow(cluster, interpolation='none', aspect='auto',
                    cmap = cmap_ef, vmin=0, vmax=4)
    ax[4].set_xlabel('Electrofacies')
    ax[4].xaxis.set_label_position('top')
    ax[4].xaxis.set_ticks_position('top')
    ax[4].set_xticks([])
    ax[4].set_yticklabels([])


    # color bar
    divider = make_axes_locatable(ax[4])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax = cax)
    cbar.set_label((40*' ').join(['Cy', 'Fu', 'Be', 'SI', 'Sy']))
    cbar.set_ticks(range(0,1)); cbar.set_ticklabels('')

    # title
    fig.suptitle('%s Well'%df['Well'].iloc[0], fontsize = 14)

    plt.show()

  
# deposition environment classifier plot
def envplot_data(df, well):
    df = df[df['Well'] == well]

    # deposition environment color map
    # color order = [0, 1, 2, 3, ...]
    env_colors = ['saddlebrown', 'yellowgreen', 'turquoise', 'darkgreen', 'grey', 'blue'] 
    cmap_env = colors.ListedColormap(env_colors) # make color into colormap

    cluster = np.repeat(np.expand_dims(df.Environment, 1), 100, 1)

    # Set the top and bottom of depth
    top = df['Depth'].max()
    bottom = df['Depth'].min()

    # plotting
    fig, ax = plt.subplots(1, 7, figsize = (20, 12))

    # tops
    fm_tops = dict(df[['Formation', 'Depth']].dropna().values.tolist())

    ax[0].set_xlabel('Tops ', fontsize = '12' )
    ax[0].set_ylabel('Measured Depth (m) ', fontsize = '12' )
    ax[0].set_xticklabels([])
    ax[0].set_xticks([])
    ax[0].set_facecolor('#ffffed')
    ax[0].set_ylim(df.Depth.min(), df.Depth.max())
    ax[0].xaxis.set_label_position("top")
    ax[0].invert_yaxis()
    for Top in fm_tops.values() :
        ax[0].axhline(y = float(Top), color = 'k', lw = 1, ls = '-',    
                            alpha = 0.9, xmin = 0.06, xmax = 0.95 )
    for Top, MD in fm_tops.items():
        ax[0].text(x = 0.45,  y = float(MD), s = Top , fontsize = '9', 
                horizontalalignment = 'center', verticalalignment = 'bottom')

    # GR
    ax[1].plot(df.GR, df.Depth, c='g')
    ax[1].set_xlabel('Gamma Ray (API)')
    ax[1].set_ylim(top, bottom)
    ax[1].set_xlim(df.GR.min(), df.GR.max())
    ax[1].grid()
    ax[1].xaxis.set_label_position('top')
    ax[1].xaxis.set_ticks_position('top')
    ax[1].set_yticklabels([])

    # RHOB
    ax[2].plot(df.RHOB, df.Depth, c='r')
    ax[2].set_xlabel('Density (g/cc)')
    ax[2].set_ylim(top, bottom)
    ax[2].set_xlim(df.RHOB.min(), df.RHOB.max())
    ax[2].grid()
    ax[2].xaxis.set_label_position('top')
    ax[2].xaxis.set_ticks_position('top')
    ax[2].set_yticklabels([])

    # NPHI
    ax[3].plot(df.NPHI, df.Depth, c='black')
    ax[3].set_xlabel('NPHI (.pu)')
    ax[3].set_ylim(top, bottom)
    ax[3].set_xlim(df.NPHI.min(), df.NPHI.max())
    ax[3].grid()
    ax[3].xaxis.set_label_position('top')
    ax[3].xaxis.set_ticks_position('top')
    ax[3].set_yticklabels([])

    # DTCO
    ax[4].plot(df.DTCO, df.Depth, c='blue')
    ax[4].set_xlabel('DTCO (us/f)')
    ax[4].set_ylim(top, bottom)
    ax[4].set_xlim(df.DTCO.min(), df.DTCO.max())
    ax[4].grid()
    ax[4].xaxis.set_label_position('top')
    ax[4].xaxis.set_ticks_position('top')
    ax[4].set_yticklabels([])

    # DTSM
    ax[5].plot(df.DTSM, df.Depth, c='red')
    ax[5].set_xlabel('DTSM (us/f)')
    ax[5].set_ylim(top, bottom)
    ax[5].set_xlim(df.DTSM.min(), df.DTSM.max())
    ax[5].grid()
    ax[5].xaxis.set_label_position('top')
    ax[5].xaxis.set_ticks_position('top')
    ax[5].set_yticklabels([])
  
    # deposition environment
    im = ax[6].imshow(cluster, interpolation='none', aspect='auto',
                    cmap = cmap_env, vmin=0, vmax=6)
    ax[6].set_xlabel('Environment')
    ax[6].xaxis.set_label_position('top')
    ax[6].xaxis.set_ticks_position('top')
    ax[6].set_xticks([])
    ax[6].set_yticklabels([])

    # color bar
    divider = make_axes_locatable(ax[6])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax = cax)
    cbar.set_label((30*' ').join(['MoS ', 'Sh', 'MI', 
                                  'ImS', 'Ind', 'Ma']))
    cbar.set_ticks(range(0,1)); cbar.set_ticklabels('')

    # title
    fig.suptitle('%s Well'%df['Well'].iloc[0], fontsize = 14)

    plt.show()


def envplot_val(df, well):
    df = df[df['Well'] == well]

    # deposition environment color map
    env_colors = ['saddlebrown', 'yellowgreen', 'turquoise', 'darkgreen', 'grey', 'blue'] 
    cmap_env = colors.ListedColormap(env_colors) # make color into colormap

    cluster1 = np.repeat(np.expand_dims(df.Environment, 1), 100, 1)
    cluster2 = np.repeat(np.expand_dims(df.Env_pred, 1), 100, 1)

    # Set the top and bottom of depth
    top = df['Depth'].max()
    bottom = df['Depth'].min()

    # plotting
    fig, ax = plt.subplots(1, 8, figsize = (20, 12))

    # tops
    fm_tops = dict(df[['Formation', 'Depth']].dropna().values.tolist())

    ax[0].set_xlabel('Tops ', fontsize = '12' )
    ax[0].set_ylabel('Measured Depth (m) ', fontsize = '12' )
    ax[0].set_xticklabels([])
    ax[0].set_xticks([])
    ax[0].set_facecolor('#ffffed')
    ax[0].set_ylim(df.Depth.min(), df.Depth.max())
    ax[0].xaxis.set_label_position("top")
    ax[0].invert_yaxis()
    for Top in fm_tops.values() :
        ax[0].axhline(y = float(Top), color = 'k', lw = 1, ls = '-',    
                            alpha = 0.9, xmin = 0.06, xmax = 0.95 )
    for Top, MD in fm_tops.items():
        ax[0].text(x = 0.45,  y = float(MD), s = Top , fontsize = '9', 
                horizontalalignment = 'center', verticalalignment = 'bottom')

    # GR
    ax[1].plot(df.GR, df.Depth, c='g')
    ax[1].set_xlabel('Gamma Ray (API)')
    ax[1].set_ylim(top, bottom)
    ax[1].set_xlim(df.GR.min(), df.GR.max())
    ax[1].grid()
    ax[1].xaxis.set_label_position('top')
    ax[1].xaxis.set_ticks_position('top')
    ax[1].set_yticklabels([])

    # RHOB
    ax[2].plot(df.RHOB, df.Depth, c='r')
    ax[2].set_xlabel('Density (g/cc)')
    ax[2].set_ylim(top, bottom)
    ax[2].set_xlim(df.RHOB.min(), df.RHOB.max())
    ax[2].grid()
    ax[2].xaxis.set_label_position('top')
    ax[2].xaxis.set_ticks_position('top')
    ax[2].set_yticklabels([])

    # NPHI
    ax[3].plot(df.NPHI, df.Depth, c='black')
    ax[3].set_xlabel('NPHI (.pu)')
    ax[3].set_ylim(top, bottom)
    ax[3].set_xlim(df.NPHI.min(), df.NPHI.max())
    ax[3].grid()
    ax[3].xaxis.set_label_position('top')
    ax[3].xaxis.set_ticks_position('top')
    ax[3].set_yticklabels([])

    # DTCO
    ax[4].plot(df.DTCO, df.Depth, c='blue')
    ax[4].set_xlabel('DTCO (us/f)')
    ax[4].set_ylim(top, bottom)
    ax[4].set_xlim(df.DTCO.min(), df.DTCO.max())
    ax[4].grid()
    ax[4].xaxis.set_label_position('top')
    ax[4].xaxis.set_ticks_position('top')
    ax[4].set_yticklabels([])

    # DTSM
    ax[5].plot(df.DTSM, df.Depth, c='red')
    ax[5].set_xlabel('DTSM (us/f)')
    ax[5].set_ylim(top, bottom)
    ax[5].set_xlim(df.DTSM.min(), df.DTSM.max())
    ax[5].grid()
    ax[5].xaxis.set_label_position('top')
    ax[5].xaxis.set_ticks_position('top')
    ax[5].set_yticklabels([])
 
    # actual environment
    im = ax[6].imshow(cluster1, interpolation='none', aspect='auto',
                    cmap = cmap_env, vmin=0, vmax=6)
    ax[6].set_xlabel('Environment')
    ax[6].xaxis.set_label_position('top')
    ax[6].xaxis.set_ticks_position('top')
    ax[6].set_xticks([])
    ax[6].set_yticklabels([])


    # predicted environment
    im = ax[7].imshow(cluster2, interpolation='none', aspect='auto',
                    cmap = cmap_env, vmin=0, vmax=6)
    ax[7].set_xlabel('Predicted Environment')
    ax[7].xaxis.set_label_position('top')
    ax[7].xaxis.set_ticks_position('top')
    ax[7].set_xticks([])
    ax[7].set_yticklabels([])


    # color bar
    divider = make_axes_locatable(ax[7])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax = cax)
    cbar.set_label((30*' ').join(['MoS ', 'Sh', 'MI',
                                  'ImS', 'Ind', 'Ma']))
    cbar.set_ticks(range(0,1)); cbar.set_ticklabels('')

    # title
    fig.suptitle('%s Well' %df['Well'].iloc[0], fontsize = 14)

    fig.savefig('%s Depo Env Validation' %df['Well'].iloc[0])

    plt.show()


def envplot_test(df, well):
    df = df[df['Well'] == well]

    # deposition environment color map
    env_colors = ['saddlebrown', 'yellowgreen', 'turquoise', 'darkgreen', 'grey', 'blue'] 
    cmap_env = colors.ListedColormap(env_colors) # make color into colormap

    cluster = np.repeat(np.expand_dims(df.Env_pred, 1), 100, 1)

    # Set the top and bottom of depth
    top = df['Depth'].max()
    bottom = df['Depth'].min()

    # plotting
    fig, ax = plt.subplots(1, 5, figsize = (8, 12))

    # GR
    ax[0].plot(df.GR, df.Depth, c = 'g')
    ax[0].set_ylabel('Depth (m)')
    ax[0].set_xlabel('Gamma Ray (API)')
    ax[0].set_ylim(top, bottom)
    ax[0].set_xlim(df.GR.min(),df.GR.max())
    ax[0].grid()
    ax[0].xaxis.set_label_position('top')
    ax[0].xaxis.set_ticks_position('top')

    # RHOB
    ax[1].plot(df.RHOB, df.Depth, c = 'r')
    ax[1].set_xlabel('Density (g/cc)')
    ax[1].set_ylim(top, bottom)
    ax[1].set_xlim(df.RHOB.min(),df.RHOB.max())
    ax[1].grid()
    ax[1].xaxis.set_label_position('top')
    ax[1].xaxis.set_ticks_position('top')
    ax[1].set_yticklabels([])

    # NPHI
    ax[2].plot(df.NPHI, df.Depth, c = 'black')
    ax[2].set_xlabel('NPHI (.pu)')
    ax[2].set_ylim(top, bottom)
    ax[2].set_xlim(df.NPHI.min(),df.NPHI.max())
    ax[2].grid()
    ax[2].xaxis.set_label_position('top')
    ax[2].xaxis.set_ticks_position('top')
    ax[2].set_yticklabels([])

    # DTCO
    ax[3].plot(df.DTCO, df.Depth, c = 'blue')
    ax[3].set_xlabel('DTCO (us/f)')
    ax[3].set_ylim(top, bottom)
    ax[3].set_xlim(df.DTCO.min(),df.DTCO.max())
    ax[3].grid()
    ax[3].xaxis.set_label_position('top')
    ax[3].xaxis.set_ticks_position('top')
    ax[3].set_yticklabels([])
  
 
    # deposition environment
    im = ax[4].imshow(cluster, interpolation='none', aspect='auto',
                    cmap = cmap_env, vmin=0, vmax=6)
    ax[4].set_xlabel('Environment')
    ax[4].xaxis.set_label_position('top')
    ax[4].xaxis.set_ticks_position('top')
    ax[4].set_xticks([])
    ax[4].set_yticklabels([])


    # color bar
    divider = make_axes_locatable(ax[4])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax = cax)
    cbar.set_label((30*' ').join(['MoS ', 'Sh', 'MI', 
                                'ImS', 'Ind', 'Ma']))
    cbar.set_ticks(range(0,1)); cbar.set_ticklabels('')

    # title
    fig.suptitle('%s Well'%df['Well'].iloc[0], fontsize = 14)

    plt.show()


# gas level plotting
def gasplot_data(df, well):
    df = df[df['Well'] == well]

    # gas color map
    # color order = [0, 1, 2, 3, ...]
    gas_colors = ['blue', 'yellow']
    cmap_gas = colors.ListedColormap(gas_colors)  # make color into colormap

    cluster = np.repeat(np.expand_dims(df.Gas, 1), 100, 1)

    # Set the top and bottom of depth
    top = df['Depth'].max()
    bottom = df['Depth'].min()

    # plotting
    fig, ax = plt.subplots(1, 5, figsize=(8, 12))

    # GR
    ax[0].plot(df.GR, df.Depth, c='g')
    ax[0].set_ylabel('Depth (m)')
    ax[0].set_xlabel('Gamma Ray (API)')
    ax[0].set_ylim(top, bottom)
    ax[0].set_xlim(df.GR.min(), df.GR.max())
    ax[0].grid()
    ax[0].xaxis.set_label_position('top')
    ax[0].xaxis.set_ticks_position('top')

    # RHOB
    ax[1].plot(df.RHOB, df.Depth, c='r')
    ax[1].set_xlabel('Density (g/cc)')
    ax[1].set_ylim(top, bottom)
    ax[1].set_xlim(df.RHOB.min(), df.RHOB.max())
    ax[1].grid()
    ax[1].xaxis.set_label_position('top')
    ax[1].xaxis.set_ticks_position('top')
    ax[1].set_yticklabels([])

     # NPHI
    ax[2].plot(df.NPHI, df.Depth, c='black')
    ax[2].set_xlabel('NPHI (.pu)')
    ax[2].set_ylim(top, bottom)
    ax[2].set_xlim(df.NPHI.min(), df.NPHI.max())
    ax[2].grid()
    ax[2].xaxis.set_label_position('top')
    ax[2].xaxis.set_ticks_position('top')
    ax[2].set_yticklabels([])

    # DTCO
    ax[3].plot(df.DTCO, df.Depth, c='blue')
    ax[3].set_xlabel('DTCO (us/f)')
    ax[3].set_ylim(top, bottom)
    ax[3].set_xlim(df.DTCO.min(), df.DTCO.max())
    ax[3].grid()
    ax[3].xaxis.set_label_position('top')
    ax[3].xaxis.set_ticks_position('top')
    ax[3].set_yticklabels([])

    # lithology
    im = ax[4].imshow(cluster, interpolation='none', aspect='auto',
                      cmap=cmap_gas, vmin=0, vmax=1)
    ax[4].set_xlabel('Gas Level')
    ax[4].xaxis.set_label_position('top')
    ax[4].xaxis.set_ticks_position('top')
    ax[4].set_xticks([])
    ax[4].set_yticklabels([])

    # color bar
    divider = make_axes_locatable(ax[4])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax=cax)
    cbar.set_label((85 * ' ').join(['Low', 'Average']))
    cbar.set_ticks(range(0, 1));
    cbar.set_ticklabels('')

    # title
    fig.suptitle('%s Well' % df['Well'].iloc[0], fontsize=14)

    plt.show()


def gasplot_val(df, well):
    df = df[df['Well'] == well]

    # gas color map
    gas_colors = ['blue', 'yellow']
    cmap_gas = colors.ListedColormap(gas_colors)  # make color into colormap

    cluster1 = np.repeat(np.expand_dims(df.Gas, 1), 100, 1)
    cluster2 = np.repeat(np.expand_dims(df.Gas_pred, 1), 100, 1)

    # Set the top and bottom of depth
    top = df['Depth'].max()
    bottom = df['Depth'].min()

    # plotting
    fig, ax = plt.subplots(1, 6, figsize=(12, 12))

    # GR
    ax[0].plot(df.GR, df.Depth, c='g')
    ax[0].set_ylabel('Depth (m)')
    ax[0].set_xlabel('Gamma Ray (API)')
    ax[0].set_ylim(top, bottom)
    ax[0].set_xlim(df.GR.min(), df.GR.max())
    ax[0].grid()
    ax[0].xaxis.set_label_position('top')
    ax[0].xaxis.set_ticks_position('top')

    # RHOB
    ax[1].plot(df.RHOB, df.Depth, c='r')
    ax[1].set_xlabel('Density (g/cc)')
    ax[1].set_ylim(top, bottom)
    ax[1].set_xlim(df.RHOB.min(), df.RHOB.max())
    ax[1].grid()
    ax[1].xaxis.set_label_position('top')
    ax[1].xaxis.set_ticks_position('top')
    ax[1].set_yticklabels([])

    # NPHI
    ax[2].plot(df.NPHI, df.Depth, c='black')
    ax[2].set_xlabel('NPHI (.pu)')
    ax[2].set_ylim(top, bottom)
    ax[2].set_xlim(df.NPHI.min(), df.NPHI.max())
    ax[2].grid()
    ax[2].xaxis.set_label_position('top')
    ax[2].xaxis.set_ticks_position('top')
    ax[2].set_yticklabels([])

    # DTCO
    ax[3].plot(df.DTCO, df.Depth, c='blue')
    ax[3].set_xlabel('DTCO (us/f)')
    ax[3].set_ylim(top, bottom)
    ax[3].set_xlim(df.DTCO.min(), df.DTCO.max())
    ax[3].grid()
    ax[3].xaxis.set_label_position('top')
    ax[3].xaxis.set_ticks_position('top')
    ax[3].set_yticklabels([])

    # actual gas level
    im = ax[4].imshow(cluster1, interpolation='none', aspect='auto',
                      cmap=cmap_gas, vmin=0, vmax=1)
    ax[4].set_xlabel('Actual Gas Level')
    ax[4].xaxis.set_label_position('top')
    ax[4].xaxis.set_ticks_position('top')
    ax[4].set_xticks([])
    ax[4].set_yticklabels([])

    # predicted gas level
    im = ax[5].imshow(cluster2, interpolation='none', aspect='auto',
                      cmap=cmap_gas, vmin=0, vmax=1)
    ax[5].set_xlabel('Predicted Gas Level')
    ax[5].xaxis.set_label_position('top')
    ax[5].xaxis.set_ticks_position('top')
    ax[5].set_xticks([])
    ax[5].set_yticklabels([])

    # color bar
    divider = make_axes_locatable(ax[5])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax=cax)
    cbar.set_label((85 * ' ').join(['Low', 'Average']))
    cbar.set_ticks(range(0, 1));
    cbar.set_ticklabels('')

    # title
    fig.suptitle('%s Well' % df['Well'].iloc[0], fontsize=14)

    plt.show()


def gasplot_test(df, well):
    df = df[df['Well'] == well]

    # gas color map
    gas_colors = ['blue', 'yellow']
    cmap_gas = colors.ListedColormap(gas_colors)  # make color into colormap

    cluster = np.repeat(np.expand_dims(df.Gas_pred, 1), 100, 1)

    # Set the top and bottom of depth
    top = df['Depth'].max()
    bottom = df['Depth'].min()

    # plotting
    fig, ax = plt.subplots(1, 5, figsize=(8, 12))

    # GR
    ax[0].plot(df.GR, df.Depth, c='g')
    ax[0].set_ylabel('Depth (m)')
    ax[0].set_xlabel('Gamma Ray (API)')
    ax[0].set_ylim(top, bottom)
    ax[0].set_xlim(df.GR.min(), df.GR.max())
    ax[0].grid()
    ax[0].xaxis.set_label_position('top')
    ax[0].xaxis.set_ticks_position('top')

    # RHOB
    ax[1].plot(df.RHOB, df.Depth, c='r')
    ax[1].set_xlabel('Density (g/cc)')
    ax[1].set_ylim(top, bottom)
    ax[1].set_xlim(df.RHOB.min(), df.RHOB.max())
    ax[1].grid()
    ax[1].xaxis.set_label_position('top')
    ax[1].xaxis.set_ticks_position('top')
    ax[1].set_yticklabels([])

    # NPHI
    ax[2].plot(df.NPHI, df.Depth, c='black')
    ax[2].set_xlabel('NPHI (.pu)')
    ax[2].set_ylim(top, bottom)
    ax[2].set_xlim(df.NPHI.min(), df.NPHI.max())
    ax[2].grid()
    ax[2].xaxis.set_label_position('top')
    ax[2].xaxis.set_ticks_position('top')
    ax[2].set_yticklabels([])

    # DTCO
    ax[3].plot(df.DTCO, df.Depth, c='blue')
    ax[3].set_xlabel('DTCO (us/f)')
    ax[3].set_ylim(top, bottom)
    ax[3].set_xlim(df.DTCO.min(), df.DTCO.max())
    ax[3].grid()
    ax[3].xaxis.set_label_position('top')
    ax[3].xaxis.set_ticks_position('top')
    ax[3].set_yticklabels([])

    # gas level
    im = ax[4].imshow(cluster, interpolation='none', aspect='auto',
                      cmap=cmap_gas, vmin=0, vmax=1)
    ax[4].set_xlabel('Gas Level')
    ax[4].xaxis.set_label_position('top')
    ax[4].xaxis.set_ticks_position('top')
    ax[4].set_xticks([])
    ax[4].set_yticklabels([])

    # color bar
    divider = make_axes_locatable(ax[4])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar = plt.colorbar(im, cax=cax)
    cbar.set_label((85 * ' ').join(['Low', 'Average']))
    cbar.set_ticks(range(0, 1));
    cbar.set_ticklabels('')

    # title
    fig.suptitle('%s Well' % df['Well'].iloc[0], fontsize=14)

    plt.show()