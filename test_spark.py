from pyspark import SparkContext,SparkConf
conf = SparkConf.setAppName("test")

sc= SparkContext(conf=conf)

words = sc.textFile("test.txt").flatmap(lambda line:line.split(" "))
dis_word = words.map(lambda word: word ,1).reduceBykey(lambda a,b:a+b)

print(dis_word)
