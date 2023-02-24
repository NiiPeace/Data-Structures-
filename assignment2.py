#NiiPeace 
#6946221
#LIST OF AVAILABLE CARS AND THEIR PRICES
cars={"Mustang":236000,"F150":120000,"Kuga":21000,"explorer":211000,"escape":123200,"yaris":25000,"camry":90000,"tundra":67000,"tacoma":65000,"corolla":637997,
"civic":765333,"CRV":3748467,"hrv":234509,"closed coupled":4530000,"Rolls-royce":51000,"Bugatti":770000, "Mclaren": 230000,"Mercedes":135000,\
"Buick":45000,"Hyundai":129000,"Nissan":110050,"Alfa Romeo":79430,"Mazda":310000,"Volkswagen":212935,"Kia":72950,"Audi":990000,"Honda":100350,"Porsche":815000 ,"Cadillac":310000,"Jeep":290000,"Lexus":490000,"Tesla":694950 }
#
car_name= input (" what model of cars do you want : ")
if car_name in cars:
    print(' "model is available" ')
    car_price=cars[car_name]
    print(f"the price of {car_name} here is ${car_price}.")
else:
    print(f"sorry, all {car_name}'s are off the market.")
 
