./cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
scramv1 project CMSSW CMSSW_8_0_12
cd CMSSW_8_0_12/src
eval `scramv1 runtime -sh`

cp ../../ttreeAnalyzer_hh_alphabet_MC_QCD700.py .
cp ../../JetHT_TriggerComparisons.root .

python ttreeAnalyzer_hh_alphabet_MC_QCD700.py -f root://cmseos.fnal.gov//store/user/mkrohn/HHHHTo4b/V23/QCD700/QCD_HT700to1000_noExt_0.root -o root://cmseos.fnal.gov//store/user/mkrohn/HHHHTo4b/V24/QCD/HT700/SlimMiniTrees/

xrdcp QCD_HT700to1000_noExt_0.root root://cmseos.fnal.gov//store/user/mkrohn/HHHHTo4b/V24/QCD/HT700/SlimMiniTrees/
