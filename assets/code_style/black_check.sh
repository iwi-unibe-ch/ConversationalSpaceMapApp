printf 'Install black'
python -m pip install black --upgrade

printf 'Format Package: ... '
python -m black ./../../conversationalspacemapapp --diff

printf 'Format tests: ... '
python -m black ./../../tests --diff
