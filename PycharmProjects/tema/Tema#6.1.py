#1Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei


class cerc:
    raza = 8
    aria=3.14*(raza)**2
    circumferinta=2*3.14*(raza)
    culoare='Albastru'

    def __init__(self,raza,culoare,aria,circumferinta):
        self.raza = raza
        self.culoare = culoare
        self.aria = aria


    def arie_cerc(self,aria):
        return aria
    print(f'Aria este: {aria}')

    def arie_circumferinta(self,circumferinta):
        return circumferinta
    print(f'Circumferinta este: {circumferinta}')

    def culoare_cerc(self,culoare):
        return culoare
    print(f'Culoarea este: {culoare}')

#2