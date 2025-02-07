def get_processed_files(spark,mysql_url,mysql_properties):
    """Fetch the list of processed files from MySQL."""
    processed_files_df=spark.read.jdbc(url=mysql_url,table="processed_files",properties=mysql_properties)
    return (row["file_name"]for row in processed_files_df.collect())

