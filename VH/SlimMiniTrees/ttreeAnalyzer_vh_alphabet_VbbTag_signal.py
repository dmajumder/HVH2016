import os
import glob
import math    

import ROOT 
#ROOT.gROOT.Macro("rootlogon.C")

import FWCore.ParameterSet.Config as cms

import sys
from DataFormats.FWLite import Events, Handle

from array import array

from optparse import OptionParser
parser = OptionParser()
#output file name
parser.add_option("-f", "--pathIn", dest="inputFile",
                  help="inputFile path")

parser.add_option("-o", "--outName", dest="outName",
                  help="output file name")

parser.add_option("-l", "--file", dest="txt",
                  help="input txt file")

parser.add_option("-i", "--min", dest="min",
                  help="input index low end")

parser.add_option("-j", "--max", dest="max",
                  help="input index high end")

(options, args) = parser.parse_args()
outputfilename = options.outName

inputfile = options.txt

ff_n = int(options.max)

num1 = int(options.min)
num2 = int(options.max)


def open_files(file_name) : #opens files to run on

    g = open(file_name)
    list_file = []
    final_list = []
    for i in range(ff_n):  # this is the length of the file
        list_file.append(g.readline().split())
    s = options.inputFile

    for i in range(len(list_file)):
        for j in range(len(list_file[i])) :
            final_list.append(s + list_file[i][j])
    print final_list
    return final_list



Files_list      = open_files( inputfile )

f =  ROOT.TFile(outputfilename, 'recreate')
#print outputfilename
f.cd()
#getting old tree
mynewTree = ROOT.TTree('mynewTree', 'mynewTree')

#getting old branches from old tree
#creating the tree objects we need
jetVpt = array('f', [-100.0])
jetHpt = array('f', [-100.0])
jetVID = array('f', [-100.0])
jetHID = array('f', [-100.0])
jetVeta = array('f', [-100.0])
jetHeta = array('f', [-100.0])
etadiff = array('f', [-100.0])
dijetmass_puppi = array('f', [-100.0])
dijetmass_puppi_raw = array('f', [-100.0])
dijetmass = array('f', [-100.0])
dijetmass_corr = array('f', [-100.0])
dijetmass_corr_punc = array('f', [-100.0])
jetVtau21 = array('f', [-100.0])
jetHtau21 = array('f', [-100.0])
jetVtau21DDT = array('f', [-100.0])
jetHtau21DDT = array('f', [-100.0])
jetV_puppi_msoftdrop_TheaCorr = array('f', [-100.0])
jetH_puppi_msoftdrop_TheaCorr = array('f', [-100.0])
jetV_puppi_msoftdrop_raw_TheaCorr = array('f', [-100.0])
jetH_puppi_msoftdrop_raw_TheaCorr = array('f', [-100.0])
#pjet1pmass = array('f', [-100.0])
#pjet2pmass = array('f', [-100.0])
jetVbbtag = array('f', [-100.0])
jetHbbtag = array('f', [-100.0])
nHiggsTags = array('f', [-100.0]) 
nTrueInt = array('f', [-100])
#PUWeight  = array('f', [-100.0])
vtype = array('f', [-100.0])
isData = array('f', [100.0])
jetVnbHadron = array('f', [-100.0])
jetHnbHadron = array('f', [-100.0])
jetVflavor = array('f', [-100.0])
jetHflavor = array('f', [-100.0])
jetVncHadron = array('f', [-100.0])
jetHncHadron = array('f', [-100.0])
jetVl1l2l3 = array('f', [-100.0])
jetVl2l3 = array('f', [-100.0])
jetHl1l2l3 = array('f', [-100.0])
jetHl2l3 = array('f', [-100.0])
jetVJER = array('f', [-100.0])
jetHJER = array('f', [-100.0])
puWeights = array('f', [-100.0])
puWeightsUp = array('f', [-100.0])
puWeightsDown = array('f', [-100.0])
json = array('f', [-100.0])
SF = array('f', [-100.0])
SFup = array('f', [-100.0])
SFdown = array('f', [-100.0])
trigWeight = array('f', [-100.0])
trigWeightUp = array('f', [-100.0])
trigWeightDown = array('f', [-100.0])
trigWeight2Up = array('f', [-100.0])
trigWeight2Down = array('f', [-100.0])
evt = array('f', [-100.0])
ht = array('f', [-100.0])
xsec = array('f', [-100.0])
HLT_PFHT800_v = array('f', [-100.0])
HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v = array('f', [-100.0])
HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v = array('f', [-100.0])
HLT_AK8PFJet360_V = array('f', [-100.0])
HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v = array('f', [-100.0])
HLT_PFJet260_v = array('f', [-100.0])

