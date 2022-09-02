import os
import stat
from datetime import datetime

path = "permissao.txt"
n = str(datetime.now())

if os.path.isfile(path):
    os.chmod(path, stat.S_IRWXU)

with open(path, 'w') as file:
    path.write(n)
    os.chmod(path, stat.S_IRUSR)