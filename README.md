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

#### System Requirements

* Install both AFNI and FSL software packages on a Linux or Mac OS.
* If you use Windows, please refer to NeuroDebian virtual machine from https://neuro.debian.net/
* Python 3.7.x version preferred


##### Current System Specs

* Ubuntu 18.04 64-bit OS
* 16 GB RAM
* 3.7 GHZ 4 Core
* Single run dataset: `~5GB`
* Whole dataset: `~300GB`
* `Python 3.7.6 64-bit` with Miniconda3
* Framework requirements are in `requirements.txt` file

##### Installation steps:
* Please follow this wiki guide to install both AFNI and FSL libraries:
* http://miykael.github.io/nipype-beginner-s-guide/installation.html

---

## How to use
Project has a couple of different workflow in it.

* Folder manipulation
* Pre-processing
* Localizing
* Visualizing

---

##### Pre-processing usage
* `python3 main.py --pre-process`
    * Only pre-processing

* `python3 main.py --pre-process --localize`
    * Pre-processing after localization
    
* `python3 main.py --select-data patient01 patient02 --pre-process localize`
    * Pre-processing and localization on only specified datas
    
##### Using previous pre-processed data
* `python3 main.py --use-pre ...`
    * Use `--use-pre` instead of `--pre-process to get avoid long process time
    
##### Localizing
* Localizing raw data
    * `python3 main.py --localize`

* Localizing processed data
    * `python3 main.py --use-pre --localize`
    
##### Visualizing correlations
* Can visualize one dataset only
    * `python3 main.py --select-data patient01 --use-pre --visualize-corr`

##### Batch Processing
* Only works with processed data
    * `python3 main.py --use-pre --localize --batch-process`
---
#### Arguments

* Console input:

`python3 main.py --help`

--- 
`-h, --help`
* Shows help message

`-p, --pre-process`
* Pre-process whole data in raw directory.
May take several hours according to the computer. 
Use the `--select-data` parameter to pre-process only the desired data
                    
`-u, --use-pre`
* When the flag is activated, uses pre-processed data to localize faces.
                    
`-l, --localize`
* Applies localize task activation to the MRI input

`--pipeline PIPELINE`
* Specifies the path to the bash code that will create the pipeline, leave it as default to work normally.
                    
`-S SELECT_DATA [SELECT_DATA ...], --select-data SELECT_DATA [SELECT_DATA ...]`
* Select data, otherwise all of them going to be used.
                    
`--data-folder` DATA_FOLDER
* Specifies the path to the folder containing the raw data.
                    
`--pre-data-folder` PRE_DATA_FOLDER
* Specifies the path to the folder where the processed data is located or to be saved after pre-processing.

`-b, --batch_process`
* Applies linear alignment and registration with correlation into T1 image.

`-v, --visualize-corr`
* Visualize different between processed and unprocessed data corr. Needs to be used with `--use-pre`
                    
`-i INPUT_FILE, --input-file INPUT_FILE`
* Specifies the input MRI image file name

`-o OUTPUT_FILE, --output-file OUTPUT_FILE`
* Specifies the output MRI image file name

`-e EVENT_FILE, --event-file EVENT_FILE`
* Specifies the events file name

`-H HRF_FILE, --hrf-file HRF_FILE`
* Specifies the HRF file name

`-t TEMPLATE, --template TEMPLATE`
* Specifies the path to template T1 space, leave it as default to work normally.
                    

