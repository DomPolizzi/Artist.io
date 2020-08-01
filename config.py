'''
retireve the freakin tokens :
'''

#Mod
  curl --request POST \
  --url 'https://dev-56d3ctn7.auth0.com/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data grant_type=client_credentials \
  --data username=fj@mail.com \
  --data password=Monkey13 \
  --data audience=capper \
  --data client_id=hH9I9ZNG6XyMTl6CsdCAxht3fLnBLwvc \
  --data client_secret=Gf9hEVgMr39H-6LIyxcS2tpuWodd3U0K-BUNEX4VpCv5tZ3SHSNU1OEhCKO9-eUn

#artist
  curl --request POST \
  --url 'https://dev-56d3ctn7.auth0.com/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data grant_type=client_credentials \
  --data username=gg@mail.com \
  --data password=Monkey13 \
  --data audience=capper \
  --data client_id=hH9I9ZNG6XyMTl6CsdCAxht3fLnBLwvc \
  --data client_secret=Gf9hEVgMr39H-6LIyxcS2tpuWodd3U0K-BUNEX4VpCv5tZ3SHSNU1OEhCKO9-eUn
  # Token
  # : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVKNHZEUnhBakREWDhTZkxrei15VCJ9.eyJpc3MiOiJodHRwczovL2Rldi01NmQzY3RuNy5hdXRoMC5jb20vIiwic3ViIjoiaEg5STlaTkc2WHlNVGw2Q3NkQ0F4aHQzZkxuQkx3dmNAY2xpZW50cyIsImF1ZCI6ImNhcHBlciIsImlhdCI6MTU5NjI0NDExMiwiZXhwIjoxNTk2MzMwNTEyLCJhenAiOiJoSDlJOVpORzZYeU1UbDZDc2RDQXhodDNmTG5CTHd2YyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbXX0.SQMi3v4lfNDFmEGit_EGfHAzOTIvu-O_4tMrfHe53G_PpQ7RdZn2r1L7uYsXSAJuzF3Gt3CY84tmu2mhtB1D-v9-UJQPJEdv8Lb1xseApF7pLAzuXo9PWETbyyMw8cv1G2gN18T8SUIaoUmUuIdThb9QIGfFcVAlxGsZEh7EP2QQEnxmYuFDtNnlt5TT77SNwef4rBsmMGfcN77pDJuab6SSwD5t6LrAamSwDBIjZFOizBnQfqHoyaWGwoKyTj4pkgfxQ62GcGXmDMByoSUcX13GEzUPjxJpPT5AHVjtHiXfjQ7fwp68MqFReecCm9dM_u9OHO09CgUse7Vafk-JgQ