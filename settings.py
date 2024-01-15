from os import environ

SESSION_CONFIGS = [
    dict(
        name='Project_BEMO_Q',
        app_sequence=['Project_BEMO_Q'],
        num_demo_participants=1,
    ),
    dict(
        name='Project_BEMO_QV',
        app_sequence=['Project_BEMO_QV'],
        num_demo_participants=1,
    ),
]

ROOMS = [
    dict(
        name='Project_BEMO',
        display_name='Project_BEMO',
        participant_label_file='_rooms/batch1.txt',
        use_secure_urls=False
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '8896389584933'

"""
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}: 
    DEBUG = True 
else: 
    DEBUG = False
"""