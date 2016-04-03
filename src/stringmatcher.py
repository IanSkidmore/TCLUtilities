class StringHelper:
    def toConsonant(self, s):
        return s.translate(None, "aeiouy")

    def soundex(self, s):
        res = ""
        cc = ""
        pc = ""

        res+= s[0].upper()
        for c in s[1:]:
            c = c.lower()
            if c in "bfpv":
                cc = "1"
            elif c in "cgjkqsxz":
                cc = "2"
            elif c in "dt":
                cc = "3"
            elif c in "l":
                cc = "4"
            elif c in "mn":
                cc = "5"
            elif c in "r":
                cc = "6"

            if cc != pc:
                res += cc

            if len(res) > 3:
                break

            if cc != "":
                pc = cc

        if len(res) <4:
            res += "0000"[0:4-len(res)]

        return res

class StringMatcher(StringHelper):
    def __init__(self, s, *args, **kwargs):
        self.source = s

    def Match(self, s):
        if self.fullMatch(s):
            return "FullMatch"
        elif self.transposeMatch(s):
            return "TransposeMatch"
        elif self.duplicateCharacterMatch(s):
            return "DuplicateCharacterMatch"
        elif self.consonantMatch(s):
            return "ConsonantMatch"
        elif self.soundexMatch(s):
            return "SoundexMatch"
        else:
            return "NoMatch"

    def fullMatch(self, s):
        return s == self.source

    def consonantMatch(self, s):
        return StringMatcher.toConsonant(self, s) == StringMatcher.toConsonant(self, self.source)

    def soundexMatch(self, s):
        return StringMatcher.soundex(self, s) == StringMatcher.soundex(self, self.source)

    def transposeMatch(self, s):
        if self.fullMatch(s):
            return False

        if len(s) != len(self.source):
            return False

        i = 0
        c = 0
        while i < len(s):
            if s[i] == self.source[i]:
                i += 1
                continue

            if s[i] == self.source[i+1] and s[i+1] == self.source[i]:
                if c > 0:
                    return False
                c += 1
                i += 2
                continue

            return False

        return True

    def duplicateCharacterMatch(self, s):
        if self.fullMatch(s):
            return False

        if abs(len(s) - len(self.source)) > 1:
            return False

        if len(s) > len(self.source):
            longstring = s
            shortstring = self.source
        else:
            longstring = self.source
            shortstring = s

        i = 0
        j = 0
        c = 0

        while i < len(shortstring):
            if shortstring[i] == longstring[j]:
                i += 1
                j += 1
                continue

            if shortstring[i] == longstring[j+1] and longstring[j] == longstring[j-1]:
                if c > 0:
                    return False
                c += 1
                i += 1
                j += 2
                continue

            return False

        return True

class SynonymMatcher(StringMatcher):
    def __init__(self, s, filename, *args, **kwargs):
        StringMatcher.__init__(self, s, *args, **kwargs)

        self.synonyms = {}
        self.filename = filename
        self.readSynonyms()
        self.synonym = self.getSynonym(self.source)

    def __del__(self):
        import csv
        oRow = 0

        try:
            f = open(self.filename, 'w')
            csvWriter = csv.writer(f, delimiter=',', quotechar='"')
            for key in self.synonyms.keys():
                if len(key) > 0:
                    l = [key, self.synonyms[key].rstrip('\r\n')]
                    csvWriter.writerow(l)
                    oRow += 1
            f.close()
            print "Number of known forenames: {0}".format(len(self.synonyms))
            print "Number of rows written: {0}".format(oRow)
        except:
            return

        return

    def readSynonyms(self):
        import csv
        f = open(self.filename)
        csvReader = csv.reader(f, delimiter=',', quotechar='"')
        for rows in csvReader:
            if len(rows) > 0:
                self.synonyms[rows[0]] = rows[1].rstrip('\r\n')
        f.close()
        print "Number of known forenames: {0}".format(len(self.synonyms))
        return

    def getSynonym(self, s):
        try:
            return self.synonyms[s]
        except:
            return ""

    def addValue(self, s):
        if self.getSynonym(s) == "":
            self.synonyms[s] = s

    def addSynonym(self, s, k):
        self.addValue(s)
        self.synonyms[k] = s

    def synonymMatch(self, s):
        return self.synonym == self.getSynonym(s)

    def Match(self, s):
        if self.fullMatch(s):
            return "FullMatch"
        elif self.synonymMatch(s):
            return "SynonymMatch"
        elif self.transposeMatch(s):
            return "TransposeMatch"
        elif self.duplicateCharacterMatch(s):
            return "DuplicateCharacterMatch"
        elif self.consonantMatch(s):
            return "ConsonantMatch"
        elif self.soundexMatch(s):
            return "SoundexMatch"
        else:
            return "NoMatch"


