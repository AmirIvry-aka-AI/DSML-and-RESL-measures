# Objective Metrics to Evaluate Residual-Echo Suppression During Double-Talk 

<p align="center">
Amir Ivry, Prof. Israel Cohen, and Dr. Baruch Berdugo<br /> 
Andrew and Erna Viterbi Faculty of Electrical and Computer Engineering, Technion - Israel Institute of Technology<br /> 
This research was supported by the Pazy Research Foundation and the ISF-NSFC joint research program
</p>

## Overview
Human subjective evaluation is optimal to assess speech quality for human perception. The recently introduced deep noise suppression mean opinion score (DNSMOS) metric was shown to estimate human ratings with great accuracy. The signal-to-distortion ratio (SDR) metric is widely used to evaluate residual-echo suppression (RES) systems by estimating speech quality during double-talk. However, since the SDR is affected by both speech distortion and residual-echo presence, it does not correlate well with human ratings according to the DNSMOS. To address that, we introduce two objective metrics to separately quantify the desired-speech maintained level (DSML) and residual-echo suppression level (RESL) during double-talk. These metrics are evaluated using a deep learning-based RES-system with a tunable design parameter. Using 280 hours of real and simulated recordings, we show that the DSML and RESL correlate well with the DNSMOS with high generalization to various setups. Also, we empirically investigate the relation between tuning the RES-system design parameter and the DSML-RESL tradeoff it creates and offer a practical design scheme for dynamic system requirements. 

<br /> 

| ![setup-1](https://user-images.githubusercontent.com/22732198/124920790-60960b80-e000-11eb-9754-bbadd0a88299.jpg) |
|:--:|
| *Residual echo suppression scenario* |
