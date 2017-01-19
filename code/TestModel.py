'''
Created on Jan 19, 2017

@author: Merima Kulin
'''

import subprocess
import logging
import time
import argparse
import threading
import os
import matplotlib.pyplot as plt
import numpy as np
import argparse

def runWeka(wekapath, modelpath, datapath):
    os.chdir(wekapath)
    proc = subprocess.Popen(['/usr/bin/java', '-classpath', 'weka.jar', 'weka.classifiers.functions.MultilayerPerceptron', '-l', modelpath, '-T', datapath, '-p', '0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    return out


"""
Test offline trained model in Weka on a test set
"""
if __name__ == '__main__':
    
    #Input arguments
    my_arg_parser = argparse.ArgumentParser()
    my_arg_parser.add_argument("-p","--weka-path", help="Path to Weka application folder", dest="wekapath")
    my_arg_parser.add_argument("-m","--weka-model", help="Path to Weka serialized model", dest="modelpath")
    my_arg_parser.add_argument("-d","--weka-dataset", help="Path to testset", default="", dest="datapath")

    my_args = my_arg_parser.parse_args()
    
    #wekapath="/home/mkulin/Desktop/eWINE/Experiments/Repository/Testing/Weka_stable-3-6/weka/"
    #modelpath="/home/mkulin/Desktop/eWINE/Experiments/Repository/Testing/Neural_network_MACperf_prediction.model"
    #datapath="/home/mkulin/Desktop/eWINE/Experiments/Repository/Testing/802_15_4_perf_30s_testset_Weka.csv"
    
    predictions=runWeka(my_args.wekapath, my_args.modelpath, my_args.datapath)
    
    k=1
    matrix = []
    for row in predictions.split('\n'):
    
        if k<6:
            k=k+1
            continue
        else:
            if row=='':
                continue
            instance, actual, predicted, error=row.split()
            matrix.append([int(instance), float(actual), float(predicted)])
            
    matrix=np.array(matrix)    
    matrix[:,2][matrix[:,2]<0]=0 #disable negative predictions
       
    #Visualize results   
    plt.style.use('ggplot')
    f=plt.figure(1)
    plt.plot(matrix[:,0], matrix[:,1], label='actual', color='red')
    plt.plot(matrix[:,0], matrix[:,2], label='predicted', color='royalblue')
    plt.xlabel('Instance number')
    plt.ylabel('Packet Loss Rate')
    plt.grid(True)
    plt.legend(loc=1)
    
    plt.show()
