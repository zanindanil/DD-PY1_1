import pprint
OUTPUT_FILE = "output.csv"

headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
data = [

    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]


def to_csv_file(filename,rows,headers,delimiter=",",new_line="\n"):
    k=0
    with open(filename,'w') as f:
        for i in headers:


            if k==len(headers)-1:
                f.write(i + new_line)
            else:
                f.write(i + delimiter)
            k += 1
        k=0
        for j in rows:
            for p in j:

                if k==len(j)-1:
                    f.write(p + new_line)
                else:
                    f.write(p + delimiter)
                k += 1
            k=0

to_csv_file(OUTPUT_FILE,data,headers_list)




with open(OUTPUT_FILE) as f:
    for i in f:
       print(i.strip("\n"))