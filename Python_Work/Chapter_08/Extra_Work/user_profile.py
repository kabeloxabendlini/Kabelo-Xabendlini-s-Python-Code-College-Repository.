def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Building my profile with three additional key-value pairs
my_profile = build_profile('Kabelo', 'Xabendlini',
                           location='South Africa',
                           profession='Software Developer',
                           hobby='Photography')

print(my_profile)