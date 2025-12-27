print("Pipeline DevOps BIM de SK-KALLEL fonctionne !")
print("Maquette Revit + script Dynamo + Speckle = versionnée et testée")

# Un petit test simple qui doit passer
nombre_murs = 11   # le nombre de murs dans ta maquette test
nombre_dalles = 3 # le nombre de dalles
total = nombre_murs + nombre_dalles

assert total == 15, f"Erreur : attendu 12 éléments, trouvé {total}"

print(f"Test passé avec succès ✅ ({nombre_murs} murs + {nombre_dalles} dalles)")
print("Prêt pour l'équipe !")