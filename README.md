# kartplattformen_common
Common files to run kartplattformen API applications in same OS process
# Installation
## Create file structure
├── manage.py\: If needed copy manage.py here from manage.py in this repo\
├── kartplattformen_common: main folder connected to OS process through for example wsgi\
│   ├── wsgi.py\
│   ├── settings.py\
│   ├── urls.py\
│   └── secrets_env.py\: Copy secrets_env.py.template
└── other repos\
## Prepare installation with easy way of go back
- Clone repo kartplattformen_common in main folder
- Configure settings for enviroment\
Copy secrets_env.py.template to secrets_env.py\
Set settings in secrets_env.py\
- Make link to support config:\
  ln -snf kartplattformen_common sagendatabas\
- Backup old configuration if needed later:\
  mv sagendatabas sagendatabas_before_kartplattformen_common\
- Rename applications/repos to names following python standard:\
  mv Sagenkarta-Rest-API sagenkarta_rest_api\
  mv Sagendatabas-ES-API sagendatabas_es_api\
  mv Sagendatabas-ES-API-advanced sagendatabas_es_api-advanced\
