## How to create Virtual Enviorment

virtual envorment is used to sprate your work from global work and save from conflit .

1) python -m venv adeelenv
2) source adeelenv/Scripts/activate
3) deactivate
4) pip install package-name ( for singal package install)

* Sharing to other one for that run freeze command that list all the package in requirement.txt file so other simple run requiremnt.txt  file so other get the full code 

1) pip freeze > requirements.txt (before sharing)
2) pip install -r requirements.txt (other run this )
