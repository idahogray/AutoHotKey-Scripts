import os
import os.path
import subprocess
import tempfile
from datetime import date
from jinja2 import Environment, FileSystemLoader

# Set These Variables Appropriately
evernote_exe_location = r"C:\Program Files (x86)\Evernote\Evernote"
evernote_database = os.path.join(os.path.expanduser(r"~\AppData\Local\Evernote\Evernote\Databases"), r"idahogray.exb")
template_file = os.path.join(os.path.expanduser(r"~\Documents\EvernoteTemplates"), r"DailyNoteTemplate.enex")
evernote_notebook = r"Daily Notes"
my_name = r'Keith Gray'

# Render the Template
env = Environment(loader=FileSystemLoader(os.path.split(template_file)[0]))
template = env.get_template(os.path.split(template_file)[1])

temporary_file = tempfile.NamedTemporaryFile(delete=False)

rendered_template = template.render(current_date=date.today())

# Write the Rendered Template to a Temporary File
temporary_file.write(rendered_template)
temporary_file.close()

# Call the ENScript and Load the Temporary File with the Rendered Template Data
os.chdir(evernote_exe_location)
subprocess.call(['ENScript', 'ImportNotes', '/s', temporary_file.name, '/n', evernote_notebook, '/d', evernote_database])

os.remove(temporary_file.name)

