from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import sqlite3 as sql

app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = "AIzaSyCEpaTXYc8aZyP4tysJNvT8amHd8WgP7QA"

GoogleMaps(app, key="AIzaSyCEpaTXYc8aZyP4tysJNvT8amHd8WgP7QA")

@app.route("/")
def Index():
    return render_template('Index.html')

@app.route("/map")
def map():
    return render_template('map.html')

@app.route("/markermap")
def markermap():
    return render_template('markermap.html')

@app.route('/markermaps', methods = ['POST'])
def markermaps():
    con = sql.connect("database4.db")
    my = request.form['yup']
    cur = con.cursor()

    query = ("Select latitude from register where area = '{my}'"). format(my=my)
    cur.execute(query)
    lat1 = cur.fetchone();
    latitude = str(lat1)
    latitude1 = latitude[2:-3]
    

    query1 = ("Select longitude from register where area = '{my}'"). format(my=my)
    cur.execute(query1)
    N = cur.fetchone();
    longitude = str(N)
    longitude1 = longitude[2:-3]
    print(latitude1)
    print(longitude1)
    return render_template('markermaps.html', latitude1=latitude1, longitude1=longitude1)

@app.route("/doublemarkermap")
def doublemarkermap():
    return render_template('doublemarkermap.html')
 
@app.route("/doublemarkermaps", methods = ['POST'])
def doublemarkermaps():
    con = sql.connect("database4.db")
    my = request.form['yup']
    mine = request.form['yupiee']
    cur = con.cursor()

    query = ("Select latitude from register where area = '{my}'"). format(my=my)
    cur.execute(query)
    lat1 = cur.fetchone();
    latitude = str(lat1)
    latitude1 = latitude[2:-3]
    

    query1 = ("Select longitude from register where area = '{my}'"). format(my=my)
    cur.execute(query1)
    N = cur.fetchone();
    longitude = str(N)
    longitude1 = longitude[2:-3]

    query2 = ("Select latitude from register where area = '{mine}'"). format(mine=mine)
    cur.execute(query2)
    lat2 = cur.fetchone();
    lattoo = str(lat2)
    latitude2 = lattoo[2:-3]
    

    query3 = ("Select longitude from register where area = '{mine}'"). format(mine=mine)
    cur.execute(query3)
    S = cur.fetchone();
    loongi = str(S)
    longitude2 = loongi[2:-3]
    print(latitude1)
    print(longitude1)
    print(latitude2)
    print(longitude2)
    return render_template('doublemarkermaps.html', latitude1=latitude1, longitude1=longitude1, latitude2=latitude2, longitude2=longitude2)

@app.route("/another")
def another():
    return render_template('another.html')

@app.route("/movingmap")
def movingmap():
    mymap = Map(
        identifier="movingmap_markers",
        lat=37.4419,
        lng=-122.1419,
        markers=[{'lat': 37.4419, 'lng': -122.1419}]
    )
    return render_template('movingmap.html')

@app.route("/clustermap")
def clustermap():
    mymap = Map(
        identifier="cluster-map",
        lat=37.4419,
        lng=-122.1419,
        markers=[{'lat': 37.4419, 'lng': -122.1419}, {'lat': 37.4500, 'lng': -122.1419}, {'lat': 36.4419, 'lng': -120.1419}]
        #marker_Cluster=True,
        #cluster_gridsize=10
    )
    return render_template('clustermap.html', clustermap=clustermap)

@app.route('/simplemap', methods = ['POST'])
def simplemap():
    con = sql.connect("database4.db")
    my = request.form['yup']
    cur = con.cursor()

    query = ("Select latitude from register where area = '{my}'"). format(my=my)
    cur.execute(query)
    lat1 = cur.fetchone();
    latitude = str(lat1)
    latitude1 = latitude[2:-3]
    

    query1 = ("Select longitude from register where area = '{my}'"). format(my=my)
    cur.execute(query1)
    N = cur.fetchone();
    longitude = str(N)
    longitude1 = longitude[2:-3]
    print(latitude1)
    print(longitude1)
    return render_template('map.html', latitude1=latitude1, longitude1=longitude1)



if __name__ == '__main__':
   app.run(debug=True)
