from configparser import ConfigParser
def config(filename = 'cogs\\database\\database.ini', section = 'Postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params =parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('section {0} not found in {1} file'.format(section,filename))        
    return db

    