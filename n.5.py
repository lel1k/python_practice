import json
from random import randint

class WorkingDays:

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def num_working_days(self):
        return randint(20,23)


class HourIncome:

    def __init__(self, input_file):
        self.input_file = input_file

    def convert_to_dict(self):
        with open(self.input_file, 'r') as JSON:
            json_dict = json.load(JSON)
        return json_dict


    def get_hour_income(self):
        info = self.convert_to_dict()
        working_days = WorkingDays(info['year'], info['month'])
        num_days = working_days.num_working_days()
        info['hour_income'] = "{:.2f}".format(info['salary']/8/num_days)
        return info

    def return_json(self, data):
        data = json.dumps(data)
        data = self.get_hour_income()
        with open('output.json', 'w', encoding='utf-8') as file:
            file.write(data)

def main():
    service = HourIncome('test_input.json')
    answer = service.get_hour_income()
    print(answer)

if __name__ == "__main__":
    main()
