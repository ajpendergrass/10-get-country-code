def get_country_codes(prices):
    split_list = prices.split(", ")
    country_codes = []
    for i in split_list:
      country_codes.append(i[:2])
    print(country_codes)