jet1_puppi_pt = array('f', [-100.0])
jet2_puppi_pt = array('f', [-100.0])
jet1_puppi_eta = array('f', [-100.0])
jet2_puppi_eta = array('f', [-100.0])
jet1_puppi_phi = array('f', [-100.0])
jet2_puppi_phi = array('f', [-100.0])
jet1_puppi_mass = array('f', [-100.0])
jet2_puppi_mass = array('f', [-100.0])
jet1_puppi_tau21 = array('f', [-100.0])
jet2_puppi_tau21 = array('f', [-100.0])
jet1_puppi_msoftdrop = array('f', [-100.0])
jet2_puppi_msoftdrop = array('f', [-100.0])
jet1_puppi_msoftdrop_raw = array('f', [-100.0])
jet2_puppi_msoftdrop_raw = array('f', [-100.0])
jet1_puppi_msoftdrop_corrL2L3 = array('f', [-100.0])
jet2_puppi_msoftdrop_corrL2L3 = array('f', [-100.0])
jet1_puppi_TheaCorr = array('f', [-100.0])
jet2_puppi_TheaCorr = array('f', [-100.0])
triggerpassbb = array('f', [-100.0])

#creating the tree branches we need
mynewTree.Branch('jetVpt', jetVpt, 'jetVpt/F')
mynewTree.Branch('jetHpt', jetHpt, 'jetHpt/F')
mynewTree.Branch('jetVeta', jetVeta, 'jetVeta/F')
mynewTree.Branch('jetHeta', jetHeta, 'jetHeta/F')
mynewTree.Branch('etadiff', etadiff, 'etadiff/F')
mynewTree.Branch('dijetmass_puppi', dijetmass_puppi, 'dijetmass_puppi/F')
mynewTree.Branch('dijetmass_puppi_raw', dijetmass_puppi_raw, 'dijetmass_puppi_raw/F')
mynewTree.Branch('dijetmass', dijetmass, 'dijetmass/F')
mynewTree.Branch('dijetmass_corr', dijetmass_corr, 'dijetmass_corr/F')
mynewTree.Branch('dijetmass_corr_punc', dijetmass_corr_punc, 'dijetmass_corr_punc/F')
mynewTree.Branch('jetVtau21', jetVtau21, 'jetVtau21/F')
mynewTree.Branch('jetHtau21', jetHtau21, 'jetHtau21/F')
mynewTree.Branch('jetVtau21DDT', jetVtau21DDT, 'jetVtau21DDT/F')
mynewTree.Branch('jetHtau21DDT', jetHtau21DDT, 'jetHtau21DDT/F')
mynewTree.Branch('jetV_puppi_msoftdrop_TheaCorr', jetV_puppi_msoftdrop_TheaCorr, 'jetV_puppi_msoftdrop_TheaCorr/F')
mynewTree.Branch('jetH_puppi_msoftdrop_TheaCorr', jetH_puppi_msoftdrop_TheaCorr, 'jetH_puppi_msoftdrop_TheaCorr/F')
mynewTree.Branch('jetV_puppi_msoftdrop_raw_TheaCorr', jetV_puppi_msoftdrop_raw_TheaCorr, 'jetV_puppi_msoftdrop_raw_TheaCorr/F')
mynewTree.Branch('jetH_puppi_msoftdrop_raw_TheaCorr', jetH_puppi_msoftdrop_raw_TheaCorr, 'jetH_puppi_msoftdrop_raw_TheaCorr/F')


