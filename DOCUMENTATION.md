API Documentation
=================


'Fleet' Model API
-----------------
---------------------
**Request Type**: GET

**Description**: List/retrieve the 'fleets' table result(-s)

**API Query Parameters**:
* **offset** -> starting offset for results retrieval
* **limit**  -> limiting number of results retrieval up to maximum limit
* **name**   -> retrieving fleets with name containing queried name pattern
~~~~~~~~~~~~~~~~~~~~~~~~~~
    URL: {host-url}/fleets/
    URL: {host-url}/fleets/id/
~~~~~~~~~~~~~~~~~~~~~~~~~~

----------------------
**Request Type**: POST

**Description**: Add new row to the 'fleets' table
~~~~~~~~~~~~~~~~~~~~~~~~~~
    URL: {host-url}/fleets/
    
    Request Body:
    {
        "name": "City name" ('fleet' name)
    }

    Required Fields: name
~~~~~~~~~~~~~~~~~~~~~~~~~~

----------------------
**Request Type**: PATCH

**Description**: Update existing the 'fleets' table row
~~~~~~~~~~~~~~~~~~~~~~~~~~
    URL: {host-url}/fleets/id/

    Request Body:
    {
        "name": "New city name" (updated 'fleet' name)
    }
~~~~~~~~~~~~~~~~~~~~~~~~~~

----------------------
**Request Type**: DELETE

**Description**: Remove the row from the 'fleets' table

~~~~~~~~~~~~~~~~~~~~~~~~~~
    URL: {host-url}/fleets/id/
~~~~~~~~~~~~~~~~~~~~~~~~~~

'Bike' Model API
-----------------
---------------------
**Request Type**: GET

**Description**: List/retrieve the 'bikes' table result(-s)

**API Query Parameters**:
* **offset** -> starting offset for results retrieval
* **limit**  -> limiting number of results retrieval up to maximum limit
* **fleet**   -> retrieving bikes with related fleet ids (exact lookup)
* **status**   -> retrieving bikes according to queried status: either 'unlocked' or 'locked' (exact lookup)
* **latitude**   -> retrieving bikes located on queried latitude (exact lookup)
* **longitude**   -> retrieving bikes located on queried longitude (exact lookup)
~~~~~~~~~~~~~~~~~~~~~~~~~~
    URL: {host-url}/bikes/
    URL: {host-url}/bikes/id/
~~~~~~~~~~~~~~~~~~~~~~~~~~

----------------------
**Request Type**: POST

**Description**: Add new row to the 'bikes' table
~~~~~~~~~~~~~~~~~~~~~~~~~~
    URL: {host-url}/bikes/
    
    Request Body:
    {
        "fleet": "FL_004", (related 'fleet' id)
        "status": "unlocked", (bike status -> either 'locked' or 'unlocked')
        "location": {
            "latitude": "-52.0939846102364761", (bike location's latitude) 
            "longitude": "-160.0939846102364" (bike location's longitude)
        }
    }

    Required Fields: status, location (whole JSON Object)
~~~~~~~~~~~~~~~~~~~~~~~~~~

----------------------
**Request Type**: PATCH

**Description**: Update existing the 'bikes' table row
~~~~~~~~~~~~~~~~~~~~~~~~~~
    URL: {host-url}/bikes/id/

    Request Body:
    {
        "fleet": "FL_005", (updated 'fleet' id relation)
        "status": "locked", (updated bike status -> either 'locked' or 'unlocked')
        "location": {
            "latitude": "52.0939846102364761", (updated bike location's latitude)
            "longitude": "16.0939846102364" (updated bike location's longitude)
        }
    }
~~~~~~~~~~~~~~~~~~~~~~~~~~

----------------------
**Request Type**: DELETE

**Description**: Remove the row from the 'bikes' table

~~~~~~~~~~~~~~~~~~~~~~~~~~
    URL: {host-url}/bikes/id/
~~~~~~~~~~~~~~~~~~~~~~~~~~
