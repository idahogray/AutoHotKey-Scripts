AutohotKey-Scripts
==================

This repository contains the scripts I use for AutoHotKey. The script run by
AutoHotKey is a python application that presents the user with a menu.
The menu lists the possible Evernote templates.  Once the user chooses the
template type, that specific template script is called.

Evernote Templates
------------------
I have created two templates at this point.
The first is a template note is for Green Sheet meetings at work.
The second is a simple template for a daily log.

~~~~~~~~~~~~~~~~~~~~~~~~~~~
Main Menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The TemplateChooser.pyw script presents the user with a menu of possible templates
to create.

=====
Usage
=====
* Right click on GreenSheetTemplate.ahk and click Run Script
* Press Win+t to see the menu of possible templates
* Choose the template by entering the number associated with that template
* Press enter

============
Requirements
============
* Evernote
* AutoHotKeys
* Python
* jinja2

~~~~~~~~~~~~~~~~~~~~~~~~~~~
Daily Log Evernote Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~
=============
Prerequisites
=============
* Export a template note from Evernote as an enex file
* Change the variables at the top of the script to appropriate values

=====
Usage
=====
* Choose "1. Daily Note" from the menu by entering 1 and press enter
* The new note will be created in the "Daily Notes" notebook by default
  can be changed via the evernote_notebook variable

============
Requirements
============
* Green Sheet Template note stored in "My Documents\EvernoteTemplates" as DailyNoteTemplate.enex
  
  - Must remove the <created></created> and <updated></updated> tags (plus their contents) or the note will have the templates creation date

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Green Sheet Evernote Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
=============
Prerequisites
=============
* Export a template note from Evernote as an enex file
* Change the variables at the top of the script to appropriate values

=====
Usage
=====
* Choose "2. Green Sheet Note" from the menu by entering 2 and press enter
* The new note will be created in the "Inbox" notebook by default
  can be changed via the evernote_notebook variable

============
Requirements
============
* Green Sheet Template note stored in "My Documents\EvernoteTemplates" as GreenSheetTemplate.enex
  
  - Must remove the <created></created> and <updated></updated> tags (plus their contents) or the note will have the templates creation date
