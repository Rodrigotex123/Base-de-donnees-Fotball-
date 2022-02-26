# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:49:09 2022

@author: rodri
"""

import sqlite3



arg = 1

while arg != 0:
    print("*"*30)
    print("\nChoisissez :\n")
    print("0\tQuitter le programme")
    print("1\tCherche le Nom dans la table Football")
    print("2\tCherche la Selection dans la table Football")
    print("3\tCherche le Club dans la table Football")
    print("4\tAjouter un element dans la table Football")
    print()
    arg = int(input("Choisir une option: "))
    
    if arg == 1:
        
        connexion = sqlite3.connect("Footbal.db")
        curseur = connexion.cursor()
    
        param = input("Ecrire le nom du joueur: ")
        param = [f"%{param}%"]
    
        requete_sql = """
                        SELECT *
                        FROM Football as F
                        WHERE F.Nom LIKE ?;"""
        
        
        #resultat = curseur.execute(requete_sql, (table))
        resultat = curseur.execute(requete_sql, param)
        resultat = resultat.fetchall()
        connexion.close()
        
        print("\nVoici les resultats obtenus:\n")
        for r in resultat:
            print(r)
            
    elif arg == 2:
        
        connexion = sqlite3.connect("Footbal.db")
        curseur = connexion.cursor()
    
        param = input("Ecrivez la selection du joueur: ")
        param = [f"%{param}%"]
    
        requete_sql = """
                        SELECT *
                        FROM Football as F
                        WHERE F.Selection LIKE ?;"""
        
        
        #resultat = curseur.execute(requete_sql, (table))
        resultat = curseur.execute(requete_sql, param)
        resultat = resultat.fetchall()
        connexion.close()
        
        print("\nVoici les resultats obtenus:\n")
        for r in resultat:
            print(r)
            
    elif arg == 3:
        
        connexion = sqlite3.connect("Footbal.db")
        curseur = connexion.cursor()
    
        param = input("Ecrivez le club du joueur: ")
        param = [f"%{param}%"]
    
        requete_sql = """
                        SELECT *
                        FROM Football as F
                        WHERE F.Club LIKE ?;"""
        
        
        #resultat = curseur.execute(requete_sql, (table))
        resultat = curseur.execute(requete_sql, param)
        resultat = resultat.fetchall()
        connexion.close()
        
        print("\nVoici les resultats obtenus:\n")
        for r in resultat:
            print(r)


            
    elif arg == 4:
        
        try:
            connexion = sqlite3.connect("Footbal.db")
            curseur = connexion.cursor()
        
            inp1=input("Insérer un nom")
            inp2=input("Insérer une sélection")
            inp3=input("Insérer un club")
            
        
            requete_sql = f"""
                            INSERT INTO Football (Nom,Selection,Club) VALUES ('{inp1}', '{inp2}', '{inp3}');
                            """
                            
            
            
            #resultat = curseur.execute(requete_sql, (table))
            #resultat = curseur.execute(requete_sql, param)
            resultat = curseur.execute(requete_sql)
            
            connexion.commit()
            
            requete_sql = """
                            SELECT * FROM Football;
                            """
            
            
            #resultat = curseur.execute(requete_sql, (table))
            resultat = curseur.execute(requete_sql)
            
            
            resultat = resultat.fetchall()
            connexion.close()
        
            print("\nVoici la tabale Football:\n")
            for r in resultat:
                print(r)
        except Exception as e:
            print(e)
            connexion.close()





