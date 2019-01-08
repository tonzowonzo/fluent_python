dial_codes = [
        (86, "China"),
        (1, "USA"),
        (44, "Germany"),
        (45, "Austria"),
        (25, "Africa")]

country_code = {country: code for code, country in dial_codes}
filtered_codes = {code: country.upper() for country, code
                  in country_code.items()
                  if code < 42}
