import tinyapi
from getpass import getpass

session = tinyapi.Session("liguoqinjim", getpass())

draft = session.create_draft()

draft.subject = "Testing TinyAPI"
draft.body = "Just a test."
draft.save()

draft.send_preview()