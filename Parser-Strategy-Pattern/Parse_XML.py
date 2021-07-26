from Interface_of_parser import InterfaceParser
import dicttoxml
from xml.dom.minidom import parseString


class ParseXML(InterfaceParser):

    def convert(self, fileName):
        student_data = []
        with open(fileName) as f:
            for line in f:
                line = line.split(',')
                student_data.append({"name": line[0], "batch": line[1], "roll": line[2]})
        student_data = {"Students": student_data}

        xml = dicttoxml.dicttoxml(student_data, attr_type=False, root=False, )
        dom = parseString(xml)

        with open("data.xml", "w") as f:
            f.write(dom.toprettyxml())
