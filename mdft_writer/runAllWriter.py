import json

class runAllWriter:      
    def __init__(self):
        with open("./references/serversParam/serversParam.json", 'r') as json_param:
            self.serv_param = json.load(json_param)
                
    def write(self, server_name, commit_hash):                 
        with open("./references/runAll_file/runAll.sh", 'r') as frun_in:
            lines = frun_in.readlines()
            for i, line in enumerate(lines):
                if ".do" in line:
                    lines[i] = "\t    " + self.serv_param[server_name]["runCmd"] + ' ' + self.serv_param[server_name]["jobFile"] + '\n'
                elif "git clone" in line and commit_hash != None:
                    lines.insert(i+2, "    git checkout " + commit_hash + "\n")
                
        
        with open("runAll.sh", 'w') as frun_out:
            frun_out.write("".join(lines))
            

    def getDoFile(self, server_name):
        return self.serv_param[server_name]["jobFile"]