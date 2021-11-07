# Cei Integration Service

## Preparing enviroment

export AMAZON_ACCESS_KEY_ADRIANO=<YOUR_AMAZON_ACCESS_KEY>
export AMAZON_SECRET_KEY_ADRIANO=<YOUR_AMAZON_SECRET_KEY>

## Updating libs

sudo apt install libpq-dev
pip install -r requirements.txt

## Run

### Local

python3 manage.py runserver --noreload

## Run database migrations

python3 manage.py migrate