mynewTree.Branch('jetVbbtag', jetVbbtag, 'jetVbbtag/F')
mynewTree.Branch('jetHbbtag', jetHbbtag, 'jetHbbtag/F')
mynewTree.Branch('nTrueInt',nTrueInt,'nTrueInt/F')
mynewTree.Branch('puWeights',puWeights,'puWeights/F')
mynewTree.Branch('puWeightsUp',puWeightsUp,'puWeightsUp/F')
mynewTree.Branch('puWeightsDown',puWeightsDown,'puWeightsDown/F')
mynewTree.Branch('jetVID', jetVID, 'jetVID/F')
mynewTree.Branch('jetHID', jetHID, 'jetHID/F')
mynewTree.Branch('vtype', vtype, 'vtype/F') 
mynewTree.Branch('isData', isData, 'isData/F') 
mynewTree.Branch('jetVnbHadron', jetVnbHadron, 'jetVnbHadron/F')
mynewTree.Branch('jetHnbHadron', jetHnbHadron, 'jetHnbHadron/F')
mynewTree.Branch('jetVflavor', jetVflavor, 'jetVflavor/F') 
mynewTree.Branch('jetHflavor', jetHflavor, 'jetHflavor/F') 
mynewTree.Branch('jetVncHadron', jetVncHadron, 'jetVncHadron/F')
mynewTree.Branch('jetHncHadron', jetHncHadron, 'jetHncHadron/F')
mynewTree.Branch('jetVl1l2l3', jetVl1l2l3, 'jetVl1l2l3/F') 
mynewTree.Branch('jetVl2l3', jetVl2l3, 'jetVl2l3/F')
mynewTree.Branch('jetHl1l2l3', jetHl1l2l3, 'jetHl1l2l3/F') 
mynewTree.Branch('jetHl2l3', jetHl2l3, 'jetHl2l3/F')
mynewTree.Branch('jetVJER', jetVJER, 'jetVJER/F') 
mynewTree.Branch('jetHJER', jetHJER, 'jetHJER/F') 
mynewTree.Branch('json', json, 'json/F')
mynewTree.Branch('SF', SF, 'SF/F')
mynewTree.Branch('SFup', SFup, 'SFup/F')
mynewTree.Branch('SFdown', SFdown, 'SFdown/F')
mynewTree.Branch('trigWeight', trigWeight, 'trigWeight/F')
mynewTree.Branch('trigWeightUp', trigWeightUp, 'trigWeightUp/F')
mynewTree.Branch('trigWeightDown', trigWeightDown, 'trigWeightDown/F')
mynewTree.Branch('trigWeight2Up', trigWeight2Up, 'trigWeight2Up/F')
mynewTree.Branch('trigWeight2Down', trigWeight2Down, 'trigWeight2Down/F')
mynewTree.Branch('evt',evt,'evt/F')
mynewTree.Branch('ht', ht, 'ht/F')
mynewTree.Branch('xsec', xsec, 'xsec/F')

mynewTree.Branch('HLT_PFHT800_v', HLT_PFHT800_v, 'HLT_PFHT800_v/F')
mynewTree.Branch('HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v', HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v, 'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v/F')
mynewTree.Branch('HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v', HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v, 'HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v/F')
mynewTree.Branch('HLT_AK8PFJet360_V', HLT_AK8PFJet360_V, 'HLT_AK8PFJet360_V/F')
mynewTree.Branch('HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v', HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v, 'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v/F')
mynewTree.Branch('HLT_PFJet260_v', HLT_PFJet260_v, 'HLT_PFJet260_v/F')
mynewTree.Branch('triggerpassbb', triggerpassbb, 'triggerpassbb/F')


CountWeightedmc = ROOT.TH1F("CountWeighted","Count with sign(gen weight) and pu weight",1,0,2)

bbj = ROOT.TH1F("bbj", "Before any cuts", 3, -0.5, 1.5)

print outputfilename

