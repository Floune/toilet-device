from random import *

robin = ["Bonjour maitre.", "Mes respects, mon créateur", "contente de vous revoir", "prout", "Ca faisait longtemps, vieille branche"]
hayate = ["Metaaaaaaal", "Tu es ravissante", "sba el nour, mi amour", "Trop mignonne", "et alors, on va déposer les copains à la piscine ? ha ha ha ha", "sara connor ?"]
suleyman = ["Méga ninja dragon de feu activé", "coucoudoudou choubidoubidou palapbapbap", "Attention, un léviator a été aperçu dans les canalisations"]

def start(name):
	if (name == "robin"):
		greet = choice(robin)
	if (name == "hayate"):
		greet = choice(hayate)
	if (name == "suleyman"):
		greet = choice(suleyman)
	return greet
