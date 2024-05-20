from main import Fractions, Temperature, Len, Volume
fractions1 = Fractions(3,4)
fractions2 = Fractions(1,2)

result = fractions1.add(fractions2)
result.display()

farengeit_temp = Temperature.celcius_to_farengeit(30)
print(farengeit_temp)

celsius_temp = Temperature.farengeit_to_celsius(60)
print(celsius_temp)

killometters = Len.mills_to_kilometers(40)
print(killometters)

mills = Len.kilometers_to_mills(30)
print(mills)

litters = Volume.gallons_to_liters(3)
print(litters)

gallons = Volume.liters_to_gallons(5)
print(gallons)
