git init
git config user.email "virtualfabio@gmail.com"
git config user.name "Fabio FS"
git add .
git status
git commit -m "Projeto para deploy"
git branch -M main
git remote add origin https://github.com/virtualfabio/python-fastapi.git
git push -u origin main

# mkvirtualenv vsecao07 -p python3.10

# pip install -r requirements.txt


#acesso ao banco 
http://127.0.0.1/pgadmin4/browser/

Gerando o Token Local:
#  python3.10
Python 3.10.15 (main, Sep  7 2024, 18:35:33) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import secrets
>>> token: str = secrets.token_urlsafe(32)
>>> token
'ciIqKZxxxxxxxxxxxxxxxxx'
///Copia o token gerado para colocar no configs.py........
#
