# Git Pair Trix

Git Pair Trix is a simple command line tool to generate your team [Pair Programming Matrix](https://blog.pivotal.io/labs/labs/pair-programming-matrix) back from a git repo.

It assumes you are using [pivotal git-pair script](https://github.com/pivotal/git_scripts#git-pair) to configure the git authors in your repo

## Usage (TO DO)

    $ gitpairtrix --since=2016-01-01 .

    ```
	         |aaronk
	alex     |63     |alex
	bruno    |0      |5      |bruno
	claudivan|0      |0      |0      |claudivan
	daniel   |93     |75     |8      |2      |daniel
	joshua   |16     |175    |0      |0      |99     |joshua
	marcondes|0      |1      |5      |3      |8      |1      |marcondes
	mauricio |5      |0      |0      |6      |6      |4      |41     |mauricio
	michael  |27     |72     |0      |0      |98     |17     |0      |0      |michael
	rodrigo  |15     |7      |3      |6      |9      |0      |20     |19     |1      |rodrigo
	thiago   |34     |8      |3      |13     |141    |53     |1      |0      |10     |1      |thiago
	vinicius |4      |2      |3      |14     |9      |0      |24     |12     |9      |21     |7      |vinicius
	solo     |80     |24     |1      |0      |32     |19     |20     |15     |75     |22     |79     |21     |solo
	other    |4      |0      |11     |0      |0      |5      |35     |21     |0      |21     |0      |6      |0      |other

	```


## Setup

### Environment/Dependencies

	- Python 2.7

### Initial Setup

    $ make

### Running tests

    $ make test