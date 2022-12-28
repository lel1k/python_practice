
class StrategyDeal:
    def __init__(self, **kargs):
        self.bank = float(kargs['bank'][0])
        self.targets = list(map( lambda x: float(x) , kargs['target'] ))
        self.entry = float(kargs['entry'][0])
        self.close = float(kargs['close'][0])
    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        return float(self.targets)

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        return list(map(lambda x: x/self.entry, self.targets))

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]

        return list(map(lambda x: x*self.bank, self.get_target_percents()))
    def prepare_data(self):
        # текстовое представление сделки
        data = ''
        data += 'BANK: {}\n'.format(self.bank)
        data += 'START PRICE: {}\n'.format(self.entry)
        data += 'STOP PRICE: {}\n'.format(self.close)

        data += '\n\n'
        percents = self.get_target_percents()
        target_banks = self.get_target_banks()

        for i,el in enumerate(self.targets):
            data += '{} target: {}\n'.format(i+1, el)
            data += 'Percent: {}%\n'.format('%.2f' % ((percents[i] - 1)*100) )
            data += 'Bank: {} \n'.format('%.3f' % target_banks[i])
            data += '\n'

        data += "-----\n"

        return data


    def __str__(self):
        return self.prepare_data()


def read_data(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        data = [dict()]
        for line in file:
            line = line.strip()
            if '---' not in line:
                if ':' in line:
                    key, value = line.split(':')
                    key = key.lower()
                    data[-1][key] = list(map(lambda x: x.replace("USD", "").strip(), value.strip().split(';')))

            else:
                data.append(dict())
        data.pop()
    return data


def write_data(file_name, data):
    with open(file_name, 'w', encoding="utf-8") as file:
        for el in data:

            deal = StrategyDeal(**el)
            file.write(deal.prepare_data())


def parse_data():
    pass


def main():


    content = read_data('deals.txt')

    write_data('out.txt', content)

if __name__ == '__main__':
    main()









