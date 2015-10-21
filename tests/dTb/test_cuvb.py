"""

test_21cm_cxrb.py

Author: Jordan Mirocha
Affiliation: University of Colorado at Boulder
Created on: Mon Nov 11 13:02:00 MST 2013

Description: 

"""

import os, ares
import matplotlib.pyplot as pl

pars = \
{
 'pop_sed{0}': 'bb',
 'pop_Emin{0}': 5.,
 'pop_Emax{0}': 13.58,
 'pop_EminNorm{0}': 10.2,
 'pop_EmaxNorm{0}': 13.6,
 'pop_yield{0}': 9690.,
 'pop_yield_units{0}': 'photons/baryon',
 'pop_solve_rte{0}': True,
 'pop_tau_Nz{0}': 400,
 'include_H_Lya': False,
 'lya_nmax': 5,
}

logTsurf = [4.]

ax_dTb = None
fig_Ja = pl.figure(2); ax_Ja = fig_Ja.add_subplot(111)
ls = '-', '--'
colors = 'b', 'g', 'm'
for j, injected in enumerate([False]):
    tpB = []

    for i, logT in enumerate(logTsurf):
                
        pars.update({'source_temperature{0}': 10**logT, 
            'lya_injected{0}': injected})
        sim = ares.simulations.Global21cm(**pars)
        sim.run()

        if j == 0:
            label = r'$T_{\ast} = 10^{%.2g} \ \mathrm{K}$' % (logT)
        else:
            label = None

        anl = ares.analysis.Global21cm(sim)
        ax_dTb = anl.GlobalSignature(ax=ax_dTb, color=colors[i], label=label,  
            ls=ls[j])
            
        mask = sim.history['z'] < 50
        ax_Ja.semilogy(sim.history['z'][mask], sim.history['igm_Ja'][mask], 
            color=colors[i], ls=ls[j])
        
        pl.draw()
        
# Fiducial model, approximate Lyman-alpha background
sim_fid = ares.simulations.Global21cm()
sim_fid.run()

anl = ares.analysis.Global21cm(sim_fid)
ax_dTb = anl.GlobalSignature(ax=ax_dTb, color='k', ls='-')

mask = sim_fid.history['z'] < 50
ax_Ja.semilogy(sim_fid.history['z'][mask], sim_fid.history['igm_Ja'][mask], 
    color='k', ls='-')

pl.show()

