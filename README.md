# Aprendiendo-Python
Fragmentos de código que abarcan los temas fundamentales del lenguaje de programación Python abordados desde el Laboratorio de Informatica y Ciencia de la informacion EIB. 

Ejemplos desde los cuales se pueden ampliar conocimientos sobre variables, estructuras, objetos, metodos, funciones. etc.

Todas las pruebas de fragmentos de codigo python se realizaron en un equipo con ubuntu 18.04, desde el interprete de comandos Bash; los interactive python notebooks se corrieron en un entorno basico de Jupyter.

## antes de empezar con los temas:
## tener un entorno de trabajo:sistema operativo en una maquina virtual.
see this tutorial for ''HOW INSTALL UBUNTU IN VIRTUAL MACHINE IN WINDOWS'' 
se this tutorial for ''INTRO COMMAND LINE INTERFACE IN LINUX''  

## instalar python y acceder al modo interactivo(python cli)
Install python in Ubuntu linux machine(OS-Base-Debian)".here there are some instructions for done that.   

if you are using ubuntu 16.04 launch terminal an issue:
    
    $sudo apt-get update
    $sudo apt-get install python3.6
    
if you are using another version of ubuntu(e.g. the latest LTS release) or you want to use a more current python, we recommend to use deadsnakes PPA
to install python 3.8:
    
    $sudo apt-get install software.properties-common
    $sudo add-apt-repository ppa:deadsnakes/ppa
    $sudo apt-get update
    $sudo apt-get install python3.8
    
at this point you may have  system python2.7 avaible as well. issue python on terminal:
    
    $python
this launch interactive python 2.7 CLI. insert 

    >>>exit()
this allow us exit from interactive mode.

    $python3

this this launch interactive python 3.8 CLI.
   
    >>>help
this insert us in mode python docs-guides

## instalar notebook y lanzar jupyter notebook

    $pip3 install notebook
this install jupyter notebook in your machine. notebooks allow us make interactive python notebooks.to do thar, issue:
    
    $jupyter notebook 
this launch command jupyter notbook environment.

## Learning Topics

python programming language

python scripts

python reserve keywords

computer programming logic

variables

data structures

logic structures

functions

built-in functions

objects

classes(or blue-prints for create objects)

class variables - instance variables

class methods

inheritance(from a simple base class)

standar library

    os
    sys
    json
    requests
    
pip install 

Install third-party python packages
  from python ecosistem developers:  
    
    numpy
    pandas
    sckitlearn
    nltk
    spacy
    gensym
    textblob

Install software from github 
    
    somedatascience project
