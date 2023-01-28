def get_size(json_response):
    size = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"]

    first_size = float(size['upperCorner'].split()[1]) - float(size["lowerCorner"].split()[1])
    second_size = float(size['upperCorner'].split()[0]) - float(size["lowerCorner"].split()[0])
    return(str(second_size), str(first_size))
