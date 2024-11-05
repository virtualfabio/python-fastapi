git init
git config user.email "virtualfabio@gmail.com"
git config user.name "Fabio FS"

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
'ciIqKZgIYekxZq9FMhNzVTrZEyms8vse73T7hmqYJ2M'
///Copia o token gerado para colocar no configs.py........
#

# 

# 