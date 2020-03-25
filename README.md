
# setInterval-python
Sometimes, when you're writing code in python, you have to make a function that needs to be executed every certain amount of time. 
This class will help you do that easily and dynamically on python. Open all of the flexibility to maintain the interval.

Declaring 
---------
To declare an interval function, you just need to call the setInterval class. The parameter is as follows:
```setInterval(Function,Interval[, Arguments=[]  ])``` 
The `Interval` is in second, by using number data type.
The `Arguments` is the arguments you need to pass to the function in array.

Here's a simple example:
```Python
def interval(name="world"):
  print(f"Hello {name}!")

# function named interval will be called every two seconds
#output: "Hello world!"
interval1 = setInterval(interval, 2) 

# function named interval will be called every 1.5 seconds
#output: "Hello Jane!"
interval2 = setInterval(interval, 1.5, ["Jane"]) 
```

## Clear interval
To clear the interval, you just need to call `.stop()` from the object of setInterval. This method will immediately stop the interval

## Change the interval
To change the interval, there are two options available:
1. you change the interval immediately. Use `.change_interval(new_interval)`
2. you change the interval after the next interval. Use `.change_next_interval(new_interval)`

The difference is, if you change it immediately to `x` seconds, your function will be called right `x` seconds after you call the `change_interval` method.
If you change it after the next interval, it will allow to run the remaining queued function. Your change will be applied after the next call, **and not immediately**.

Here's the difference example:
```Python
from time import sleep

i1 = setInterval(print,5,["hello"])
i2 = setInterval(print,5,["world"])

sleep(1) 

#the first 'hello' will be printed after 3 seconds of execution time (sleep:1 second + new interval : 2 second)
#the second 'hello' will be printed after 5 seconds of execution time
i1.change_interval(2) 

#the first 'world' will be printed after 5 seconds (old interval: 5 seconds)
#the second 'world' will be printed after 8 seconds (old interval: 5 seconds + new interval: 3 seconds)
i2.change_next_interval(3)

#stop those intervals after 10 seconds of execution time
time.sleep(10)
i1.stop(); i2.stop() 
```

## Change the function
To change the function, you must call the method
```change_func(newFunction[,newArgument=[]  ])```
The changes will be immediately applied.

Example:
```Python
import time

def a():
	print('a')
def b():
	print('b')

i = setInterval(a, 3)
time.sleep(4)
i.change_func(b)
time.sleep(7)
i.stop()

# output:
# a
# b
# b
```

