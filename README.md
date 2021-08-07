# citation-context

This repository contains exploratory analysis of Influence-IR S2ORC corpus. 

1. [Date of Pulication Distribution](examples/1.0_hp_dist.ipynb) notebook contains aggregated data & figure showing text presence across years
2. [Citation context](examples/2.0_hp_citation-context.ipynb) notebook is about graph representation of inbound & outbound citations


## Usage

To use or contribute to this repository, first checkout the code. 
Then create a new virtual environment for python:

```console
$ git clone git@github.com:hp0404/citation-context.git
$ cd citation-context
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Then download S2ORC corpus (`metadata.jsonl` and `texts.jsonl` files) from GDrive and put them into [data/raw](data/raw) folder.

To start notebooks, run in the terminal:
```console
$ jupyter lab
```
