# Download-Large-File-From-Google-Drive-Using-Python

This is a simple yet effective method to download LARGE files from google drive using Python
I have only tried it with Python 3.6
I have NOT tried it with Folders instead of Files

I have only taken the python code in [this stackoverflow answer](https://stackoverflow.com/a/39225039) and put it in a IPython Notebook

All you need to do is this:
1) Get the file ID of your file on Google Drive (i.e. from the sharable link)
2) Paste the file ID in file_id
3) Specify the full path of where you want to save the downloaded file
4) call the function download_file_from_google_drive(file_id, destination)

## Example:
```
file_id = '0B6lEo20DNMISIJDSJDVBMENXbkE'
destination = '/home/myusername/work/myfile.ext'
download_file_from_google_drive(file_id, destination)
```
