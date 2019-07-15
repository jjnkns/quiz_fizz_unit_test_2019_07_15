## Quiz: FizzBuzzer class
## Jennifer Jenkins
## July 15, 2019

### Part 1

#Create a class called FizzBuzzer
# It has an init method and a next val. The init method has an argument, `start`
# whose default value is 0. An integer instance property called `number` is set 
# to equal `start`
# It has a (normal, not class) method called `next` that takes no arguments.
# This method increases number by 1 and then returns a string of that number's
# fizzbuzz value.


class FizzBuzzer:
    def __init__(self, start=0):
        self.number = start
        self.next_val = self.number+1 #leave original number intact but keep incrementing nextval?
        self.fizz_count = 0
        self.buzz_count = 0
        self.fizzbuzz_count = 0
        self.count_dict = {}
    
    def next(self):
        
        if self.next_val%3 == 0 and self.next_val%5 == 0:
            fb_value='fizzbuzz'
            self.fizzbuzz_count+=1
            self.store_counts({fb_value : self.fizzbuzz_count})
        elif self.next_val%5 == 0:
            fb_value = 'buzz'
            self.buzz_count+=1
            self.store_counts({fb_value : self.buzz_count})
        elif self.next_val%3 == 0:
            fb_value = 'fizz'
            self.fizz_count+=1
            self.store_counts({fb_value : self.fizz_count})
        else:
            fb_value = str(self.next_val)
        print(f'number: {self.next_val}\tresult: {fb_value}\trunning counts: {self.count_dict}')
        self.next_val+=1    
        return({"number_in" : self.number, "result" : fb_value})
        #return fb_value, self.next_val, self.count_dict
    def store_counts(self, dict1):
        self.count_dict.update(dict1)

# buzzer = FizzBuzzer(2)
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()
# buzzer.next()

# # Fizzbuzz value of n = "fizz" if n is evenly divisible by 3, "buzz" if n is
# # evenly divisible by 5, and "fizzbuzz" if n is evenly divisible by 3 and 5. If
# # n is not divisible by 3 or 5 then the fizzbuzz value is the value of n converted
# # into a string.




# Now, add three attributes- one that stores the number of times you've returned
# "fizz", one that stores the number of times you've returned "buzz", and one that
# stores the number of times you've returned "fizzbuzz". Write a method that
# will a dictionary of each of these counts.

### Open book, open notes

# * You are free to use Google & look at your code from class. Do not ask anyone
# to help you write or debug your code. If the question is unclear, please ask an
# instructor or T.A. to clarify over Discord.