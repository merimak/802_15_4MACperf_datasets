# *802_15_4_MAC_perf* datasets introduction

The *802_15_4_MAC_perf* datasets is a repository that stores measurements collected from the wilab2 testbed facility in Ghent about the MAC layer performance in IEEE 802.15.4 networks. The data is collected for my research on modeling the MAC-level performance in wireless sensor networks.
The data is also available for participants of the eWINE Grand Challenge: https://ewine-project.eu/grand-challenge/ .


**Experimental setup**.
To  understand  the  MAC-level packet delivery  performance several experiments in the wilab2 testbed have been set up.
We used 28 RM090 nodes with an IEEE 802.15.4 radio organized in a star-like network topology, as shown on the figure below. All nodes use a CSMA/CA MAC protocol and periodically generate a 100 B message to a single receiver located in the center of the topology. The transmission power  is  set  to  the  maximum, i.e. 5dBm,  to  ensure all nodes are in communication range.  To incorporate all factors that impact the MAC performance we setup several experiments varying the number of sending nodes (2-28 nodes), and the application traffic load (1pckt/2, 1pckt/, 2pckts/, 4pckts/s, 8pckts/s, 16pckts/s and 64pckts/s).
We used a USRP B210 to generate controllable interference patterns by transmitting a modulated carrier for 2ms, followed by a 8ms idle period.

![experiment_setup](https://cloud.githubusercontent.com/assets/7999611/21597995/51e8ae4a-d154-11e6-8984-554d0109b8b1.png)

**Data collection**.
To simplify experiment control and data collection we created a global control program on the global controller using the Unified Programming Interfaces (UPIs) developed by the WiSHFUL project (http://www.wishful-project.eu/documents). We  run  several  experiments  with  the  aforementioned setups and measured several aspects of the MAC-level
performance, while the system was operating (around 21 hours).

For more details about the datasets please see the README file in the *datasets* folder. 

The *ML_model* folder contains the trained model from the publication in form of a Java binary serialized object exported from Weka.

#Citation
If using this dataset in your research, citation of the dataset with the assigned DOI and our publication introducing the dataset would be greatly appreciated! 

##Cite publication
To cite our work in progress introducing the dataset please use:

```
@ARTICLE{2016arXiv161203932K,
   author = {{Kulin}, M. and {de Poorter}, E. and {Kazaz}, T. and {Moerman}, I.
	},
    title = "{Poster: Towards a cognitive MAC layer: Predicting the MAC-level performance in Dynamic WSN using Machine learning}",
  journal = {ArXiv e-prints},
archivePrefix = "arXiv",
   eprint = {1612.03932},
 primaryClass = "cs.NI",
 keywords = {Computer Science - Networking and Internet Architecture},
     year = 2016,
    month = dec,
   adsurl = {http://adsabs.harvard.edu/abs/2016arXiv161203932K},
  adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```
This Poster publication is accepted for publiction in the Proceedings of the 2017 International Conference on Embedded Wireless Systems and Networks (EWSN), Uppsala, Sweden — February  20- 22, 2017.

##Cite dataset

To cite our dataset please use the following doi: 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.228613.svg)](https://doi.org/10.5281/zenodo.228613)


```
@misc{merima_kulin_2017_228613,
  author       = {Merima Kulin and
                  Eli de Poorter and
                  Tarik Kazaz and
                  Ingrid Moerman},
  title        = {{merimak/802\_15\_4MACperf\_datasets: MAC-level 
                   performance dataset for 802.15.4 WSNs}},
  month        = jan,
  year         = 2017,
  doi          = {10.5281/zenodo.228613},
  url          = {https://doi.org/10.5281/zenodo.228613}
}

```

##Acknowledgements
The research leading to these results has received funding from the European Horizon 2020 Programmes under grant agreement number 645274 (WiSHFUL) and number 688116 (eWINE).
I am particularly grateful to the following colleagues, for their assistance in the data collection phase:
* Jan Bauwens and Peter Ruckebush for their support when writting the UPI control programs in the phase of developing and testing the UPI interfaces for 802.15.4 nodes.
* Michael Mehari for his technical support in setting up the experimentation environment in the wilab2 testbed.

##Contact
For any additional information please do not hesitate to contact me:
**merima.kulin@intec.ugent.be** or **merima.kulin@gmail.com**
