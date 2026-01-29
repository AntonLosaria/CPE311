
    
            #Class for Routes
class Route():
    def __init__(self, n, d, t, c): #Abstraction \\ Making variables private
        self.routename = n
        self.distance = d           # in kilometers (km)
        self.traffic = t            # traffic from 1 - 10
        self.cost = c               # total cost (php)
    def getDistance(self):          #Access to variable distance
        return self.distance        
    def getTraffic(self):           #Access to variable traffic
        return self.traffic
    def getCost(self):              #Access to variable cost
        return self.cost
    def trafficToDistance(self):    #Returning percentage of 
        return (self.getTraffic() / 10) * (self.getDistance() / (self.getDistance() + 1)) * 100
    def traveltime(self):           # total travel time with traffic and distance included
        return self.getDistance() * (1 + (self.trafficToDistance() / 100))
    def __str__(self):              #Printing of the best route
        return (self.routename + '\nTraffic Congestion: ' + str(self.trafficToDistance()) + 
                '% \nTotal Distance: ' + str(self.distance) + 
                ' km \nTotal Cost: ' + str(self.cost) + ' PHP')
    

def RouteList(names, distance, traffic, cost): #Puts all routes in a list
    route = []
    for i in range(len(distance)):
        route.append(Route(names[i], distance[i], traffic[i], cost[i]))
    return route

def FastestRoute(item, limit):      
    mintime = float('inf')                 #Declaration of mintime that will always be a positive float
    fastestroute = None                    #Declaration of fastest route -- Currently none --

    for route in item:                     #Iterates over every route
        if route.getCost() <= limit:       #Checks if current route is over, skips over routes that is over that limit
            time = route.traveltime()
            
            if time < mintime:             #In the first iteration, the first route will be the mintime and fastest route
                mintime = time             #This is then used to compare for the next routes, where if it's time is less than
                fastestroute = route       #the mintime, then it will become the mintime and fastest route
    return fastestroute

routes = RouteList(
    names=["Route A", "Route B", "Route C"],
    distance=[10, 8, 6],
    traffic=[6, 7, 4],
    cost=[500, 300, 200]
)
maxcost = 400
bestroute = FastestRoute(routes, maxcost)
print(f"Fastest Route: {bestroute}")
