import os
from datetime import datetime, timedelta

dias = 10  # Número de dias passados
commits_por_dia = 3  # Número de commits por dia

for i in range(dias):
    for j in range(commits_por_dia):
        data = datetime.now() - timedelta(days=i)
        with open("log.txt", "a") as f:
            f.write(f"Commit automático em {data}\n")
        os.system("git add .")
        os.system(f'git commit --date="{data}" -m "commit automático {i}-{j}"')

os.system("git push origin main")
