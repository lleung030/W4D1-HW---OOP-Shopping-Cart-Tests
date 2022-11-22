# The question asks the following: Write a function that takes an integer flight_length
#  (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean
#  indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
movie_lengths1 = [20, 30, 110, 40, 50] #true
movie_lengths2 = [20, 80, 110, 40]  #false
flight_length = 160

def flight_plan_complete (flight_length, movie_lengths):
    copy = movie_lengths[:]
    for n in copy:
        magic_num = flight_length - n
        check = movie_lengths(n)
        if magic_num in check:
            return True
    else:
        return False

    
print(flight_plan_complete(flight_length, movie_lengths1))
print(flight_plan_complete(flight_length, movie_lengths2))


