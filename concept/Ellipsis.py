'''
Ellipsis is a special object in Python that is used to represent an incomplete slice or a placeholder for future code.

it's used as a place holder in python matlb hum asi jaga used karty hai jaha agy code nahi pata hota waha as a placeholder use akrty hai 

it's is also represented by the literal `...`.

'''

x=...
print(x)  # Output: Ellipsis


def my_function():
    ...
    # This means: I'll fill this in later!

class MyClass:
    ...



# Ellipsis ka used advaced slicing me bhi hota hai numpy me ..
'''
📌 Use in multi-dimensional array slicing (NumPy)
Jab hum multi-dimensional arrays (jaise 3D, 4D arrays) ke saath kaam karte hain, toh ellipsis (...) use hota hai to:

“Skip some dimensions in between.”
Matlab: sab dimensions ko manually likhne ki zarurat nahi hoti — ... use karke hum unko short kar sakte hain.

'''

# import numpy as np

# arr = np.arange(27).reshape(3, 3, 3)
# print(arr)



# it's return 

'''
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],

       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])
'''

# is ko access karne ke liy hum ya used karty hai 

# arr[:, :, 0]


# acha 3d demension ko kasy access karty hai [:,:,0] ka matlab hai agr 3d demension hai to : ka matlab all sab block ,,,, os k bad : show karta hai all row and , 3rd show 0 colume of all 


# ab ellipsis ka used karty hai
# arr[..., 0]  # This is equivalent to arr[:, :, 0]


'''

| What you write      | What NumPy sees    |
|---------------------|--------------------|
| `arr[..., 0]`       | `arr[:, :, 0]`     |
| `arr[..., 1]`       | `arr[:, :, 1]`     |
| `arr[0, ..., 0]`    | `arr[0, :, 0]`     |
| `arr[0, 1, ...]`    | `arr[0, 1, :]`     |

'''