#!/usr/bin/python2
# coding: utf-8
# basado en customEval.py de E. Mendelowitz:
# http://cs.smith.edu/dftwiki/index.php/Tutorial:_Moodle_VPL_--_Evaluation_Using_A_Custom_Python_Program
import unittest

__author__ = "Emiliano Dalla Verde Marcozzi <edvm@fedoraproject.org>"


# funciones generales para comunicarse con VPL (moodle)
def vpl_comment(s):
    """Formatea un string para crear comentarios VPL"""
    print ("Comment :=>> %s" % s)


def vpl_grade(num):
    """Formatea un número para indicar una nota en VPL"""
    print ("Grade :=>> %s" % num)


# importar el script del alumno para poder ejecutarlo:
try:
    import ej7
    _ = ej7  # pep8
except SyntaxError as e:
    vpl_comment("Error de sintaxis al importar ej7.py ... ejecutelo y corrijalo previamente: %s" % e)
    # sin calificación...
    vpl_grade(0)
    exit()
except Exception as e:
    vpl_comment("Imposible importar ej7.py: %s" % e)
    # calificación indicativa/diferenciativa
    vpl_grade(5)
    exit()


# pruebo si estan definidas las clases Piedra, Papel, Tijera y Juego...
try:
    from ej7 import Piedra
except ImportError:
    vpl_comment("La clase Piedra no esta definida!")
    vpl_grade(10)
    exit()
try:
    from ej7 import Papel
except ImportError:
    vpl_comment("La clase Papel no esta definida!")
    vpl_grade(11)
    exit()
try:
    from ej7 import Tijera
except ImportError:
    vpl_comment("La clase Tijera no esta definida!")
    vpl_grade(12)
    exit()
try:
    from ej7 import Juego
except ImportError:
    vpl_comment("La clase Juego no esta definida!")
    vpl_grade(13)
    exit()


class ScoreBorg(object):
    __sh = {}

    def __init__(self):
        self.__dict__ = self.__sh


class TestJuego(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.borg = ScoreBorg()
        cls.borg.score = 0

    @classmethod
    def tearDownClass(cls):
        print(cls.borg.score)

    def test_piedra_vs_piedra(self):
        piedra_1 = Piedra()
        piedra_2 = Piedra()
        assert piedra_1 == piedra_2
        self.borg.score += 5

    def test_piedra_vs_tijera(self):
        piedra = Piedra()
        tijera = Tijera()
        assert piedra > tijera
        self.borg.score += 10

    def test_piedra_vs_papel(self):
        piedra = Piedra()
        papel = Papel()
        assert piedra < papel
        self.borg.score += 10

    def test_tijera_vs_tijera(self):
        tijera_1 = Tijera()
        tijera_2 = Tijera()
        assert tijera_1 == tijera_2
        self.borg.score += 5

    def test_tijera_vs_papel(self):
        tijera = Tijera()
        papel = Papel()
        assert papel < tijera
        self.borg.score += 10

    def test_tijera_vs_piedra(self):
        tijera = Tijera()
        piedra = Piedra()
        assert piedra > tijera
        self.borg.score += 10

    def test_papel_vs_papel(self):
        papel_1 = Papel()
        papel_2 = Papel()
        assert papel_1 == papel_2
        self.borg.score += 5

    def test_papel_vs_piedra(self):
        papel = Papel()
        piedra = Piedra()
        assert papel > piedra
        self.borg.score += 10

    def test_papel_vs_tijera(self):
        papel = Papel()
        tijera = Tijera()
        assert tijera > papel
        self.borg.score += 10

    def test_juego_empate(self):
        m1 = ['piedra', 'papel', 'tijera']
        m2 = ['tijera', 'papel', 'piedra']
        juego = Juego(m1, m2)
        assert juego.jugar() == 0
        self.borg.score += 5

    def test_juego_gana_jugador_1(self):
        m1 = ['piedra', 'tijera', 'papel']
        m2 = ['piedra', 'papel', 'papel']
        juego = Juego(m1, m2)
        assert juego.jugar() == 1
        self.borg.score += 10

    def test_juego_gana_jugador_2(self):
        m1 = ['piedra', 'tijera', 'papel']
        m2 = ['papel', 'piedra', 'tijera']
        juego = Juego(m1, m2)
        assert juego.jugar() == 2
        self.borg.score += 10


if __name__ == '__main__':
    unittest.main()
