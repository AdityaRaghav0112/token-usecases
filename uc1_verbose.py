def calculate_average_user_age_from_database(database_user_records_list):
    total_accumulated_age_of_all_users = 0
    valid_user_record_count = 0
    
    for individual_user_record in database_user_records_list:
        if individual_user_record.get('is_account_active', False):
            user_age_value = individual_user_record.get('user_age_in_years', 0)
            if user_age_value > 0:
                total_accumulated_age_of_all_users += user_age_value
                valid_user_record_count += 1
                
    if valid_user_record_count > 0:
        return total_accumulated_age_of_all_users / valid_user_record_count
    else:
        return 0.0
