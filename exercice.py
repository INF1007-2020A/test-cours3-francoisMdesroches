#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    # TODO completer la fonction
    nouvNom = ""
    for i in (range(len(nom))):
        if i == 0:
            nouvNom += nom[i].upper()
        else:
            nouvNom+= nom[i].lower()

    return nom


if __name__ == '__main__':
    pays = [
        'AfghanIstan',
        'albania',
        'algeria',
        'AndorRa',
        'angolA',
        'antigua ANd barbuda',
        'argEntina',
        'Armenia',
        'austrAlia',
        'ausTria',
        'azerBaijaN'
    ]
    for i in range(len(pays)):
        pays[i] = capitaliser_pays(pays[i])

    print(pays)
