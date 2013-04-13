from pyn4gmail.exception import DumbProgrammerException

class IMAPSearchFilter(object):
  """
  Abstract class for IMAP search filters.
  """

  def __init__(self):
    pass

  def get_search_pattern(self):
    """
    Obtains the string pattern for the IMAP search operation.

    This method should be overrided!
    """
    raise DumbProgrammerException('This method should be overrided!')

class IMAPUnreadFilter(IMAPSearchFilter):
  """
  Default filter. It filters for unread emails.
  """
  def __init__(self):
    super(IMAPUnreadFilter, self).__init__()

  def get_search_pattern(self):
    return '(UNSEEN)'

