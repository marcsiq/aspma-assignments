import essentia
import os
import json
from essentia.standard import *
from essentia import pool
from pylab import plot, show, figure, imshow
import numpy as np
import heapq
from scipy.cluster.vq import vq, kmeans, whiten
import matplotlib.pyplot as plt

inputDir = '/home/msiquier/SMC/sms-tools/workspace/A10/sounds'
nRepetitions = 10
results_file_name =  'results/output_essentia.txt'

extractor = Extractor(dynamics = True,
    					dynamicsFrameSize = 88200,
        				dynamicsHopSize = 44100,
        				highLevel = True,
        				lowLevel = True,
        				lowLevelFrameSize = 2048,
        				lowLevelHopSize = 1024,
        				midLevel = True,
        				namespace = "",
        				relativeIoi = False,
        				rhythm = True,
        				sampleRate  = 44100,
        				tonalFrameSize  = 4096,
        				tonalHopSize = 2048,
						tuning = True)

descriptorMapping = [ 'lowLevel.spectral_centroid.mean',
                      'lowLevel.dissonance.mean',
                      'lowLevel.hfc.mean',
                      'sfx.logattacktime.mean',
                      'sfx.inharmonicity.mean',
                      'lowLevel.spectral_contrast.mean',
                      'lowLevel.mfcc.mean',
                      'lowLevel.barkbands_kurtosis.mean',
                      'lowLevel.spectral_complexity.mean',
                      'lowLevel.spectral_crest.mean',
                      'lowLevel.spectral_energyband_high.mean',
                      'lowLevel.spectral_energyband_low.mean',
                      'lowLevel.spectral_strongpeak.mean',
                      'lowLevel.spectral_kurtosis.mean',
                      'lowLevel.sccoeffs.mean',
                      'lowLevel.spectral_rolloff.mean'
                    ]

bestDescriptorMapping = [ 'lowLevel.spectral_centroid.mean',
                      'lowLevel.dissonance.mean',
                      'sfx.logattacktime.mean',
                      'sfx.inharmonicity.mean',
                      'lowLevel.mfcc.mean',
                      'lowLevel.barkbands_kurtosis.mean',
                      'lowLevel.spectral_complexity.mean',
                      'lowLevel.spectral_crest.mean',
                      'lowLevel.spectral_strongpeak.mean',
                      'lowLevel.spectral_kurtosis.mean',
                      'lowLevel.sccoeffs.mean',
                      'lowLevel.spectral_rolloff.mean'
                    ]                  

descriptorMapping2 = [ 'lowLevel.spectral_centroid',
                      'lowLevel.dissonance',
                      'lowLevel.hfc',
                      'sfx.logattacktime',
                      'sfx.inharmonicity',
                      'lowLevel.spectral_contrast',
                      'lowLevel.mfcc',
                      'lowLevel.barkbands_kurtosis',
                      'lowLevel.spectral_complexity',
                      'lowLevel.spectral_crest',
                      'lowLevel.spectral_energyband_high',
                      'lowLevel.spectral_energyband_low',
                      'lowLevel.spectral_strongpeak',
                      'lowLevel.spectral_kurtosis',
                      'lowLevel.sccoeffs',
                      'lowLevel.spectral_rolloff'
                    ]

def fetchFiles(inputDir, descExt=".mp3"):
	files = []
	for path, dname, fnames  in os.walk(inputDir):
		for fname in fnames:
			if descExt in fname.lower():
				files.append((path, fname))
	return files

def extractFeatures(inputDir):
	data = fetchFiles(inputDir)
	for path, file in data:
		file_name = path + "/" + file
		print file_name
		loader = essentia.standard.MonoLoader(filename = file_name)
		audio = loader()
		pool = 	essentia.Pool()
		pool = extractor(audio)
		aggrPool = PoolAggregator(defaultStats = [ 'mean', 'var' ])(pool)
		YamlOutput(filename = path + '/essentia_features_all.json', format="json")(pool)
		YamlOutput(filename = path + '/essentia_features.json', format="json")(aggrPool)

def fetchEssentiaFeatures(inputDir):
	dataDetails = {}
	for path, dname, fnames  in os.walk(inputDir):
		for fname in fnames:
			if fname == "essentia_features.json":
				file_name = path + "/" + fname
				remain, rname, cname, sname = path.split('/')[:-3], path.split('/')[-3], path.split('/')[-2], path.split('/')[-1]
				if not dataDetails.has_key(cname):
					dataDetails[cname]={}
				fDict = YamlInput(filename = file_name, format="json").compute()
				dataDetails[cname][sname]={'file': fname, 'feature':fDict}
	return dataDetails

