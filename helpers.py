pobut = dict()
pobut['15-60'] = .00097
pobut['15-19'] = .00072
pobut['20-24'] = .00110
pobut['45-49'] = .001
pobut['60-64'] = .0014

genetic = dict()
pobut['15-60'] = .03800
genetic['15-19'] = .00030
genetic['20-24'] = .00040
genetic['45-49'] = .0048
genetic['60-64'] = .025

living_place = {
    "accidents": {
        "village": {
            "male": 1.9,
            "female": .31
        },
        "city": {
            "male": 1.6,
            "female": .28
        }
    },
    "illness": {
        "village": {
            "male": 1.7,
            "female": .42 
        },
        "city": {
            "male": 1.45,
            "female": .38
        }
    }
}

hobbies = dict()

hobbies['student'] = 5 * (10 ** (-8))
hobbies['driving'] = .000001
hobbies['skiing'] =  .0000003
hobbies['driver-professional'] = .0000003
hobbies['potter'] = .00000025
hobbies['speliolog'] = .000027

habits = dict()

habits['smoking'] = .008
habits['drinking'] = .000212
habits['car-accident'] = .00019
habits['drowning'] = .000091