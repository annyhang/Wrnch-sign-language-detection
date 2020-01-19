#!/usr/bin/python

import requests
import json
import time
import wow #determines the letter

def cloudAPI():
    LOGIN_URL = 'https://api.wrnch.ai/v1/login'
    JOBS_URL = 'https://api.wrnch.ai/v1/jobs'

    #Save the Cloud API key
    API_KEY = "fd51ce79-9d9a-4cee-82eb-b546d4e1bcbc"

    resp_auth = requests.post(LOGIN_URL,data={'api_key':API_KEY})
    #print(resp_auth.text)
    # the jwt token is valid for an hour
    JWT_TOKEN = json.loads(resp_auth.text)['access_token']

    return JWT_TOKEN, LOGIN_URL, JOBS_URL

def process(filename, JWT_TOKEN, LOGIN_URL, JOBS_URL):
    filename += '.png'
    #open file as byte stream
    with open(filename, 'rb') as f:
        resp_sub_job = requests.post(JOBS_URL,
                                     headers={'Authorization':f'Bearer {JWT_TOKEN}'},
                                     files={'media':f},
                                     data={'work_type':'json', 'hands':'true'}
                                    )
        
    #send post request with authentification and the file
    job_id = json.loads(resp_sub_job.text)['job_id']
    #print('Status code:',resp_sub_job.status_code)
    #print('Response:',resp_sub_job.text)

    #delay next step so that image can have time to process
    time.sleep(3)

    #retrieve the information from the json file and get the letter

    GET_JOB_URL = JOBS_URL + '/' +job_id
    #print(GET_JOB_URL)
    resp_get_job = requests.get(GET_JOB_URL,headers={'Authorization':f'Bearer {JWT_TOKEN}'})
    return wow.init(json.loads(resp_get_job.text))

if __name__ == '__main__':
    key, log, job = cloudAPI()

    word = process('a', key, log, job)
    word = process('b', key, log, job)
    word = process('c', key, log, job)

