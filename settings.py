from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [

    # main Apps
    # ------------------------------------------------------------------------------------------------------------------
    # {
    #     'name': 'PSM_Streamlined',
    #     'display_name': "Preference Survey Module, Streamlined Version (Global Preference Survey)",
    #     'num_demo_participants': 1,
    #     'app_sequence': [
    #         'risk_qual', 'risk_staircase', 'willingness_to_act', 'patience_staircase',
    #         'self_assessment', 'dictator_hypothetical', 'pos_reciprocity'
    #          ],
    # },
    # {
    #     'name': 'PSM_Laboratory',
    #     'display_name': "Preference Survey Module, Laboratory Version",
    #     'num_demo_participants': 1,
    #     'app_sequence': [
    #         'risk_qual', 'risk_mpl', 'willingness_to_act', 'patience_mpl',
    #         'trust_hypothetical', 'self_assessment', 'dictator_hypothetical',
    #         'pos_reciprocity', 'ultimatum_hypothetical'
    #     ],
    # },

    # single modules
    # ------------------------------------------------------------------------------------------------------------------
    # {
    #     'name': 'willingness_to_act',
    #     'display_name': "Module 1: Patience Qual + Neg Recipr Qual 1 + Neg Recipr Qual 2 + Altruism Qual",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['willingness_to_act'],
    # },
    # {
    #     'name': 'risk_qual',
    #     'display_name': "Module 2: Risk Aversion Qual",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['risk_qual'],
    # },
    # {
    #     'name': 'self_assessment',
    #     'display_name': "Module 3: Pos Recipr Qual + Neg Recipr Qual 3 + Trust Qual",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['self_assessment'],
    # },
    # {
    #     'name': 'risk_mpl',
    #     'display_name': "Module 4/A: Risk Aversion Quant, Multiple Price List",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['risk_mpl'],
    # },
    # {
    #     'name': 'risk_staircase',
    #     'display_name': "Module 4/B: Risk Aversion Quant, Staircase Method",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['risk_staircase'],
    # },
    # {
    #     'name': 'patience_mpl',
    #     'display_name': "Module 5/A: Patience Quant (Today vs 12 Months), Multiple Price List",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['patience_mpl'],
    # },
    {
        'name': 'Project_BEMO_Q',
        'display_name': "Project BEMO Question",
        'num_demo_participants': 1,
        'app_sequence': ['Project_BEMO_Q'],
    },
    {
        'name': 'Project_BEMO_MAIN',
        'display_name': "Project BEMO",
        'num_demo_participants': 1,
        'app_sequence': ['Project_BEMO_MAIN'],
    },

    {
        'name': 'Project_BEMO_QV',
        'display_name': "Project BEMO Question Visualization",
        'num_demo_participants': 1,
        'app_sequence': ['Project_BEMO_QV'],
    },
    # {
    #     'name': 'present_bias_staircase',
    #     'display_name': "Module 5/C: Patience Quant (12 Months vs 24 Months), Staircase Method",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['present_bias_staircase'],
    # },
    # {
    #     'name': 'pos_reciprocity',
    #     'display_name': "Module 6: Positive Recipr Quant 1",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['pos_reciprocity'],
    # },
    # {
    #     'name': 'dictator_hypothetical',
    #     'display_name': "Module 7: Altruism Quant (Dictator Game)",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['dictator_hypothetical'],
    # },
    # {
    #     'name': 'trust_hypothetical',
    #     'display_name': "Module 8: Pos Recipr Quant 2 + Trust Quant (Trust Game)",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['trust_hypothetical'],
    # },
    # {
    #     'name': 'ultimatum_hypothetical',
    #     'display_name': "Module 9: Neg Recipr Quant (Ultimatum Game)",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['ultimatum_hypothetical'],
    # },
]

# settings.py
STATIC_URL = '/static/'

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
dict(
    name='Prolific_1',
    display_name='Prolific_1',
    use_secure_urls=False
),
dict(
    name='Prolific_2',
    display_name='Prolific_2',
    use_secure_urls=False
),
dict(
    name='Prolific_3',
    display_name='Prolific_3',
    use_secure_urls=False
),
dict(
    name='SONA_1',
    display_name='SONA_1',
    use_secure_urls=False
),
dict(
    name='SONA_2',
    display_name='SONA_2',
    use_secure_urls=False
),
dict(
    name='SONA_3',
    display_name='SONA_3',
    use_secure_urls=False
),
dict(
    name='BELSS',
    display_name='BELSS',
    participant_label_file='_rooms/belss.txt',
    use_secure_urls=True
),
dict(
    name='30463',
    display_name='Intro to Cognitive Science',
    use_secure_urls=False
),
dict(
    name='live_demo',
    display_name='Room for Live Demo (No Participant Labels)',
)
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '$89h(ho1ce&^#rqd$vt+us($26)$-6&e)l*86u_rb@wwb)l39p'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
