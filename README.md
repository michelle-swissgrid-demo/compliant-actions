# compliant-actions

## Script for finding usage of action
- a script that goes over all the repositories of the organization. looks over the workflows used in the repositories and identifies where '.github/workflows/buggy-actions' have been used
- possible in both python and bash (not sure which one is better)

## Preventing using such actions in the future

- in the settings of the organization, it is possible to specify which workflows are allowed to be used
- moreover, we can also write a workflow that routinely scans all workflows which checks whether there are vulnerabilities or other tools that can find issues

https://github.com/ossf/allstar?tab=readme-ov-file#what-is-allstar