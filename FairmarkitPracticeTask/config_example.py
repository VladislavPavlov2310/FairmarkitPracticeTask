def database_info(data):
    """
    Return secret information of your database.
    """
    information = {
        'USER': 'your_username',
        'PASSWORD': 'your_password'
    }
    return information.get(data)
