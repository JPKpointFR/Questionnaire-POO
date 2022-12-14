# LES FONCTIONS : PROJET QUESTIONNAIRE
# class Qcm:
#  - titre  -str
#  - choix  -list[str]
#  - bonne réponse  -str

#  - poser() -> boolean

# Questionnaire
# - questions---(question,,,)

# - Lancer()


class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def poser(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print(f"   {i+1} - {self.choix[i]}")
        print()

        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(
            1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")

        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input(
            f"Votre réponse (entre {min} et {max}): ")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)


# class Questionnaire:
#     def __init__(self, questions):
#         self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print(f"Score final : {score} sur {len(self.questions)}")
        return score


data = (
    ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
q = Question.FromData(data)
q.poser()

"""Questionnaire(
    (
        Question("Quelle est la capitale de la France ?",
                 ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
        Question("Quelle est la capitale de l'Italie ?",
                 ("Rome", "Venise", "Pise", "Florence"), "Rome"),
        Question("Quelle est la capitale de la Belgique ?",
                 ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
    )
).lancer()"""
