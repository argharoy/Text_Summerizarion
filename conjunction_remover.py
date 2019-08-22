def remove(sentence):

	eliminates = ['if','and','but','then']

	modified_list = []

	frags = sentence.split();

	length = len(frags)

	for i in range(0,length):
		if frags[i] not in eliminates:
			modified_list.append(frags[i])

	text = ' '.join(modified_list)

	return text