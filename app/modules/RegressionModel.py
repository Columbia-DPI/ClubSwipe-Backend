
from ..modules import MongoHelper
import math

'''

in vector format:


"active": str,
"governing": str,
"tech design": str,
"music arts": str,
"preproffesional": str,
"publications": str,
"activism service": str,
"hours": str,
"selectivity": str,
"size": str,

'''

def optimize(db, col, input_vector):
    clubLi = MongoHelper.DB_fetch_clubs(db, col) #get club list

    returnClubLi = []
    lowestError = {1000,1000,1000,1000,1000}


    for club in clubLi:
        clubVect = club['vector']
        sum = 0
        error = -1

        for value in input_vector.keys():

            if value != 'hours' and value != 'selectivity' and value != 'size':
                personVectVal = float(input_vector[value])
                clubVectVal = float(clubVect[value])
                sum += abs(personVectVal - clubVectVal)**2
        
        error = math.sqrt(sum)

        if error < max(lowestError):
            lowestError.remove(max(lowestError))
            lowestError.add(error)
            returnClubLi.append(club)
            
    return returnClubLi
        



 