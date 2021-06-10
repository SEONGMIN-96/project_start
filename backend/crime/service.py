from common.models import FileDTO
from common.service import Printer, Reader
from common.abstracts import ReaderBase


class CrimeServer(ReaderBase):

    def csv(self, payload):
        printer = Printer()
        reader = Reader()
        file = FileDTO()
        file.context = payload.get('context')
        file.fname = payload.get('fname')
        printer.dframe(reader.csv(file))

    def xls(self, payload):
        printer = Printer()
        reader = Reader()
        file = FileDTO()
        file.context = payload.get('context')
        file.fname = payload.get('fname')
        printer.dframe(reader.xls(file, 0, None))

    def json(self):
        pass

    def new_file(self):
        pass






