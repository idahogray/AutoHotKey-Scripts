print("1. Daily Note")
print("2. Green Sheet Note")
choice = None

while choice not in ['1', '2']:
    choice = raw_input("Enter Choice: ").strip()

if choice == '1':
    import DailyNoteTemplate
elif choice == '2':
    import GreenSheetTemplate
