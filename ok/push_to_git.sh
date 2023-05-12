#!/bin/bash

# check if at least one file and commit message is provided
if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <file1> [<file2> ...] <commit message>"
  exit 1
fi

# add each file to git
for (( i=1; i<=$#-1; i++ )); do
  git add "${!i}"
done

# commit changes with provided message
commit_msg="${!#}"
git commit -m "$commit_msg"

#git push
