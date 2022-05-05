from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
# from pyspark.context import SparkContext
# from pyspark.sql.session import SparkSession

# sc = SparkContext('local')
# spark = SparkSession(sc)
training = spark.read.csv("trainIdx2_matrix.txt", header = False)
training.show(5)

# testing = testing.withColumn("userID", testing["userID"].cast(IntegerType()))
# testing = testing.withColumn("itemID", testing["itemID"].cast(IntegerType()))
# testing = testing.withColumn("rating", testing["rating"].cast('float'))
# testing.show(3)
