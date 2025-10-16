def file_type_getter(file_extension_tuples):
    file_dictionary = {}
    for item in file_extension_tuples:
        file_type = item[0]
        for extension in item[1]:
            file_dictionary[extension] = file_type
    return lambda search: file_dictionary.get(search, "Uknown")


# Lambda [parameter]:expression
