def get_field_errors(errors):
    error_list = []
    error_keys = errors.keys()
    for error in error_keys:
        error_msg = errors.get(error)[0]
        error_list.append(
            {
                'field': error,
                'message': error_msg
            }
        )
    return error_list