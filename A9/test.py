import soundDownload
import soundAnalysis

dur = (0,10)
tdir = "/home/msiquier/SMC/sms-tools/workspace/A9/freesound/target"
qdir = "/home/msiquier/SMC/sms-tools/workspace/A9/freesound/queries"
APIkey = "9GUfpnadafRpnB3v76G7M5x9i7X3tNHtZ2a4FrBb" 
nResults = 20

query = "violin"
tags = "single-note"

#soundDownload.downloadSoundsFreesound(queryText = query, tag=tags, duration=dur, API_Key = APIkey, outputDir = tdir, topNResults = nResults, featureExt = '.json')

query = "trumpet"
tags = "single-note"

#soundDownload.downloadSoundsFreesound(queryText = query, tag=tags, duration=dur, API_Key = APIkey, outputDir = tdir, topNResults = nResults, featureExt = '.json')

query = "cello"
tags = "single-note"

#soundDownload.downloadSoundsFreesound(queryText = query, tag=tags, duration=dur, API_Key = APIkey, outputDir = tdir, topNResults = nResults, featureExt = '.json')

#soundAnalysis.descriptorPairScatterPlot(inputDir = odir, descInput = (14,15), anotOn = 0)

#soundAnalysis.clusterSounds(targetDir=odir, nCluster = 3, descInput=[14,15,4])

query = "guitar"
tags = "single-note"

#soundDownload.downloadSoundsFreesound(queryText = query, tag=tags, duration=dur, API_Key = APIkey, outputDir = qdir, topNResults = 5, featureExt = '.json')

soundAnalysis.classifySoundkNN(queryFile=qdir+'/guitar/110455/110455_1075352-lq.json', targetDir=tdir, K=5, descInput = [14,15,4])

soundAnalysis.classifySoundkNN(queryFile=qdir+'/guitar/13709/13709_18811-lq.json', targetDir=tdir, K=5, descInput = [14,15,4])

soundAnalysis.classifySoundkNN(queryFile=qdir+'/guitar/13710/13710_18811-lq.json', targetDir=tdir, K=5, descInput = [14,15,4])

soundAnalysis.classifySoundkNN(queryFile=qdir+'/guitar/13711/13711_18811-lq.json', targetDir=tdir, K=5, descInput = [14,15,4])

soundAnalysis.classifySoundkNN(queryFile=qdir+'/guitar/91199/91199_1075352-lq.json', targetDir=tdir, K=5, descInput = [14,15,4])