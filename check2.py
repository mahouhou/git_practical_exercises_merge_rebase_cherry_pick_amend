#!/usr/bin/env python3

import subprocess

# Check top 5 commit message on main branch
command = subprocess.run(['git', 'log', 'main', '-n', '5', '--pretty=format:%s'], stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().lower().split("\n"))

assert result[0] == "merge branch 'feature1' into main", "The top most commit on branch main does not have the commit message 'Merge branch 'feature1' into main'"
assert result[1] == "add extension for feature1", "The second commit on branch main does not have the commit message 'Add extension for feature1'"
assert result[2] == "extend feature1", "The third commit on branch main does not have the commit message 'Extend feature1'"
assert result[3] == "add feature1", "The fourth commit on branch main does not have the commit message 'Add feature1'"
assert result[4] == "add one more line to file_on_master_branch.txt", "The fifth commit on branch main does not have the commit message 'Add one more line to file_on_master_branch.txt'"


print ("Exercise successfully done")
