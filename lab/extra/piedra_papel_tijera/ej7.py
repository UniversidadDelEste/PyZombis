#!/usr/bin/python2
# coding: utf-8
# Bienvenido al juego Piedra, Papel o Tijera!. Desafortunadamente el juego no funciona
# puesto que se han perdido algunas partes del código fuente. Si eres tan amable, por
# favor te pido me ayudes a ponerlo en funcionamiento nuevamente. Para ello deberás
# como primer paso, leer y entender el código existente. Luego, notaras que falta completar
# la implementación de las clases Piedra y Papel, puede que leyendo el ćodigo de la clase
# Tijera te sirva de guia. También creo haber notado que en la clase Juego, en el método
# jugar, pareciera que falta definir cuando gana un jugador una partida, te he dejado un
# comentario en el código fuente para indicarte en qué parte deberías escribir el código faltante,
# espero te sea de ayuda. Muchas gracias por tu ayuda!

import unittest


__author__ = "Emiliano Dalla Verde Marcozzi <edvm@fedoraproject.org>"


class Elemento(object):

    @property
    def name(self):
        """Nombre del elemento"""
        return self._name


class Tijera(Elemento):

    def __init__(self):
        self._name = 'tijera'

    def __cmp__(self, obj):
        """Reglas:
            - Tijera empata con Tijera
            - Tijera pirde contra piedra
            - Tijera gana contra papel
        """
        if obj.name == 'tijera':
            return 0
        if obj.name == 'piedra':
            return -1
        if obj.name == 'papel':
            return 1


class Piedra(Elemento):

    def __init__(self):
        self._name = 'piedra'

    def __cmp__(self, obj):
        """Reglas:
            - Piedra empata con piedra
            - Piedra pirde contra papel
            - Piedra gana contra tijera
        """
        # Recuerda que puedes obtener ayuda sobre como implementar __cmp__
        # en: https://docs.python.org/2/reference/datamodel.html#object.__cmp__


class Papel(Elemento):

    def __init__(self):
        self._name = 'papel'

    def __cmp__(self, obj):
        """Reglas:
            - Papel empata con papel
            - Papel pierde contra tijera
            - Papel gana contra piedra
        """
        # Recuerda que puedes obtener ayuda sobre como implementar __cmp__
        # en: https://docs.python.org/2/reference/datamodel.html#object.__cmp__


class Juego(object):

    def __init__(self, player1, player2, number_of_games=3):
        """Parametros:
            - player1(str):     Movimientos del jugador 1
            - player2(str):     Movimientos del jugador 2
        """
        # Validamos que los parametros sean como los esperamos
        for moves in [player1, player2]:
            if not isinstance(moves, list):
                raise TypeError('El argumento debe ser de tipo lista')
            assert len(moves) == number_of_games, 'Cantidad de movimientos insuficiente'
            for elem in moves:
                assert elem in ['piedra', 'papel', 'tijera'], 'Elemento de lista no valido'
        self.m_player1 = player1
        self.m_player2 = player2
        self.score_player1 = 0  # puntaje del player1
        self.score_player2 = 0  # puntaje del player2
        self.number_of_games = number_of_games  # cantidad de partidas que se van a jugar

    def _get_elem(self, elem):
        elementos = dict(
            piedra=Piedra,
            papel=Papel,
            tijera=Tijera
        )

        return elementos[elem]()

    def jugar(self):
        """Retorna un entero:
            - 0 si la partida fue un empate
            - 1 si gano el jugador 1
            - 2 si gano el jugador 2
        """
        for x in range(self.number_of_games):
            mov1, mov2 = self._get_elem(self.m_player1[x]), self._get_elem(self.m_player2[x])
            if mov1 == mov2:       # empate
                self.score_player1 += 1
                self.score_player2 += 1
            # Completar el resto de las movidas, si gana mov1 contra mov2, o si gana
            # mov2 contra mov1 sumar el puntaje al jugador que corresponda

        winner = 0
        if self.score_player1 > self.score_player2:
            winner = 1
        if self.score_player1 < self.score_player2:
            winner = 2

        return winner
