# Import Packages
from flask import Blueprint, jsonify, request
from enum import Enum
from os import path

# Import db_operations and psycopg2
from config import create_connection, commit_destroy_connection, psycopg2

# Import select_operations
from operations import GET_ALL, GET_SINGLE, INSERT, UPDATE, DELETE

# Define Blueprint
zone_employee = Blueprint('zone_employee', __name__)

definers = [
    path.basename(__file__)[0:14],
    path.basename(__file__)[0:13]
]

# Get zone_employees
@zone_employee.route('/', methods=['GET'])
def get_zones_employees():
    # Declaration of a List of Records
    list_records = []

    try:
        # Establish the connection and creation of the cursor
        connection = create_connection()
        cur = connection.cursor()

        # Creating the SQL Command
        encoded_command = (
            f"{GET_ALL(definers[0])}")

        cur.execute(encoded_command)

        # Fetching all the records from the cursor
        database_records = cur.fetchall()

        print(database_records)

        # Will store everysingle record in a list formated with a certain format
        for record in database_records:
            dictionary_row = {
                "Zone_Cod": record[0],
                "Zone_Employee": record[1],
                "Zone_Employee_Work_Hour": record[2]
            }
            list_records.append(dictionary_row)

        # Returning the records complete list
        return jsonify({
            "Message": (f"{definers[0]} returned with success!"),
            "Records": list_records
        }), 200

    except (Exception, psycopg2.Error) as error:
        # Convert error to string, break the string on "!"
        error = str(error)
        error = error.split("\n")

        return jsonify({
            "Message": {
                "Message": (f"There was an error getting the {definers[0]}!"),
                "Error": error[0]
            }
        }), 500
    finally:
        # commiting and closing database connection.
        if(connection):
            commit_destroy_connection(connection, cur)

# Get zone_employees
@zone_employee.route('/<cod_zone>', methods=['GET'])
def get_zone_employees(cod_zone):
    try:
        # Establish the connection and creation of the cursor
        connection = create_connection()
        cur = connection.cursor()

        # Creating the SQL Command
        encoded_command = (
            f"{GET_SINGLE(definers[1],cod_zone)}")

        print(encoded_command)

        cur.execute(encoded_command)

        # Fetching all the records from the cursor
        database_record = cur.fetchall()

        print(database_record)

        # Returning the records complete list
        return {
            "Message": (f"{definers[1]} returned with success!"),
            "Record": database_record
        }, 200

    except (Exception, psycopg2.Error) as error:

        # Convert error to string, break the string on "!"
        error = str(error)
        error = error.split("\n")

        return jsonify({
            "Message": {
                "Message": (f"There was an error getting the {definers[1]}!"),
                "Error": error[0]
            }
        }), 500
    finally:
        # commiting and closing database connection.
        if(connection):
            commit_destroy_connection(connection, cur)

    try:
        # Establish the connection and creation of the cursor
        connection = create_connection()
        cur = connection.cursor()

        # Creating the SQL Command
        encoded_command = (
            f"{GET_SINGLE(definers[1],cod_zone)}")

        print(encoded_command)

        cur.execute(encoded_command)

        # Fetching all the records from the cursor
        database_record = cur.fetchall()

        print(database_record)

        # Returning the records complete list
        return {
            "Message": (f"{definers[1]} returned with success!"),
            "Record": database_record
        }, 200

    except (Exception, psycopg2.Error) as error:

        # Convert error to string, break the string on "!"
        error = str(error)
        error = error.split("\n")

        return jsonify({
            "Message": {
                "Message": (f"There was an error getting the {definers[1]}!"),
                "Error": error[0]
            }
        }), 500
    finally:
        # commiting and closing database connection.
        if(connection):
            commit_destroy_connection(connection, cur)

# Post zone_employee
@zone_employee.route('/', methods=['POST'])
def post_zone_employee():
    try:
        # Establish the connection and creation of the cursor
        connection = create_connection()
        cur = connection.cursor()

        # Get the Data as Json
        data_json = request.get_json()

        # Encode to "" instead of '
        data_json = str(data_json).replace("'", '"')

        # Creating the SQL Command
        encoded_command = (
            f"{INSERT(definers[1], data_json)}")

        print(encoded_command)

        # Executing the SQL Command
        cur.execute(encoded_command)

        return jsonify({
            "Message": (f"{definers[1]} created with success!")
        }), 201

    except (Exception, psycopg2.Error) as error:

        # Convert error to string, break the string on "!"
        error = str(error)
        error = error.split("\n")

        return jsonify({
            "Message": {
                "Message": (f"There was an error creating the {definers[1]}!"),
                "Error": error[0]
            }
        }), 500
    finally:
        # commiting and closing database connection.
        if(connection):
            commit_destroy_connection(connection, cur)

# Put zone_employee
@zone_employee.route('/<cod_zone>', methods=['PUT'])
def put_zone_employee(cod_zone):
    try:
        # Establish the connection and creation of the cursor
        connection = create_connection()
        cur = connection.cursor()

        # Get the Data as Json
        data_json = request.get_json()

        # Encode to "" instead of '
        data_json = str(data_json).replace("'", '"')

        # Creating the SQL Command
        encoded_command = (
            f"{UPDATE(definers[1], cod_zone, data_json)}")

        print(encoded_command)

        # Executing the SQL Command
        cur.execute(encoded_command)

        return jsonify({
            "Message": (f"{definers[1]} updated with success!")
        }), 201

    except (Exception, psycopg2.Error) as error:

        # Convert error to string, break the string on "!"
        error = str(error)
        error = error.split("\n")

        return jsonify({
            "Message": {
                "Message": (f"There was an error creating the {definers[1]}!"),
                "Error": error[0]
            }
        }), 500
    finally:
        # commiting and closing database connection.
        if(connection):
            commit_destroy_connection(connection, cur)

# Delete zone_employee
@zone_employee.route('/<cod_zone>', methods=['DELETE'])
def delete_zone_employee(cod_zone):
    try:
        # Establish the connection and creation of the cursor
        connection = create_connection()
        cur = connection.cursor()

        # Creating the SQL Command
        encoded_command = (
            f"{DELETE(definers[1],cod_zone)}")

        cur.execute(encoded_command)

        # Returning the records complete list
        return {
            "Record": (f"{definers[1]} was deleted with success!")
        }, 200

    except (Exception, psycopg2.Error) as error:

        # Convert error to string, break the string on "!"
        error = str(error)
        error = error.split("\n")

        return jsonify({
            "Message": {
                "Message": (f"There was an error deleting the {definers[1]}!"),
                "Error": error[0]
            }
        }), 500
    finally:
        # commiting and closing database connection.
        if(connection):
            commit_destroy_connection(connection, cur)
