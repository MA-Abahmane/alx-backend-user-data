#!/usr/bin/env bash

# Terminal 1
python app.py


# Terminal 2
curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
    # < ....
    # {"email": "bob@me.com", "message": "user created"}
    # * Closing connection 0


curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
    # < ....
    # {"message":"email already registered"}
    # * Closing connection 0
