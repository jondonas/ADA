from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min
from pyspark.sql.functions import unix_timestamp
from pyspark.sql.types import *

from pyspark.ml.feature import StringIndexer

from datetime import datetime  
from datetime import timedelta

from pyspark.sql import SparkSession
from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

########## Use this when running on cluster ##########
# This reads in all files that start with amazon_reviews_us (the english reviews)
dataFile = 'hdfs:///datasets/amazon_multiling/tsv/amazon_reviews_us*tsv.gz'

# Manually specify the schema
schema = StructType([
    StructField('marketplace', StringType()),
    StructField('customer_id', IntegerType()),
    StructField('review_id', StringType()),
    StructField('product_id', StringType()),
    StructField('product_parent', IntegerType()),
    StructField('product_title', StringType()),
    StructField('product_category', StringType()),
    StructField('star_rating', IntegerType()),
    StructField('helpful_votes', IntegerType()),
    StructField('total_votes', IntegerType()),
    StructField('vine', StringType()),
    StructField('verified_purchase', StringType()),
    StructField('review_headline', StringType()),
    StructField('review_body', StringType()),
    StructField('review_date', DateType()),
])

df = spark.read.csv(dataFile, sep="\t", header=True, schema=schema)
query1 = '''
SELECT df.product_id, df.review_id, df.product_category, df.star_rating, df.helpful_votes, df.total_votes, df.customer_id, df.verified_purchase, df.review_body, df.review_date  FROM
  df
  INNER JOIN
  (
    SELECT product_id
    FROM df
    WHERE product_category='Beauty' 
    GROUP BY product_id
    HAVING COUNT(*) >= 50 AND COUNT(*) <= 100 
  ) interesting
  on df.product_id = interesting.product_id
	WHERE total_votes >= 10
'''

df.registerTempTable("df")
df_queried = spark.sql(query1)

df_queried.write.json("beauty3")

print("********** FINISHED **********")
