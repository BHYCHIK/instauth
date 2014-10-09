import config

def get_auth_url():
    return 'https://api.instagram.com/oauth/authorize/?client_id={0}&redirect_uri={1}&response_type=code'.format(config.Config.client_id, config.Config.redirect_uri)


