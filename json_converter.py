def preprocess_data(data):
    title = data.pop(0).strip().split(',')
    return title, data


def convert_row_to_pretty_json(title, values):
    result_data = []
    for current_values in values:
        current_dict = dict(zip(title, current_values.split(",")))
        pretty_line = "{"
        current_list = []
        for key in current_dict:
            current_list.append('"{key}": "{value}"'.format(key=key, value=current_dict[key]))

        pretty_line += ", ".join(current_list) + "}"
        result_data.append(pretty_line)

    result_data = "[" + ", ".join(result_data) + "]"
    print(result_data)
    return result_data


class SelfConverter:
    def __init__(self, csv_path, json_path):
        self.csv_path = csv_path
        self.json_path = json_path

    def read_data(self):
        with open(self.csv_path, "r", newline="") as f:
            content = f.read().splitlines()
            f.close()
        return preprocess_data(content)

    def write_data(self, data):
        with open(self.json_path, "w") as f:
            f.write(data)
        print("Data was converted successfully.")
        print(data)
        return data


def main():
    csv_path = "./input.csv"
    json_path = "./output.json"
    converter = SelfConverter(csv_path, json_path)
    title, values = converter.read_data()

    data = convert_row_to_pretty_json(title, values)
    converter.write_data(data)


if __name__ == "__main__":
    main()