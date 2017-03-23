import json

class ParserJson:  
    def __init__(self):
        self.syst = ''
        self.iupac = ''
        self.calc_dg = ''
        self.exp_dg = ''
            
    def parseEnergies(self, fjson, name):
		self.syst = name         
        with open(fjson, 'r') as json_file:            
            solute_db = json.load(json_file)
            self.iupac = solute_db[self.syst]["iupac"]
            self.calc_dg = str(float(solute_db[self.syst]["calc"] * 4.187))
            self.exp_dg = str(float(solute_db[self.syst]["expt"]*4.187))
            
	def getCalcDg(self):
		return self.calc_dg
	
	def getExpDg(self):
		return self.exp_dg	
		
	def getSystName(self):
		return self.syst
	
