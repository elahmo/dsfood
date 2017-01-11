function getCode(code) {
  return PCOLIST.filter(
      function(data){ return data.onscode == code }
  );
}

var DiabetesChoropleth = {
  init: function(div, year) {
    this.div = div;
    this.map = L.map(this.div).setView([53.0, -1.5], 7);
    window.map = this.map;
    
    L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.{ext}', {
      attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      subdomains: 'abcd',
      minZoom: 0,
      maxZoom: 20,
      ext: 'png'
    }).addTo(this.map);

    window.info = L.control();

    window.info.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info');
        this.update();
        return this._div;
    };

    window.info.update = function (props) {
        // console.log(props);
        this._div.innerHTML = '<h4>Obesity cases per region</h4>' +  (props ?
            '<b>' + props.ccg_name + '</b><br /><b>' + props.registered_patients + '</b> obesity cases' +
            '</b><br /><b>' + props.cases_per_100k + ' </b>cases per 100k'
            : 'Hover over a region');
    };

    window.info.addTo(this.map);

    if (!year){
        year = '2015';
    }
    if (year == '2013'){
        mergedFeatureLayer(this.map, "/static/csv/map_health"+year+".csv", "/static/js/ukla.json", "LAD13CD", this.style, null, null, "lad", true);

    }else{
        mergedFeatureLayer(this.map, "/static/csv/map_health"+year+".csv", "/static/js/ukboundaries.json", "ccg_code", this.style, null, null, "ccg_boundaries");
    }
    addLegend([0, 100, 200, 300, 400, 500, 600, 800, 1000, 1500, ''], this.map, this.color);

  },
  
  destroy: function() {
    this.map.remove();
  },
  
  refresh: function(year) {
    this.destroy();
    this.init(this.div, year);
  },
  
  color: function(d) {
    if (typeof(d) == 'string') {
        d = d.replace(',','');
    }
    if (d == 'NA'){ return '#000000'}
    else if (d == 'undefined'){ return '#ffffff'}
    else if (d > 1500){ return '#340007'}
    else if (d > 1000){ return '#67000d'}
    else if (d > 800){ return '#a50f15'}
    else if (d > 600){ return '#cb181d'}
    else if (d > 500){ return '#ef3b2c'}
    else if (d > 400){ return '#fb6a4a'}
    else if (d > 300){ return '#fc9272'}
    else if (d > 200){ return '#fcbba1'}
    else if (d > 100){ return '#fee0d2'}
    else {return '#ffe4d7'};
            
  },
  style: function(feature) {
    return {
      fillColor: DiabetesChoropleth.color(feature.properties.cases_per_100k),
      weight: 1.5,
      opacity: 1,
      color: 'white',
      dashArray: '2',
      fillOpacity: 0.8
    }
  },
  
  defaultStyle: function(feature) {
    return {
      outlineColor: "#f44336",
      outlineWidth: 0.5,
      weight: 1,
      opacity: 1,
      fillOpacity: 0
    };
  },

}


function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: 'red',
        dashArray: '',
        fillOpacity: 0.6
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }

    window.info.update(layer.feature.properties);
}

function resetHighlight(e) {
    window.geojson.resetStyle(e.target);
    window.info.update();
}

window.zoomed = false;
function zoomToFeature(e) {
    if (window.zoomed == false){
       window.zoomed = true;
       window.map.fitBounds(e.target.getBounds()); 
    } else {
       window.map.setView([53.0, -1.5], 7)
       window.zoomed = false;
    } 
    
}

window.onEachFeature = function(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
    });
};

function addInfo(map, callback) {

    var info = L.control();

    info.onAdd = function (map) {

        this._div = L.DomUtil.create('div', 'info');
        this.update();
        return this._div;
    };

    info.update = function (props) {
        if (props) {
            this._div.innerHTML = callback(props);
        } else {
            this._div.innerHTML = "Hover over map";
        }
    };

    info.addTo(map);
    map.info = info;
};



function addLegend(gradesParam, map, color) {

    var legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {

        this._div = L.DomUtil.create('div', 'info legend'),
            grades = gradesParam,
            labels = [];

        // loop through our density intervals and generate a label with a colored square for each interval
        for (var i = 0; i < grades.length - 1; i++) {
            this._div.innerHTML +=
                '<i style="background:' + color(grades[i] + 1) + '"></i> ' +
                    grades[i] + ' &ndash; ' + grades[i + 1] + '<br>';
        }
        return this._div;
    };

    legend.addTo(map);
};


function addCategoricalLegend(categories, map, categoricalColor) {
    var legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {

        this._div = L.DomUtil.create('div', 'info legend'),
            grades = categories,
            labels = [];

        // loop through categories and generate a label with a colored square for each category
        for (var i = 0; i < grades.length; i++) {
            this._div.innerHTML +=
                '<i style="background:' + categoricalColor(grades[i]) + '"></i> ' +
                    grades[i] + '<br>';
        }
        return this._div;
    };

    legend.addTo(map);
};

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

