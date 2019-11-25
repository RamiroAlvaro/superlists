Provisionamento de um novo site
===============================

## Pacotes necessários:

* nginx
* Python 3.6
* virtualenv + pip
* Git

Por exemplo, no Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python36 python3.6-venv

## Cofig do Nginx Virtual Host

* veja nginx.template.conf
* substitua SITENAME, por exemplo, staging.my-sitename.com

## Serviço Systemd

* veja gunicorn-systemd.template.service
* substitua SITENAME, por exemplo, staging.my-sitename.com

## Estructura de pastas:

Suponha que temos uma conta de usuário em /home/username

/home/username
└── sites
    ├── SITENAME_1
    │    ├── database
    │    ├── source
    │    ├── static
    │    └── virtualenv
    └── SITENAME_2
         ├── database
         ├── source
         ├── static
         └── virtualenv