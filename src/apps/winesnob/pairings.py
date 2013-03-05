#{{{ Food to wine mappings
_pairings = {
	'beef'        : ('cabernet sauvignon', 'merlot', 'pinot noir', 'chianti', 'barolo', 'brunello',),
	'steak'       : ('cabernet', 'bordeaux',),
	'chicken'     : ('chardonnay', 'pinor blanc', 'zinfandel', 'merlot', 'rioja', 'barbera', 'grenache', 'burgundy',),
	'fish'        : ('chardonnay', 'sauvignon blanc', 'pinot grigio', 'chablis',),
	'lamb'        : ('cabernet sauvignon', 'merlot', 'zinfandel', 'pinot noir', 'chianti', 'barolo',),
	'ostrich'     : ('beaujolais', 'zinfandel', 'riesling', 'chenin blanc',),
	'pork'        : ('merlot', 'zinfandel', 'beaujolais', 'dolcetto',),
	'turkey'      : ('beaujolais', 'zinfandel', 'riesling', 'gewurztraminer', 'chenin blanc', 'pinot noir',),
	'veal'        : ('cabernet sauvignon', 'pinot blanc', 'barolo', 'brunello', 'chianti', 'syrah',),
	'salad'       : ('sauvignon blanc', 'pinot blanc',),
	'pasta'       : ('chianti', 'zinfandel', 'pinot blanc', 'pinot grigio', 'chardonnay', 'viognier', 'gavi',),
	'shellfish'   : ('champagne', 'sauvignon blanc',),

	'chinese'     : ('riesling', 'gewurztraminer', 'sauvignon blanc', 'pinot noir',),
	'indian'      : ('zinfandel', 'chardonnay',),
	'japanese'    : ('beaujolais', 'sauvignon blanc', 'riesling',),
	'thai'        : ('chablis', 'chardonnay',),

	'cheese'      : {
		'brie'        : ('red burgundy', 'chardonnay', 'chablis',),
		'camembert'   : ('red burgundy', 'chardonnay', 'chablis',),
		'goat'        : ('sauvignon blanc', 'sancerre', 'pouilly', 'fume',),
		'gouda'       : ('chianti', 'dolcetto', 'pinot noir',),
		'smoked'      : ('gewurztraminer', 'sauternes', 'shiraz',),
		'blue'        : ('sauternes', 'port', 'hermitage', 'madeira',),
		'ceddar'      : ('merlot', 'cabernet sauvignon',),
		'swiss'       : ('pinot noir',),
		'gruyere'     : ('pinot noir',),
		'parmigiano'  : ('chianti', 'barolo', 'sangiovese', 'sherry', 'port',),
		'romano'      : ('chianti', 'barolo', 'sangiovese', 'sherry', 'port',),
	}
}
#}}}


def _suggest(words, pairings):
	suggestions = tuple()

	for i, word in enumerate(words):
		if word in pairings:
			s = pairings[word]
			if isinstance(s, tuple):
				suggestions += s
			else:
				suggestions += _suggest(words[:i] + words[i+1:], s)

	return suggestions


def suggest_wines(phrase):
	return list(set(_suggest(phrase.lower().split(), _pairings)))
