#Adrianne Verstraete
def my_get_method(k,d, default):
    if k in d:
        print (d[k])
    else:
        print (default)

d={"a":1, "b":2}
my_get_method("d",d, 4)

my_get_method("c",d,"pink")

my_get_method("a",d,False)

my_get_method("e",d,3.15)
