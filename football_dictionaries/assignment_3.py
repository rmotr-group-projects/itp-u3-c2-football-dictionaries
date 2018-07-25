def players_by_country_and_position(squads_list): 
  country_dict = {} 
    for index, item in enumerate(squads_list):
      adder = {} 
      adder["number"] = item[0] 
      adder["position"] = item[1] 
      adder["name"] = item[2]
      adder["date_of_birth"] = item[3] 
      adder["caps"] = item[4] 
      adder["club"] = item[5] 
      adder["country"] = item[6] 
      adder["club_country"] = item[7]
      adder["year"] = item[8] 
      country_dict.setdefault(adder["country"], {}) 
      country_dict[adder["country"]].setdefault(adder["position"], [])
      country_dict[adder["country"]][adder["position"]].append(adder) 
  return country_dict 



