# Remote repository
* Use fork on https://github.com/Jedi-University/jedi.bigdata.1

# Location repository

* Cloning this repository

```bazaar
git clone git@github.com:fifo2019/jedi.bigdata.1.git
cd jedi.bigdata.1
```

* Create folder pdudkov
```bazaar
mkdir pdudkov
touch ./pdudkov/.gitkeep
git add .
git commit -m "Create folder pdudkov"
git push -u origin main
```

* Add remote branch v1-8-stable
```bazaar
git remote add airflow git@github.com:apache/airflow.git
git fetch airflow v1-8-stable
git merge airflow/v1-8-stable --allow-unrelated-histories
Resolution of conflicts in files such as READMY.md and .gitignore
git add .
git commit -m "Add airflow"
```

* Change 10 files in main branch
```bazaar
Add by once fild in files such as 
    CHANGELOG.txt, 
    CONTRIBUTING.md, 
    DISCLAIMER, 
    LICENSE, 
    MANIFEST.in, 
    NOTICE, 
    README.md, 
    TODO.md, 
    UPDATING.md, 
    setup.py.
git add .
git commit -m "WIP: Testing working with git"
git push
```

* Create branch fix and filter commits form  Jul 16, 2017.

```bazaar
git checkout -b fix
git log --before="2017-06-17"
git reset --hard ca97ca752bad4b793c24d574a2f434bb561e84cd
git push -u origin fix
```

* Create file with description commands (SOLUTION.md)
```bazaar
nano SOLUTION.md
write commands info to this file
git add .
git commit -m "Create SOLUTION.md"
git push
```