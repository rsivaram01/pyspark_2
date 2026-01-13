Python ===> 2.8,2.9,3.0,3.1,3.2

Apache spark  ===> 2.8,2.9,3.0,


2.x

3.x


==================================

SparkContext =====> 2.x 

SparkSession =====> 3.x


Spark ===> is data processing framework ===> package ( classes, functions )
If we want to work with package, we need create object for the same.

===> sparkconext ( upto 2.x)  ====> sc


sc = sparkContext()

val sc = new sparkContext()

if we want to connect with hive =====> hivecontext()
we want to work with spark SQL ======> sqlcontext()

================================================================================
3.x
sparksession ====> spark

spark = sparkSession()

spark = sparkSession.builder.appName("dummy_app").getOrCreate()

spark


===============================
rdd
[(101, 'Alice', 50000), (102, 'Bob', 60000), (103, 'Charlie', 55000)]


dataframe
+------+-------+------+
|emp_id|   name|salary|
+------+-------+------+
|   101|  Alice| 50000|
|   102|    Bob| 60000|
|   103|Charlie| 55000|
+------+-------+------+

=============================================
rdd 

Dataframes and Datasets ( this were not supported in python --> java, scala, R)

Dataframes  ===> which is similar like table structre ( columns, rows ) ( fields , records )

41,42,43,44  ===> pages, read, write running notes

1. What is sparkContext and sparksession 
2. what is rdd
3. what is dataframe and dataset
4. what is the diffrence between rdd, dataframe and dataset
5. how to create sparkconext instance (sc)
6. how to create sparksession instance in pyspark 
    example :spark = sparkSession.builder.appName("dummy_app").getOrCreate()



