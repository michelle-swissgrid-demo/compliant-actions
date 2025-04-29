# compliant-actions

> Task context: Our software architects have advised us that some of the 3rd party GitHub actions used in our GitHub organization are not secure. Up to know, we have allowed users to download actions from marketplace. This week we have detected that one of the actions called buggy-actions/expose-passwords contain very serious vulnerability.

## Implementation

> find out which repositories have been using buggy-actions/expose-passwords action (we have over 500 repostiories)
A script that goes over all the repositories of the organization. It searches over the workflows used in the repositories and identifies where '.github/workflows/buggy-actions' have been used. The organization, the action, and the location for the results can be specified by the user. 

## Proposal for Solution/Prevention
> propose a solution to prevent such a situation in future (there are many actions in the marketplace that could have such vulnerability).
1. It is possible to specify, organization wide, a list of actions that can be used. This prevents particular (unsafe) actions being used in workflows. This can be done through Organization > Settings > Actions > Policies
2. More generally, we can enable `allstar` on the whole organization. They are a generic tool that allows us to detect the use of actions that may have been compromised. 
https://github.com/ossf/allstar?tab=readme-ov-file#what-is-allstar


## Communication
> Communication: create a communication with the users
