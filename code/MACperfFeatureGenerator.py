'''
Created on Nov 2, 2016

@author: Merima Kulin
'''
#Copy of Create_trainingset.py

import pandas as pd
from numpy import *
from scipy.stats import mode
import csv
import sys
import os
import argparse

def load_dataset(path, tableName):
    """
        Loads observations
        
        Args:
            path (str): path to the data
            tableName (str): the table in the database where the data is located
        Returns:
            dataMatrix (df): data matrix
    """
    try:
        import sqlite3

        con = sqlite3.connect(path)
        df = pd.read_sql_query("SELECT * from " + tableName, con)
        con.close()
        return df
        
    except Exception, e:
        print("Connect Error: unable to start thread (" + str(e) + ")")


def extract_features_from_macstats(filename, observations):
    
    """Extracts features from 802.15.4 MAC statistics from a given observation interval
    Args:
        MAC statistics (df)
    Returns:
        feature vector (dict): has keys 'NumOfReceived', 'PRR', 'packetLoss', 'PLR', 'throughput', 'IPI', 'Density', 'COR'
    """

    name=filename.split("/")[-1]
    cor=name.split("COR")[0]
    numOfReceived=len(observations.index)
    packetLoss=float(sum(observations['packetLoss'].apply(int)))
    ipi=int(mode(observations['IPI'].apply(int))[0])
    density=int(mode(observations['Density'].apply(int))[0])
    sent=(numOfReceived+packetLoss)
    PLR=packetLoss/sent
    PRR=numOfReceived/float(sent)
    first=observations.head(1)
    last=observations.tail(1)
    timeframe=(float(last['timestamp'])-float(first['timestamp']))
    throughput= numOfReceived*100*8/(timeframe*pow(10,-6)) #total number of bits per time interval given the application payload of 100 B
    feature_vector={'NumOfReceived':numOfReceived, 'PRR':PRR, 'packetLoss':packetLoss, 'PLR':PLR, 'throughput':throughput, 'IPI': ipi, 'Density':density, 'COR':cor}

    return feature_vector

"""
Feature generator main program
"""
if __name__ == '__main__':
    
    #Input arguments
    my_arg_parser = argparse.ArgumentParser()
    my_arg_parser.add_argument("-d","--weka-dataset", help="Path to testset", default="", dest="datapath")

    my_args = my_arg_parser.parse_args()

    #Path to the collected data
    #dirpath="/home/mkulin/Desktop/eWINE/Experiments/Repository/example/";
    training_file_list=[my_args.datapath+filename for filename in os.listdir(my_args.datapath)]
    
    #Features extraction
    new=pd.DataFrame(columns=['NumOfReceived','PRR','packetLoss','PLR','throughput', 'IPI', 'Density', 'COR'])

    #Data integration
    print("Processing data files:")
    for f in file_list:
        print(f)
        data=load_dataset(f, "RIME_appPerPacket_rxstats")
        feature_vector=extract_features_from_macstats(f, data)
        new=new.append(feature_vector, ignore_index=True)
    #print(new.shape)

    exportpath="/home/mkulin/Desktop/eWINE/Experiments/Repository/Testing/"
    new[['NumOfReceived','PRR','packetLoss','PLR','throughput', 'IPI', 'Density']].to_csv(exportpath+'802_15_4_perf_30s.csv', sep=',', index=False)
    print("Generated feature vectors!")


