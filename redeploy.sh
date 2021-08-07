cd server
gcloud builds submit --tag gcr.io/flask-homepage-test/flask-fire
gcloud beta run deploy --image gcr.io/flask-homepage-test/flask-fire
cd ..
./node_modules/.bin/firebase deploy

