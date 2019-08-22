import json
from nltk.tree import Tree

def json_parser():
	with open('data.json') as data_file:
		data = json.load(data_file)

	extracted_trees = []

	for key in data:
		if key == "sentences":
			count_lists = len(data["sentences"])
			for i in range(0,count_lists):
				dictionary = data["sentences"][i]
				data_tree = dictionary.get("parsetree")
				extracted_trees.append(data_tree)
		else:
			pass
	
	return extracted_trees

def sorting(data):
	ret_list = []

	for tokens in data:
		if tokens not in ret_list:
			ret_list.append(tokens)

	return ret_list


trees = json_parser()
length_trees = len(trees)

noun_phrase, verb_phrase = ([] for lis in range(2))

for i in range(0,length_trees):
	tree = Tree.fromstring(trees[i])
	NP_tree = list(tree.subtrees(filter=lambda x: x.label() == 'NP'))
	VP_tree = list(tree.subtrees(filter=lambda x: x.label() == 'VP'))

	for j in NP_tree:
		noun_phrase.append(' '.join(j.flatten()))
	for j in VP_tree:
		verb_phrase.append(' '.join(j.flatten()))

noun_phrase = sorting(noun_phrase)
verb_phrase = sorting(verb_phrase)

np_len = len(noun_phrase)
vp_len = len(verb_phrase)

print "Summarized Text :-"
for i in range(0,np_len):
	print noun_phrase[i]

print "*-*"*60

print "Summarized Text (Hold 2):-"
for i in range(0,vp_len):
	print verb_phrase[i]