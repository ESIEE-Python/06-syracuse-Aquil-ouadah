"""
Fonction syracuse
"""
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Crée le graphique de syracuse
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ list(range(len(lsyr))) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """
    Génère la suite de Syracuse à partir d'une valeur source n.

    Args:
        n (int): La source de la suite.

    Returns:
        list: La suite de Syracuse générée.
    """
    l = [ ]
    uk = n
    l.append(uk)
    while uk != 1 :
        if uk % 2 == 0 :
            uk /= 2
        else :
            uk = (uk * 3) + 1
        l.append(uk)
    return l

def temps_de_vol(l):
    """
    Calcule le temps de vol total de la suite de Syracuse.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: Le temps de vol total (nombre d'itérations pour atteindre 1).
    """
    n = 0
    n = len(l)
    return n

def temps_de_vol_en_altitude(l):
    """
    Calcule le temps de vol en altitude de la suite de Syracuse.

    Le temps de vol en altitude est défini comme le nombre d'itérations
    où la valeur est supérieure ou égale à la valeur initiale.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: Le temps de vol en altitude.
    """
    n = 0
    for nbr in l:
        if nbr >= l[0] :
            n += 1
        else :
            break
    return n


def altitude_maximale(l):
    """
    Détermine l'altitude maximale atteinte dans la suite de Syracuse.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: La valeur maximale atteinte dans la suite.
    """
    n = 0
    for nbr in l:
        n = max(n, nbr)
    return n


#### Fonction principale


def main():
    """
    Main
    """
    # vos appels à la fonction secondaire ici

    lsyr = syracuse_l(6)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))
if __name__ == "__main__":
    main()
