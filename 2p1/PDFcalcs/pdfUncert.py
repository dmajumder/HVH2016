#!/usr/bin/env python

### PDF4LHC recommendations for LHC Run II: http://arxiv.org/abs/1510.03865

import os, sys, ROOT
import math
from ROOT import *
from math import *
import glob
import FWCore.ParameterSet.Config as cms
from DataFormats.FWLite import Events, Handle
from array import *
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-o", "--outName", dest="outName",
                  help="output file name")
parser.add_option("-m", "--mass", dest="mass",
                  help="mass")
parser.add_option("-l", "--list", dest="list",
                  help="list of input files")
parser.add_option("-n", "--num", dest="num",
                  help="number of input files")
(options, args) = parser.parse_args()

ff_n = 1000

def open_files(file_name) : #opens files to run on

    g = open(file_name)
    list_file = []
    final_list = []
    for i in range(ff_n):  # this is the length of the file
        list_file.append(g.readline().split())
    #s = options.inputFile

    for i in range(len(list_file)):
        for j in range(len(list_file[i])) :
            final_list.append(list_file[i][j])
    print final_list
    return final_list


outputfilename = options.outName

inputfile = options.list
Files_list = open_files( inputfile )
maxfile = int(options.num)

idxpdfs=range(1,1+101)
nwts=len(idxpdfs)

allevt   = 0
allevtup = [] 
allevtlo = [] 

passevt   = 0
passevtup = []
passevtlo = []

#  f = ROOT.TFile.Open(sys.argv[1], "READ")
#  mychain = f.Get("tree")
#  entries=mychain.GetEntriesFast()

for i in idxpdfs:

  evtwt=0
  evtwtpdfUp=0
  evtwtpdfLo=0
  passevtwt=0
  passevtwtpdfUp=0
  passevtwtpdfLo=0

