from lib.Fighter_Class import Fighter
from lib.Fight_Class import Fight
from lib.Event_Class import Event


Fighter_A = Fighter('Alexa Grasso', "Women's Strawweight")
Fighter_B = Fighter('Carla Esparza', "Women's Strawweight")

odds_A = {'win': '-125', 'DEC': '+135', 'KO/TKO': '+885', 'SUB': '+995', '1': '+975', '2': '+1275', '3': '+2050'}
odds_B = {'win': '+105', 'DEC': '+165', 'KO/TKO': '+1180', 'SUB': '+1000', '1': '+1125', '2': '+1450', '3': '+2000'}

Fight1 = Fight(Fighter_A, odds_A, Fighter_B, odds_B, 100)

Fighter_C = Fighter('Jeremy Stephens', "Featherweight", True)
Fighter_D = Fighter('Yair Rodriguez', "Featherweight", True)

odds_C = {'win': '-115', 'DEC': '+475', 'KO/TKO': '+150', 'SUB': '+1400', '1': '+475', '2': '+650', '3': '+850', '4': '+1250', '5': '+2000'}
odds_D = {'win': '-105', 'DEC': '+300', 'KO/TKO': '+270', 'SUB': '+1385', '1': '+650', '2': '+850', '3': '+1200', '4': '+1450', '5': '+2000'}

Fight2 = Fight(Fighter_C, odds_C, Fighter_D, odds_D, 100)

Fight2.get_outcomes()

Event1 = Event(Fight1, Fight2)

a = Event1.get_event_outcomes()
