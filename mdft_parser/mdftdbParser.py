from atom import *
from molecule import *
import json

class MdftDBParser:
    "This class defines a parser for our MDFT database in JSON format"

    def __init__(self, mdft_db=None):
        self.mdft_db = mdft_db
        
        
    def parse(self, mol):
        molecule = Molecule()
        for at in self.mdft_db[mol]:
            atome = Atom(self.mdft_db[mol][at]['name'],\
                          self.mdft_db[mol][at]['index'],\
                          None,\
                          {'x':self.mdft_db[mol][at]['x'], 'y':self.mdft_db[mol][at]['y'], 'z':self.mdft_db[mol][at]['z']},\
                          self.mdft_db[mol][at]['charge'],\
                          self.mdft_db[mol][at]['epsilon'],\
                          self.mdft_db[mol][at]['sigma'],\
                          self.mdft_db[mol][at]['Zatomic'])
            molecule.addAtom(atome)
            
        return molecule
                        
            
