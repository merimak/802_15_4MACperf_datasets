# HowTo

This folder contains additional code used for model testing and feature generation. We assume the experimenter has run an experiment using the WiSHFUL UPIs for WSNs that support TAISC (http://www.wishful-project.eu/software) and a global control program with event-based monitoring using the *RIME_appPerPacket_rxstats* event.




*Feature Generator*
The Feature Generator.py extracts features from the experimental data about MAC performance statistics. The correct path to the experimental data has to be set within the script.


*Test Model*
To evaluate the provided serialized neural network model, the testModel.py script can be used in the following way:

```
python -p "Path to Weka application folder" -m "Path to Weka serialized model object" -d "Path to testing set"

```
The output is Figure 3 from the Poster paper.