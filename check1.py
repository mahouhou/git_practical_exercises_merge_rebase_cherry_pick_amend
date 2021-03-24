#!/usr/bin/env python3

import subprocess


# Check top 4 commit message on feature1 branch
command = subprocess.run(['git', 'log', 'feature1', '-n', '4', '--pretty=format:%s'], stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().lower().split("\n"))

assert result[0] == "add extension for feature1", "The top most commit on branch feature1 does not have the commit message 'Add extension for feature1'"
assert result[1] == "extend feature1", "The second commit on branch feature1 does not have the commit message 'Extend feature1'"
assert result[2] == "add feature1", "The third commit on branch feature1 does not have the commit message 'Add feature1'"
assert result[3] == "add file_on_master_branch.txt", "The fourth commit on branch feature1 does not have the commit message 'Add file_on_master_branch.txt'"


print ("Exercise successfully done")
