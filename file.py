#                                   Requirements 
#    1)google.cloud library
#    2)path of the service account key json file 
#    3)path string must be raw


from google.cloud import storage


def file_upload(path,bucket_name,new,f_name):
    storage_client=storage.Client.from_service_account_json(path)       
    if(new):
        bucket=storage_client.create_bucket(bucket_name)
    bucket=storage_client.get_bucket(bucket_name)
    parcel=bucket.blob(f_name)
    try:
        parcel.upload_from_filename(f_name)
    except:
        print("Failed")
    return

def file_download(path,bucket_name,new,f_name):
    storage_client=storage.Client.from_service_account_json(path)
    bucket=storage_client.get_bucket(bucket_name)
    parcel=bucket.blob(f_name)
    try:
        parcel.download_to_filename(f_name)
    except:
        print("Failed")
    return

if __name__=="__main__":
    pass
