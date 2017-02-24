"""
Leitherer, C., Schaerer, D., Goldader, J. D., Delgado, R. M. G., Robert, C.,
Kune, D. F., de Mello, D. F., Devost, D., & Heckman, T. M. 1999, ApJS,
123, 3

Notes
-----

"""

import re, os
import numpy as np
from scipy.interpolate import interp1d
from ares.physics.Constants import h_p, c, erg_per_ev, g_per_msun, s_per_yr, \
    s_per_myr, m_H, Lsun

_input = os.getenv('ARES') + '/input/bpass_v1/SEDS'

metallicities = \
{
 '040': 0.040,
 '020': 0.020,
 '008': 0.008,
 '004': 0.004,
 '001': 0.001,
}

sf_laws = \
{
 'continuous': 1.0,       # solar masses per year
 'instantaneous': 1e6,    # solar masses
}

imf_options = None

info = \
{
 'flux_units': r'$L_{\odot} \ \AA^{-1}$',
}

_log10_times = np.arange(6, 10.1, 0.1)
times = 10**_log10_times / 1e6            # Convert from yr to Myr

def _kwargs_to_fn(**kwargs):
    """
    Determine filename of appropriate BPASS lookup table based on kwargs.
    """

    # All files share this prefix
    fn = 'sed.bpass'
    
    if kwargs['pop_ssp']:
        fn += '.instant'
    else:
        fn += '.constant'
    
    if kwargs['pop_nebular']:
        fn += '.cloudy'
    else:
        fn += '.nocont'
    
    if kwargs['pop_binaries']:
        fn += '.bin'
    else:
        fn += '.sin'
    
    # Metallicity
    fn += '.z%s' % str(int(kwargs['pop_Z'] * 1e3)).zfill(3)   
            
    return _input + '/' + fn    
            
def _load(**kwargs):
    """
    Return wavelengths, fluxes, for given set of parameters (at all times).
    """
    
    Zvals = np.sort(metallicities.values())

    # Interpolate
    if kwargs['pop_Z'] not in Zvals:
        tmp = kwargs.copy()
                
        spectra = []
        del tmp['pop_Z']
        for Z in Zvals:
            _w1, _d1 = _load(pop_Z=Z, **tmp)
            spectra.append(_d1.copy())
        
        wavelengths = wave = _w1
        data = spectra

    # No interpolation necessary
    else:        
        fn = _kwargs_to_fn(**kwargs)
        _raw_data = np.loadtxt(fn)
        
        data = np.array(_raw_data[:,1:])
        wavelengths = _raw_data[:,0]

        data *= Lsun

    return wavelengths, data    
            
