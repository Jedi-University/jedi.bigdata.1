git checkout -b airflow
git remote add https://github.com/apache/airflow.git

#here was a kind of mental eclipse and i didnt log my commands

git checkout -b fix
git revert 95f5b80542fc6259f333a426c13f1652fa5631b4
git revert ca97ca752bad4b793c24d574a2f434bb561e84cd

git remote rm airflow
git branch -d airflow
git checkout main && git push --force
git push --set-upstream origin fix
#couldn't create pull request, so pull initial commit 
git remote add ancestor https://github.com/Jedi-University/jedi.bigdata.1.git
git checkout -b ancestor
git pull ancestor main --allow-unrelated-histories
git checkout main && git merge ancestor && git push
git checkout fix  && git merge ancestor && git push