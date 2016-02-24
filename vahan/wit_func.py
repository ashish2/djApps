import wit
wit_access_token = 'ACCESS_TOKEN'
wit.init()
response = wit.voice_query_auto(wit_access_token)
print("Response: {}".format(response) )
wit.close()



