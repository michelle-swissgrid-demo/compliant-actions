# compliant-actions

> Task context: Our software architects have advised us that some of the 3rd party GitHub actions used in our GitHub organization are not secure. Up to know, we have allowed users to download actions from marketplace. This week we have detected that one of the actions called buggy-actions/expose-passwords contain very serious vulnerability.

## Implementation

> find out which repositories have been using buggy-actions/expose-passwords action (we have over 500 repostiories)

The script `detect_actions.py` goes over all the repositories of a specified organization. It searches over the workflows used in the repositories and identifies where a specific action has been used. The organization, the action, and the location where the results should be written can be specified by the user as arguments to the script. It can be run by exporting the `GITHUB_TOKEN` to the environment and then running `python detect_actions.py`.

## Proposal for Solution/Prevention
> propose a solution to prevent such a situation in future (there are many actions in the marketplace that could have such vulnerability).
1. It is possible to specify, organization wide, a list of actions that can be used. This prevents particular (unsafe) actions being used in workflows. This can be done through Organization > Settings > Actions > Policies. By limiting the workflows allowed, admins can then check the actions in the marketplace for vulnerabilities before they are deployed in workflows in the organization.
2. In addition, we can enable `allstar` on the whole organization. They are a generic tool that allows us to detect security vulnerabilities in the overall organization. However, it is not as straightforward as the above solution and it does more than configure a list of allowed actions. 

## Communication
> Communication: create a communication with the users

The communication for this will follow a similar structure as for announcing the mandatory community health files. There should be a clear internal message explaining that only certain actions are allowed since many in the market place contain vulnerabilities that can undermine the security of the organization. 


### Internal Message
The internal message below can be formatted as an email or as an internal confluence article which is sent out to inform people of the change. A list of actions that will be allowed and not allowed will be pubicly documented so that users can consult it when building their workflows. 
```md
# [Action Required] New GitHub Repository Standards for Community Health Files

Dear all,
To improve the security our GitHub repositories, we’re going to allow only internal and some external actions to be used in the workflows of the repositories. Only actions that have been audited by the admin team will be allowed to be added to workflows to ensure we do not introduce external vulnerabilities into our repositories. 

## What’s Changing?

Starting [specific date], every repository will only be allowed to use approved actions. Some which will no longer be permitted are below:

1. buggy/buggy-actions

## How is this enforced?

The restriction will placed organization wide and will be enacted on [date]. Before this, please consult the list of actions that are no longer allowed to replace them and find the list of permitted actions here [list]. 

Thanks for helping make our engineering practices and organisation more sustainable!  
– The Engineering Team
```