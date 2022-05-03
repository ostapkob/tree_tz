This project convert json to table and table to json
  
```
json  ->  table  ->  postgres -> table  ->  json 
                                ├─> level  ├─> level
                                └─> file   └─> file
```


### input in postgresql:
        psql;
        CREATE USER vladlink WITH PASSWORD 'vladlink' CREATEDB;
        CREATEDB menu;

### input in folder:
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

