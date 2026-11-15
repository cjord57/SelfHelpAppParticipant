"""
    LIFEGUARD COMMUNITY
    Date: 01/30/2025
    DePaul University

    EDITOR: Corey Jordan-Zamora

    DESC: Flask app for participant that allows database connection. This app handles retrieving Participant profile information
"""

# Participant File General Framework: Flask App
# For Sprint 2

# Edit 2/13/25: Commented out additional items (some personal information identifiers, answers to questions, modules and progress tracking, etc.), as we are only focused on getting the Participant connected to the database; the other items are backlogged
# Edit 2/19/25: Completely removed those comments of the obsolete items^
# Edit 2/27/25: Added code to retrieve ALL participants
# IMPORTANT: This FlaskParticipant.py file might just be obsolete since we already have a Flask app that contains all the different functionalities for all the objects. We don't need to have this file when we already have an encompassing Flask app

from flask import Flask, request, jsonify
import mysql.connector # To connect to MariaDB in order to retrieve participant information
import Participant

app = Flask(__name__)

# Database configuration (our MariaDB connection details)
db_config = {
    'host': 'lifeguarddb.cn284c0kopag.us-east-2.rds.amazonaws.com',
    'user': 'admin',
    'password': 'L1f3Gr3eNC0m^',
    'database': 'lifeguarddb'
}

# Helper function to get the database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Helper function to get participant by ID from MariaDB
def get_participant_by_id(participant_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM participants WHERE participant_id = %s', (participant_id,))
    result = cursor.fetchone()
    
    cursor.close()
    connection.close()

    if result:
        return Participant(
            participant_id=result['participant_id'],
            name=result['name'],
            email=result['email'],
        )
    return None

# Helper function to get all participants from MariaDB
def get_all_participants():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM participants')
    result = cursor.fetchall() # Fetch all rows

    cursor.close()
    connection.close()

    participants = []
    for row in result:
        participants.append(Participant(
            participant_id=row['participant_id'],
            name=row['participant_name'],
            email=row['participant_email'],
        ))
    
    return participants

# Endpoint to get participant profile by ID
@app.route('/api/participant/<int:participant_id>', methods=['GET'])
def get_participant(participant_id):
    participant = get_participant_by_id(participant_id)
    if participant:
        # Return participant profile as JSON
        profile = {
            'name': participant.name,
            'email': participant.email,
        }
        return jsonify(profile)
    else:
        return jsonify({'error': 'Participant not found'}), 404

# Endpoint to get all participant profiles
@app.route('/api/participants', methods=['GET'])
def get_participants():
    participants = get_all_participants()
    if participants:
        # Return list of participants as JSON
        profiles = []
        for participant in participants:
            profiles.append({
                'name': participant.name,
                'email': participant.email,
            })
        return jsonify(profiles)
    else:
        return jsonify({'error': 'No participants found'}), 404

if __name__ == '__main__':
    app.run(debug=True)