import urllib

def url_escape(text):
  # See OAUTH 5.1 for a definition of which characters need to be escaped.
  return urllib.quote(text, safe='~-._')


def url_unescape(text):
  # See OAUTH 5.1 for a definition of which characters need to be escaped.
  return urllib.unquote(text)

def format_url_params(params):
  """Formats parameters into a URL query string.

  Args:
    params: A key-value map.

  Returns:
    A URL query string version of the given parameters.
  """
  param_fragments = []
  for param in sorted(params.iteritems(), key=lambda x: x[0]):
    param_fragments.append('%s=%s' % (param[0], url_escape(param[1])))
  return '&'.join(param_fragments)

