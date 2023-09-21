class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name


    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, 'name'):
            self._name = name
        else:
            print('not a valid entry')

    name = property(get_name, set_name)
    

    def trips(self):
        r_list =[]
        for trip in Trip.all:
            if isinstance(trip, Trip) and trip.national_park == self:
                r_list.append(trip)
        return r_list

    
    def visitors(self):
        r_list =[]
        for trip in Trip.all:
            if isinstance(trip, Trip) and trip.national_park == self and trip.visitor not in r_list:
                r_list.append(trip.visitor)
        return r_list
    
    def total_visits(self):
        visits = 0
        for trip in Trip.all:
            if isinstance(trip, Trip) and trip.national_park == self:
                visits += 1
        return visits
   
    def best_visitor(self):
        current_best = None
        current_best_count = 0
        all_visitors = self.visitors()
        for visitor in all_visitors:
            count = visitor.total_visits_at_park(self)
            if count > current_best_count:
                current_best = visitor
                current_best_count = count
        return current_best



class Trip:
    valid_month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December") 
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    def get_start_date(self):
        return self._start_date
    
    def set_start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            split_str = start_date.split()
            if split_str[0] in Trip.valid_month and 3<=len(split_str[1])<=4:
                self._start_date = start_date
            else:
                print("Invalid start date format")
        
        else:
            print("This is not a valid start date")

    def get_end_date(self):
        return self._end_date
    
    def set_end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            split_str = end_date.split()
            if split_str[0] in Trip.valid_month and 3<=len(split_str[1])<=4:
                self._end_date = end_date
            else:
                print("Invalid end date format")
        
        else:
            print("This is not a valid end date")

    
    def get_visitor(self):
        return self._visitor
    
    def set_visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            print("Not a valid visitor")

     
    def get_national_park(self):
        return self._national_park
    
    def set_national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            print("Not a valid National Park")

    start_date = property(get_start_date, set_start_date)
    national_park = property(get_national_park, set_national_park) 
    visitor = property(get_visitor, set_visitor)
    end_date = property(get_end_date, set_end_date)

class Visitor:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name   

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            print("This is not a valid entry")
        
    name = property(get_name, set_name)
    
    
    def trips(self):
        r_list =[]
        for trip in Trip.all:
            if isinstance(trip, Trip) and trip.visitor == self:
                r_list.append(trip)
        return r_list


    
    def national_parks(self):
        r_list =[]
        for trip in Trip.all:
            if isinstance(trip, Trip) and trip.visitor == self and trip.national_park not in r_list:
                r_list.append(trip.national_park)
        return r_list
    
    def total_visits_at_park(self, park):
        our_trips = self.trips()
        count = 0
        for trip in our_trips:
            if trip.national_park is park:
                count +=1
        return count



yosemite = NationalPark("Yosemite")
rmnp = NationalPark("RMNP")
terence = Visitor("Terence") 
tim = Visitor("Tim")
luisa = Visitor("Luisa")
Trip(terence, rmnp, "August 1st", "September 10th") 
Trip(terence,yosemite,"July 4th", "July 14th")
Trip(terence, rmnp, "August 1st", "August 10th")
Trip(tim, yosemite, "September 11th", "September 20th")
Trip(luisa, yosemite, "September 4th", "September 8th")
Trip(luisa, yosemite, "November 1st", "November 7th")
# print(luisa.trips())
# print(tim.national_parks()[0]is yosemite)   
# print(rmnp.visitors()[0] is terence)
# print(yosemite.total_visits())
# print(luisa.total_visits_at_park(yosemite))