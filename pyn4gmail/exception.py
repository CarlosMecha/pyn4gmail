
class AuthException(Exception):
  """ Authentication exception. """
  def __init__(self, msg):
    super(AuthException, self).__init__(self, msg)

class DumbProgrammerException(Exception):
  """ Implementation exception. """
  def __init__(self, msg):
    super(DumbProgrammerException, self).__init__(self, 'Ya dumb: %s' % msg)

