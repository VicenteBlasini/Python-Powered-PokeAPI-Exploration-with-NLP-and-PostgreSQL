def secrets():
    return {"host": "XXXX", # Insert correct values

            "port": XXXX, # Insert correct values

            "database": "XXXX", # Insert correct values

            "user": "XXXX", # Insert correct values

            "pass": "XXXX"} # Insert correct values


def elastic() :
    return {"host": "www.pg4e.com",
            "prefix" : "elasticsearch",# Insert correct values

            "port": 443, # Insert correct values

            "scheme": "https", # Insert correct values

            "user": "XXXX", # Insert correct values

            "pass": "XXXX"} # Insert correct values

def readonly():
    return {"host": "pg.pg4e.com", # Insert correct values

            "port": 5432,
            "database": "readonly",
            "user": "readonly",
            "pass": "readonly_password"}

# Return a psycopg2 connection string

# import hidden
# secrets = hidden.readonly()
# sql_string = hidden.psycopg2(hidden.readonly())

# 'dbname=pg4e_data user=pg4e_data_read password=pg4e_p_d5fab7440699124 host=pg.pg4e.com port=5432'

def psycopg2(secrets) :
     return ('dbname='+secrets['database']+' user='+secrets['user']+
        ' password='+secrets['pass']+' host='+secrets['host']+
        ' port='+str(secrets['port']))

# Return an SQLAlchemy string

# import hidden
# secrets = hidden.readonly()
# sql_string = hidden.alchemy(hidden.readonly())

# postgresql://pg4e_data_read:pg4e_p_d5fab7440699124@pg.pg4e.com:5432/pg4e_data

def alchemy(secrets) :
    return ('postgresql://'+secrets['user']+':'+secrets['pass']+'@'+secrets['host']+
        ':'+str(secrets['port'])+'/'+secrets['database'])