//helper functions
var mergedFeatureLayer = function mergedFeatureLayer(map, csvDir, jsonDir, joinFieldKey, style, onEachFeature, pointToLayer, featureObject, conversion) {

    var buildingData = jQuery.Deferred();

    d3.csv(csvDir, function (csv) {

        if (csv) {
            jQuery.ajax(
                {
                    url: jsonDir,
                    async: false,
                    data: 'json',

                    success: function (data) {
                        var pcts = topojson.feature(data, data.objects[featureObject])
                        features = pcts.features;
                        data.features = processData(csv, features, joinFieldKey);
                        buildingData.resolve(data);
                    },
                    error: function (xhr, ajaxOptions, thrownError) {
                        console.log(xhr.status + " - " + thrownError);
                    }
                });
        }
        else {
            console.log("Error loading CSV data");
        }
    });

    buildingData.done(function (d) {
        var mergedLayer = L.geoJson(d, {style: style, onEachFeature: window.onEachFeature, pointToLayer: pointToLayer}).addTo(map);
        // console.log("Loading merged data: "+csvDir+" and "+jsonDir);
        window.geojson = mergedLayer;
        mergedLayer.bringToFront();

    });
};

var mergedClusteredMarkers = function mergedClusteredMarkers(map, csvDir, jsonDir, joinFieldKey, style, onEachFeature, pointToLayer, featureObject, iconFeature, addPopup, getCustomIcon) {

    var buildingData = jQuery.Deferred();

    d3.csv(csvDir, function (csv) {

        if (csv) {
            jQuery.ajax(
                {
                    url: jsonDir,
                    async: false,
                    data: 'json',

                    success: function (data) {
                        var pcts = topojson.feature(data, data.objects[featureObject])
                        features = pcts.features;
                        data.features = processData(csv, features, joinFieldKey);
                        buildingData.resolve(data);
                    },
                    error: function (xhr, ajaxOptions, thrownError) {
                        console.log(xhr.status + " - " + thrownError);
                    }
                });
        }
        else {
            console.log("Error loading CSV data");
        }
    });

    buildingData.done(function (d) {
        var markers = new L.MarkerClusterGroup({
            maxClusterRadius: 25,
            disableClusteringAtZoom: 10,
            iconCreateFunction: function (cluster) {
                return L.divIcon({
                    html: '<span style="display:inline-block; vertical-align:middle">'+ cluster.getChildCount()+' </span>',
                    className: 'mycluster',
                    iconSize: null
                });
            },
            spiderfyOnMaxZoom: true,
            showCoverageOnHover: false,
            zoomToBoundsOnClick: true
        });

        for (var i = 0; i < d.features.length; i++) {
            var a = d.features[i].geometry.coordinates;
            var properties = d.features[i].properties;
            var marker = new L.Marker(new L.LatLng(a[1], a[0]), {
                icon: getCustomIcon(properties[iconFeature]) });
            marker.bindPopup(addPopup(properties));
            markers.addLayer(marker);
        }
        markers.addTo(map);
    });
};


function processData(csvData, features, joinKey) {
    var joinFieldObject = {};

    jQuery.each(features, function (index, object) {

        joinFieldObject[joinKey] = object.properties[joinKey];

        var csv_data = _.findWhere(csvData, joinFieldObject);
        jQuery.extend(object.properties, csv_data);
    });
    return features;
};

var featureLayer = function featureLayer(map, jsonDir, defaultStyle, featureObject) {
    var layer = L.geoJson(null, { style: defaultStyle});
    // console.log("Loading feature data: "+jsonDir);
    map.addLayer(layer);
    d3.json(jsonDir, function (error, data) {
        var pcts = topojson.feature(data, data.objects[featureObject]);
        var geojsonLayer = L.geoJson(pcts, {style: defaultStyle}).addTo(map);
        geojsonLayer.bringToBack();
    });
};

/* Function that is used to estimate the width of the custom tooltip */
function measureText(pText, pFontSize, pStyle) {
    var lDiv = document.createElement('lDiv');

    document.body.appendChild(lDiv);

    if (pStyle != null) {
        lDiv.style = pStyle;
    }
    lDiv.style.fontSize = "" + pFontSize + "px";
    lDiv.style.position = "absolute";
    lDiv.style.left = -1000;
    lDiv.style.top = -1000;

    lDiv.innerHTML = pText;

    var lResult = {
        width: lDiv.clientWidth,
        height: lDiv.clientHeight
    };

    document.body.removeChild(lDiv);
    lDiv = null;

    return lResult;
}