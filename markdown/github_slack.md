# GitHub-Slack Integration
* Github can send notifications to Slack.
1. Install "Github app" in Slack
  + Requires workspace admin approval, may be difficult in university-wide workspaces.
  + Apply for Common Work Space (CWS) and install there.
  + In our case, we have Lab-level workspace. Ask your teacher.
2. Configure from Slack after installing Github app
  + Link with Github account
  + Configure app bot with `/github subscribe organization-name`
  + Example: Receive all commits: `/github subscribe organization-name commit:*`
3. Configure in Github authentication screen when it opens
