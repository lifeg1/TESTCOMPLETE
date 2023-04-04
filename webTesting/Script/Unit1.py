def Test1():
  Browsers.Item[btChrome].Navigate("https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html")
  browser = Aliases.browser
  page=browser.Page("*") #expecting to be this page *-  any page
  #links=page.NativeWebObject.Find()
  
  links=page.contentDocument.links
  for i in range(links.length):
    Log.Message(links.item(i).InnerHtml)
  
  
  