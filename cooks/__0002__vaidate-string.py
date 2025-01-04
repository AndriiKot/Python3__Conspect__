def validation_string_value(input_string):
    strip_input_string = input_string.strip()    
    return {'true': 'True', 'false': 'False'}.get(strip_input_string.lower(), strip_input_string)


