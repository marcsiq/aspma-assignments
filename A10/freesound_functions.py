import soundDownload
import soundAnalysis
import json
import heapq
import numpy as np
import os.path


#VARIABLE DEFINITION
tdir = "/home/msiquier/SMC/sms-tools/workspace/A10/sounds/"							#output directory
dur = (2,10)																		#(min Duration, max Duration) for queries
APIkey = "9GUfpnadafRpnB3v76G7M5x9i7X3tNHtZ2a4FrBb" 								#freesound api key
descriptorMapping = [4,9, 11, 12,14,15]		#descriptors to be used in order to compute results
query = [("violin", "single-note"),													#query names and tags
			("trumpet", "single-note"), 
			("cello", "single-note"),
			("bassoon", "multisample"), 
			("clarinet", "single-note"), 
			("flute", "single-note"), 
			("naobo", "icassp2014-dataset"),
			("snare", "multisample"),
			("mridangam", "mridangam-stroke-dataset"),
			("daluo", "icassp2014-dataset")]

nQueries = 20																		#number of queries for query name
nRepetitions = 10																	#number of repetitions for each cluster
nResults = 5																		#number of best results to output
nDescriptors = len(descriptorMapping)												#length of descriptors list
results_file_name = "results/output_all.txt"												#base file_name


def download_sounds():
	#downloads all queries
	for sound , tag in query:
		print "----- Downloading " + str(nQueries) + " samples for the query: " + sound + " with tag: " + tag + " -----"
		soundDownload.downloadSoundsFreesound(queryText = sound, tag=tag, duration=dur, API_Key = APIkey, outputDir = tdir, topNResults = nQueries, featureExt = '.json')

def test_all_pair_scatter_plot():		
	#scatter plot for all descriptors pair combinaiton
	for i in range(nDescriptors):
		for j in range(nDescriptors):
			print "----- Descriptor Pair Scatter Plot for " + str(i) + ", " + str(j) + " -----"
			soundAnalysis.descriptorPairScatterPlot(inputDir = tdir, descInput = (i,j), anotOn = 0)

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
				r = soundAnalysis.clusterSounds2(targetDir=tdir, nCluster = len(query), descInput=el)
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

def main():
#	download_sounds()
#	test_all_pair_scatter_plot()
#	if not os.path.isfile(results_file_name):
#		get_results_by_descriptors() #15 hours for 17 descriptors
	print_results(get_k_best_results(nResults))

#	r = soundAnalysis.clusterSounds(targetDir=tdir, nCluster = len(query), descInput=[15, 14, 13])




if __name__ == "__main__":
    main()