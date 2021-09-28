#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools as iter

def order(values: list = None) -> list:
    if values is None:
        values = [None] * 11
        # TODO: demander les valeurs ici
        for i in range(0, 11):
            values[i] = input("Entrez une valeur.")

    return values.sort()


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = [None]*2
        words[0] = input("Entrez la premiere chaine: ")
        words[1] = input("Entrez la deuxieme chaine: ")

    if(len(words[0]) != len(words[1])):
        print("Les deux mots ne sont pas des anagrames")
        return False

    for wordsPermuter in iter.permutations(words[0],len(words[0])):
        if list(wordsPermuter) == list(words[1]):
            print("Les deux mots sont des anagrames")
            return True

    print("Les deux mots ne sont pas des anagrames")
    return False


def contains_doubles(items: list) -> bool:
    for i in items:
        if(items.count(i) > 1):
            return True
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    bestStudentGrade = 0
    bestStudentName = ""
    for student in student_grades:
        notes = student_grades.get(student)
        moyenne = sum(notes)/len(notes)
        if(moyenne > bestStudentGrade):
            bestStudentGrade = moyenne
            bestStudentName = student
    return {bestStudentName : bestStudentGrade}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    result = dict.fromkeys(chr(97+i) for i in range(0, 26))
    for lettre in result:
        result[lettre] = sentence.count(lettre)
    print(result)
    return result


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    ajouterNoms = True
    listeRecette = []

    i = 0
    while ajouterNoms == True:
        nomDeRecette = input("Nom de la recette %d: " % (i+1))
        listeRecette.append(nomDeRecette)
        i += 1

        ajouterNoms = (str(input("Voulez vous ajouter un nom de recette encore (oui/non)? ")) == "oui")

    ajouterIngredient = True
    print(len(listeRecette))
    listeIngredients = []
    for j in range(0, len(listeRecette)):
        i = 0
        listeIngredientsTemp = []
        while ajouterIngredient == True:
            nomIngredient = input("Nom de la l'ingrédient %d de la recette %d: " % (i+1, j+1))
            listeIngredientsTemp.append(nomIngredient)
            i += 1

            ajouterIngredient = (input("Voulez vous encore ajouter un ingredient a la recette "+str(j+1)+" (oui/non)?") == "oui")

        listeIngredients.append(listeIngredientsTemp)
        ajouterIngredient = True

    return dict.fromkeys(listeRecette, listeIngredients)


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recetteAAfficher = input("Quel recette voulez vous affichez? ")
    if(not ingredients.contains(recetteAAfficher)):
        print("Pas de recette de ce noms.")
        return

    print(ingredient for ingredient in ingredients[recetteAAfficher])


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    #order()

    print(f"On vérifie les anagrammes...")
    #anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    #print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    #best_student = best_grades(grades)
    #print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    #frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
