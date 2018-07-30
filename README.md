# Listen-Project

Note : Projet mis en parenthèse car pas intéressant pour le public

LISTEN PROJECT

DATA

- On récupère les data sur le dataset de Google

    - Contraintes 
        Les données sont rangés dans un tensorflow.SequenceExample 
        on a le son enrigistré sous la forme 128 8bit quantized à l'aide de VGGish

    - Conséquences
        Soit je récupère les données sous format tensorflow et j'utilise tensorflow
        pour construire le réseau de neurones


APPRENTISSAGE

- On utilise un CNN pour entrainer un model qu'on enregistra sous python (tensorflow,keras)


PREDICTION

- On enregistre un son sur le téléphone, on le formate grâce a VGGish puis on le passe dans
  le model entrainé, on retourne sur l'application le texte qui donne le nom du son
