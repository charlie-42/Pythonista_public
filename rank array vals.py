import numpy as np
import matplotlib.pyplot as plt

# ~ -------------------------------------------

def array_ranked (source_data):
	"""takes an array (rank 1 vector ny default) and reorganises it to return dest_values and dest_addresses
	
	receives:     source_array - an array to be re-ordered
	
	does:         ranks the array in order from largest to smallest, and saves the addresses of the values
	
	returns:      dest_values - the array of ordered values
	              dest_addresses - the array of addresses the values came from in original array
	"""
	
	source_copy = np.copy(source_data)
	# ~ set up the destination array for addresses and values
	dest_addresses = np.zeros((source_data.shape))
	dest_values = np.zeros((source_data.shape))

	# ~ set up the variables for the loop
	max_value = 0
	max_address = 0
	abs_min = np.min(source_copy) - 1 # ~ need this to ensure a value that never gets saved as a max_value

	#nested loop over i, j: i for locations in dest arrays, j for looping over source
	for i in range(dest_addresses.shape[0]):
		for j in range (source_copy.shape[0]):
			if source_copy[j] == np.max(source_copy):
				max_address = j
				max_value = source_copy[j]
				source_copy [j] = abs_min
				break
			
		dest_addresses[i] = max_address
		dest_values[i] = max_value
	
	return dest_values, dest_addresses
	
# ~ --------------------------------

a = np.array([89,0,3,5,2,55,1,34,21,1,8])

dataset1 = np.random.randn(100,) * 100
#dataset = dataset.reshape(10,100)
dataset2 = np.random.randn(100,) * 100
dataset3 = np.random.randn(100,) * 100


print (dataset1.shape)

vals1, addrs1 = array_ranked(dataset1)
vals2 = vals1
addrs2 = addrs1+3
vals3, addrs3 = array_ranked(dataset3)

print ('\n')
print ('a is')
print (a)
print ('vals')
print (vals1)
print ('addrs')
print (addrs1)

plt.plot(addrs1, vals1)
plt.plot(addrs2, vals2)
#plt.plot(addrs3, vals3)
plt.xlabel('addrs')
plt.ylabel('vals')
plt.show()

# ~ actually what you'd want to do is take the top cohort of addresses, say 20, and histogram them
# ~ so .. np.concatenate

full_array = np.concatenate((addrs1[:10],addrs2[:10],addrs3[:10]))
print (full_array.shape)
print (full_array)

plt.clf()
plt.hist(full_array)
plt.show()
	



