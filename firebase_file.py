import  pyrebase                                 

config={
  "apiKey": "AIzaSyBA3070LTSIOeGEPU6WRpRWC1LaTYFjJa8",
  "authDomain": "cloud-malware.firebaseapp.com",
  "projectId": "cloud-malware",
  "storageBucket": "cloud-malware.appspot.com",
  "databaseURL":"https://cloud-malware.firebaseio.com",
  "serviceAccount":"service_key.json"
   }

firebase=pyrebase.initialize_app(config)


def upload(local_path,cloud_path,firebase=firebase):       
  storage=firebase.storage()
  try:
    storage.child(cloud_path).put(local_path)
  except:
    pass
  return 


def download(cloud_path,fname,firebase=firebase):
  storage=firebase.storage()
  try:
    storage.download(cloud_path,fname)
  except:
    pass
  return 
if __name__=="__main__":
  upload("map.jpg","map2.jpg")  
  download("map.jpg","test.jpg")
  pass




'''   
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
'''
