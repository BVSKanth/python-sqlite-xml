import sqlite3


def create_tables():
    con = sqlite3.connect('../scripts/uncommitted/warehouse.db')
    cur = con.cursor()
    
    cur.execute('''
        DROP TABLE IF EXISTS posts
        ''')
    
    cur.execute('''
            CREATE TABLE IF NOT EXISTS posts (
            Id integer not null primary key,
            PostTypeId integer,
            AcceptedAnswerId integer,
            CreationDate text,
            Score integer,
            ViewCount integer,
            Body text,
			OwnerUserId integer,
			LastEditorUserId integer,
			LastEditDate text,
			LastActivityDate text,
			Title text,
			Tags text,
            AnswerCount integer,
            CommentCount integer,
			FavoriteCount integer,
            ContentLicense text,
            ClosedDate text,
            CommunityOwnedDate text,
            OwnerDisplayName text,
            ParentId integer,
            LastEditorDisplayName text
            )
            ''')
    
    cur.execute('''
        DROP TABLE IF EXISTS tags
        ''')
    
    cur.execute('''
                CREATE TABLE IF NOT EXISTS tags (
                    Id integer not null primary key,
                    TagName text,
                    Count integer,
                    ExcerptPostId integer,
                    WikiPostId integer
                )
                ''')
    
    con.commit()


def insert_record(element, table_name):
    '''
    Convert element to record and insert into table_name
    '''
    
    con = sqlite3.connect('../scripts/uncommitted/warehouse.db')
    placeholders = ''  
    record = {}  
    no_of_cols = len(tuple(element.keys()))
    for i in range(0, no_of_cols):
        placeholders = ''.join(['?,'*no_of_cols]).rstrip(',')
        
        record[element.keys()[i]] = element.attrib[element.keys()[i]]

    insert_sql = (''' INSERT INTO {}(''' + ','.join(tuple(record.keys())) + ') VALUES(' + placeholders + ') '''). \
        format(table_name)

    cur = con.cursor()
    cur.execute(insert_sql, tuple(record.values()))
    con.commit()
    return cur.lastrowid


def read_record(table_name, rowid):
    '''
    Fetch record by rowid
    '''
    
    con = sqlite3.connect('../scripts/uncommitted/warehouse.db')
    cur = con.cursor()
    cur.execute(''' select * from {} where rowid = {}'''.format(table_name, rowid))
    fetch_record = cur.fetchone()
    con.commit()
    return fetch_record


