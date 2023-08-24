import configparser

config = configparser.RawConfigParser()
config.read(r"D:\Ailaysa_automation\trail1st\configurations\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def get_user_email():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_account_name():
        account_name = config.get('profile info', 'account_name')
        return account_name

    @staticmethod
    def get_org_name():
        org_name = config.get('profile info', 'account_name')
        return org_name

    @staticmethod
    def get_phone_num():
        phone_num = config.get('profile info', 'account_name')
        return phone_num

    @staticmethod
    def get_linkedin_id():
        linkedin_id = config.get('profile info', 'account_name')
        return linkedin_id

    @staticmethod
    def get_website():
        website = config.get('profile info', 'account_name')
        return website

    @staticmethod
    def get_project_name():
        txt_project_name = config.get('word project creation','txt_project_name')
        return txt_project_name

    @staticmethod
    def get_file_path():
        file_path = config.get('word project creation','file_path')
        return file_path




