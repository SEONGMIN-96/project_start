from real_estate.dataset import Dataset
from real_estate.service import Service


class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, housing):
        this = self.preprocess(housing)
        return this

    def preprocess(self, housing) -> object:
        service = self.service
        this = self.dataset
        this.housing = service.new_model(housing)
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