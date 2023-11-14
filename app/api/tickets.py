from flask import Blueprint, request, jsonify
from app import db
from app.models.ticket import Ticket

# Creación del Blueprint 'tickets'
tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route('/tickets', methods=['POST'])
def create_ticket():
    # Lógica para crear un ticket
    data = request.get_json()
    new_ticket = Ticket(
        description=data['description'],
        state=data['state'],
        client_id=data['client_id']
    )
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify(new_ticket.to_dict()), 201

@tickets_bp.route('/tickets', methods=['GET'])
def get_tickets():
    # Lógica para obtener todos los tickets
    all_tickets = Ticket.query.all()
    return jsonify([ticket.to_dict() for ticket in all_tickets]), 200

@tickets_bp.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    # Lógica para obtener un ticket específico
    ticket = Ticket.query.get_or_404(ticket_id)
    return jsonify(ticket.to_dict()), 200

@tickets_bp.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    # Lógica para actualizar un ticket específico
    ticket = Ticket.query.get_or_404(ticket_id)
    data = request.get_json()
    ticket.description = data.get('description', ticket.description)
    ticket.state = data.get('state', ticket.state)
    db.session.commit()
    return jsonify(ticket.to_dict()), 200

@tickets_bp.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    # Lógica para eliminar un ticket específico
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    return jsonify({'message': 'Ticket deleted successfully.'}), 200

# Método auxiliar para convertir un modelo a diccionario
def to_dict(self):
    return {
        'id': self.id,
        'description': self.description,
        'state': self.state,
        'client_id': self.client_id
    }