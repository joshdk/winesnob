import urllib
import faroo
from django.http import HttpResponse
from django import template
from django.template import loader
from django.shortcuts import redirect
import pairings




#{{{ Render helper
def render(template_data, context_data={}):
	t = template.Template(template_data)
	c = template.Context(context_data)
	return t.render(c)
#}}}


#{{{ Views
#{{{ Search view
def search(request):
	t = loader.get_template('search_template.html')
	c = template.Context({})
	content = t.render(c)
	return HttpResponse(content)
#}}}


#{{{ Results view
def results(request, query):
	query = urllib.unquote(query).decode('utf8')
	if len(query) == 0:
		return redirect('/')
	else:
		content = render_search(query)
	return HttpResponse(content)
#}}}
#}}}


#{{{ Fetch a set of results
def fetch_results(query):
	freq = faroo.Faroo()
	results = []

	# Fetch regular results
	fres = freq.param('length', 8).query(query)
	if fres is not None and fres.results is not None:
		results = fres.results + results

	# Fetch wine results
	fres = freq.param('length', 3).query(query + ' wine')
	if fres is not None and fres.results is not None:
		results = fres.results + results

	# Augment results with suggestions
	results = [(result, fetch_suggestion(result)) for result in results]

	# Sort results, augmented results first
	return [result for result in results if result[1] is not None] + [result for result in results if result[1] is None]
#}}}


#{{{ Fetch a suggestion
def fetch_suggestion(result):
	import random
	suggestions = pairings.suggest_wines(result.title)
	if len(suggestions) > 0:
		return random.choice(suggestions)
	return None
#}}}


#{{{ Render entire query page
def render_search(query):
	content = ''
	results = fetch_results(query)
	content += render_results(results)
	t = loader.get_template('results_template.html')
	c = template.Context({'query': query, 'results': content})
	content = t.render(c)
	return content
#}}}


#{{{ Render a set of results
def render_results(results):
	if len(results) == 0:
		return ''
	return render_result(results[0]) + render_results(results[1:])
#}}}


#{{{ Render a single suggestion
def render_suggestion(suggestion=None):
	if suggestion is None:
		return ''

	return render(
		'Might I suggest trying some <a href="{{url}}">{{title}}</a>',
		{'url': 'https://en.wikipedia.org/wiki/' + suggestion, 'title': suggestion}
	)
#}}}


#{{{ render a single result
def render_result(pair):
	result     = pair[0]
	suggestion = pair[1]

	return render(
		'<div class="row"><div class="span8 offset2">{{result|safe}}</div></div>',
		{
			'result': render(
				'<a href="{{url}}">{{title}}</a>',
				{'url': result.url, 'title': result.title}
			)
		}
	) + render(
		'<div class="row"><div class="span8 offset2">{{suggestion|safe}}</div></div>',
		{'suggestion': render_suggestion(suggestion)}
	) + render(
		'<div class="row"><div class="span8 offset2"><hr></div></div>'
	)
#}}}
