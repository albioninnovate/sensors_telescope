"""
Takes as input a nested dictionary of the form below
and returns a flat dictionary.  The keys are appended
with ordinal numbers (key_0, key_1...) to flatten.

"""
received = {'1': {'acceleration': [-0.19, -0.52, 9.5],
                  'euler': [0.0, -1.1875, 3.125],
                  'gravity': [-0.2, -0.53, 9.78],
                  'gyro': [0.13962634015954636,
                           -0.003272492347489368,
                           0.0],
                  'linear_acceleration': [1.3, 0.0, -0.28],
                  'magnetic': [40.0, -11.375, -48.0625],
                  'quaternion': [0.99957275390625,
                                 -0.02752685546875,
                                 0.0106201171875,
                                 0.0],
                  'temperature': 22},
            '2': {'acceleration': [-0.20, -0.52, 9.5],
                  'euler': [0.0, -1.1875, 3.125],
                  'gravity': [-0.2, -0.53, 9.78],
                  'gyro': [0.13962634015954636,
                           -0.003272492347489368,
                           0.0],
                  'linear_acceleration': [1.3, 0.0, -0.28],
                  'magnetic': [40.0, -11.375, -48.0625],
                  'quaternion': [0.99957275390625,
                                 -0.02752685546875,
                                 0.0106201171875,
                                 0.0],
                  'temperature': 32}
            }


def flatten(received):
    flat = {}  # the received, imu data, in a flat dictionary to be aggregated in flats
    flats = {}  # dictionary of flat dictionaries to be averaged
    # cnt = 0  # counter used to label the values associated with the 3 and 4 axis imu data attributes
    dct = 0  # counter use to label the multiple flattened dictionaries

    for time_stamp in received:
        data_dict = received[time_stamp]

        for keys in data_dict:
            q = data_dict[keys]

            if type(q) is int:
                flat[keys + '_0'] = q  # add ordinal for consistency

            elif type(q) is list:
                cnt = 0  # reset the count for each list
                for lst in q:
                    flat[keys + '_' + str(cnt)] = lst
                    cnt += 1
        # pprint.pp(flat)
        flats['d_' + str(dct)] = flat
        flat = {}
        # print(flat)
        dct += 1

    # print(flats)
    return flats


def add_dict(data):
    accum = {'acceleration_0': 0, 'acceleration_1': 0, 'acceleration_2': 0,
             'euler_0': 0, 'euler_1': 0, 'euler_2': 0,
             'gravity_0': 0, 'gravity_1': 0, 'gravity_2': 0,
             'gyro_0': 0, 'gyro_1': 0, 'gyro_2': 0,
             'linear_acceleration_0': 0, 'linear_acceleration_1': 0, 'linear_acceleration_2': 0,
             'magnetic_0': 0, 'magnetic_1': 0, 'magnetic_2': 0,
             'quaternion_0': 0, 'quaternion_1': 0, 'quaternion_2': 0, 'quaternion_3': 0,
             'temperature_0': 0}

    samples = 0
    average = {}

    # print('dats being added-------',data)

    for keys in data:
        dict2 = data[keys]
        samples += 1

        # pprint.pprint(dict2)

        for key in dict2:
            accum[key] = dict2[key] + accum[key]

    # pprint.pprint(accum)
    # print('samles', samples)

    for keys in accum:
        average[keys] = accum[keys] / samples

    return average


def main(received):
    flatened = flatten(received)

    # print('data flattened', flatened)

    average = add_dict(flatened)
    # pprint.pprint(average)

    return average


if __name__ == '__main__':
    main(received)