#  evts=200
  ievt = 0
    #for each event
  totalEv = 0
  passEv = 0

  for j in range(0,maxfile):
    files = Files_list[j]
    print files
    f = ROOT.TFile.Open(files, "READ")
    mychain = f.Get("tree")
    entries=mychain.GetEntriesFast() 
    for event in mychain:
      ievt = ievt+1
 #     if ievt > evts: break
      
      totalEv += 1

      #get this variable
      lhewts = event.LHE_weights_pdf_wgt
      lhewtcentral = float(lhewts[idxpdfs[0]])

      #total lhewtcentral for all events
      evtwt+=lhewtcentral

      happy = 0
      if ievt%2 == 0:
        happy = 1
      #for the ith PDF, get the lhewts and determine whether it's an up or down, calculate total for all events
      lhewt = lhewts[i-1]
      if i%2 == 0:
        evtwtpdfUp += float(lhewt) 
      elif i%2 == 1:
        evtwtpdfLo += float(lhewt)
    
      #event selection goes here
      if len(event.FatjetAK08ungroomed_pt) > 0 and len(event.Jet_pt) > 3:
        AK8 = ROOT.TLorentzVector()
        AK8.SetPtEtaPhiM(event.FatjetAK08ungroomed_pt[0], event.FatjetAK08ungroomed_eta[0], event.FatjetAK08ungroomed_phi[0], event.FatjetAK08ungroomed_mass[0])
        AK40j = ROOT.TLorentzVector()
        AK40j.SetPtEtaPhiM(event.Jet_pt[0], event.Jet_eta[0], event.Jet_phi[0], event.Jet_mass[0])
        AK41j = ROOT.TLorentzVector()
        AK41j.SetPtEtaPhiM(event.Jet_pt[1], event.Jet_eta[1], event.Jet_phi[1], event.Jet_mass[1])
        AK42j = ROOT.TLorentzVector()
        AK42j.SetPtEtaPhiM(event.Jet_pt[2], event.Jet_eta[2], event.Jet_phi[2], event.Jet_mass[2])
        AK43j = ROOT.TLorentzVector()
        AK43j.SetPtEtaPhiM(event.Jet_pt[3], event.Jet_eta[3], event.Jet_phi[3], event.Jet_mass[3])
        if len(event.Jet_pt) > 4:
          AK44j = ROOT.TLorentzVector()
          AK44j.SetPtEtaPhiM(event.Jet_pt[4], event.Jet_eta[4], event.Jet_phi[4], event.Jet_mass[4])
          if len(event.Jet_pt) > 5:
            AK45j = ROOT.TLorentzVector()
            AK45j.SetPtEtaPhiM(event.Jet_pt[5], event.Jet_eta[5], event.Jet_phi[5], event.Jet_mass[5])
        AK41 = ROOT.TLorentzVector()
        AK42 = ROOT.TLorentzVector()
        AK43 = ROOT.TLorentzVector()
        AK41.SetPtEtaPhiM(-1.,-100.,-100.,-1.)
        AK42.SetPtEtaPhiM(-1.,-100.,-100.,-1.)
        AK43.SetPtEtaPhiM(-1.,-100.,-100.,-1.)
        dCSV1 = 0
        dCSV2 = 0
        if AK8.DeltaR(AK40j) > 0.8:
          AK41 = AK40j
          dCSV1 = (event.Jet_btagDeepCSVb[0] + event.Jet_btagDeepCSVbb[0])
          if AK8.DeltaR(AK41j) > 0.8:
            AK42 = AK41j
            dCSV2 = (event.Jet_btagDeepCSVb[1] + event.Jet_btagDeepCSVbb[1])
          else:
            if AK8.DeltaR(AK42j) > 0.8:
              AK42 = AK42j
              AK43 = AK43j
              dCSV2 = (event.Jet_btagDeepCSVb[2] + event.Jet_btagDeepCSVbb[2]) 
            else:
              if AK8.DeltaR(AK43j) > 0.8:
                AK42 = AK43j
                AK43 = AK44j
                dCSV2 = (event.Jet_btagDeepCSVb[3] + event.Jet_btagDeepCSVbb[3])
              else:
                if len(event.Jet_pt) > 4:
                  if AK8.DeltaR(AK44j) > 0.8:
                    AK42 = AK44j
                    dCSV2 = (event.Jet_btagDeepCSVb[4] + event.Jet_btagDeepCSVbb[4])
                    if AK8.DeltaR(AK45j) > 0.8:
                      AK43 = AK45j
        else:
          if AK8.DeltaR(AK41j) > 0.8:
            AK41 = AK41j
            dCSV1 = (event.Jet_btagDeepCSVb[1] + event.Jet_btagDeepCSVbb[1])
            if AK8.DeltaR(AK42j) > 0.8:
              AK42 = AK42j
              AK43 = AK43j
              dCSV2 = (event.Jet_btagDeepCSVb[2] + event.Jet_btagDeepCSVbb[2])
            else:
              if AK8.DeltaR(AK43j) > 0.8:
                AK42 = AK43j
                dCSV2 = (event.Jet_btagDeepCSVb[3] + event.Jet_btagDeepCSVbb[3])
                if len(event.Jet_pt) > 4:
                  AK43 = AK44j
              else:
                if len(event.Jet_pt) > 4:
                  if AK8.DeltaR(AK44j) > 0.8:
                    AK42 = AK44j
                    dCSV2 = (event.Jet_btagDeepCSVb[4] + event.Jet_btagDeepCSVbb[4])
                    if AK8.DeltaR(AK45j) > 0.8:
                       AK43 = AK45j
          else:
            if AK8.DeltaR(AK42j) > 0.8:
              AK41 = AK42j
              dCSV1 = (event.Jet_btagDeepCSVb[2] + event.Jet_btagDeepCSVbb[2])
              if AK8.DeltaR(AK43j) > 0.8:
                AK42 = AK43j
                dCSV2 = (event.Jet_btagDeepCSVb[3] + event.Jet_btagDeepCSVbb[3])
                AK43 = AK44j
              else:
                if len(event.Jet_pt) > 4:
                  if AK8.DeltaR(AK44j) > 0.8:
                    AK42 = AK44j
                    dCSV2 = (event.Jet_btagDeepCSVb[4] + event.Jet_btagDeepCSVbb[4])
                    if AK8.DeltaR(AK45j) > 0.8:
                      AK43 = AK45j
            else:
              if AK8.DeltaR(AK43j) > 0.8:
                AK41 = AK43j
                dCSV1 = (event.Jet_btagDeepCSVb[3] + event.Jet_btagDeepCSVbb[3])
                if len(event.Jet_pt) > 4:
                  AK42 = AK44j
                  dCSV2 = (event.Jet_btagDeepCSVb[4] + event.Jet_btagDeepCSVbb[4])
                  if AK8.DeltaR(AK45j) > 0.8:
                    AK43 = AK45j
                     
        dRAK8J1 = AK8.DeltaR(AK41)
        dRAK8J2 = AK8.DeltaR(AK42)
        dRAK4 = AK41.DeltaR(AK42)
        dEta = abs((AK41+AK42).Eta() - AK8.Eta())
        djm = (AK41+AK42).M()
        if event.FatjetAK08ungroomed_puppi_tau1[0] > 0:
          tau21 = event.FatjetAK08ungroomed_puppi_tau2[0]/event.FatjetAK08ungroomed_puppi_tau1[0]
        else:
          tau21 = 1.
        passv = 0
        if event.Vtype == -1:
          passv = 1
        if event.Vtype == 4:
          passv = 1

        if (event.FatjetAK08ungroomed_pt[0] > 300 and abs(event.FatjetAK08ungroomed_eta[0]) < 2.4 and AK41.Pt() > 30 and AK42.Pt() > 30 and abs(AK41.Eta()) < 2.4 and abs(AK42.Eta()) < 2.4 and dCSV1 > 0.6324 and dCSV2 > 0.6324 and dRAK8J1 > 0.8 and dRAK8J2 > 0.8 and dRAK4 < 1.5 and event.FatjetAK08ungroomed_puppi_msoftdrop_raw[0] > 105 and event.FatjetAK08ungroomed_puppi_msoftdrop_raw[0] < 135 and tau21 < 0.55 and event.FatjetAK08ungroomed_bbtag[0] > 0.8 and djm > 90 and djm < 140 and (AK41+AK42+AK43).M() > 200 and dEta < 2.0 and (AK41 + AK42 + AK8).M() > 700 and passv > 0): 
          passEv += 1
        #total lhewtcentral for all passing events
          passevtwt+=lhewtcentral
          #for the ith PDF, get the lhewts and determine whether it's an up or down, calculate total for passed events
          if i%2 == 0:
            passevtwtpdfUp += float(lhewt) 
          elif i%2 == 1:
            passevtwtpdfLo += float(lhewt)

  allevt=evtwt
  allevtup.append(evtwtpdfUp)
  allevtlo.append(evtwtpdfLo)

  passevt=passevtwt
  passevtup.append(passevtwtpdfUp)
  passevtlo.append(passevtwtpdfLo)

  #evtwt passing/ all evt wt
aenominal = passevt/allevt
  
allevtup_sum=0
for k in allevtup:
  allevtup_sum += pow(k - allevt,2.)
allevtup_sum = math.sqrt(allevtup_sum/100)

passevtup_sum=0
for k in passevtup:
  passevtup_sum += pow(k - passevt,2.)
passevtup_sum = math.sqrt(passevtup_sum/100)

  #total pdf up passing / total pdf up all
aepdfup = passevtup_sum/allevtup_sum

allevtlo_sum=0
for k in allevtlo:
  allevtlo_sum += pow(k - allevt,2.)
allevtlo_sum = math.sqrt(allevtlo_sum/100)

passevtlo_sum=0
for k in passevtlo:
  passevtlo_sum += pow(k - passevt,2.)
passevtlo_sum = math.sqrt(passevtlo_sum/100)

  #total pdf down passing / total pdf down all
aepdflo = passevtlo_sum/allevtlo_sum

mass = options.mass
txtfile = open(outputfilename,"w")
txtfile.write("%s CMS_PDF_Scales lnN %1.3f/%1.3f  -\n" % (mass, aepdfup/aenominal, aepdflo/aenominal)) 
