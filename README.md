# Eventex

Sistema de eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/paulopinda/eventex.svg?branch=master)](https://travis-ci.org/paulopinda/eventex)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/88b3ce008eb84c3f89c6a88bfb31d517)](https://www.codacy.com/app/paulo-pinda/eventex)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/ac47d2ebea5b4156b8221946d240e9a2/badge.svg)](https://www.quantifiedcode.com/app/project/ac47d2ebea5b4156b8221946d240e9a2)
[![Code Climate](https://codeclimate.com/github/paulopinda/eventex/badges/gpa.svg)](https://codeclimate.com/github/paulopinda/eventex)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5. 
3. Ative virtualenv.
4. Instale as depedências.
5. Configure a instancia com o .env. 
6. Execute os testes.

```console
git clone git@github.com:paulopinda/eventex.git wttd 
cd wttd
python -m venv .wttd 
source .wttd/bin/activate
pip install -r requirements-dev.txt 
cp contrib/env-sample .env
python manage.py test 
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie configurações para o heroku.
3. Define uma SECRET_KEY segura na instância.
4. Defina DEBUG=False.
5. Configure o serviço de e-mail.
6. Envie o código para o heroku.

```console 
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False 
# Configura o e-mail.
git push heroku master --force
```
