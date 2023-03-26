import numpy as np
import matplotlib.pyplot as plt

expNominal = "/Users/theo/Downloads/HEPData-ins2628398-v1-excl_strong_mgluino_2400_GeV_exp_nominal.csv"
expNominaldata = np.genfromtxt(expNominal, delimiter=',', skip_header=11, names=['X','Y'])

expUp = "/Users/theo/Downloads/HEPData-ins2628398-v1-excl_strong_mgluino_2400_GeV_exp_up.csv"
expUpdata = np.genfromtxt(expUp, delimiter=',', skip_header=11, names=['X','Y']) 

expDown = "/Users/theo/Downloads/HEPData-ins2628398-v1-excl_strong_mgluino_2400_GeV_exp_down.csv"
expDowndata = np.genfromtxt(expDown, delimiter=',', skip_header=11, names=['X','Y']) 

obsNominal = "/Users/theo/Downloads/HEPData-ins2628398-v1-excl_strong_mgluino_2400_GeV_obs_nominal.csv"
obsNominaldata = np.genfromtxt(obsNominal, delimiter=',', skip_header=11, names=['X','Y']) 

obsUp = "/Users/theo/Downloads/HEPData-ins2628398-v1-excl_strong_mgluino_2400_GeV_obs_up.csv"
obsUpdata = np.genfromtxt(obsUp, delimiter=',', skip_header=11, names=['X','Y']) 

obsDown = "/Users/theo/Downloads/HEPData-ins2628398-v1-excl_strong_mgluino_2400_GeV_obs_down.csv"
obsDowndata = np.genfromtxt(obsDown, delimiter=',', skip_header=11, names=['X','Y']) 


plt.plot(expNominaldata['X'], expNominaldata['Y'], linestyle='dashed', color='black', label='Exp limit(\u00B1 1$\sigma_{exp}$)')
plt.plot(expUpdata['X'],expUpdata['Y'],color='yellow', label= 'Exp. limit(\u00B1 1$\sigma_{exp}$)')
plt.plot(expDowndata['X'],expDowndata['Y'], color='yellow')
plt.plot(obsNominaldata['X'],obsNominaldata['Y'],color='firebrick', label='Obs. limit(\u00B1 1$\sigma^{SUSY}_{theory}$)')
plt.plot(obsUpdata['X'], obsUpdata['Y'],linestyle='dotted',color='firebrick', label='Obs. limit(\u00B1 1$\sigma^{SUSY}_{theory}$)')
plt.plot(obsDowndata['X'],obsDowndata['Y'],linestyle='dotted',color='firebrick')
plt.xscale('log')
plt.xlabel('\u03C4 [ns]')
plt.ylabel('$m_{\u03C7_{1}^0}$ [GeV]')
plt.ylim(0,2500)
plt.text(.1, 2300 ,'$ATLAS$', fontsize=15)
plt.text(.09,2200, '$\sqrt{s}$ = 13TeV, L = 139 $fb^{-1}$ ', fontsize=10)
plt.text(.1,2100, '$m_{\widetilde{g}}$ = 2.4 TeV', fontsize=10)
plt.legend(loc='center', frameon=False)
plt.show()
