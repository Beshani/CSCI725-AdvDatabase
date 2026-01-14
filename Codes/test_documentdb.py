import pymongo
import random
import string
import time

# client = pymongo.MongoClient("mongodb://beshani:bnw12345@docdb-2023-11-03-20-42-15.cj3muyzqsxtr.us-east-1.docdb.amazonaws.com:27017/?retryWrites=false")
clusterendpoint = 'docdb-2023-11-28-17-51-48'
username = 'beshani'
password = 'bnw12345'
# client = pymongo.MongoClient(clusterendpoint, username=username, password=password, port=27017, tls='false',retryWrites='false')
client = pymongo.MongoClient(rf'mongodb://{username}:{password}@docdb-2023-11-28-17-51-48.cj3muyzqsxtr.us-east-1.docdb.amazonaws.com:27017/?retryWrites=false')
##Specify the database to be used
db = client["testdb"]

##Specify the collection to be used
collection = db['test_collection']

# Helper function to generate random strings for username and password
def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Insert user data and measure execution time
def insert_user(username, password):
    start_time = time.time()
    user_document = {
        'Username': username,
        'Password': password
    }
    result = collection.insert_one(user_document)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Inserted user: {username} (Execution time: {execution_time:.4f} seconds)")
    return execution_time

# Update a user's password and measure execution time
def update_password(username, new_password):
    start_time = time.time()
    result = collection.update_one({'Username': username}, {'$set': {'Password': new_password}})
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Updated password for user: {username} (Execution time: {execution_time:.4f} seconds)")
    return execution_time

# Select a user's data and measure execution time
def select_user(username):
    start_time = time.time()
    user_document = collection.find_one({'Username': username})
    end_time = time.time()
    execution_time = end_time - start_time
    if user_document:
        print(f"Selected user: {username} (Execution time: {execution_time:.4f} seconds)")
    else:
        print(f"User '{username}' not found.")
    return execution_time


# Delete a user document and measure execution time
def delete_user(username):
    start_time = time.time()
    result = collection.delete_one({'Username': username})
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Deleted user: {username} (Execution time: {execution_time:.4f} seconds)")
    return execution_time


# Generate 1000 dummy users with random usernames and passwords
dummy_users = [{'Username': generate_random_string(), 'Password': generate_random_string()} for _ in range(2000)]

# Perform 100 iterations of each operation on random users
num_iterations = 1000
insertion_times = []
update_times = []
deletion_times = []
selection_times = []

# Populate the table with the initial set of users
populate_start_time = time.time()
for user in dummy_users:
    insert_user(user['Username'], user['Password'])
populate_end_time = time.time()
populate_duration = populate_end_time - populate_start_time

# Calculate and print the time it took to populate the table
print(f"Time to Populate the Table: {populate_duration:.4f} seconds")
print(f"Average time for each population insert: {populate_duration/len(dummy_users):.4f} seconds")

for _ in range(num_iterations):
    random_user = random.choice(dummy_users)
    random_insert_user = {'Username': generate_random_string(), 'Password': generate_random_string()}

    # Insert
    insertion_time = insert_user(random_insert_user['Username'], random_insert_user['Password'])
    insertion_times.append(insertion_time)

    # Select
    select_time = select_user(random_user['Username'])
    selection_times.append(select_time)

    random_user = random.choice(dummy_users)

    # Update
    update_time = update_password(random_user['Username'], generate_random_string())
    update_times.append(update_time)

    random_user = random.choice(dummy_users)

    # Delete
    delete_time = delete_user(random_user['Username'])
    deletion_times.append(delete_time)


# Calculate and print average execution times
average_insertion_time = sum(insertion_times) / num_iterations
average_update_time = sum(update_times) / num_iterations
average_deletion_time = sum(deletion_times) / num_iterations
average_selection_time = sum(selection_times) / num_iterations

print(f"Average Insertion Time: {average_insertion_time:.4f} seconds")
print(f"Average Update Time: {average_update_time:.4f} seconds")
print(f"Average Deletion Time: {average_deletion_time:.4f} seconds")
print(f"Average Selection Time: {average_selection_time:.4f} seconds")