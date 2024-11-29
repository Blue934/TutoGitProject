                                        #Partie Python


Todos = []


#New Todo
def Todo(Title):
    todo = {"Titre" : Title, "statut" : "A faire"} 
    Todos.append(todo)
print("Quel est le titre de votre todo ?")
Title = str(input())
print("Confirmez-vous ?")
reponse = input()
if reponse == "oui":
    Todo (Title)
else:
    print("Annulation")
    

#print (Todos)
#List Todo
def Show():
    for todo in Todos:
        print(f"Title: {todo['Titre']}\n",f"Statut: {todo['statut']}")
        
        
Show()
#Update()
def Update(Titleof):
    for todo in Todos:
        if todo['Titre'] == Titleof:
            if todo['statut'] == "A faire":
                todo['statut'] = "Fait"
                print(f"Le {Titleof} a été mis à jour")
            elif todo['statut'] == "Fait":
                todo['statut'] = "A fair" #J'ai volontairement oublier le e , dans le respect des consignes
           
#Update(Nom_du_titre_du_todo)