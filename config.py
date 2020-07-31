'''
retireve the freakin tokens :
'''
  curl --request POST \
  --url 'https://dev-56d3ctn7.auth0.com/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data grant_type=client_credentials \
  --data username=fj@mail.com \
  --data password=Monkey12 \
  --data audience=capper \
  --data client_id=hH9I9ZNG6XyMTl6CsdCAxht3fLnBLwvc \
  --data client_secret=Gf9hEVgMr39H-6LIyxcS2tpuWodd3U0K-BUNEX4VpCv5tZ3SHSNU1OEhCKO9-eUn