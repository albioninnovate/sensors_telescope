

"""
Takes as input a nested dictionary of the form below
and returns a flat dictionary.  The keys are appended
with ordinal numbers (key_0, key_1...) to flatten.

data_dict_0 = {'temperature': 24,
             'acceleration': [-0.24, -0.55, 9.47],
             'magnetic': [31.25, 7.25, -51.0625],
             'gyro': [0.001090830782496456,
                      -0.001090830782496456,
                      0.001090830782496456],
             'euler': [8.0,
                       -1.4375,
                       3.375],
             'quaternion': [0.99945068359375,
                            -0.0296630859375,
                            0.0125732421875,
                            0.0],
             'linear_acceleration': [1.3,
                                     0.02,
                                     -0.27],
             'gravity': [-0.24,
                         -0.58,
                         9.78]
             }

"""
data_dict = {'temperature': 24,
             'acceleration': [-0.24, -0.55, 9.47],
             'magnetic': [31.25, 7.25, -51.0625],
             'gyro': [0.001090830782496456,
                      -0.001090830782496456,
                      0.001090830782496456],
             'euler': [8.0,
                       -1.4375,
                       3.375],
             'quaternion': [0.99945068359375,
                            -0.0296630859375,
                            0.0125732421875,
                            0.0],
             'linear_acceleration': [1.3,
                                     0.02,
                                     -0.27],
             'gravity': [-0.24,
                         -0.58,
                         9.78]
             }


def flatten(data_dict):

    flat = {}
    cnt = 0

    for keys in data_dict:
        q = data_dict[keys]
        # print(keys)
        # print(q)
        # print(type(q))

        if type(q) is int:
            flat[keys+'_'+str(cnt)] = q # add ordinal for consistency

        elif type(q) is list:
            cnt = 0  # reset the count for each list
            for l in q:
                flat[keys+'_'+str(cnt)] = l
                cnt +=1

    print(flat)
    return flat

if __name__ == '__main__':
    flatend = flatten(data_dict)

# TOOD  add the ability to input a super dictionay one with a
# timestamp on the data_dict. strip the time stamp and flaten then average
# the average dictioan shoulf have the time stamp of the last set
