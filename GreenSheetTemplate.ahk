; Map F1 key to F2 to keep help from opening in Excel when trying to edit a cell
f1::f2

; Run the Evernote Template Creation python script with Win+T
SetWorkingDir %A_ScriptDir%
#t::Run python TemplateChooser.pyw

; Shortcut for searching outlook for attachments
#h::
Send hasattachment:yes from:
return
