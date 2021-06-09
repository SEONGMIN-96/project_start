from real_estate.housingdto import Dto
import pandas as pd


class HounsingService (object):

    dataset = Dto()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_excel(this.context + this.fname, sheet_name='평균전세')