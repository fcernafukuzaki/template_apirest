# TEMPLATE API REST
API REST service template.

## Installation
### WINDOWS
#### Database variables
```sh
set DATABASE_USER=<USER_NAME>
set DATABASE_PASSWORD=<USER_PASSWORD>
set DATABASE_HOST=<DATABASE_HOSTNAME>
set DATABASE_NAME=<DATABASE_NAME>
```

#### Model variables
```sh
set MODEL_CHECKPOINT=<MODEL_CHCKPOINT_NAME>
set MODEL_SAVE_NAME=<MODEL_FILE_NAME>
```

#### API KEY variable
```sh
set API_KEY=<API_KEY>
```

### LINUX
#### Database variables
```sh
export DATABASE_USER=<USER_NAME>
export DATABASE_PASSWORD=<USER_PASSWORD>
export DATABASE_HOST=<DATABASE_HOSTNAME>
export DATABASE_NAME=<DATABASE_NAME>
```

#### Model variables
```sh
export MODEL_CHECKPOINT=<MODEL_CHCKPOINT_NAME>
export MODEL_SAVE_NAME=<MODEL_FILE_NAME>
```

#### API KEY variable
```sh
export API_KEY=<API_KEY>
```

## Run API
```sh
cd apirest/
python3 app.py
```

## Development
### WINDOWS
```sh
python -m venv .\venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### LINUX
```sh
python3 -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

## Testing from localhost
Example to invoke API REST from CMD.
```sh
curl -X POST http://localhost:5000/api/v1/predict -H "X-Api-Key: <API_KEY>" -H "Content-Type: application/json" -d "{\"message\":\"Message.\"}"
```

Example to invoke API REST using JavaScript.
```sh
fetch('http://localhost:5000/api/v1/predict', {
  method: "POST",
  headers: {"Content-type": "application/json;charset=UTF-8", "X-Api-Key": <API_KEY>},
  body:JSON.stringify({"message":"Message."})
}).then(response => response.json()).then(json => console.log(json)).catch(err => console.log(err));
```
