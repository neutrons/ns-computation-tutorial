# nxs-computational-tutorial-2026

## Agenda

### Set up
1. Log into `analysis.sns.gov`
2. Run script `start_jupyter.sh` provided by Jean B. in /SNS/EXAMPLES/NS2026/

### Introductory Lectures (powerpoint) 30-45 mins.
 * Intro: What is scientific software (MG)
 * Version control and collaboration: Git and GitHub (MG)
 * Environment management (micromamba, pixi and pip) (JB):
 * Running python options: scripts, python interpreter, IDE, jupyter (JB)
 * Intro to file systems at ORNL. Where are my neutron data stored? Oncat (AS)
 * LLM in the scientific data pipeline (MD)

### Tutorials

#### Malcolm tutorial

* create a git repo

#### Jean tutorial

 * Open notebook, Explanation of notebook (shift enter, shift enter...)
 * Cell: imports:
 * Demo 1: Import data from ascii to numpy array. Do this multiple ways. Mention pandas.
 * Demo 2: Plot with matplotlib. Make it interactive. Show errors?
 * Demo 3: Extend script to for loop over multiple files
 * Demo 4: Create widget to do Exercise 3.

BREAK (AS)

#### Zach Tutorial 2

 * Exercise 4 (SciPy): Set up fit to a peak: initial conditions, define to fit, define residual, define fit range, interpret errors (variance-covariance matrix)
 * Exercise 5: Use LMFIT for same process.
 * Advanced Exercise 1: Event data: Inspect nxs file with HDFView,
 * Load neutron data and log metadata from nxs file with h5py.
 * Advanced Ex 2: histogram events (with log binning)
 * Super Advanced Ex 3: Re-use fitting script, fit peaks, plot position versus experimental log.

#### Vibe coding a science app

 * We will split into teams and compete to build the best app!  

#### References

__Environment management__
* [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html)
* [pixi](https://pixi.sh/latest/)
* [pip](https://pypi.org/project/pip/)

__Python editors__
* [jupyter](https://jupyter.org/)
* [visual code](https://code.visualstudio.com/)
* [pycharm](https://www.jetbrains.com/pycharm/)

__Python librairies__
* [matplotlib](https://matplotlib.org/)
* [numpy](https://numpy.org/)
* [widgets](https://ipywidgets.readthedocs.io/en/latest/index.html)

__
