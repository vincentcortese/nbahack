import dateparser
import posttypeparser
import word2vec

class FileParser:
    def __init__(self):
        pass
    def parseFile(filepath):
        output = []
        
        fp = open(filepath, 'r')
        lines = fp.readlines()

        #discard headers
        lines = lines[1:]
        #Engagements/Followers at Posting/Created/Type/Description

        data = []
        expected = []
        
        captions = []
        joined = True
        while joined:
            joined = False
            for li in range(0, len(lines)):
                splitline = lines[li].split(',', 4)
                if len(splitline) < 5:
                    lines[li - 1 : li + 1] = [''.join(lines[li - 1 : li + 1])]
                    joined = True
                    break
                
        for line in lines:
            splitline = line.split(',', 4)
            caption = splitline[4]
            captions = captions + caption.split()
        
        w2v = word2vec.Word2Vec(captions, True)

        for line in lines:
            splitline = line.split(',', 4)
            if len(splitline) == 5:
                parsedline = []

                expected.append(int(splitline[0]))
                #engagements - add this to training input

                parsedline.append(int(splitline[1]))
                #followers

                parsedline = parsedline + dateparser.DateParser.getDateTime(splitline[2])
                #created time

                parsedline = parsedline + posttypeparser.PostTypeParser.getPostType(splitline[3])
                #post type

                parsedline = parsedline + w2v.getVector(splitline[4])            
                #description

                data.append(parsedline)
                #add parsed line to data set
            fp.close()
            output = [data, expected]
        return output

#of = open("output.txt", 'w')
#o = FileParser.parseFile("data/business/training_set.csv")


#writestring = ""
#for entry in o[0]:
#    writestring += str(entry) + '\n'
#of.write(writestring)