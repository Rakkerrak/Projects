Recently I had a problem getting Pyinstaller to run on Windows.  Through some creative Googling and a lot of frustration, this is how I got Python set up on Windows to actually allow Pyinstaller to work.

1. Remove all installations of Python if you have ever touched the Windows Store.  The Windows Store is a scourge upon their OS and commonly causes permission errors and confusion.  For me, it caused ```(1920, 'LoadLibraryExW', 'System can not access the file')```
    - Search "Programs" in your Start menu or find **Add or Remove Programs in the Control Panel**
    - Uninstall (one by one or it'll fail) every version of Python you have.  Better safe than sorry~
2. Install the latest Python from [the official site](https://www.python.org/downloads/)
3. Set up your environment/Path variables so you can use python from the command prompt
    - Search "environment" or "path" or head to the Control Panel to find **"Edit The System Environment Variable"**
    - Click **"Environment Variables"** under the Startup and Recovery box.
      - You have User environment variables and System environment variables.  I am the only user so I usually just futz with System.  Is this wise?  I dunno. See your local security guru.
    1. Find your python install.
        - This could be a little complicated.  I searched "Python" and right clicked > Open File location.  
        - That led to me a folder of shortcuts. Nifty.  Also unhelpful.  **Right click Python <version> (32 bit)**  It's the shortest filename.
        - Click Properties
        - **Copy the Target** address and paste it back into your File Explorer address bar.  **Delete the filename**(python.exe) and hit Enter to make sure you're in the right place.
          - For reference, it seems to default to C:\Users\<username>AppData\Local\Programs\Python\Python<ver>\ and I'm sure you know how to get to appdata from all that minecraft modding you did in middle school riiiight?
          - Keep an eye out for the Scripts folder there as well.  You'll want that path too for things installed via pip.
    2. **Add your python install folder to PATH**
        - Double-click PATH in System variables (or click once > Edit)
        - Click New in the window that lists locations
        - Paste the address to the folder with python.exe
        - Click New again.
        - Paste the address to the scripts folder (with pip.exe)
    3. **Check your variables for other Python installs.**  Verify that the install has an exe and if it does not, Delete the entry.
4. Tell Windows it really needs to butt out of your programming ~~and MMO launchers~~
    - Search **"alias"** and choose **Manage App Execution Aliases**
    - **Turn off the App Installer** for python.exe, python3.exe, and whatever other pythons you see while you're in there to stop it from launching the Windows Store every time you type python into a command prompt.

python, pip, and any packages such as pyinstaller should all work nicely from the command prompt now.  You can set custom variables for them in the main environment variable window (instead of Editing PATH) but that seems harder to maintain than just pointing it to scripts.
