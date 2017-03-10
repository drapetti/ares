"""
Mirocha, Sun, and Furlanetto (2016), in prep.

Parameters defining the fiducial model (see Table 1).
"""

from numpy import inf
from ares.physics.Constants import E_LyA

# Calibration set!
dpl = \
{

 # Halos, MAR, etc.
 'pop_Tmin{0}': 1e4,
 'pop_Tmin{1}': 'pop_Tmin{0}',
 'pop_sfr_model{0}': 'sfe-func',
 'pop_sfr_model{1}': 'link:sfrd:0',
 'pop_MAR{0}': 'hmf',
 'pop_MAR_conserve_norm{0}': False,
 
 # Stellar pop + fesc
 'pop_sed{0}': 'eldridge2009',
 'pop_binaries{0}': False,
 'pop_Z{0}': 0.02,
 'pop_Emin{0}': 10.19,
 'pop_Emax{0}': 24.6,
 'pop_rad_yield{0}': 'from_sed', # EminNorm and EmaxNorm arbitrary now
                             # should make this automatic

 'pop_fesc{0}': 0.1,
 
 # Solve LWB!
 'pop_solve_rte{0}': (10.2, 13.6),

 
 # SFE
 'pop_fstar{0}': 'pq[0]',
 'pq_func{0}[0]': 'dpl',
 'pq_func_var{0}[0]': 'Mh',
 
 ##
 # IMPORTANT
 ##
 'pq_func_par0{0}[0]': 0.05,       # Table 1 in paper (last 4 rows)
 'pq_func_par1{0}[0]': 2.8e11,
 'pq_func_par2{0}[0]': 0.49,       
 'pq_func_par3{0}[0]': -0.61,      
 'pop_calib_L1600{0}': 1.0185e28,      # Enforces Equation 13 in paper 
 ##
 #
 ##

 # Careful with X-ray heating
 'pop_sed{1}': 'mcd',
 'pop_Z{1}': 'pop_Z{0}',
 'pop_rad_yield{1}': 2.6e39,
 'pop_rad_yield_Z_index{1}': None,
 'pop_alpha{1}': -1.5, # not used unless fesc > 0
 'pop_Emin{1}': 2e2,
 'pop_Emax{1}': 3e4,
 'pop_EminNorm{1}': 5e2,
 'pop_EmaxNorm{1}': 8e3,
 'pop_logN{1}': -inf,

 'pop_solve_rte{1}': True,
 'pop_tau_Nz{1}': 1000,
 'pop_approx_tau{1}': 'neutral',

 # Control parameters
 'include_He': True,
 'approx_He': True,
 'secondary_ionization': 3,
 'approx_Salpha': 3,
 'problem_type': 102,
 'photon_counting': True,
 'cgm_initial_temperature': 2e4,
 'cgm_recombination': 'B',
 'clumping_factor': 3.,
 #'smooth_derivative': 0.5,
 'final_redshift': 5.,
}

_floor_specific = \
{
'pq_val_floor{0}[0]': 0.005,
}

floor = dpl.copy()
floor.update(_floor_specific)

_steep_specific = \
{
 'pq_focc{0}': 'pq[1]',
 'pq_func{0}[1]': 'okamoto',
 'pq_func_var{0}[1]': 'Mh',
 'pq_func_par0{0}[1]': 1.,
 'pq_func_par1{0}[1]': 1e9,
}

steep = dpl.copy()
steep.update(_steep_specific)

"""
Redshift-dependent options.
"""

_flex = \
{
 'pq_func{0}[0]': 'dpl_arbnorm',
 'pq_func_var{0}[0]': 'Mh',
 
 # Standard dpl model at 10^8 Msun
 'pq_func_par0{0}[0]': 'pq[1]',
 'pq_func_par1{0}[0]': 'pq[2]',
 'pq_func_par2{0}[0]': 0.49,
 'pq_func_par3{0}[0]': -0.61,
 'pq_func_par4{0}[0]': 1e8,        # Mass at which fstar,0 is defined
 
 # Evolving part
 'pq_func{0}[1]': 'pl',
 'pq_func_var{0}[1]': '1+z',
 'pq_func_par0{0}[1]': 0.00205,
 'pq_func_par1{0}[1]': 7.,
 'pq_func_par2{0}[1]': 0.,   # power-law index!
 
 'pq_func{0}[2]': 'pl',
 'pq_func_var{0}[2]': '1+z',
 'pq_func_par0{0}[2]': 2.8e11,
 'pq_func_par1{0}[2]': 7.,
 'pq_func_par2{0}[2]': 0.,   # power-law index!
  
}

dpl_flex = dpl.copy()
dpl_flex.update(_flex)

_flex2 = \
{
 'pq_func{0}[0]': 'dpl_arbnorm',
 'pq_func_var{0}[0]': 'Mh',
 
 # Standard dpl model at 10^8 Msun
 'pq_func_par0{0}[0]': 'pq[1]',
 'pq_func_par1{0}[0]': 'pq[2]',
 'pq_func_par2{0}[0]': 'pq[3]',
 'pq_func_par3{0}[0]': 'pq[4]',
 'pq_func_par4{0}[0]': 1e8,        # Mass at which fstar,0 is defined
 
 # Evolving part
 'pq_func{0}[1]': 'pl',
 'pq_func_var{0}[1]': '1+z',
 'pq_func_par0{0}[1]': 0.00205,
 'pq_func_par1{0}[1]': 7.,
 'pq_func_par2{0}[1]': 0.,   # power-law index!
 
 'pq_func{0}[2]': 'pl',
 'pq_func_var{0}[2]': '1+z',
 'pq_func_par0{0}[2]': 2.8e11,
 'pq_func_par1{0}[2]': 7.,
 'pq_func_par2{0}[2]': 0.,   # power-law index!
 
 'pq_func{0}[3]': 'pl',
 'pq_func_var{0}[3]': '1+z',
 'pq_func_par0{0}[3]': 0.49,
 'pq_func_par1{0}[3]': 7.,
 'pq_func_par2{0}[3]': 0.,   # power-law index!
 
 'pq_func{0}[4]': 'pl',
 'pq_func_var{0}[4]': '1+z',
 'pq_func_par0{0}[4]': -0.61,
 'pq_func_par1{0}[4]': 7.,
 'pq_func_par2{0}[4]': 0.,   # power-law index!
 
 
}

dpl_evol = dpl.copy()
dpl_evol.update(_flex2)

