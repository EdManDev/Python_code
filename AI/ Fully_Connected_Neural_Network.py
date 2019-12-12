import numpy as np
np.random.seed(1) #La generation d'aleatoire sera toujours la meme a chaque execution du programme.

#Variable dans lesquelles on stockera nos coordonees x et y du graphique
#Permet de viasualiser efficacement l'evolution du reseau de neuronne
import matplotlib.pyplot as plt
xGraphCostFunction=[]
yGraphCostFunction=[]

#Fonction d'activation sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#Derive de notre fonction d'activation
def sigmoidPrime(x):
    return x * (1 - x)


#-------------------   Cree les donnes
#Donnes d'inputs
inputs = np.array([ [0, 0, 0, 1],
                    [0, 0, 1, 1],
                    [0, 1, 1, 1],
                    [1, 0, 1, 0],
                    [1, 1, 1, 1]])

#Les outputs qu'on attend
reponses = np.array([ [0],
                      [0],
                      [1],
                      [0],
                      [1]])

#Donnee d'inputs. On s'en servira une fois que notre reseau aura ete entraine pour verifier qu'il a compris
inputs_test = np.array([[1, 1, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 1, 0],
                        [1, 0, 0, 0]])
#----------------------------------------


#------------------   Dimension de notre reseau de neurones
nb_input_neurons = 4        #Nombre de neurones d'entree
nb_hidden_neurons = 4       #Nombre de neurones dans le hidden layer
nb_output_neurons = 1       #Nombre de neurones de sortie
#------


#Initialise tout nos poids de maniere aleatoire entre -1 et 1
hidden_layer_weights = 2 * np.random.random((nb_input_neurons, nb_hidden_neurons)) - 1
output_layer_weights = 2 * np.random.random((nb_hidden_neurons, nb_output_neurons)) - 1

#===================================
#           Phase d'entrainement
#===================================

#Nombre d'iteration pour la phase d'entrainement
nb_training_iteration = 10000

for i in range(nb_training_iteration):

    #----------------FEED FORWARD-----------------
    # Propage nos informations a travers notre reseau de neurones.

    input_layer = inputs
    hidden_layer = sigmoid(np.dot(input_layer, hidden_layer_weights))   #Fonction de feedforward entre l'input layer et le hidden layer
    output_layer = sigmoid(np.dot(hidden_layer, output_layer_weights))  #Fonction de feedforward entre le hidden layer et l'ouput layer


    # ----------------BACKPROPAGATION-----------------

    #calcul du cout pour chacune de nos donnes. Represente a quel point on est loin du resultat attendu.
    #L'objectif est de le diminuer le plus possible
    output_layer_error = (reponses - output_layer)
    print("erreur : " + str(output_layer_error))
    # output_layer_error = []

    #Calcul de la valeur avec laquelle on vas corriger nos poids entre le hidden layer et le output layer
    output_layer_delta = output_layer_error * sigmoidPrime(output_layer)

    #Quels sont les poids entre l'input layer et le hidden layer qui ont  contribues a l'erreur, et dans quelle mesure?
    hidden_layer_error = np.dot(output_layer_delta, output_layer_weights.T)

    #Calcul de la valeur avec laquelle on vas corriger nos poids entre le input layer et le hidden layer
    hidden_layer_delta = hidden_layer_error * sigmoidPrime(hidden_layer)


    #Correction de nos poids
    output_layer_weights += np.dot(hidden_layer.T,output_layer_delta)
    hidden_layer_weights += np.dot(input_layer.T,hidden_layer_delta)

    #Affichage du cout.
    if (i % 10) == 0:
        cout = str(np.mean(np.abs(output_layer_error))) #Calcul de la moyenne de toute les valeurs de notre erreur
        print("Cout:" + cout)

        #Abscisse du graph -> iteration de la boucle d'apprentissage
        xGraphCostFunction.append(i)
        #Ordonee du grap -> valeure du cout (arrondis a 3 decimales)
        v = float("{0:.3f}".format(float(cout)))
        yGraphCostFunction.append(v)

#===================================
#           Phase de test
#===================================

# Propage nos informations a travers notre reseau de neurones.
input_layer = inputs_test
hidden_layer = sigmoid(np.dot(input_layer, hidden_layer_weights))
output_layer = sigmoid(np.dot(hidden_layer, output_layer_weights))

#Affiche le resultat
print("------")
print("resultat : ")
print(str(output_layer))

#Affiche le graphique
plt.plot(xGraphCostFunction, yGraphCostFunction)
plt.show()


#Tadaaaaa, finis! :3