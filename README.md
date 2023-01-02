
# Backend Service Provider(BSP)

This project makes service creation easier.

# Quick install guide

Being based on Python and Django, BSP requires both of them.

**1- Check If Python Is Available:**

You can verify that Python is installed by typing `python` from your shell.
you should see something like:

```
Python 3.x.y
[GCC 4.x] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
**2- Check If PIP Is Already Installed**

To check if `PIP` is already installed on Windows, we should open the command line again, type `pip`, and press Enter.

If PIP is installed, we will receive a long notification explaining the program usage, all the available commands and options. Otherwise, if `PIP` is not installed, the output will be:

```
 'pip' is not recognized as an internal or external command, operable program or batch file. 
```

**3- Install BSP**
clone this repository on your system, then open the command line again and open
repository directory, then type

```
pip intall -r requirements.txt
```

**4- create database**

This project use sqlite DB as default database. So open command line and type:

```
python manage.py makemigrations
```

then type:
```
python manage.py migrate
```

**5- Running Tests**