count = 0
for i in range(num1, num2):
    files = Files_list[i]
    print files
    f1 = ROOT.TFile.Open(files, "READ")
    treeMine  = f1.Get('myTree')
    nevent = treeMine.GetEntries();
    nFills = 0

    bbj.Add(f1.Get("bbj"))
    CountWeightedmc.Add(f1.Get("CountWeighted"))

    for i in range(0, nevent) :
        treeMine.GetEntry(i)
        count = count + 1
        if count % 1000 == 0 :
            print "processing events", count

        if treeMine.jet2pt < -10.:
            continue

	if treeMine.jet1_puppi_pt < 0 or treeMine.jet2_puppi_pt < 0:
	    continue       

	jet1_puppi_msoftdrop[0] = treeMine.jet1_puppi_msoftdrop
        jet2_puppi_msoftdrop[0] = treeMine.jet2_puppi_msoftdrop
        jet1_puppi_TheaCorr[0] = treeMine.jet1_puppi_TheaCorr
        jet2_puppi_TheaCorr[0] = treeMine.jet2_puppi_TheaCorr
	jet1_puppi_msoftdrop_raw[0] = treeMine.jet1_puppi_msoftdrop_raw
        jet2_puppi_msoftdrop_raw[0] = treeMine.jet2_puppi_msoftdrop_raw

        whichJetIsV = 0.

        if treeMine.jet1bbtag > treeMine.jet2bbtag:
  	   whichJetIsV = 2

        if treeMine.jet1bbtag < treeMine.jet2bbtag:
	   whichJetIsV = 1
 
        if whichJetIsV == 1: 
           jetVpt[0] = treeMine.jet1pt
           jetVeta[0] = treeMine.jet1eta
           jetVtau21[0] = treeMine.jet1tau21

	   if treeMine.jet1mass*treeMine.jet1mass/treeMine.jet1pt > 0:
             jetVtau21DDT[0] = treeMine.jet1tau21+0.063*math.log(treeMine.jet1mass*treeMine.jet1mass/treeMine.jet1pt)
	   else:
	     jetVtau21DDT[0] = -99999

   	   jetV_puppi_msoftdrop_TheaCorr[0] = jet1_puppi_msoftdrop[0]*jet1_puppi_TheaCorr[0]
           jetV_puppi_msoftdrop_raw_TheaCorr[0] = jet1_puppi_msoftdrop_raw[0]*jet1_puppi_TheaCorr[0]
           jetVbbtag[0] = treeMine.jet1bbtag
           jetVID[0] = treeMine.jet1ID
           jetVnbHadron[0] = treeMine.jet1nbHadron
           jetVflavor[0] = treeMine.jet1flavor
           jetVncHadron[0] = treeMine.jet1ncHadron
           jetVl1l2l3[0] = treeMine.jet1l1l2l3
           jetVl2l3[0] = treeMine.jet1l2l3
           jetVJER[0] = treeMine.jet1JER
           jetHpt[0] = treeMine.jet2pt
           jetHeta[0] = treeMine.jet2eta
           jetHtau21[0] = treeMine.jet2tau21

	   if treeMine.jet2mass*treeMine.jet2mass/treeMine.jet2pt > 0:
             jetHtau21DDT[0] = treeMine.jet2tau21+0.063*math.log(treeMine.jet2mass*treeMine.jet2mass/treeMine.jet2pt)
	   else:
	     jetHtau21DDT[0] = -99999

           jetH_puppi_msoftdrop_TheaCorr[0] = jet2_puppi_msoftdrop[0]*jet2_puppi_TheaCorr[0]
           jetH_puppi_msoftdrop_raw_TheaCorr[0] = jet2_puppi_msoftdrop_raw[0]*jet2_puppi_TheaCorr[0]
	   jetHbbtag[0] = treeMine.jet2bbtag
           jetHID[0] = treeMine.jet2ID
           jetHnbHadron[0] = treeMine.jet2nbHadron
           jetHflavor[0] = treeMine.jet2flavor
           jetHncHadron[0] = treeMine.jet2ncHadron
           jetHl2l3[0] = treeMine.jet2l2l3
           jetHJER[0] = treeMine.jet2JER

        if whichJetIsV == 2: 
           jetHpt[0] = treeMine.jet1pt
           jetHeta[0] = treeMine.jet1eta
           jetHtau21[0] = treeMine.jet1tau21

	   if treeMine.jet1mass*treeMine.jet1mass/treeMine.jet1pt > 0:
             jetHtau21DDT[0] = treeMine.jet1tau21+0.063*math.log(treeMine.jet1mass*treeMine.jet1mass/treeMine.jet1pt)
	   else:
	     jetHtau21DDT[0] = -99999

           jetH_puppi_msoftdrop_TheaCorr[0] = jet1_puppi_msoftdrop[0]*jet1_puppi_TheaCorr[0]
           jetH_puppi_msoftdrop_raw_TheaCorr[0] = jet1_puppi_msoftdrop_raw[0]*jet1_puppi_TheaCorr[0]
           jetHbbtag[0] = treeMine.jet1bbtag
           jetHID[0] = treeMine.jet1ID
           jetHnbHadron[0] = treeMine.jet1nbHadron
           jetHflavor[0] = treeMine.jet1flavor
           jetHncHadron[0] = treeMine.jet1ncHadron
           jetHl1l2l3[0] = treeMine.jet1l1l2l3
           jetHl2l3[0] = treeMine.jet1l2l3
           jetHJER[0] = treeMine.jet1JER
           jetVpt[0] = treeMine.jet2pt
           jetVeta[0] = treeMine.jet2eta
           jetVtau21[0] = treeMine.jet2tau21

	   if treeMine.jet2mass*treeMine.jet2mass/treeMine.jet2pt > 0:
             jetVtau21DDT[0] = treeMine.jet2tau21+0.063*math.log(treeMine.jet2mass*treeMine.jet2mass/treeMine.jet2pt)
	   else:
	     jetVtau21DDT[0] = -99999

           jetV_puppi_msoftdrop_TheaCorr[0] = jet2_puppi_msoftdrop[0]*jet2_puppi_TheaCorr[0]
           jetV_puppi_msoftdrop_raw_TheaCorr[0] = jet2_puppi_msoftdrop_raw[0]*jet2_puppi_TheaCorr[0]
           jetVbbtag[0] = treeMine.jet2bbtag
           jetVID[0] = treeMine.jet2ID
           jetVnbHadron[0] = treeMine.jet2nbHadron
           jetVflavor[0] = treeMine.jet2flavor
           jetVncHadron[0] = treeMine.jet2ncHadron
           jetVl1l2l3[0] = treeMine.jet2l1l2l3
           jetVl2l3[0] = treeMine.jet2l2l3
           jetVJER[0] = treeMine.jet2JER

        
        SF[0] = treeMine.SF
        SFup[0] = treeMine.SFup
        SFdown[0] = treeMine.SFdown

        etadiff[0] = abs(treeMine.jet1_puppi_eta - treeMine.jet2_puppi_eta)
 
        jet1_puppi_raw_TL = ROOT.TLorentzVector()
        jet1_puppi_raw_TL.SetPtEtaPhiM(treeMine.jet1_puppi_pt, treeMine.jet1_puppi_eta, treeMine.jet1_puppi_phi, treeMine.jet1_puppi_msoftdrop_raw*treeMine.jet1_puppi_TheaCorr)

        jet2_puppi_raw_TL = ROOT.TLorentzVector()
        jet2_puppi_raw_TL.SetPtEtaPhiM(treeMine.jet2_puppi_pt, treeMine.jet2_puppi_eta, treeMine.jet2_puppi_phi, treeMine.jet2_puppi_msoftdrop_raw*treeMine.jet2_puppi_TheaCorr)

        jet1_puppi_TL = ROOT.TLorentzVector()
        jet1_puppi_TL.SetPtEtaPhiM(treeMine.jet1_puppi_pt, treeMine.jet1_puppi_eta, treeMine.jet1_puppi_phi, treeMine.jet1_puppi_msoftdrop*treeMine.jet1_puppi_TheaCorr)

        jet2_puppi_TL = ROOT.TLorentzVector()
        jet2_puppi_TL.SetPtEtaPhiM(treeMine.jet2_puppi_pt, treeMine.jet2_puppi_eta, treeMine.jet2_puppi_phi, treeMine.jet2_puppi_msoftdrop*treeMine.jet2_puppi_TheaCorr)

        dijetmass_puppi[0] = (jet1_puppi_TL + jet2_puppi_TL).M()

        dijetmass_puppi_raw[0] = (jet1_puppi_raw_TL + jet2_puppi_raw_TL).M()
        dijetmass[0] = treeMine.dijetmass
        dijetmass_corr[0] = treeMine.dijetmass_corr
        dijetmass_corr_punc[0] = treeMine.dijetmass_corr_punc


        nTrueInt[0] = treeMine.nTrueInt
        puWeights[0] = treeMine.puWeights
        puWeightsUp[0] = treeMine.puWeightsUp
        puWeightsDown[0] = treeMine.puWeightsDown
        vtype[0] = treeMine.vtype
        isData[0] = treeMine.isData
        json[0] = treeMine.json
        trigWeight[0] = treeMine.trigWeight
        trigWeightUp[0] = treeMine.trigWeightUp
        trigWeightDown[0] = treeMine.trigWeightDown
        trigWeight2Up[0] = treeMine.trigWeight2Up
        trigWeight2Down[0] = treeMine.trigWeight2Down
        evt[0] = treeMine.evt
        ht[0] = treeMine.ht
        xsec[0] = treeMine.xsec
	triggerpassbb[0] = treeMine.triggerpassbb
        HLT_PFHT800_v[0] = treeMine.HLT_PFHT800_v
        HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v[0] = treeMine.HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v
        HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v[0] = treeMine.HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v
        HLT_AK8PFJet360_V[0] = treeMine.HLT_AK8PFJet360_V
        HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v[0] = treeMine.HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v
        HLT_PFJet260_v[0] = treeMine.HLT_PFJet260_v

        mynewTree.Fill()

print "nFills"
print nFills
print "OK"
print "done " + outputfilename

f.cd()
f.Write()
f.Close()

