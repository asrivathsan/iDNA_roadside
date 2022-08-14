#This script randomizes species assignments to different sites (here based on distance to road)
#usage python randomize.py inputfile 
#input file should contain 4 columns, tab delimited. Sampleid VertebrateID Site Distance
import sys,random
with open(sys.argv[1]) as infile:
	l=infile.readlines()
	sampledict={}
	distdict={}
	for each in l:
		m=each.strip().split('\t')
		distdict[m[0]]=int(m[3])
		try:
			sampledict[m[0]].append(m[1])
		except KeyError:
			sampledict[m[0]]=[m[1]]

	distfreq={}
	for each in distdict.values():
		try:
			distfreq[each]+=1
		except KeyError:
			distfreq[each]=1
dists=list(distfreq.keys())
dists.sort()
ndict={}
n=0
while n<100:
	ndict[n]=[]
	n+=1
n=0
while n<100:
	samples=list(sampledict.keys())
	eachlist=[]
	nlist=[]
	for each in dists:
		
		randsamplelist=random.sample(samples,distfreq[each])
		print(len(samples),len(randsamplelist))
		for s in randsamplelist:
			samples.remove(s)
			for vert in sampledict[s]:
				if vert not in eachlist:
					eachlist.append(vert)

		ndict[n].append(str(len(eachlist)))
	n+=1
with open(sys.argv[2],'w') as outfile:
	for n in list(ndict.keys()):
		outfile.write('\t'.join(ndict[n])+'\n')
