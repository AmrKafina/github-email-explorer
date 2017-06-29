from github_email_explorer import github_email

github_api_auth = ('01e205f4384983c0c41e', '73761b234bf6ed01596137ec634ee616c1b4923c')
ges = github_email.collect_email_info('parse-community', 'parse-server', ['star', 'watch'], 0, 1, github_api_auth=github_api_auth)

for ge in ges:
    if ge.email is not None:
        print "%s, %s" % (ge.name, ge.email)

# With Authentication
# github_api_auth = ('<your_client_id>', '<your_client_secret>')
# ges = github_email.collect_email_info('yuecen', 'github-email-explorer', ['star', 'watch'],
#                                        github_api_auth=github_api_auth)