def fetchAllEssentiaFeatures(inputDir):
	dataDetails = {}
	for path, dname, fnames  in os.walk(inputDir):
		for fname in fnames:
			if fname == "essentia_features_all.json":
				file_name = path + "/" + fname
				remain, rname, cname, sname = path.split('/')[:-3], path.split('/')[-3], path.split('/')[-2], path.split('/')[-1]
				if not dataDetails.has_key(cname):
					dataDetails[cname]={}
				fDict = YamlInput(filename = file_name, format="json").compute()
				dataDetails[cname][sname]={'file': fname, 'feature':fDict}
	return dataDetails	

def fetchEnergyEssentiaFeatures(inputDir):
	dataDetails = {}
	for path, dname, fnames  in os.walk(inputDir):
		for fname in fnames:
			if fname == "essentia_features_energy.json":
				file_name = path + "/" + fname
				remain, rname, cname, sname = path.split('/')[:-3], path.split('/')[-3], path.split('/')[-2], path.split('/')[-1]
				if not dataDetails.has_key(cname):
					dataDetails[cname]={}
				fDict = YamlInput(filename = file_name, format="json").compute()
				dataDetails[cname][sname]={'file': fname, 'feature':fDict}
	return dataDetails

def convFtrDict2List(ftrDict, descInput):
	ftr = []
	for ftrName in ftrDict.descriptorNames():
		if ftrName in descInput:
			if hasattr(ftrDict[ftrName], "__len__"):
				for value in ftrDict[ftrName]:
					ftr.append(float(value))
			else:
				ftr.append(float(ftrDict[ftrName]))
	return np.array(ftr)

def clusterSounds2(targetDir, nCluster = -1, descInput = []):
	dataDetails = fetchEnergyEssentiaFeatures(targetDir)

	ftrArr = []
	infoArr = []
	
	if nCluster ==-1:
		nCluster = len(dataDetails.keys())
	for cname in dataDetails.keys():
	#iterating over sounds
		for sname in dataDetails[cname].keys():
			pool = essentia.Pool()
			pool = dataDetails[cname][sname]['feature']
			l = convFtrDict2List(pool, descInput)
			if l.size == 28:
				ftrArr.append(l)
				infoArr.append([sname, cname])

	ftrArr = np.array(ftrArr)
	infoArr = np.array(infoArr)

	ftrArrWhite = whiten(ftrArr)
	centroids, distortion = kmeans(ftrArrWhite, nCluster)
	clusResults = -1*np.ones(ftrArrWhite.shape[0])

	for ii in range(ftrArrWhite.shape[0]):
		diff = centroids - ftrArrWhite[ii,:]
		diff = np.sum(np.power(diff,2), axis = 1)
		indMin = np.argmin(diff)
		clusResults[ii] = indMin

	ClusterOut = []
	classCluster = []
	globalDecisions = []  
	for ii in range(nCluster):
		ind = np.where(clusResults==ii)[0]
		freqCnt = []
		for elem in infoArr[ind,1]:
			freqCnt.append(infoArr[ind,1].tolist().count(elem))
		indMax = np.argmax(freqCnt)
		classCluster.append(infoArr[ind,1][indMax])

		decisions = []
		for jj in ind:
			if infoArr[jj,1] == classCluster[-1]:
				decisions.append(1)
			else:
				decisions.append(0)
		globalDecisions.extend(decisions)
		ClusterOut.append(np.hstack((infoArr[ind],np.array([decisions]).T)))
	globalDecisions = np.array(globalDecisions)
	totalSounds = len(globalDecisions)
	nIncorrectClassified = len(np.where(globalDecisions==0)[0])
	return round(float(100.0*float(totalSounds-nIncorrectClassified)/totalSounds),2)

