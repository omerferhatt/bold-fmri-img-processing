# Image processing on BOLD fMRI data

Blood oxygen level dependent functional magnetic resonance imaging (BOLD fMRI) is the most common
method for measuring human brain activity non-invasively in-vivo. BOLD fMRI images are 4-dimensional, consisting of a
time series of 3d volumes, acquired in quick succession (every 1 or 2 seconds) typically over a period of 8-15 minutes


##### Task
We will work with the `Multisubject - Multimodal Face Processing Dataset` available at openneuro.org.
* Link: https://openneuro.org/datasets/ds000117/versions/1.0.3

This dataset involves presentation of images of faces to the subject while acquiring BOLD fMRI images of the subject’s
brain activity. Your job is to preprocess these scans and then, in python, localize the brain area that processes faces.

---

### System Requirements

* Install both AFNI and FSL software packages on a Linux or Mac OS.
* If you use Windows, please refer to NeuroDebian virtual machine from https://neuro.debian.net/
* Python 3.7.x version preferred
* Anaconda3 or Miniconda3 used as Python environment

---

### Current System Specs

* Ubuntu 18.04 64-bit OS
* 16 GB RAM
* 3.7 GHZ 4 Core
* Single dataset: `~1GB`
* Whole dataset: `~45GB`

---

* `Python 3.7.6 64-bit` with Miniconda3
* Framework requirements are in `requirements.txt` file

---

### Installation steps:
* Please follow this wiki guide to install both AFNI and FSL libraries:
* http://miykael.github.io/nipype-beginner-s-guide/installation.html
