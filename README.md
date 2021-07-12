# Objective Metrics to Evaluate Residual-Echo Suppression During Double-Talk (Accepted to WASPAA 2021 Conference)
## Amir Ivry, Prof. Israel Cohen, Dr. Baruch Berdugo
> Human subjective evaluation is optimal to assess speech quality for human perception, and the recently introduced deep noise suppression mean opinion score (DNSMOS) metric was shown to estimate human ratings with great accuracy. Still, the signal-to-distortion ratio (SDR) metric is widely used to evaluate residual-echo suppression (RES) systems by estimating speech quality during double-talk. However, since the SDR is affected by both speech distortion and residual-echo presence, it does not correlate well with human ratings according to the DNSMOS. <br/> To address that, we introduce two objective metrics to separately quantify the desired-speech maintained level (DSML) and residual-echo suppression level (RESL) during double-talk, and share the code here for reproducability. <br/> You are also encouraged to refer to the more elaborated [github page](https://amirivry-aka-ai.github.io/DSML-and-RESL-measures/) and published paper [Arxiv].
> Demo can be found [_here_](https://soundcloud.com/ai4audio/sets/objective-metrics-to-evaluate-residual-echo-suppression-during-double-talk). 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- Provide general information about your project here.
- What problem does it (intend to) solve?
- What is the purpose of your project?
- Why did you undertake it?
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- Python 3.8.6
- scipy==1.7.0
- matplotlib==3.4.2
- numpy==1.21.0


## Setup
To prepare for usage, the user should follow steps:
- Clone this repo
- Set up a virtual environment and run: `pip install -r requirements.txt`
- Create a parent direcotry and assign its relative path to `data_path` variable inside `main.py`
- Inside this dir, locate every separate set of examples to analyze in a separate subdirectory, and name it uniquely. Each subfolder must contain at least 3 .wav files - the near end speech, the RES input, and the RES prediction. The names of these 3 files should be uniform accross all subdirectories. Assign these 3 file names to the `patterns` variable inside `main.py`. 

The last two steps are explained with the following snippet. After cloning the repo and setting up the venv, a parent directory called _Demo_ is created and its name is assigned to `data_path`. Inside _Demo_, there are 5 subdirectories uniquely named _Example 1_ through _Exmaple 5_. Inside _Example 1_, for instance, there are several files, 3 of which are essential - _near_end_speech.wav_, _res_input.wav_, and _res_prediction.wav_. These names are consistent across all subdirectores and are assigned in *that order* to `patterns`.


| ![image](https://user-images.githubusercontent.com/22732198/125336393-64a29000-e356-11eb-910d-1b7af4520549.png) |
|:--:|
| *Snippet of the project setup before run* |


## Usage
After setup, the user should follow these steps to use the code:
- run: `main.py`
- The log file `evaluation_metrics.txt` will appear inside the path specified in `data_path` (see _Setup_ for details). It contains the mean and standard deviation values for every subdirectory.


| ![image](https://user-images.githubusercontent.com/22732198/125337140-4ab57d00-e357-11eb-91d7-40c16f2864f8.png) |
|:--:|
| *Snippet of the project setup after run* |


## Project Status
Project is complete with respect to occassional fine-tuning (see _Room for Improvement_ below)


## Room for Improvement
Future release may include: 
- Double-talk detector for efficient analysis of measures
- Additional parameters for enhanced user experience (e.g., saving option of raw measures data and its figures)
- Option to run code from shell


## Acknowledgements
This research was supported by the Pazy Research Foundation, the Israel Science Foundation (ISF), and the International Speech Communication Association (ISCA). We would also like to thank stem audio for their technical support.


## Contact
Created by [Amir Ivry](https://www.linkedin.com/in/amirivry/) - feel free to contact me also via [amirivry@gmail.com](amirivry@gmail.com).
