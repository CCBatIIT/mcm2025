committee = '''Miguel	Arratia	Department of Physics and Astronomy	U California, Riverside
Ronald	Cools	Department of Computer Science	KU Leuven
Xinwei	Deng	Department of Statistics	Virginia Polytechnic and State U
Jing	Dong	Graduate School of Business	Columbia
Mike	Giles	Mathematical Institute	Oxford U
Emmanuel	Gobet	Centre de Mathématiques Appliquées	École Polytechnique
Shane	Henderson	School of Operations Research and Information Engineering	Cornell U
Xuhui	Huang	Department of Chemistry	UW Madison
Joshua	Isaacson		Fermilab
Peter	Kritzer	Johann Radon Institute for Computational and Applied Mathematics	Austrian Academy of Sciences
Frances	Kuo	School of Mathematics and Statistics	U New South Wales
Pierre	L'Ecuyer	Département d'informatique et de recherche opérationnelle	U Montréal
Christiane	Lemieux	Department of Statistics and Actuarial Science	U Waterloo
Gunther	Leobacher	Institute of Mathematics and Scientific Computing	U Graz
Chunfang Devon	Lin	Department of Mathematics and Statistics	Queens U
Simon	Mak	Department of Statistical Science	Duke U
Thomas	Müller-Gronbach	Faculty of Computer Science and Mathematics	U Passau
Ben	Nachman		Lawrence Berkeley National Lab
Chris	Oates	School of Mathematics, Statistics, and Physics	U Newcastle Upon Tyne
Art	Owen	Department of Statistics	Stanford U
Raghu	Pasupathy	Department of Statistics	Purdue U
Natesh	Pillai	Department of Statistics	Harvard U
Pieterjan	Robbe		Sandia National Labs
Veronika	Rockova	Chicago Booth School of Business	U Chicago
Jeffrey	Rosenthal	Department of Statistics	U Toronto
Aretha	Teckentrup	School of Mathematics	U Edinburgh
Bruno	Tuffin		INRIA Rennes Bretagne-Atlantique
Jonathan	Weare	Courant Institute of Mathematical Sciences	New York U'''

for line in committee.split('\n'):
    (fname,lname,department,affiliation) = line.split('\t')
    if not (department==''):
        print(f'* {fname} {lname}, {department}, {affiliation}')
    else:
        print(f'* {fname} {lname}, {affiliation}')

