from common.models import DataTransferObject

class Dto(DataTransferObject):

    ccc: object

    @property
    def ccc(self) -> object: return self._ccc

    @ccc.setter
    def ccc(self, ccc): self._ccc = ccc