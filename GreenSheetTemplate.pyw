import os
import os.path
import subprocess
import tempfile
from datetime import date
from jinja2 import Environment, FileSystemLoader

# Set These Variables Appropriately
evernote_exe_location = r"C:\Program Files (x86)\Evernote\Evernote"
evernote_database = os.path.join(os.path.expanduser(r"~\AppData\Local\Evernote\Evernote\Databases"), r"idahogray.exb")
template_file = os.path.join(os.path.expanduser(r"~\Documents\EvernoteTemplates"), r"GreenSheetTemplate.enex")
evernote_notebook = r"Inbox"
my_name = r'Keith Gray'

# Render the Template
env = Environment(loader=FileSystemLoader(os.path.split(template_file)[0]))
template = env.get_template(os.path.split(template_file)[1])
project_number = raw_input('Project Number: ')
project_name = raw_input('Project Name: ')
attendee_2 = raw_input('Attendee #2: ')
attendee_3 = raw_input('Attendee #3: ')
attendee_4 = raw_input('Attendee #4: ')
attendee_5 = raw_input('Attendee #5: ')
attendee_6 = raw_input('Attendee #6: ')
attendee_7 = raw_input('Attendee #7: ')

temporary_file = tempfile.NamedTemporaryFile(delete=False)

rendered_template = template.render(date=date.today(), project_number=project_number, 
        project_name=project_name, Attendee_1 = my_name,
        Attendee_2 = attendee_2, Attendee_3 = attendee_3,
        Attendee_4 = attendee_4, Attendee_5 = attendee_5,
        Attendee_6 = attendee_6, Attendee_7 = attendee_7)

# Write the Rendered Template to a Temporary File
temporary_file.write(rendered_template)
temporary_file.close()

# Call the ENScript and Load the Temporary File with the Rendered Template Data
os.chdir(evernote_exe_location)
subprocess.call(['ENScript', 'ImportNotes', '/s', temporary_file.name, '/n', evernote_notebook, '/d', evernote_database])

os.remove(temporary_file.name)

