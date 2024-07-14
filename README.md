Here is a GitHub description for your CRUD Python project:

---

# YouTube Manager App

## Overview

The YouTube Manager App is a simple Python application that demonstrates basic CRUD (Create, Read, Update, Delete) operations using MongoDB. The app allows users to manage a collection of YouTube videos, including listing all videos, adding new videos, updating existing videos, and deleting videos.

## Features

- **List Videos:** Display all videos in the collection with their ID, name, and time.
- **Add Video:** Add a new video with a specified name and time.
- **Update Video:** Update the name and time of an existing video using its ID.
- **Delete Video:** Delete a video from the collection using its ID.

## Prerequisites

- Python 3.x
- `pymongo` library
- MongoDB Atlas account or local MongoDB server

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/youtube-manager-app.git
   cd youtube-manager-app
   ```

2. Install the required Python libraries:
   ```bash
   pip install pymongo
   ```

3. Set up your MongoDB connection string as an environment variable:
   ```bash
   export MONGODB_URI="your_mongodb_connection_string"
   ```

## Usage

Run the application:
```bash
python yt_man.py
```

Follow the on-screen menu to list, add, update, or delete videos.

## Code Structure

- **list_videos:** Lists all videos in the collection.
- **add_video:** Adds a new video to the collection.
- **update_video:** Updates an existing video's name and time using its ID.
- **delete_video:** Deletes a video from the collection using its ID.

## Security Note

Ensure you do not include sensitive information such as database credentials directly in your code. Use environment variables to securely manage these details.

---

Feel free to customize this description further to match your project's specifics and style.
