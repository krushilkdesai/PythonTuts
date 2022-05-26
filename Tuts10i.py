d1={"Krushil":"Keri", "Car":"Land Rover",
    "Processor":"i5 11gn",
    "CPU":"Zebion"}
print(d1)
print (d1["Krushil"])

d1["Mobile"]="Realme"
print (d1)

d1["Wifi"]="Jio"
print (d1)

print (d1["Mobile"])

del d1["Wifi"]
print (d1)

d3 = d1.copy()
del d3["Car"]

d1.update({"Keybord":"Logitech"})
print (d1)

print (d1.items())
print (d1.values())
