import json

import pandas as pd
from common.abstracts import PrinterBase, ReaderBase


class Printer(PrinterBase):

    def dframe(self, this):
        print(f'"" 의 Type 은 {type(this)}')


class Reader(ReaderBase):

    def new_file(self, file) -> str:
        return file.context + file.fname

    def csv(self, file) -> object:
        print(pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8', thousands=','))

    def xls(self, file, header, usecols) -> object:
        print(pd.read_excel(f'{self.new_file(file)}.xls', header=header, usecols=usecols))

    def json(self, file) -> object:
        return json.load(open(f'{self.new_file(file)}.json', encoding='UTF-8'))
