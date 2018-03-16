

curryPasteIngredients = [
        # Name, unit
        ('cardamom',             'tbps'),   # 0
        ('flour',                'cup'),    # 1
        ('weed',                 'buds'),   # 2
        ('tumeric',              'tbps'),   # 3
        ('garlic',               'clove'),  # 4
        ('thai chili peppers, deveined and deseeded',   ''),       # 5
        ('chips',                'g'),      # 6
        ('madras curry powder',  'tbps'),   # 7
        ('cumin',                'tbps'),   # 8
        ('coriander powder',     'tbps'),   # 9
        ('ginger',               'thumbs'), #10
        ('heart of dragon',      ''),       #11
        ('oignon',               ''),       #12
        ('bell pepper',           ''),       #13
        ('garam massala',        'tbps'),   #14
        ('salt',                  'tbps'),   #15
        ('chili powder',         'tbps'),   #16
        ('maple syrup',          'tbps'),   #17
        ('rice',                 'cups'),   #18
        ('tomato paste (the contents of the can, not the can itself)',         'can'),    #19
        ('oil (olive or sesame or whatever)', 'tbps'),   #20
        ]


def getRandomIngredientsAndQuantities():
    # Rolled with a fair d20 -1
    ingredientIndices =  [20, 3, 0, 8, 9, 14, 7, 15, 16, 4, 10, 5,12, 13, 19, 17]

    # Rolled with a fair d20/4
    ingredientQuantities = [4, 1, 0.5, 1, 1, 2, 2, 0.25, 2, 4, 2, 3,  1, 1, 1, 3]
    return ingredientIndices, ingredientQuantities
# -----------------------------------------------------------------------------

def getIngredients():
    ingrIndices, ingrQuantities = getRandomIngredientsAndQuantities()
    ingredients = [curryPasteIngredients[k] for k in ingrIndices]

    lines = []
    for (ingr, unit), quantity in zip(ingredients, ingrQuantities):
        if unit:
            msg = "%s %s of %s" % (quantity, unit, ingr)
        else:
            msg = "%s %s" % (quantity, ingr)
        lines.append(msg)
    return '\n'.join(lines)
# -----------------------------------------------------------------------------

def getDirectives():
    msg = ("Chop all the things that can be chopped"
           "\nHeat up the oil in a large pan"
           "\nAdd all the powdered spices to the oil"
           "\nHeat for 2 minutes or until very fragrant"
           "\nAdd the chopped things (except garlic & ginger), cook at high heat for 10 minutes"
           "\nAdd all the remaining ingredients, cook at high heat for 5 minutes"
           "\nUsing a blender, turn the mixture in a purée"
           "\nVoila, curry paste. "
           "\nAdd 2 cups of RED lentils and 4 cups of water/broth"
           "\nBring to a boil then simmer (covered) for 30-45 minutes"
           "\nYou may replace 2 cups of water with coconut milk"
           )
    return msg



if __name__ == '__main__':
    print(getIngredients() + '\n')
    print(getDirectives())
