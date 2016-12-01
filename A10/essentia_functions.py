import essentia
import os
import json
from essentia.standard import *
from essentia import pool
from pylab import plot, show, figure, imshow

inputDir = '/home/msiquier/SMC/sms-tools/workspace/A10/sounds'

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


def main():
#	extractFeatures(inputDir)
	data = fetchEssentiaFeatures(inputDir)
	for c in data:
		for s in data[c]:
			pool = essentia.Pool()
			pool = data[c][s]['feature']
			print pool['lowLevel.mfcc.mean']

if __name__ == "__main__":
    main()