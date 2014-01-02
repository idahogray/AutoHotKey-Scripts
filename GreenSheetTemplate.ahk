; Map F1 key to F2 to keep help from opening in Excel when trying to edit a cell
f1::f2

; Run the Evernote Template Creation python script with Win+T
SetWorkingDir %A_ScriptDir%
#t::Run python TemplateChooser.pyw

; Shortcut for searching outlook for attachments
#h::
Send hasattachment:yes from:
return

; Shortcut for sending CID files
#C::
Send {Tab}FTPUSER{Tab}TAIL{Tab}{Tab}{Enter}
return

; Shortcut for changing the Local Area Connection IP Address
#i::Run python ChangeIP.py

; Shortcut for downloading budget reports
#b::Run python C:\Users\kgray\Documents\Software\budget-downloader\budget_downloader\budget_downloader.py

; Text expansion
::Kieth::Keith

::@home::
(
4228 Millers Ridge
St. Charles, MO 63304
)

; Toggle speaker mute with Win+S because my office keyboard doesn't have multimedia keys
#s:: Send {Volume_Mute}
#PgUp:: Send {Volume_Up 3}
#PgDn:: Send {Volume_Down 3}