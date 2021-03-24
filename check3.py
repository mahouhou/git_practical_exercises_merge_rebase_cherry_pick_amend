#!/usr/bin/env python3

import subprocess

# Check top 3 commit message on feature_in_progress branch
command = subprocess.run(['git', 'log', 'feature_in_progress', '-n', '3', '--pretty=format:%s'], stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().lower().split("\n"))

assert result[0] == "extend feature in progress", "The top most commit on branch feature_in_progress does not have the commit message 'Merge branch 'Extend feature in progress'"
assert result[1] == "add feature in progress", "The second commit on branch feature_in_progress does not have the commit message 'Add feature in progress'"
assert result[2] == "merge branch 'feature1' into main", "The third commit on branch feature_in_progress does not have the commit message 'Merge branch 'feature1' into main'"

print ("Exercise successfully done")
