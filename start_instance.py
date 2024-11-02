from awscode import listInstances,startInstances

dev_filter = {'Name': 'tag:env', 'Values': ['dev']}

startInstances(listInstances(dev_filter))

