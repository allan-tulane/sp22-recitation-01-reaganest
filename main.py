"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
  while (left <= right ):
    middle = (left + right)//2
    if key == mylist[middle]:
      return middle
      
    elif key > mylist[middle]:
      left = middle + 1 
    elif key < mylist[middle]:
      right = middle - 1
      
  return -1
      
def test_binary_search():
	#assert time_search(binary_search,[1,2,3,4,5],5)
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	assert binary_search([1,2,3,4,5], 2) == 1
	assert binary_search([1,2,3,4,5], 4) == 3
	
def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.
 create start and end time for function( search_fn) and subtract to get total time
 
	Note 1: `search_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
  	Params:
	  search_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this search function on this input.
	"""
	### TODO
  #create start and end time for function( search_fn) and subtract to get total time
  
	start_time = time.time()
	search_fn(mylist,key)
	end_time = time.time()
	total_time = (end_time - start_time) * 1000
	#print(total_time)
	return total_time 

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  values = []
  for i in sizes:
    my_list = tuple(range(int(i)))
    linear_search_time=time_search(linear_search,my_list,-1)
    binary_search_time=time_search(binary_search,my_list,-1)
    values.append([len(my_list),linear_search_time, binary_search_time])
  return values

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".8f",
							tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1


print_results(compare_search())
	
