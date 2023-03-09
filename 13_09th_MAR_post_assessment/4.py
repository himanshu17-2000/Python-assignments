import argparse
import sys
import os
class Country():
    def __init__(self,name):
        self.name=name
        self.states=[]
    def add_states(self,state):
        self.states.append(state.name)
    def print_country(self):
        print("country:",self.name)
        print("states:",self.states)
       
class State(Country):
    def __init__(self,name):
        self.name=name
        self.districts=[]
        self.cities=[]
    def add_district(self,district):
        self.districts.append(district.name)
    def add_cities(self,city):
        self.cities.append(city.name)
    def print_state(self):
        print("State:",self.name)
        print("districts:",self.districts)
        print("cities:",self.cities)

class District(State):
    def __init__(self,name):
        self.name=name
    def print_district(self):
        print("District:",self.name)
class City(State):
    def __init__(self,name):
        self.name=name
    def print_city(self):
        print("City:",self.name)
class Unionterritory():
    def __init__(self,name):
        self.name=name
        self.cities=[]
    def add_city(self,city):
        self.cities.append(city.name)
    def print_ut(self):
        print("UnionTerritory:",self.name)
        print("cities:",self.cities)

def generate(args):
        country_name=args.country
        state_name=args.state
        district_name=args.district
        city_name=args.city
        ut_name=args.ut
        country_object=Country(country_name)
        state_object=State(state_name)
        city_object=City(city_name)
        district_object=District(district_name)
        country_object.add_states(state_object)
        state_object.add_district(district_object)
        state_object.add_cities(city_object)
        ut_object=Unionterritory(ut_name)
        country_object.print_country()
        print("")
        state_object.print_state()
        print("")
        district_object.print_district()
        print("")
        city_object.print_city()
        print("")
        ut_object.print_ut()
        print("")
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--country',type=str,default="new Country",help="Enter the name of the Country")
    parser.add_argument('--state',type=str,default="new State",help="Enter the name of the State")
    parser.add_argument('--district',type=str,default="new district",help="Enter the name of the District")
    parser.add_argument('--city',type=str,default="new city",help="Enter the name of the City")
    parser.add_argument('--ut',type=str,default="new ut",help="Enter the name of the Union Territory")

    args=parser.parse_args()
    sys.stdout.write(str(generate(args)))