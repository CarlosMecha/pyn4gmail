"""
IMAP module.
"""

import imaplib
import re
from email.parser import HeaderParser
from email.utils import parsedate


def _get_unread_emails(conn):
  """Retrieves a list of unread emails in an open connection.
  
  It uses the ENVELOPE format.

  In RFC3501 says:

    The fields of the envelope structure are in the following
    order: date, subject, from, sender, reply-to, to, cc, bcc,
    in-reply-to, and message-id.  The date, subject, in-reply-to,
    and message-id fields are strings.  The from, sender, reply-to,
    to, cc, and bcc fields are parenthesized lists of address
    structures.
  """
  pattern = re.compile('^\d+\ \(ENVELOPE\ \("(.*?)"\ "(.*?)"\ \(\("(.*?)"\ .*?\ "(.*?)"\ "(.*?)"\)\).*$')


def _print_basic_email_information(emails, conn):
  """A simple regex parser of IMAP response.
  Prints the date, subject and sender.

  """
  for mid in emails:
    (res, data) = conn.fetch(mid, '(ENVELOPE)')
    headers = pattern.match(data[0])
    print 'Date: %s' % headers.group(1)
    print 'Subject: %s' % headers.group(2)
    print 'From: %s <%s@%s>' % (headers.group(3), headers.group(4), headers.group(5))
    print

