# -*- coding: UTF-8 -*-

# standard
import os


class SpecialFolderPath:
    # public

    # prohibit instantiation
    def __init__():
        pass

    @classmethod
    def get(cls, value=None):
        if value:
            if isinstance(value, str):
                if value in cls._SPECIAL_FOLDER.keys():
                    return cls._get(value)
                else:
                    raise ValueError(f'{value} is not a valid special folder')
            elif isinstance(value, int):
                if value in cls._SPECIAL_FOLDER.values():
                    return cls._get(value)
                else:
                    raise ValueError(f'{value} is not a valid special folder')
            else:
                raise TypeError(f'{type(value)} is not a valid type')
        else:
            paths = []
            for k in cls._SPECIAL_FOLDER.keys():
                paths.append(cls._get(k))
            return paths
    
    @classmethod
    def get_with_keys(cls):
        path = {}
        for k in cls._SPECIAL_FOLDER.keys():
            path[k] = cls._get(k)
        return path

    @classmethod
    def get_dict(cls):
        return cls._SPECIAL_FOLDER


    # private

    _SPECIAL_FOLDER = {
        'AdminTools':             48,
        'ApplicationData' :       26,
        'CDBurning':              59,
        'CommonAdminTools':       47,
        'CommonApplicationData':  35,
        'CommonDesktopDirectory': 25,
        'CommonDocuments':        46,
        'CommonMusic':            53,
        'CommonOemLinks':         58,
        'CommonPictures':         54,
        'CommonProgramFiles':     43,
        'CommonProgramFilesX86':  44,
        'CommonPrograms':         23,
        'CommonStartMenu':        22,
        'CommonStartup':          24,
        'CommonTemplates':        45,
        'CommonVideos':           55,
        'Cookies':                33,
        'Desktop':                0,
        'DesktopDirectory':       16,
        'Favorites':              6,
        'Fonts':                  20,
        'History':                34,
        'InternetCache':          32,
        'LocalApplicationData':   28,
        'LocalizedResources':     57,
        'MyComputer':             17,
        'MyDocuments':            5,
        'MyMusic':                13,
        'MyPictures':             39,
        'MyVideos':               14,
        'NetworkShortcuts':       19,
        'Personal':               5,
        'PrinterShortcuts':       27,
        'ProgramFiles':           38,
        'ProgramFilesX86':        42,
        'Programs':               2,
        'Recent':                 8,
        'Resources':              56,
        'SendTo':                 9,
        'StartMenu':              11,
        'Startup':                7,
        'System':                 37,
        'SystemX86':              41,
        'Templates':              21,
        'UserProfile':            40,
        'Windows':                36,
    }

    def _get(value):
        return os.popen(f'powershell -Command ([Environment])::GetFolderPath("""{value}""")').read().rstrip('\n')


def main():
    from pprint import pprint
    pprint(SpecialFolderPath.get())
    pprint(SpecialFolderPath.get('MyPictures'))
    pprint(SpecialFolderPath.get_with_keys())
    pprint(SpecialFolderPath.get_dict())


if __name__ == '__main__':
    main()

