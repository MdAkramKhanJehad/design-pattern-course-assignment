import json
from Interface_of_parser import InterfaceParser


class ParseJSON(InterfaceParser):

    def convert(self, fileName):
        student_data = []
        with open(fileName) as f:
            for line in f:
                line = line.split(',')
                student_data.append({"name": line[0], "batch": line[1], "roll": line[2]})

        with open("data.json", 'w') as fout:
            json.dump(student_data, fout, indent=4)
