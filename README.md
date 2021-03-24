# git_practical_exercises_merge_rebase_cherry_pick_amend
This repository is the base for a practical git exercise.

This exercise is a beginner one and it is focusing on practising rebase, merge, cherry-pick and amend.

## Exercise:

There are four branch in the repository: main, feature1, extension_of_feature_1 and feature_in_progress. You will work with these branches

1. On the branch extension_of_feature_1 there's a commit with the message "Add extension for feature1". This commit shall be cherry-picked on the top of branch feature1.
2. Merge the branch "feature1" into the main branch. Keep the default commit message for the merge commit.
3. Rebase the branch feature_in_progress on the top of the main branch
4. Now if you open the file "feature_in_progress.txt" an "e" is missing in the end of the second line, it shall be "Second line" instead of "Second lin", fix it and amend this change to the top most commit.

## Hints:

The exercise is built up in the way, that there shouldn't be any conflict between the files if you are doing everything in the right order and way.

You can run the right check file after each of the subtask to check if your solution is fine. (check1.py after the first subtask etc.)
