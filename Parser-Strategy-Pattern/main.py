from Parse_CSV import ParseCSV
from Parse_JSON import ParseJSON
from Parse_XML import ParseXML
from Parser import Parser


def main():
    parser = Parser()
    data = "data.txt"
    while True:
        print("\nWhat is do you want?\n1) Parse to CSV \t2) Parse to JSON \t3) Parse to XML \t4) Exit")
        inp = int(input())

        if inp == 1:
            parser.parse(ParseCSV(), data)
        elif inp == 2:
            parser.parse(ParseJSON(), data)
        elif inp == 3:
            parser.parse(ParseXML(), data)
        else:
            break


if __name__ == "__main__":
    main()
