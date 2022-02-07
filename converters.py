# We can take these two functions and put them in a separate
# module called converter. And we can import that module into
# any program that needs these converter functions.

def lbs_to_kg(weight):
    return weight * 0.45

def kg_to_lbs(weight):
    return weight / 0.45