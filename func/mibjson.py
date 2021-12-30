import json
import os


class MibJson():
    def __init__(self):
        self.Matrix = {}

    def CreateFstBranch(self, key, value):
        if value:
            self.Matrix[key] = value
        else:
            self.Matrix[key] = {}

    def CreateSecBranch(self, key1, key2, value):
        if value:
            self.Matrix[key1][key2] = value
        else:
            self.Matrix[key1][key2] = {}

    def CreateTrdBranch(self, key1, key2, key3, value):
        if value:
            self.Matrix[key1][key2][key3] = value
        else:
            self.Matrix[key1][key2][key3] = {}

    def CreateForBranch(self, key1, key2, key3, key4, value):
        if value:
            self.Matrix[key1][key2][key3][key4] = value
        else:
            self.Matrix[key1][key2][key3][key4] = {}

    def CreateFivBranch(self, key1, key2, key3, key4, key5, value):
        if value:
            self.Matrix[key1][key2][key3][key4][key5] = value
        else:
            self.Matrix[key1][key2][key3][key4][key5] = {}

    def CreateJson(self):
        jsonpath = 'E:\\Python_Repositories\\mib_project\\demo\\1.json'
        if os.path.exists(jsonpath):
            print("1.json exist , now delate")
            os.remove(jsonpath)
        with open('../demo/1.json', 'w') as f:
            json.dump(self.Matrix, f, indent=2)

    def ShowJson(self):
        print(json.dumps(self.Matrix, indent=2))
