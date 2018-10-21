# EigenFaces
The following is a Demonstration of Principal Component Analysis, dimensional reduction. The following has been developed in python2.7 however can be run on machines which use Python3, by using a python virtual environment

This project is based on the following paper:- 
[Face recognition using eigenfaces by Matthew A. Turk and Alex P. Pentland](https://ieeexplore.ieee.org/document/139758)

Dataset courtesy - http://vis-www.cs.umass.edu/lfw/

### Development
The following can be best developed using `pipenv`. If you do not have `pipen`, simply run the following command (using pip3 or pip based on your version of Python)
```
pip install pipenv
```

Then clone the following repository
```
git clone https://github.com/sahitpj/EigenFaces
```

Then change the following working directory and then run the following commands

```
pipenv install --dev
```

This should have installed all the necessary dependencies for the project. If the pipenv shell doesn't start running after this, simply run the following command

```
pipenv shell
```

Now in order to run the main program run the following command

```
pipenv run python main.py
```

Make sure to use python and not python3 because the following pip environment is of Python2.7. Any changes which are to be made, are to documented and make sure to lock dependencies if dependencies have been changed during the process.

```
pipenv lock
```

The detailed report about this, can be viewd [here](REPORT.md)
or can be found at https://sahitpj.github.io/EigenFaces

If you like this repository and find it useful, please consider &#9733; starring it :)