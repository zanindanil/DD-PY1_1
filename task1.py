import pprint


def function():
    type_ = {'dec': 'form1', 'bin': 'form2', 'oct': 'form3', 'hex': 'form4'}
    dict_list = []
    for i in range(0, 16):
        new = type_.copy()
        new['dec'] = i
        new['bin'] = bin(i)
        new['oct'] = oct(i)
        new['hex'] = hex(i)
        dict_list.append(new)
    pprint.pprint(dict_list)


function()
