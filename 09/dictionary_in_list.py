# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2021-06-11 17:40:54
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2021-06-11 17:58:53

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, visits, cities):
  entry = {"country": country,
    "visits": visits,
    "cities": cities,
  }
  travel_log.append(entry)
  print(f"You've visited {country} {visits} times.")
  cities_ = ", ".join(cities[:-1])
  cities_ += f" and {cities[-1]}"
  print(f"You've been to {cities_}.")
  return travel_log


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



