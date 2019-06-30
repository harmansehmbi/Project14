import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('path/to/customer.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
print("done")

# Insert Operation
# cRef = Customer("Fionna", "+91 99999 88888", "fionna@example.com")
# data = cRef.__dict__
#
# db.collection("Customer").document().set(data)
#
# print(">> ",cRef.name,"Saved in Firebase")

docs = db.collection("customer").get()

for doc in docs:
    print(doc.id, doc.to_dict())