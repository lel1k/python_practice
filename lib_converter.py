import json
import csv


class LibConverter:
    """
    Converter class
    """

    def __init__(self, csv_path, json_path):
        self.ipath = csv_path
        self.opath = json_path


    def read(self):
        with open(self.ipath, 'r', newline='') as f:
            return list(csv.DictReader(f, delimiter=','))

    def write(self, content):
        content = json.dumps(content)
        with open(self.opath, 'w') as f:
            f.write(content)


def main():
    csv_path = './input.csv'
    json_path = './output.json'
    conv = Converter(csv_path=csv_path, json_path=json_path)

    content = conv.read()
    print(content)
    conv.write(content)

    # print(content)


# test load # works just fine
def load_json():
    file_path = './output.json'
    with open(file_path, 'r') as f:
        content = f.read()
        content = json.loads(content)
    # print(content)


if __name__ == "__main__":
    print('init')
    main()
    # load_json()
    print('fin')
