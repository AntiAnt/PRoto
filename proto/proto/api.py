from django.conf import settings

import datetime
import jwt

def create_jwt():
    payload = {
      # issued at time
      'iat': datetime.datetime.utcnow(),
      # JWT expiration time (10 minute maximum)
      'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
      # GitHub App's identifier
      'iss': settings.GITHUB_APP_ID
    }

    encoded_jwt = jwt.encode({'some': 'payload'}, settings.GITHUB_PRIVATE_KEY, algorithm='RS256')

    return encoded_jwt
