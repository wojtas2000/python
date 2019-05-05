"""Zle przyklady jak nie robic (po to sa obiekty!)"""
auto = {
    'kolor': 'Czerwony',
    'marka': 'Volvo'
}

nowe_auto = {}
nowe_auto['kolro'] = "Niebieski"
nowe_auto['marka'] = 'Fiat'


def wlacz_silnik(auto):
    print("{} brum brum".format(auto['marka']))