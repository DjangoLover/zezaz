#!/bin/sh

echo "Content-type: text/html"
alias my_python="/home/zezaz_dash/.pythonbrew/pythons/Python-2.7.5/bin/python"
alias my_pip="/home/zezaz_dash/.pythonbrew/pythons/Python-2.7.5/bin/pip"

cd /home/zezaz_dash/zezaz.amazingworks.com.br/zezaz
git pull

#my_python manage.py syncdb --noinput
my_python manage.py collectstatic --noinput
#my_pip install -r requirements.txt

pkill python
