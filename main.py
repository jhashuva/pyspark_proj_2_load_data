from read_data import df
if df:
    print(df.printSchema())
    print("\n\n")
    print(df.show(5))
    print("\n\n")
    print(df.describe())