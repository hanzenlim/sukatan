#!/bin/sh
git fetch
if [ $(git rev-parse HEAD) = $(git rev-parse @{u}) ]
then
    echo "The same"
else
   git fetch
   git pull
   echo "Git pull"
fi