def clusterSounds(targetDir, nCluster = -1, descInput = []):
	dataDetails = fetchEssentiaFeatures(targetDir)

	ftrArr = []
	infoArr = []

	if nCluster ==-1:
		nCluster = len(dataDetails.keys())
	for cname in dataDetails.keys():
	#iterating over sounds
		for sname in dataDetails[cname].keys():
			pool = essentia.Pool()
			pool = dataDetails[cname][sname]['feature']
			l = convFtrDict2List(pool, descInput)
			ftrArr.append(l)
			infoArr.append([sname, cname])

	ftrArr = np.array(ftrArr)
	infoArr = np.array(infoArr)

	ftrArrWhite = whiten(ftrArr)
	centroids, distortion = kmeans(ftrArrWhite, nCluster)
	clusResults = -1*np.ones(ftrArrWhite.shape[0])

	for ii in range(ftrArrWhite.shape[0]):
		diff = centroids - ftrArrWhite[ii,:]
		diff = np.sum(np.power(diff,2), axis = 1)
		indMin = np.argmin(diff)
		clusResults[ii] = indMin

	ClusterOut = []
	classCluster = []
	globalDecisions = []  
	for ii in range(nCluster):
		ind = np.where(clusResults==ii)[0]
		freqCnt = []
		for elem in infoArr[ind,1]:
			freqCnt.append(infoArr[ind,1].tolist().count(elem))
		indMax = np.argmax(freqCnt)
		classCluster.append(infoArr[ind,1][indMax])

		decisions = []
		for jj in ind:
			if infoArr[jj,1] == classCluster[-1]:
				decisions.append(1)
			else:
				decisions.append(0)
		globalDecisions.extend(decisions)
		ClusterOut.append(np.hstack((infoArr[ind],np.array([decisions]).T)))
	globalDecisions = np.array(globalDecisions)
	totalSounds = len(globalDecisions)
	nIncorrectClassified = len(np.where(globalDecisions==0)[0])
	return round(float(100.0*float(totalSounds-nIncorrectClassified)/totalSounds),2)


def lattice(l):
	if l ==[]:
		return [[]]
	ll = lattice(l[1:])
	return [e+[l[0]] for e in ll] + ll			

def get_results_by_descriptors():
	#get nRepetitions for all possible combination of descriptors
	li = lattice(descriptorMapping)
	results = []

	for el in li:
		results_el = []
		for i in range(nRepetitions):
			try:
				r = clusterSounds2(targetDir=inputDir, nCluster = 10, descInput=el)
				results_el.append((r,el))
			except:
				pass
		results.append(results_el)
		if results_el:
			with open(results_file_name, "a") as file:
				file.write(str(results_el))
				file.write(", ")
	return results

def get_k_best_results(num_results):
	#gets nResults from results of combinations
	text_file = open(results_file_name, "r")
	x = eval(text_file.read())
	result_means = []
	for line in x:
		mean = []
		for word in line:
			mean.append(word[0])
		if mean:
			result_means.append((np.mean(mean), np.var(mean), word[1]))
	best = heapq.nlargest(num_results, result_means)
	return best

def print_results(results):
	print "--- Results after " + str(nRepetitions) + " classification with features from " + results_file_name + " ---\n"
	for result in results:
		print "Performance mean: " + str(result[0]) + ", variance: " + str(result[1]) + ", feature set: " + str(result[2])


def plot_energy(targetDir):
	dataDetails = fetchAllEssentiaFeatures(targetDir)
	for cname in dataDetails.keys():
	#iterating over sounds
		fig = plt.figure()
		for sname in dataDetails[cname].keys():	
			pool = essentia.Pool()
			pool = dataDetails[cname][sname]['feature']
			plt.plot(pool['lowLevel.spectral_energy'])

		fig.savefig("energy/" + cname + ".png")
		plt.show()

def extractFeaturesThreshold(inputDir, descInput):
	data = fetchFiles(inputDir)

	features = []
	for path, file in data:
		file_name = path + "/" + file
		print file_name
		loader = essentia.standard.MonoLoader(filename = file_name)
		audio = loader()
		pool = 	essentia.Pool()
		pool = extractor(audio)
		pool2 = essentia.Pool()
		for ftrName in pool.descriptorNames():
			if ftrName in descInput:
				ftr = []
				for idx, sample in enumerate(pool[ftrName]):
					if pool['lowLevel.spectral_energy'][idx] > 0.010:
						pool2.add(ftrName,sample)
		aggrPool = PoolAggregator(defaultStats = [ 'mean', 'var' ])(pool2)
		YamlOutput(filename = path + '/essentia_features_energy.json', format="json")(aggrPool)



def main():
#	extractFeatures(inputDir)
#	get_results_by_descriptors()
#	print_results(get_k_best_results(10))
#	plot_energy(inputDir)
#	extractFeaturesThreshold(inputDir, descriptorMapping2)
	mean = []
	for i in range(10):
		mean.append(clusterSounds2(targetDir=inputDir, nCluster = 10, descInput=bestDescriptorMapping))
	print np.mean(mean)



if __name__ == "__main__":
    main()