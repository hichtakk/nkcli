# nkcli
CLI client for netkeiba (https://www.netkeiba.com)

## Prerequisites
* Python 3.X
* Poetry (https://python-poetry.org/)
* Pyenv (https://github.com/pyenv/pyenv)

## Install
```
$ git clone https://github.com/hichtakk/nkcli.git
$ cd nkcli
$ poetry install
```

## Usage
You can run command inside python virtualenv.  
To activate virtualenv, execute command below. 

```
$ poetry shell
```

### Get horse data
Use Netkeiba horse id as `$HORSE_ID`.
```
$ nkcil info ${HORSE_ID}
```
