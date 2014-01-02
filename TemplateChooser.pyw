print("1. Daily Note")
print("2. Green Sheet Note")
print("3. Project Kickoff Note")
choice = None

while choice not in ['1', '2', '3']:
    choice = raw_input("Enter Choice: ").strip()

if choice == '1':
    import DailyNoteTemplate
elif choice == '2':
    import GreenSheetTemplate
elif choice == '3':
    import ProjectKickoffTemplate
