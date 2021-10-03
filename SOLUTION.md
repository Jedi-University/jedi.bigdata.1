* Создаем форк и клонируем свой репозиторий

```bash
git clone git@github.com:AlexeyZavarzin/jedi.bigdata.1.git
cd jedi.bigdata.1
```

* Создаем папку по шаблону и делаем `Initial commit`

```bash
mkdir azavarzin
cd azavarzin
touch .gitkeep
git add -A
git commit -m "Initial commit"
```

* Подключаемся к удаленному репозиторию `apache airflow` и забираем ветку `v1-8-stable` и сливаем ее с основной

```bash
git remote add airflow git@github.com:apache/airflow.git
git fetch airflow v1-8-stable
git merge v1-8-stable --allow-unrelated-histories
```

* Решаем конфликты (через `vim`) и делаем коммит

```bash
git add -A
git commit -m "Add airflow"
```

* Вносим в ветку `v1-8-stable` изменения и делаем коммит

```bash
git add -A
git commit -m "WIP: Testing working with git"
```

* Создаем еще одну ветку и удаляем из нее коммиты

```bash
git checkout main
git checkout -b fix
git log
git revert ca97ca75
```

* Создаем файл со списком команд и коммитим его в `main`

```bash
git checkout main
touch SOLUTION.md
git add -A
git commit -m "Adding a solution (SOLUTION.md)"
```

* Пушим локальные ветки на удаленный репозиторий

```bash
git push origin --all
```



