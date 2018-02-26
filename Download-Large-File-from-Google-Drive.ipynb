{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#taken from this StackOverflow answer: https://stackoverflow.com/a/39225039\n",
    "import requests\n",
    "\n",
    "def download_file_from_google_drive(id, destination):\n",
    "    URL = \"https://docs.google.com/uc?export=download\"\n",
    "\n",
    "    session = requests.Session()\n",
    "\n",
    "    response = session.get(URL, params = { 'id' : id }, stream = True)\n",
    "    token = get_confirm_token(response)\n",
    "\n",
    "    if token:\n",
    "        params = { 'id' : id, 'confirm' : token }\n",
    "        response = session.get(URL, params = params, stream = True)\n",
    "\n",
    "    save_response_content(response, destination)    \n",
    "\n",
    "def get_confirm_token(response):\n",
    "    for key, value in response.cookies.items():\n",
    "        if key.startswith('download_warning'):\n",
    "            return value\n",
    "\n",
    "    return None\n",
    "\n",
    "def save_response_content(response, destination):\n",
    "    CHUNK_SIZE = 32768\n",
    "\n",
    "    with open(destination, \"wb\") as f:\n",
    "        for chunk in response.iter_content(CHUNK_SIZE):\n",
    "            if chunk: # filter out keep-alive new chunks\n",
    "                f.write(chunk)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "file_id = '0B1fGSuBXAh1IeEpzajRISkNHckU'\n",
    "destination = '/home/myusername/work/myfile.ext'\n",
    "download_file_from_google_drive(file_id, destination)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
