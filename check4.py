#!/usr/bin/env python3

import subprocess

# Check top 3 commit message on feature_in_progress branch
command = subprocess.run(['git', 'log', 'feature_in_progress', '-n', '3', '--pretty=format:%s'], stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().lower().split("\n"))

assert result[0] == "extend feature in progress", "The top most commit on branch feature_in_progress does not have the commit message 'Merge branch 'Extend feature in progress'"
assert result[1] == "add feature in progress", "The second commit on branch feature_in_progress does not have the commit message 'Add feature in progress'"
assert result[2] == "merge branch 'feature1' into main", "The third commit on branch feature_in_progress does not have the commit message 'Merge branch 'feature1' into main'"

# Check content of feature_in_progress.txt
# Check the content of the file
command = subprocess.run(['git', 'show', 'feature_in_progress:feature_in_progress.txt'], stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().split("\n"))

assert(len(result) == 2), "The number of lines in feature_in_progress.txt shall be 2 at this point, but currently this condition is not satisfied"

assert result[1] == "Second line", "The last line of feature_in_progress.txt shall be Second line, but currently this condition is not satisfied"


print ("Exercise successfully done")
