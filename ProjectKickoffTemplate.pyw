import os
import os.path
import subprocess
import tempfile
from datetime import date
from jinja2 import Environment, FileSystemLoader

# Set These Variables Appropriately
evernote_exe_location = r"C:\Program Files (x86)\Evernote\Evernote"
evernote_database = os.path.join(os.path.expanduser(r"~\AppData\Local\Evernote\Evernote\Databases"), r"idahogray.exb")
template_file = os.path.join(os.path.expanduser(r"~\Documents\EvernoteTemplates"), r"ProjectKickoff.enex")
evernote_notebook = r"Inbox"
my_name = r'Keith Gray'

# Render the Template
env = Environment(loader=FileSystemLoader(os.path.split(template_file)[0]))
template = env.get_template(os.path.split(template_file)[1])
project_number = input('Project Number: ')
client = input('Client: ')
project_name = input('Project Name: ')
project_description = input('Project Description: ')
client_contact = input('Client Contact: ')
client_contact_guidelines = input('Client Contact Guidelines: ')
end_user_client = input('End User Client: ')
powers_role = input("POWER's Role: ")
sas_role = input("SAS Role: ")
project_manager = input('Project Manager: ')
project_engineer = input('Project Engineer: ')
discipline1 = input('Discipline 1: ')
discipline1_lead = input('Discipline 1 Lead: ')
discipline2 = input('Discipline 2: ')
discipline2_lead = input('Discipline 2 Lead: ')
discipline3 = input('Discipline 3: ')
discipline3_lead = input('Discipline 3 Lead: ')
discipline4 = input('Discipline 4: ')
discipline4_lead = input('Discipline 4 Lead: ')
discipline5 = input('Discipline 5: ')
discipline5_lead = input('Discipline 5 Lead: ')
software1 = input('Software 1: ')
software2 = input('Software 2: ')
software3 = input('Software 3: ')
software4 = input('Software 4: ')
software5 = input('Software 5: ')
software6 = input('Software 6: ')
deliverable1 = input('Deliverable 1: ')
deliverable2 = input('Deliverable 2: ')
deliverable3 = input('Deliverable 3: ')
deliverable4 = input('Deliverable 4: ')
go_by = input('Go-By: ')
subtask1 = input('Subtask 1: ')
subtask2 = input('Subtask 2: ')
subtask3 = input('Subtask 3: ')
subtask4 = input('Subtask 4: ')
subtask5 = input('Subtask 5: ')
attendee_2 = input('Attendee #2: ')
attendee_3 = input('Attendee #3: ')
attendee_4 = input('Attendee #4: ')
attendee_5 = input('Attendee #5: ')
attendee_6 = input('Attendee #6: ')
attendee_7 = input('Attendee #7: ')

temporary_file = tempfile.NamedTemporaryFile(delete=False)

rendered_template = template.render(date=date.today(), project_number=project_number, 
        project_name=project_name, Attendee_1 = my_name,
        Attendee_2 = attendee_2, Attendee_3 = attendee_3,
        Attendee_4 = attendee_4, Attendee_5 = attendee_5,
        Attendee_6 = attendee_6, Attendee_7 = attendee_7,
        project_description = project_description, client_contact = client_contact,
        client_contact_guidelines = client_contact_guidelines,
        end_user_client = end_user_client, powers_role = powers_role,
        sas_role = sas_role, project_manager = project_manager,
        project_engineer = project_engineer, discipline1 = discipline1,
        discipline2 = discipline2, discipline3 = discipline3,
        discipline4 = discipline4, discipline5 = discipline5,
        discipline1_lead = discipline1_lead, discipline2_lead = discipline2_lead,
        discipline3_lead = discipline3_lead, disclipline4_lead = discipline4_lead,
        discipline5_lead = discipline5_lead, software1  = software1, 
        software2 = software2, software3 = software3, software4 = software4,
        software5 = software5, software6 = software6, deliverable1 = deliverable1,
        deliverable2 = deliverable2, deliverable3 = deliverable3,
        deliverable4 = deliverable4, go_by = go_by, subtask1 = subtask1,
        subtask2 = subtask2, subtask3 = subtask3, subtask4 = subtask4, 
        subtask5 = subtask5,)

# Write the Rendered Template to a Temporary File
temporary_file.write(bytes(rendered_template, 'UTF-8'))
temporary_file.close()

# Call the ENScript and Load the Temporary File with the Rendered Template Data
os.chdir(evernote_exe_location)
subprocess.call(['ENScript', 'ImportNotes', '/s', temporary_file.name, '/n', evernote_notebook, '/d', evernote_database])

os.remove(temporary_file.name)

