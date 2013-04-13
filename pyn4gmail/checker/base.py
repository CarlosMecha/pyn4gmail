import imaplib
from pyn4gmail.exception import AuthException
from pyn4gmail.filter.base import IMAPUnreadFilter

class Checker(object):
  """
  Base object for checkers.
  """

  def login(self, conf):
    """
    Configures and logins the checker.

    This method should be overrided!
    """
    raise DumbProgrammerException('This method should be overrided!')

  def logout(self):
    """
    Disconnects the checker.
    
    This method should be overrided!
    """
    raise DumbProgrammerException('This method should be overrided!')
  
  def check(self):
    """
    Checks the email and returns the messages ids.
    
    This method should be overrided!
    """
    raise DumbProgrammerException('This method should be overrided!')


class IMAPGmailChecker(Checker):
  """
  An checker object. It will retrieve the emails.

  You can override it for using other technologies, such POP3.
  """

  def login(self, conf):
    """
    Configures and logins the checker with the email server.
     - conf is a dictionary with connection parameters.
        + user: Account user
        + access_string: Access String
        + filter: An filter (instance of IMAPSearchFilter) 
          for emails. By default is the IMAPUnreadFilter.

    It could raise an AuthException due to expired or invalid credentials.

    """

    self._user = conf['user']
    self._access_string = conf['access_string']
    self._filter = conf['filter'] if 'filter' in conf else IMAPUnreadFilter()
    
    self._conn = imaplib.IMAP4_SSL('imap.gmail.com')
    
    try:
      self._auth()
    except imaplib.IMAP4.error:
      raise AuthException("Authentication failed.")

  def _auth(self):
    self._conn.authenticate('XOAUTH2', lambda x: self._access_string)

  def logout(self):
    """Disconnects the checker from the server."""
    self._conn.close()
    self._conn.logout()
    
  def check(self):
    """ 
      Checks emails. Each checker has its own search filter.
    """
    self._conn.select('INBOX', readonly=1)
    (retcode, messages) = self._conn.search(None, self._filter.get_search_pattern())
    if (retcode == 'OK'):
      return messages[0].split()
    else:
      return None
    
