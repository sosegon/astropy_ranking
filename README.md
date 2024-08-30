**Introduction**

This repository contains the resources for the categorization of contributors of the [Astropy project](https://github.com/astropy/astropy). 

**Content**

- [astropy_astropy_bus_factor.json](./astropy_astropy_bus_factor.json): Contains the data generated from running the [Bus Factor Explorer tool](https://github.com/JetBrains-Research/bus-factor-explorer) over the Astropy repository.
- [astropy.mailmap](./astropy.mailmap): List of mapped names of contributors of the Astropy project to their email addresses. It is taken from [here](https://github.com/astropy/astropy/blob/main/.mailmap).
- [index.py](./index.py): Script to procces the content of `astropy_astropy_bus_factor.json` and generate `astropy_authorship_table.csv`
- [env.yml](./env.yml): Configuration file to create the conda environment to run `index.py`
- [astropy_authorship_table.csv](./astropy_authorship_table.csv): Table with the contributors of the Astropy project and their level of authorship.
- [astropy_authorship_table.csv](./astropy_authorship_table.xlsx): Table with the categorization of the contributors based on their level of authorship.


