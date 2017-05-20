from gensim.summarization import summarize
import sys

fname = sys.argv[1]

with open(fname, 'r') as f :
	l = f.read()
	summary = summarize(l,split = True)
	for i, sentence in enumerate(summary) :
		print ("%d) %s" % (i+1, sentence) )
