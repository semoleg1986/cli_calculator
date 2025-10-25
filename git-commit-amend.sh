#!/bin/sh

if [ -z "$1" ]; then
  commit_message="Update ($(LANG=en_EN date +'%a, %b %d, %Y %r'))"
else
  commit_message="$1 ($(LANG=en_EN date +'%a, %b %d, %Y %r'))"
fi

echo "Сообщение коммита: $commit_message"

git commit --amend -m "$commit_message"

git push --force