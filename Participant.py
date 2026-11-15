"""
    LIFEGUARD COMMUNITY
    Date: 01/30/2025
    DePaul University

    EDITOR: Corey Jordan-Zamora

    DESC: Code for participant that stores their profile information and keeps track of their modules in their learning journey.
"""

from obj_interface import Object

# Participant File General Framework
# For Sprint 1

# Edit 2/13/25: Commented out additional items (some personal information identifiers, answers to questions, modules and progress tracking, etc.), as we are only focused on getting the Participant connected to the database; the other items are backlogged
# Edit 2/19/25: Completely removed those comments of the obsolete items^
# Good news: As of 3/3/25, we have gotten participants successfully retrieved

class Participant(Object):
    def __init__(self, name, email, participant_id = ""):
        # Personal Information
        self.participant_id = participant_id
        self.participant_name = name
        self.participant_email = email

    def __eq__(self, other):
        """Equality check for Participants."""
        if isinstance(other, Participant):
            return (self.participant_id == other.participant_id and
                    self.participant_name == other.participant_name and
                    self.participant_email == other.participant_email)
        return False

    def __repr__(self):
        return f"Participant(ID={self.participant_id}, Name={self.participant_name}, Email={self.participant_email})"

    def to_dict(self):
        return {
            "participant_id": self.participant_id,
            "participant_name": self.participant_name,
            "participant_email": self.participant_email
        }

    def display_profile(self):
        """Display the participant's profile and basic information."""
        print(f"Participant ID: {self.participant_id}")
        print(f"Name: {self.participant_name}")
        print(f"Email: {self.participant_email}")

    def getType(self):
        """Returns the type of the participant."""
        return "1005"

    def setID(self,id):
        """sets the ID"""
        self.participant_id = id

    def viewModule(self, module_id):
        """Allow the participant to view a specific module."""
        print(f"Viewing module {module_id}...")
        # Simulating module content for demonstration
        module_content = {
            'Module 1': 'Building Your Support Network',
            'Module 2': 'Navigating Life\'s Transitions',
            'Module 3': 'Overcoming Personal Barriers',
            'Module 4': 'Effective Communication Skills'
        }
        print(f"Module content: {module_content.get(module_id, 'Module not found.')}")

    # Flask-login required properties
    @property
    def is_active(self):
        """Return True since Participants are always active users."""
        return True

    @property
    def is_authenticated(self):
        """Return True since Participants are always considered authenticated."""
        return True

    @property
    def is_anonymous(self):
        """Participants are never anonymous."""
        return False

    def get_id(self):
        return str(self.participant_id) # Must return a string for Flask-Login
    
    def get_name(self):
        return str(self.name) # Must return a string for Flask-Login
    
    def get_email(self):
        return str(self.email) # Must return a string for Flask-Login