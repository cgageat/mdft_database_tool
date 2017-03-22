import os

class SoluteInWriter:  
    def __init__(self):
        self.l_x = []
        self.l_y = []
        self.l_z = []
        self.l_name = []
        self.l_charge = []
        self.l_mass = [] 
        self.l_num = []
        self.l_sigma = {}
        self.l_epsilon = {}
        self.syst = ''
        self.iupac = ''
        self.calc_dg = ''
        self.exp_dg = ''
        
    def writeSoluteIn(self):
        with open(os.path.join('./mobley',self.iupac), 'w') as solutein:
            solutein.write(self.syst + '\t' + self.calc_dg +  '\t' + self.exp_dg + "\t#mobley_id  DGsolv_calc  DGsolv_expt (kJ/mol)" + '\n')
            solutein.write(str(len(self.l_num)) + '\n')
            solutein.write("{0}    {1:10s}{2:10s}  {3:10s}  {4:10s}{5:10s}{6:9s}{7}\n".format("#","charge", "sigma(Ang)", "epsilon(kJ/mol)", "x", "y", "z", "Zatomic"))
            for i in xrange(len(self.l_num)):
                solutein.write("{0}{1:10.6f}{2:10.5f}{3:10.5f}{4:18.3f}{5:10.3f}{6:10.3f}{7:10d}\n".format(self.l_num[i], self.l_charge[i], self.l_sigma[self.l_name[i]], self.l_epsilon[self.l_name[i]], self.l_x[i], self.l_y[i],  self.l_z[i],  self.l_mass[i]))
