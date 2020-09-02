from recorder import record
import os

result = record()

if result.startswith('quels sont mes micros'):
    print(sr.Microphone.list_microphone_names())

elif result.startswith('website'):
    os.system('code /Users/marcpartensky/programs/website')

elif result.startswith('fichiers'):
    print(os.listdir())

else:
    print(result)
