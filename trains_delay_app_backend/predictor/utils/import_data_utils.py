
def filter_csv_dict(reader, filter_criteria):
    filtered_rows = []
    for row in reader:
        if all(row[key] == value for key, value in filter_criteria.items()):
            filtered_rows.append(row)
    return filtered_rows