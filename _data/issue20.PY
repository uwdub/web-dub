import yaml
import codecs
import random


def modify_conferences():
    with open('conferences.yml', 'r') as fin, open('test.yml', 'w') as fout:
        for line in fin:
            if 'id' in line:
                split = line.split('_')
                newline = split[0] + '_' + split[1] + '_' + split[2] + split[3]
                if len(split) >= 4:
                    for i in range(4, len(split)):
                        newline = newline + '_' + split[i]
                line = newline
            fout.write(line)


def modify_conferencepapers_with_conferences():
    with open('conferencepapers.yml', 'r') as fin, open('test.yml', 'w') as fout:
        cpdict = yaml.load(fin)
        newdict = {}
        for key, value in cpdict.items():
            split = value['conference'].split('_')
            newline = split[0] + '_' + split[1] + '_' + split[2] + split[3]
            if len(split) >= 4:
                for i in range(4, len(split)):
                    newline = newline + '_' + split[i]
            value['conference'] = newline
            newdict[key] = value
        out = yaml.dump(newdict, default_flow_style=False)
        fout.write(out)


def modify_conferencepapers():
    with open('conferencepapers.yml', 'r') as fin, open('test.yml', 'w') as fout:
        cpdict = yaml.load(fin)
        newdict = {}
        for key, value in cpdict.items():
            first = value['authors'][0]
            newkey = key + '_' + first[10:len(first)]
            if newkey in newdict:
                conflict = newdict[newkey]
                splitedT = conflict['title'].split(' ')
                slug1 = splitedT[random.randint(0, len(splitedT) - 1)]
                splitedT = value['title'].split(' ')
                slug2 = splitedT[random.randint(0, len(splitedT) - 1)]
                conflict['slug'] = slug1
                value['slug'] = slug2
                id1 = newkey + '_' + slug1
                id2 = newkey + '_' + slug2
                del newdict[newkey]
                newdict[id1] = conflict
                newdict[id2] = value
                print(id1)
                print(id2)
            else:
                newdict[newkey] = value
        out = yaml.dump(newdict, default_flow_style=False)
        fout.write(out)


def modify_journal():
    with open('journals.yml', 'r') as fin, open('test.yml', 'w') as fout:
        for line in fin:
            if 'id' in line:
                split = line.split('_')
                newline = split[0] + '_' + split[1] + '_' + split[2] + split[3]
                if len(split) >= 4:
                    for i in range(4, len(split)):
                        newline = newline + '_' + split[i]
                line = newline
            fout.write(line)

def modify_journalpapers():
    with open('journalpapers.yml', 'r') as fin, open('test.yml', 'w') as fout:
        cpdict = yaml.load(fin)
        newdict = {}
        for key, value in cpdict.items():
            first = value['authors'][0]
            newkey = key + '_' + first[10:len(first)]
            if newkey in newdict:
                conflict = newdict[newkey]
                splitedT = conflict['title'].split(' ')
                slug1 = splitedT[random.randint(0, len(splitedT) - 1)]
                splitedT = value['title'].split(' ')
                slug2 = splitedT[random.randint(0, len(splitedT) - 1)]
                conflict['slug'] = slug1
                value['slug'] = slug2
                id1 = newkey + '_' + slug1
                id2 = newkey + '_' + slug2
                del newdict[newkey]
                newdict[id1] = conflict
                newdict[id2] = value
                print(id1)
                print(id2)
            else:
                newdict[newkey] = value
        out = yaml.dump(newdict, default_flow_style=False)
        fout.write(out)

def modify_workshoppapers():
    with open('workshoppapers.yml', 'r') as fin, open('test.yml', 'w') as fout:
        cpdict = yaml.load(fin)
        newdict = {}
        for key, value in cpdict.items():
            first = value['authors'][0]
            newkey = key + '_' + first[10:len(first)]
            if newkey in newdict:
                conflict = newdict[newkey]
                splitedT = conflict['title'].split(' ')
                slug1 = splitedT[random.randint(0, len(splitedT) - 1)]
                splitedT = value['title'].split(' ')
                slug2 = splitedT[random.randint(0, len(splitedT) - 1)]
                conflict['slug'] = slug1
                value['slug'] = slug2
                id1 = newkey + '_' + slug1
                id2 = newkey + '_' + slug2
                del newdict[newkey]
                newdict[id1] = conflict
                newdict[id2] = value
                print(id1)
                print(id2)
            else:
                newdict[newkey] = value
        out = yaml.dump(newdict, default_flow_style=False)
        fout.write(out)

if __name__ == '__main__':
	modify_journalpapers()


