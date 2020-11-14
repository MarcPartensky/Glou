from recorder import record
import os

result = record()

if result.startswith('microphone'):
    print(sr.Microphone.list_microphone_names())

elif result.startswith('website'):
    os.system('code /Users/marcpartensky/programs/website')

elif result.startswith('dossier'):
    print(os.listdir())

elif result.startswith('sauvegarde'):
    message = result.replace('sauvegarde', '', 1).strip()
    os.system(f'git add -A; git commit -m  "{message}"; git push')

elif result.startswith('dis'):
    message = result.replace('dis', '', 1).strip()
    os.system(f'say {message}')

else:
    print(result)
