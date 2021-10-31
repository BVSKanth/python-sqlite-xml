'Entrypoint to populate the database'
import defusedxml.ElementTree as Et
import db

def to_sql(element, table_name):
    return db.insert_record(element, table_name)

'''
Iterate through posts/tags tree and insert one by one
'''
def iterate_and_insert(table_name):
    if table_name == 'posts':
        element_tree = posts_tree
    elif table_name == 'tags':
        element_tree = tags_tree
    else:
        print("Invalid table name")
        return
    for elem in element_tree.getroot():
        rowid = to_sql(elem, table_name)
    print("Last row from table", table_name)
    print(db.read_record(table_name, rowid))

# Parse xml
posts_tree = Et.parse('../scripts/uncommitted/Posts.xml')  
tags_tree = Et.parse('../scripts/uncommitted/Tags.xml') 

db.create_tables()
iterate_and_insert("posts")
iterate_and_insert("tags")
