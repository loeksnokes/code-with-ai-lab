# run from repo root
git show :2:README.md > README.ours.md
git show :3:README.md > README.theirs.md

git show :2:exercises/01-intro-python/README.md > 01-README.ours.md
git show :3:exercises/01-intro-python/README.md > 01-README.theirs.md

git show :2:requirements.txt > requirements.ours.txt
git show :3:requirements.txt > requirements.theirs.txt