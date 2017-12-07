#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-


def deco(function):
    """
    notre decorateur
    :param function: 
    :return: 
    """

    def wrapper(*nomme, **nnomme):
        """
        Cette fonction va recuperer tous les parametre de la fonction a décoré et les affichiers
        :param nomme: les parametres non nomé
        :param dic nnomme: les parametres nommés (un dictionnaire)
        :return: 
        """
        for val in nomme:
            print ("notre decorateur va affichier: %s " % val)
        return function(*nomme, **nnomme)

    return wrapper


@deco
def affiche_text(test, nom, age=12):
    """
    affichier un test
    :param str test: le text a affixhier
    :param str nom: son nom
    :return: 
    """
    print test, nom, ", vous avez : ", age


# ---------------------------------------------------------------------------------------------------------------------
def check(typpe):
    """
    Decorateur pour verifier le type des parametres 
    :param typpe: la variable qui va contenir le type que vous voulez
    :return: le type de votre chois
    """

    def deco(function):
        """
        Decorateur pour verifier si les valeurs entrées son des entiers
        :param funtion: 
        :return: 
        """

        def wrapper(*arg, **narg):
            """
            Fonction qui recupere tous les parametres de la fonction
            :param arg: parametre non nommés
            :param narg: parametre nommés
            :return: 
            """
            for nbr in arg:
                if type(nbr) is not typpe:
                    raise TypeError("L'un des parametres que vous entrer n'est pas de bon type !")
            return function(*arg, **narg)

        return wrapper

    return deco


@check(str)
def add(n1, n2):
    """
    fonction de calcule d'addition
    :param int n1: le nombre 1
    :param int n2: le nombre 2
    :return: le resultat
    :rtype int
    """
    return n1 + n2


@check(int)
def sous(n1, n2):
    """
    fonction de soustraction
    :param int n1: le nombre 1
    :param int n2: le nombre 2
    :return: le resultat
    :rtype int
    """
    return n1 - n2


if __name__ == '__main__':
    # affiche_text("bonjour", "saint fourier onesyme \n\n")
    addition = add("saint", " fourier")
    print addition
    soustarction = sous(25, 5)
    print soustarction
