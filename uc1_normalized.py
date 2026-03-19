def calculate_average_user_age_from_database(database_user_records_list):
    a = 0
    b = 0
    for c in database_user_records_list:
        if c.get('is_account_active', False):
            d = c.get('user_age_in_years', 0)
            if d > 0:
                a += d
                b += 1
    if b > 0:
        return a / b
    else:
        return 0.0