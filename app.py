
import os
import json
import instagrapi
from instagrapi import Client

client = Client()

username = 'gad_cbflicks'
password = 'gusd410!'



client.login(username, password)
user_id = client.user_id_from_username(username)


def listDir(dir):
    fileNames = os.listdir(dir)
    fileLocations = []
    for fileName in fileNames:
        filePath = os.path.abspath(os.path.join(dir, fileName))
        fileLocations.append(filePath)
    return fileLocations

def listandpostDir(dir):
    fileNames = os.listdir(dir)
    fileLocations = []
    for fileName in fileNames:
        filePath = os.path.abspath(os.path.join(dir, fileName))
        client.photo_upload_to_story(filePath)
        print('posted photo: ' + filePath)
        fileLocations.append(filePath)
    print('completed :' + dir)
    return fileLocations

def save_array_as_json(arr, filename):
    with open(filename, 'w') as file:
        json.dump(arr, file)
        
save_array_as_json(listDir(r'H:\My Drive\CB FLICKS'), 'newfolders.json')
save_array_as_json([story.pk for story in client.user_stories(user_id)], 'oldstories.json')

def isthere_a_new_folder():
    with open('pastfolders.json') as f:
        pastfolders = json.load(f)
    with open('newfolders.json') as f:
        newfolders = json.load(f)
    for folder in newfolders:
        if folder not in pastfolders:
            print('new folder found ')
            return True
    return False

def what_is_the_new_folder():
    with open('pastfolders.json') as f:
        pastfolders = json.load(f)
    with open('newfolders.json') as f:
        newfolders = json.load(f)
    for folder in newfolders:
        if folder not in pastfolders:
            print('new folder found ' + folder)
            return folder


def compare_json(file_name):
    # Read in the new JSON file
    with open(file_name, 'r') as f:
        new_data = json.load(f)
    
    # Read in the old JSON file
    with open('oldstories.json', 'r') as f:
        old_data = json.load(f)
    
    # Create a list to store any new objects that are not in the old file
    new_objects = []
    
    # Iterate over the new data and check if each object is in the old file
    for obj in new_data:
        if obj not in old_data:
            new_objects.append(obj)
    
    # Return the list of new objects
    return new_objects

# if(isthere_a_new_folder()):
print('--------------------THERE IS A NEW FOLDER FOUND!!!!!! UPLOADING IMAGES TO INSTAGRAM STORY --------------------')
# listandpostDir(r'H:\My Drive\CB FLICKS\3. LEVIATHAN')
client.highlight_create(r'3. LEVIATHAN', [story.pk for story in client.user_stories(user_id)])

    

    
save_array_as_json(listDir(r'H:\My Drive\CB FLICKS'), 'pastfolders.json')

print('reset folders')

client.logout()
print('logged out')