import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
from crime.service import CrimeServer


class Crime_API(object):

    @staticmethod
    def main():
        crimeService = CrimeServer()
        while 1:
            menu = input('0. 1. 2.')
            if menu == '0':
                break
            elif menu == '1':
                crimeService.csv({'context':'./data/', 'fname':'cctv_in_seoul'})
            elif menu == '2':
                crimeService.xls({'context':'./data/', 'fname':'pop_in_seoul'})
            else :
                continue


Crime_API.main()