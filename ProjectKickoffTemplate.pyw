import os
import os.path
import subprocess
import tempfile
from datetime import date
from jinja2 import Environment, FileSystemLoader

# Set These Variables Appropriately
evernote_exe_location = r"C:\Program Files (x86)\Evernote\Evernote"
evernote_database = os.path.join(
    os.path.expanduser(r"~\AppData\Local\Evernote\Evernote\Databases"),
    r"idahogray.exb")
template_file = os.path.join(
    os.path.expanduser(r"~\Documents\EvernoteTemplates"),
    r"ProjectKickoff.enex")
evernote_notebook = r"Inbox"
my_name = r'Keith Gray'

# Render the Template
env = Environment(loader=FileSystemLoader(os.path.split(template_file)[0]))
template = env.get_template(os.path.split(template_file)[1])
project_number = raw_input('Project Number: ')
client = raw_input('Client: ')
project_name = raw_input('Project Name: ')
project_description = raw_input('Project Description: ')
client_contact = raw_input('Client Contact: ')
client_contact_guidelines = raw_input('Client Contact Guidelines: ')
end_user_client = raw_input('End User Client: ')
powers_role = raw_input("POWER's Role: ")
sas_role = raw_input("SAS Role: ")
project_manager = raw_input('Project Manager: ')
project_engineer = raw_input('Project Engineer: ')
disciplines = []
while True:
    discipline = raw_input('Discipline: ')
    if discipline == '':
        break
    discipline_lead = raw_input('Discipline Lead: ')
    disciplines.append(
        {'discipline': discipline,
         'discipline_lead': discipline_lead})

softwares = []
while True:
    software = raw_input('Software: ')
    if software == '':
        break
    softwares.append(software)

deliverables = []
while True:
    deliverable = raw_input('Deliverable: ')
    if deliverable == '':
        break
    deliverables.append(deliverable)

go_bys = []
while True:
    go_by = raw_input('Go-By: ')
    if go_by == '':
        break
    go_bys.append(go_by)

subtasks = []
while True:
    subtask = raw_input('Subtask: ')
    if subtask == '':
        break
    subtasks.append(subtask)

attendees = []
while True:
    attendee = raw_input('Attendee: ')
    if attendee == '':
        break
    attendees.append(attendee)

temporary_file = tempfile.NamedTemporaryFile(delete=False)

rendered_template = template.render(
    client=client,
    date=date.today(),
    project_number=project_number,
    project_name=project_name,
    attendees=attendees,
    project_description=project_description,
    client_contact=client_contact,
    client_contact_guidelines=client_contact_guidelines,
    end_user_client=end_user_client,
    powers_role=powers_role,
    sas_role=sas_role,
    project_manager=project_manager,
    project_engineer=project_engineer,
    disciplines=disciplines,
    softwares=softwares,
    deliverables=deliverables,
    go_bys=go_bys,
    subtasks=subtasks)

# Write the Rendered Template to a Temporary File
temporary_file.write(rendered_template)
temporary_file.close()

# Call the ENScript and Load the Temporary File with the Rendered Template Data
os.chdir(evernote_exe_location)
subprocess.call(
    ['ENScript', 'ImportNotes', '/s',
     temporary_file.name, '/n', evernote_notebook, '/d', evernote_database])

os.remove(temporary_file.name)
