from dotenv import load_dotenv
import os
import  pyrebase              

load_dotenv()

config={
  "apiKey": os.getenv('API_KEY'),
  "authDomain": os.getenv('AUTH_DOMAIN='),
  "databaseURL": os.getenv('DATABASE_URL'),
  "projectId": os.getenv('PROJECT_ID'),
  "storageBucket":os.getenv('STORAGE_BUCKET'),
  "serviceAccount":os.getenv('SERVICE_KEY_PATH')
   }



class FirebaseStorage:
  def __init__(self,config):
    self.firebase=pyrebase.initialize_app(config)
    

  def upload(self,local_path,cloud_path):       
    storage=self.firebase.storage()
    try:
      storage.child(cloud_path).put(local_path)
    except Exception as e:
      print("Failed ",e)
    except:
       print('Failed due to Unknown Reason')
    return 


  def download(self,cloud_path,fname):
    storage=self.firebase.storage()
    try:
      storage.download(cloud_path,fname)
    except Exception as e:
      print("Failed ",e)
    except:
      print('Failed due to Unknown Reason')
    return 



