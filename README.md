# DjangoAprender
Aprendendo como funciona um projeto de Django
## Objetivos
- [x] criar páginas 


### Como utilizar o git para fazer atualizações no github

```
git add . 
git commit -m "coloque sua modificação aqui
git push
```


### Como receber novas atualizações do github?

```
git pull
```


### Rodar a aplicação em django?
Não se esqueça de estar no diretorio do arquivo manage.py 
```
python manage.py runserver
```

### Como criar tabelas no banco de dados?
Primeiro você vai ter que criar o objeto no arquivo models.py e depois, você realiza os seguintes comandos
```
python manage.py makemigrations
python manage.py migrate
```
O primeiro comando, o makemigrations, ele transforma a classe em uma migração para ser aplicada
O segundo comando, o migrate, ele aplica a migração no banco de dados.




