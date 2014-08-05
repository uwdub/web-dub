filenames = ['conferencepapers.yml','journalpapers.yml','workshoppapers.yml']

for filename in filenames:
	fin = open(filename,'r')
	lines = fin.readlines()
	fin.close()
	fout = open(filename,'w')

	for line in lines:
		if 'pubnum' not in line:
			fout.write(line)
	fout.close()