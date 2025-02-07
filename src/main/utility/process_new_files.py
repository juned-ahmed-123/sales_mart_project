def process_new_files(spark,new_files,s3_bucket,mysql_url,mysql_properties):
    # (spark, new_files, bucket_name, mysql_url, mysql_properties)
    """Process new files, load data into Spark, and update MySQL."""
    if new_files:
        for file in new_files:
            df=spark.read \
                .format("csv") \
                .option("header", "true") \
                .load(f"s3a://{s3_bucket}/{file}")
            df.show()
         # Store processed file names in MySQL
            processed_df=spark.createDataFrame([(file,)], ["file_name"])
            processed_df.write.jdbc(mysql_url, "processed_files", mode="append", properties=mysql_properties)
            print("sucessfulyy upladed in mysql proceed table")
    else:
        print("No new files to process.")

