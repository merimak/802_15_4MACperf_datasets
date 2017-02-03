# HowTo

This folder contains additional code used for model testing and feature generation. We assume the experimenter has run an experiment using the WiSHFUL UPIs for WSNs that support TAISC (http://www.wishful-project.eu/software) and a global control program with event-based monitoring using the *RIME_appPerPacket_rxstats* event.

The generic flow for modeling the MAC-level performance predictor is described below.

## Data collection

To generate experimental data for MAC statistics the following steps are involved:
* Create WiSHFUL control program (configure network and radio parameters)
* Register events for which data has to be collected (MAC statistics)
* Define scenario
* Define monitoring duration
* Dump data for post-processing (SQLite, CSV, MySQL, OML...)

![datacollection](https://cloud.githubusercontent.com/assets/7999611/22187153/9311db1e-e101-11e6-889e-95d2bbc69e05.JPG)


## Feature Generator

### *Offline Feature Extraction*

To extract MAC-level performance statistics from the collected the *MACperfFeatureGenerator.py* script is used. The script takes the path to the experimental data as input argument.
```
python MACstatsFeatureGenerator.py -d “Path to data”
```
![pre_process](https://cloud.githubusercontent.com/assets/7999611/22187164/c1465528-e101-11e6-9f2d-ab94836bf3f0.jpg)

### *On-the-fly Feature Extraction*

MAC-level performance statistics can be automatically extracted on-the-fly in the data collection phase. The framework extension module will be soon available. 

![otf_featuregen](https://cloud.githubusercontent.com/assets/7999611/22334205/223a24ba-e3da-11e6-8f50-8c96124d5129.jpg)


## Create MAC-level performance predictor
Train the MAC-level performance predictor:
```
java -classpath weka.jar weka.classifiers.functions.MultilayerPerceptron -t “Path to dataset" -L 0.1 -N 2000 -H 10 -d “Path to model"
```
![genmodel](https://cloud.githubusercontent.com/assets/7999611/22187171/cf2cda7c-e101-11e6-8684-41ebd0e7b8d4.jpg)


## Evaluate Model

To evaluate the provided serialized neural network model with trace-based simulation, the testModel.py script can be used in the following way:
```
python -p "Path to Weka application folder" -m "Path to Weka serialized model object" -d "Path to testing set"
```
The script generates a performance graph showing the real vs. predicted instance.

![testmodel](https://cloud.githubusercontent.com/assets/7999611/22187173/d9e6da58-e101-11e6-973f-8b4ad5bd3a03.jpg)
