NOID-mint Python Package

## Installation
```
create directory at command line
setup virtual environment: `python3 -m venv ENV`
activate the environment: `source ENV/bin/activate`

pip install noid-mint
git clone https://github.com/aprigge/NOID-mint.git

in command line change directory to new folder: 'cd NOID-mint'
in command line 'python3 setup.py install'
in command line install requirements 'pip3 install -r requirements.txt'

```

## Usage
* Generate noid
```
format .yml file to include appropriate ark shoulder which shoulder be in the same directory as the noid_ark.py file
you can generate a single noid in the command line using noid -f [name of file].yml


configure noid_ark.py with the four inputs the function takes:
1. the file path to the csv input file
2. the configured yml file which sets up the specifics for the ark
3. the parent ark
4. the name of the output file

run noid_ark.py in command line
```

## Testing
```
nosetests
```

## The NOID-Mint was forked from the following authors
* Virginia Tech Libraries - Digital Libraries Development developers
	* [Yinlin Chen](https://github.com/yinlinchen)
	* [Tingting Jiang](https://github.com/tingtingjh)
	* [Lee Hunter](https://github.com/whunter)

See also the list of [contributors](https://github.com/VTUL/NOID-mint/graphs/contributors) who participated in this project.

## Thanks
This tool was heavily influenced from [pynoid](https://github.com/no-reply/pynoid)
