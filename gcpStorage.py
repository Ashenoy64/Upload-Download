from google.cloud import storage



class GCP_FileStorage:
    def __ini__(self,path):
        #path to service_key.json
        self.storage_client=storage.Client.from_service_account_json(path)       
    def file_upload(self,bucket_name,new_bucket,f_name):
              
        if(new_bucket):
            bucket=self.storage_client.create_bucket(bucket_name)
        bucket=self.storage_client.get_bucket(bucket_name)
        parcel=bucket.blob(f_name)
        try:
            parcel.upload_from_filename(f_name)
        except:
            print("Failed")
        return

    def file_download(self,bucket_name,f_name):
        bucket=self.storage_client.get_bucket(bucket_name)
        parcel=bucket.blob(f_name)
        try:
            parcel.download_to_filename(f_name)
        except:
            print("Failed")
        return

if __name__=="__main__":
    pass
