#!/bin/sh

#testing

./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`
cp ../../slimTreeMaker_final3.py .
cp ../../DeepCSV_Moriond17_B_H.csv .
cp ../../gravall-v25.weights.xml .

python  slimTreeMaker_final3.py root://cmsxrootd.fnal.gov//store/user/mkrohn/HHHHTo4b/V25/JetHT_2016G.root   --saveTrig="True" --ttbar="False" --data="True" --JECUp="False" --JECDown="False" --JERUp="False" --JERDown="False" --useReg="False" --outName=JetHT_G_tree_finally1p1_3b.root
xrdcp JetHT_G_tree_finally1p1_3b.root root://cmseos.fnal.gov//store/user/asady1/V25/


