import operator
import argparse
import json
import os
class Reorder:

    def reorder(self, inputfile, outputpath, indices):

        output = "{ "
        try:
            with open(inputfile, "r") as fileobj:
                input = json.load(fileobj)
                indexes = input.get(indices)
                if not indexes:
                    return None
                if not isinstance(indexes, dict):
                    return None
                else:
                    data = []
                    for key, value in indexes.items():
                        data.append((key, (value, input.get(value))))
                    sorted_data = sorted(data, key=operator.itemgetter(0))
                    for item in sorted_data[:-1]:
                        a = "\"{}\":\"{}\", ".format(item[1][0], item[1][1])
                        output += a
                    a = "\"{}\":\"{}\"".format(sorted_data[-1][1][0], sorted_data[-1][1][1])
                    output += a
                    output += "}"

        except Exception as ex:
            print("log: input file does not exist, {}".format(ex))

        try:
            with open(os.path.join(outputpath, "output2.json"), "w") as wfile:
                wfile.write(output)
        except Exception as ex:
            print("log: directory or file does not exist {}".format(ex))

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process a JSON input and reorder according to indexes')
    parser.add_argument('--input', type=str, help='provide JSON input file', required=True)
    parser.add_argument('--output', type=str, help='output directory', required=True)
    parser.add_argument('--index', type=str, help='index key', required=True)
    args = parser.parse_args()

    obj = Reorder()
    obj.reorder(args.input, args.output, args.index)

