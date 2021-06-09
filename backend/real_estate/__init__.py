from real_estate.housingdto import Dto
from real_estate.service import HounsingService
# import xwings as xw


class Controller(object):

    dataset = Dto()
    util = HounsingService()

    def modeling(self, housing):
        this = self.preprocess(housing)
        return this

    def preprocess(self, housing) -> object:
        util = self.util
        this = self.dataset
        this.housing = util.new_model(housing)
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print(f'housing 의 Type 은 {type(this.housing)}')
        print(f'housing 의 상위 5개 행은 {this.housing.head()}이다.')
        print(f'housing 의 상위 5개 행은 {this.housing.columns}이다.')
        print(f'housing 의 null 의 갯수\n {this.housing.isnull().sum()}개')


if __name__ == '__main__':

    controller = Controller()

    controller.modeling('time_series_cost.xlsx')