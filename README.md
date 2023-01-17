# kartplattformen_common
Common files to run kartplattformen API applications in same OS process
# Installation
- main folder connected to OS process through for example wsgi
  - manage.py
  - kartplattformen_common
  - other repos
## Prepare installation with easy way of go back
- clone repo
- Make link to support config:\
  ln -snf kartplattformen_common sagendatabas\
- Backup old configuration if needed later:\
  mv sagendatabas sagendatabas_before_kartplattformen_common\
- Rename applications/repos to names following python standard:\
  mv Sagenkarta-Rest-API sagenkarta_rest_api\
  mv Sagendatabas-ES-API sagendatabas_es_api\
  mv Sagendatabas-ES-API-advanced sagendatabas_es_api-advanced\
