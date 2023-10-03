import os
def get_key():
    env_var = os.environ
    env_var['YT_API_KEY'] = "AIzaSyAWvYvv5cT7KYlK-WtJSVA0CEfw_D02ZkE"
    return os.getenv('YT_API_KEY', 'API_KEY_NOT_FOUND')