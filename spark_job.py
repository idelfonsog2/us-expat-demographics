
import configparser
from datetime import datetime, date
import os
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import udf, col, monotonically_increasing_id
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format

import numpy as np
import pandas as pd

config = configparser.ConfigParser()
config.read('dl.cfg')

if __name__ == "__main__":
    schema = ""

    spark = SparkSession \
        .builder \
        .appName("Capstone Project") \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    
    airports_df = spark.read.csv('/data/airport-codes.csv',
                        inferSchema=True,
                        header=True,
                        sep=",",
                        #mode="DROPMALFORMED"
                        )
    airports_df.createOrReplaceTempView('airport_codes') # allows you to write queires if it was postgres
    airports_df.dropna(how="any", subset=["iata_code"]
    
    s_df = spark.read.csv('/data/immigration_data_sample.csv',
                        inferSchema=True,
                        header=True,
                        sep=",")
    #mode="DROPMALFORMED"
    
    query = spark.sql("""
            SELECT DISTINCT iata_code,

            FROM airport_codes 
            """).collect()

    airports_df.write.parquet(os.path.join(output_path, 'airports'), partitionBy=('', ''))

    spark.stop()


# spark.sparkContext.parallelize(["s", "s"])