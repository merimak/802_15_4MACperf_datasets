# Dataset description

The 802.15.4 MAC layer performance datasets consist of 12 files, corresponding to measurements from different observation
interval granularity used in the experiments, located in the folder [*Training_data*](Training_data/). The folder contains a fine-granularity
dataset with short-term MAC statistics over a time interval of 5 seconds, and several derived coarse-granularity 
dataset with long-term MAC statistics over 10, 15, 20, 25, 30, 35, 40, 45, 50 and 55*s*.
In particular, it contains the following datasets:
* MAC-level statistics over a time interval of 5 seconds (i.e. 802_15_4_MACperf_5s.csv)
* MAC-level statistics over a time interval of 10 seconds (i.e. 802_15_4_MACperf_10s.csv)
* MAC-level statistics over a time interval of 15 seconds (i.e. 802_15_4_MACperf_15s.csv)
* MAC-level statistics over a time interval of 20 seconds (i.e. 802_15_4_MACperf_20s.csv)
* MAC-level statistics over a time interval of 25 seconds (i.e. 802_15_4_MACperf_25s.csv)
* MAC-level statistics over a time interval of 30 seconds (i.e. 802_15_4_MACperf_30s.csv)
* MAC-level statistics over a time interval of 35 seconds (i.e. 802_15_4_MACperf_35s.csv)
* MAC-level statistics over a time interval of 40 seconds (i.e. 802_15_4_MACperf_40s.csv)
* MAC-level statistics over a time interval of 45 seconds (i.e. 802_15_4_MACperf_45s.csv)
* MAC-level statistics over a time interval of 50 seconds (i.e. 802_15_4_MACperf_50s.csv)
* MAC-level statistics over a time interval of 55 seconds (i.e. 802_15_4_MACperf_55s.csv)
* MAC-level statistics over a time interval of 60 seconds (i.e. 802_15_4_MACperf_60s.csv)


Each file consists of the following 8 columns: '*NumOfReceived*', '*PRR*', '*packetLoss*', '*PLR*', '*throughput*', '*IPI*', '*Density*', '*COR*',
corresponding to the following MAC-level statistics:
* '*NumOfReceived*' is the number of received frames during a particular observation interval;
* '*PRR*' is the Packet Reception Rate, e.g. the percentage of received frames withing a particular observation interval;
* '*packetLoss*' is the number of erroneous frames within a particular observation interval;
* '*PLR*' is the Packet Loss Rate, i.e. the percentage of Lost frames withing a particular observation interval;
* '*throughput*' is the aggregated throughput of all sending nodes within a particular observation interval;
* '*IPI*' is the Inter-Packet-Interval of the transmitter expressed as *X*/128 (*seconds*), where *X* is the value in the '*IPI*' column;
* '*Density*' is the number of nodes that were active during the experiment observation interval;
* '*COR*' is the Channel Occupancy Ratio which indicates the level of interference generated, e.g. a level of 20 indicates a interference pattern generated 20% of a time period, i.e. transmitting a modulated carrier for 2ms, followed by a 8 ms idle period- repeated during the experiment.


The folder [*Testing_data*](Testing_data/) contains coarse-granularity measurements from a separate set of experiments that were used for testing the developed machine learning model in the publication. It has the same format as the aforementioned datasets, with an observation interval granularity of 30 seconds.

