from sympy.logic.boolalg import to_cnf, to_dnf
import sys
 

while True:
    # Entrez une expression logique ci-dessous.
    exp = input("Saisissez une expression logique (ou tapez 'exit' pour quitter): ")
    
    if exp.lower() == 'exit':
        break  # Quitter la boucle en tapant "exit".

    # Négation de l'expression en entrée.
    not_exp = '~(' + exp + ')'
    print("Expression négation : ", not_exp)

    # Simplification de l'expression négative en utilisant la CNF.
    exp_simp = to_cnf(not_exp)
    print("Expression simplifiée : ", exp_simp)

    # Extraction des clauses individuelles de l'expression simplifiée.
    exp_simp = str(exp_simp)
    clauses = [clause.split("(")[-1].split(")")[0] for clause in exp_simp.split(" & ")]
   
    print("clauses : ", clauses)

    clauses_resolvants = []

    i=0
    taille_cls = len(clauses)

    # Initialiser clauses_resolvants avec la deuxième clause s'il y a plus d'une clause.
    if taille_cls > 1:
        clauses_resolvants.append(clauses[1])
        del clauses[1]

    # Processus de résolution entre les clauses.
    while taille_cls - i > 1 :
        clause = ''
        c1 = clauses[i].split(" | ")
        c2 = clauses_resolvants[i].split(" | ")
        
        for literal_c1 in c1[:]:
            for literal_c2 in c2[:]:
                 # Vérifier la résolution et supprimer les littéraux résolus.
                if ( literal_c1 == '~'+literal_c2) or ( '~'+literal_c1 == literal_c2 ):
                    c1.remove(literal_c1)
                    c2.remove(literal_c2)
                    if len(c1) == 0 and len(c2) == 0:
                        print("La Formule est valide")
                        sys.exit()
        # Concaténer les littéraux restants pour créer une nouvelle clause.                            
        for j in range( len(c1) ):
            clause = clause + c1[j] + " | "
        
        for k in range( len(c2) ):
            clause = clause + c2[k] + " | "
            
        clause = clause[0 : len(clause)-2]
        # Convertir la nouvelle clause en Forme Normale Disjonctive (FND).
        clause = str(to_dnf(clause))
        
        clauses_resolvants.append(clause)
        
        i+=1

    clauses.extend(clauses_resolvants)

    print("La Formule n\'est pas valide")
    # Test
    # A & ~B   Non Valide
    # ~((~P | ~Z | R) & (~R) & P & (~T | Z) & T)  est Valide
