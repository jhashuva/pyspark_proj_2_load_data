from init_context import sp, sc
df = sp.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","True").load("Data/2015-summary.csv")

