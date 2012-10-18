import os
import os.path
import subprocess

print os.path.expanduser(r"~\Documents")
evernote_exe_location = r"C:\Program Files (x86)\Evernote\Evernote"
evernote_database = os.path.join(os.path.expanduser(r"~\AppData\Local\Evernote\Evernote\Databases"), r"idahogray.exb")
template_file = os.path.join(os.path.expanduser(r"~\Documents\EvernoteTemplates"), r"GreenSheetTemplate.enex")
evernote_notebook = r"Inbox"

os.chdir(evernote_exe_location)
subprocess.call(['ENScript', 'ImportNotes', '/s', template_file, '/n', evernote_notebook, '/d', evernote_database])


