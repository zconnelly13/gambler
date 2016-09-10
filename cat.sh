#!/bin/bash
for _ in `seq 1 10`;
  do
    echo "cat" >> .cat
    git add .cat
    git commit -m "cat"
done
