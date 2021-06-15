from arango import ArangoClient

client = ArangoClient(hosts="http://localhost:8529")

sys_db = client.db('_system', username='root', password='darshit')

if not sys_db.has_database('list'):
    sys_db.create_database('list')

db = client.db('list', username='root', password='darshit')

if not db.has_graph('Graph'):
    db.create_graph('Graph')

Graph = db.graph('Graph')


if not Graph.has_vertex_collection('Actors'):
    Graph.create_vertex_collection('Actors')

Actors = Graph.vertex_collection('Actors')
Actors.truncate()

# ACTORS CREATED
Actors.insert({'_key': 'Salman', 'Name': 'Salman Khan'})
Actors.insert({'_key': 'Sharukh', 'Name': 'Sharukh Khan'})
Actors.insert({'_key': 'Akshay', 'Name': 'Akshay Kumar'})
Actors.insert({'_key': 'Rajkumar', 'Name': 'Rajkumar Rao'})
Actors.insert({'_key': 'Amit', 'Name': 'Amitabh Bachhan'})
Actors.insert({'_key': 'Ayushman', 'Name': 'Ayushman Khurrana'})


if not Graph.has_vertex_collection('Movies'):
    Graph.create_vertex_collection('Movies')

Movies = Graph.vertex_collection('Movies')
Movies.truncate()
# MOVIES CREATED
Movies.insert({'_key': 'khiladi', 'movie': 'ashish'})
Movies.insert({'_key': 'kkk', 'movie': 'Khiladiyo ka khiladi'})
Movies.insert({'_key': 'omg', 'movie': 'Omg'})
Movies.insert({'_key': 'dabang', 'movie': 'Dabangg'})
Movies.insert({'_key': 'race', 'movie': 'Race'})
Movies.insert({'_key': 'karanarjun', 'movie': 'KaranArjun'})
Movies.insert({'_key': 'oso', 'movie': 'Om Shanti Om'})
Movies.insert({'_key': 'zero', 'movie': 'Zero'})
Movies.insert({'_key': 'myname', 'movie': 'MyNameIsKhan'})
Movies.insert({'_key': 'Newton', 'movie': 'Newton'})
Movies.insert({'_key': 'bala', 'movie': 'Bala'})
Movies.insert({'_key': 'Pink', 'movie': 'Pink'})


if not Graph.has_vertex_collection('Directors'):
    Graph.create_vertex_collection('Directors')

Directors = Graph.vertex_collection('Directors')

Directors.truncate()

# DIRECTORS CREATED
Directors.insert({'_key': 'Amar', 'director': 'Amar'})
Directors.insert({'_key': 'umesh', 'director': 'Umesh Shukla'})
Directors.insert({'_key': 'ashish', 'director': 'Ashish R Mohan'})
Directors.insert({'_key': 'aniruddha', 'director': 'Aniruddha Roy Chaudhary'})
Directors.insert({'_key': 'amit', 'director': 'Amit V Masurkar'})
Directors.insert({'_key': 'karan', 'director': 'karanjohar'})
Directors.insert({'_key': 'aanand', 'director': 'Aanand L rai'})
Directors.insert({'_key': 'rakesh', 'director': 'Rakesh Roshan'})
Directors.insert({'_key': 'abhinav', 'director': 'Abhinav Kashyap.'})
Directors.insert({'_key': 'remo', 'director': 'Remo DSouza'})


if not Graph.has_edge_definition('Type1'):
    Graph.create_edge_definition(
        edge_collection='Type1',
        from_vertex_collections=['Actors'],
        to_vertex_collections=['Movies']
    )

Type1 = Graph.edge_collection('Type1')


Type1.truncate()

# CONNECTING EDGES BETWEEN ACTORS AND MOVIES


Type1.insert({'_key': 'Akshay-khiladi',
             '_from': 'Actors/Akshay', '_to': 'Movies/khiladi'})
Type1.insert({'_key': 'Akshay-kkk', '_from': 'Actors/Akshay',
             '_to': 'Movies/khiladi'})
Type1.insert({'_key': 'Akshay-omg', '_from': 'Actors/Akshay',
             '_to': 'Movies/khiladi'})


Type1.insert({'_key': 'Salman-dabangg',
             '_from': 'Actors/Salman', '_to': 'Movies/dabang'})
Type1.insert(
    {'_key': 'Salman-race', '_from': 'Actors/Salman', '_to': 'Movies/race'})
Type1.insert({'_key': 'Salman-karanarjun',
             '_from': 'Actors/Salman', '_to': 'Movies/karanarjun'})


Type1.insert({'_key': 'Sharukh-karanarjun',
             '_from': 'Actors/Sharukh', '_to': 'Movies/karanarjun'})
Type1.insert({'_key': 'Sharukh-oso',
             '_from': 'Actors/Sharukh', '_to': 'Movies/oso'})
Type1.insert({'_key': 'Sharukh-zero',
             '_from': 'Actors/Sharukh', '_to': 'Movies/zero'})
Type1.insert({'_key': 'Sharukh-myname',
             '_from': 'Actors/Sharukh', '_to': 'Movies/myname'})


Type1.insert({'_key': 'Rajukumar-newton',
             '_from': 'Actors/Rajkumar', '_to': 'Movies/Newton'})
Type1.insert({'_key': 'Ayshman-bala',
             '_from': 'Actors/Ayushman', '_to': 'Movies/bala'})
Type1.insert({'_key': 'Amit-pink',
             '_from': 'Actors/Amit', '_to': 'Movies/Pink'})


if not Graph.has_edge_definition('Type2'):
    Graph.create_edge_definition(
        edge_collection='Type2',
        from_vertex_collections=['Movies'],
        to_vertex_collections=['Directors']
    )

Type2 = Graph.edge_collection('Type2')

Type2.truncate()

# CONNECTING EDGES BETWEEN MOVIES AND DIRECTORS

Type2.insert({'_key': 'bala-amar', '_from': 'Movies/bala',
             '_to': 'Directors/Amar'})


Type2.insert({'_key': 'pink-airuddha',
             '_from': 'Movies/Pink', '_to': 'Directors/aniruddha'})


Type2.insert({'_key': 'newton-amit', '_from': 'Movies/Newton',
             '_to': 'Directors/amit'})


Type2.insert({'_key': 'oso-rakesh', '_from': 'Movies/oso',
             '_to': 'Directors/rakesh'})

Type2.insert({'_key': 'karanarjun-rakesh',
             '_from': 'Movies/karanarjun', '_to': 'Directors/rakesh'})

Type2.insert({'_key': 'mnik-karan', '_from': 'Movies/myname',
             '_to': 'Directors/karan'})
Type2.insert({'_key': 'zero-aanand', '_from': 'Movies/zero',
             '_to': 'Directors/aanand'})


Type2.insert({'_key': 'dabangg-abhinav',
             '_from': 'Movies/dabang', '_to': 'Directors/abhinav'})
Type2.insert({'_key': 'race-remo', '_from': 'Movies/race',
             '_to': 'Directors/remo'})


Type2.insert({'_key': 'omg-umesh', '_from': 'Movies/omg',
             '_to': 'Directors/umesh'})
Type2.insert({'_key': 'ashish-ashish',
             '_from': 'Movies/khiladi', '_to': 'Directors/ashish'})
Type2.insert({'_key': 'kkk-umesh', '_from': 'Movies/kkk',
             '_to': 'Directors/umesh'})
