:: выгружает из базы тестов fixtures

set DJANGO_SETTINGS_MODULE=cashoff.settings.autotests

python manage.py dumpdata finances.Currency --indent=2 > website/fixtures/initial_db.json
python manage.py dumpdata ^
auth.User ^
website.UserProfile ^
website.UserSettings ^
finances.Account ^
finances.Transaction ^
sysmanager.UserInstitutionProfile --indent=2 > website/fixtures/users.json
python manage.py dumpdata finances.TransactionCategory --indent=2 > website/fixtures/categories.json
python manage.py dumpdata finances.Institution --indent=2 > website/fixtures/fi.json