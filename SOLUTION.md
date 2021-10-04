# Solution steps

git clone https://github.com/kopagm/jedi.bigdata.1

cd jedi.bigdata.1

mkdir akopeykin

cd akopeykin

touch .gitkeep

git add .gitkeep

git commit -m "Init commit"

cd ..

git remote add airflow_remote https://github.com/apache/airflow.git

git fetch airflow_remote v1-8-stable --no-tags

git checkout -b v1-8-stable airflow_remote/v1-8-stable

git checkout main

git merge v1-8-stable -m "Add airflow" --allow-unrelated-histories

#nano README.md 
#nano .gitignore

git add README.md .gitignore

git commit -m "Add airflow"

subl ./airflow/example_dags/example_latest_only.py \
./airflow/example_dags/example_python_operator.py \
./airflow/example_dags/test_utils.py \
./airflow/example_dags/example_bash_operator.py \
./airflow/example_dags/example_short_circuit_operator.py \
./airflow/example_dags/example_branch_operator.py \
./airflow/example_dags/example_docker_operator.py \
./airflow/example_dags/tutorial.py \
./airflow/example_dags/docker_copy_data.py \
./airflow/example_dags/example_passing_params_via_test_command.py

git commit -am "WIP: Testing working with git"

git checkout -b fix v1-8-stable

git log --pretty=format:"%h %ad | %s%d" --date=short

git rebase -i fix~7 # (drop ca97ca75 2017-06-16)

git checkout main

git push

git checkout fix

git push origin fix