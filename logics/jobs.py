import json
import time
import logics.settings as settings

class Jobs: 
    def __init__(self):
        self.jobs = []
        self.initializeJobs()

    def createJob(self, name, description, hp, mp, atk, deff, ascent):
        job = {
            "name": name,
            "description": description,
            "hp": hp,
            "mp": mp,
            "atk": atk,
            "deff": deff,
            "ascent": ascent
        }
        self.jobs.append(job)
    
    def getJob(self, name):
        filtered = list(filter(lambda job: job["name"] == name, self.jobs))
        if len(filtered) > 0:
            return filtered[0]
        
    def getJobAttributesByIndex(self, index, attribute):
        return self.jobs[index - 1][attribute]

    def getJobAttributes(self, name, attribute):
        filtered = list(filter(lambda job: job["name"] == name, self.jobs))
        if len(filtered) > 0:
            return filtered[0][attribute]
    
    def getJobs(self):
        for i, job in enumerate(self.jobs):
            time.sleep(0.2)
            print(str(i + 1) + ". " + settings.config.colors.GREEN + job["name"] + settings.config.colors.ENDC + settings.config.colors.YELLOW + " (" + job["description"] + ")" + settings.config.colors.ENDC)
        
    def initializeJobs(self):
        if not self.jobs:
            with open('data/jobs.json', 'r', encoding='utf-8') as f:
                jobs = json.load(f)
            for job in jobs:
                self.createJob(job["name"], job["description"], job["hp"], job["mp"], job["atk"], job["deff"], job["ascent"])
            