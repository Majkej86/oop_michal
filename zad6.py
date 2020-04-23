class Pojazd:
    pass


class Pojazd_Silnikowy(Pojazd):
    pass


class Pojazd_Wolnobiezny(Pojazd_Silnikowy):
    pass


class Pojazd_Specjalny(Pojazd_Silnikowy):
    pass


class Pojazd_Samochodowy(Pojazd_Silnikowy):
    pass


class Samochod_Osobowy(Pojazd_Samochodowy):
    pass


class Motocykl(Pojazd_Wolnobiezny):
    pass


class Autobus(Pojazd_Specjalny):
    pass
