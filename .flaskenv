#.flaskenv
FLASK_APP=app.py
FLASK_RUN_PORT=8080
LOCAL=1
INSTANCE_HOST=34.133.150.10
INSTANCE_CONNECTION_NAME=advance-branch-351506:us-central1:truesight-database
INSTANCE_UNIX_SOCKET=/cloudsql/advance-branch-351506:us-central1:truesight-database
DB_USER=developer
DB_PASS=googlesql@bangkit2022
DB_NAME=true-sight
DB_PORT=3306
BUCKET_NAME=truesight-bucket
MODEL_PATH=gs://truesight-bucket/model-indobert-base-p1-87
TOKENIZER_PATH=gs://truesight-bucket/indobert-base-p1-tokenizer-87.pickle