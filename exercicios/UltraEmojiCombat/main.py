import Lutador
import Luta

l=list(range(6))
l[0] = Lutador.Lutador('Pretty Boy','França', 31, 1.75, 68.9, 11, 2, 1)
l[1] = Lutador.Lutador('Putscript', 'México', 29, 1.68, 57.8, 14, 2, 3)
l[2] = Lutador.Lutador('Snapshadow', 'Eua', 35, 1.65, 80.9, 12, 2, 1)
l[3] = Lutador.Lutador('Dead Code', 'Austrália', 28, 1.93, 81.6, 13, 0, 2)
l[4] = Lutador.Lutador('UFO Cobol', 'Brasil', 37, 1.70, 119.3, 5, 4, 3)
l[5] = Lutador.Lutador('Nerdaart', 'Espanha', 30, 1.81, 105.7, 12, 2, 4)

UEC01 = Luta.luta(l[3], l[2], 1, True )
UEC01.marcarLuta(l[3], l[2])
UEC01.lutar()
l[3].status()
l[2].status()
