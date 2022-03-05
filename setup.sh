#! /bin/sh

pip install virtualenv

virtualenv cvenv

source cvenv/bin/activate

pip install -r requirements.txt
