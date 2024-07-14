from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.y23pv7t.mongodb.net/", tlsAllowInvalidCertificates=True)

# tlsAllowInvalidCertificates=True not a good way to handle ssl
#not a good idea to include id & passwords in code files
#use environment variables instead

#standard approach to make a database

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}. Name: {video['name']} and Time: {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name" : name, "time" : time})

def update_video(video_id,newname, newtime):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {'$set ': {"name": newname, "time": newtime}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube Manager App \n")

        print("1. List all videos")
        print("2. Add videos")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter your Choice: ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Video Name : ")
            time = input("Video Time : ")
            add_video(name,time)

        elif choice == "3":
            video_id = int(input("Enter video id: "))       
            newname= input("Enter updated video name:  ")
            newtime = input("Enter the updated video time: ") 
            update_video(video_id,newname,newtime)
        
        elif choice == "4":
            video_id = int(input("Enter video id to be deleted: "))
            delete_video(video_id)

        elif choice == "5":
            break

        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
