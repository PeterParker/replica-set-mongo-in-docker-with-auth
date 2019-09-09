HOSTNAME=$(hostname)
mongo admin<<EOF
var config = {
    "_id": "set",
    "members": [
        {
            "_id": 0,
            "host": "$HOSTNAME:27017"
        }
    ]
};
rs.initiate(config)
EOF
