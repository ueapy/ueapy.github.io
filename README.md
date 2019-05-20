# UEA Python Users Group website

Built using [pelican](https://github.com/getpelican/pelican) static website generator.

## Requirements for building the website
### Packages
- ghp-import
- ipython
- markdown
- pelican
- python>=3.6

You can create a separate conda environment using the [environment.yml](environment.yml) file provided in this repo.
```bash
conda env create -f environment.yml
```

### Pelican plugins
As specified in [pelicanconf.py](https://github.com/ueapy/ueapy.github.io/blob/src/pelicanconf.py#L33) script, building this website also requires pelican plugins.
The relevant [repository](https://github.com/ueapy/pelican-plugins) should be cloned and placed in the parent directory (or the `PLUGIN_PATHS` variable in `pelicanconf.py` should be changed).


## How to make changes in the source content
* Any changes, like adding a notebook, should be made on the `src` branch, NOT on `master`!

* After making a change and commiting it to the `src` branch, you should switch to a conda environment that has all the packages mentioned above installed.
If you created the environment using the file in this repo, you can switch to it by typing 
```bash
conda activate ueapy_web
```
Also make sure the path to plugins is correct and you have it locally.

* Publish the website by typing
```bash
make github
```
This will parse markdown files and convert Jupyter Notebooks to HTML pages using a pelican plugin, and push the changes to the `master` branch of the repository, which GitHub will read and update the website shortly.


**Note again that all the development is usually done while being on the `src` branch**.

The only time you would need to switch to the `master` branch is when you don't have a new version of the website locally - for example if your collaborator made the changes. In this case you can do
```bash
git checkout master

git pull origin master  # download and merge changes

git checkout src  # switch back to src branch
```
