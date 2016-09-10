Gambler
=======

An example repository for demonstrating the power of git-bisect.

### How To
1. Recognize problem
2. Write regression test
3. `git bisect start` 
4. `git bisect bad`
5. `git bisect good $(git rev-list HEAD | tail -n 1)`
6. `git bisect run nosetests`
7. `git bisect reset`
