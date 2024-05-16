from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gimnasio.db'
db = SQLAlchemy(app)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    pagos = db.relationship('Pago', backref='cliente', lazy=True)
    suscripciones = db.relationship('Suscripcion', backref='cliente', lazy=True)

class Pago(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    monto = db.Column(db.Float, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

class Suscripcion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    inicio = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    fin = db.Column(db.DateTime, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

@app.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.get_json()
    nuevo_cliente = Cliente(nombre=data['nombre'], apellidos=data['apellidos'])
    db.session.add(nuevo_cliente)
    db.session.commit()
    return jsonify({'id': nuevo_cliente.id, 'nombre': nuevo_cliente.nombre, 'apellidos': nuevo_cliente.apellidos}), 201

@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    clientes = Cliente.query.all()
    clientes_json = [{'id': cliente.id, 'nombre': cliente.nombre, 'apellidos': cliente.apellidos} for cliente in clientes]
    return jsonify(clientes_json), 200

@app.route('/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    data = request.get_json()
    cliente = Cliente.query.get_or_404(id)
    cliente.nombre = data.get('nombre', cliente.nombre)
    cliente.apellidos = data.get('apellidos', cliente.apellidos)
    db.session.commit()
    return jsonify({'id': cliente.id, 'nombre': cliente.nombre, 'apellidos': cliente.apellidos}), 200

@app.route('/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'mensaje': 'Cliente eliminado exitosamente'}), 200

@app.route('/pagos', methods=['POST'])
def crear_pago():
    data = request.get_json()
    nuevo_pago = Pago(fecha=data['fecha'], monto=data['monto'], cliente_id=data['cliente_id'])
    db.session.add(nuevo_pago)
    db.session.commit()
    return jsonify({'id': nuevo_pago.id, 'fecha': nuevo_pago.fecha, 'monto': nuevo_pago.monto, 'cliente_id': nuevo_pago.cliente_id}), 201

@app.route('/pagos', methods=['GET'])
def obtener_pagos():
    pagos = Pago.query.all()
    pagos_json = [{'id': pago.id, 'fecha': pago.fecha, 'monto': pago.monto, 'cliente_id': pago.cliente_id} for pago in pagos]
    return jsonify(pagos_json), 200

@app.route('/pagos/<int:id>', methods=['PUT'])
def actualizar_pago(id):
    data = request.get_json()
    pago = Pago.query.get_or_404(id)
    pago.fecha = data.get('fecha', pago.fecha)
    pago.monto = data.get('monto', pago.monto)
    pago.cliente_id = data.get('cliente_id', pago.cliente_id)
    db.session.commit()
    return jsonify({'id': pago.id, 'fecha': pago.fecha, 'monto': pago.monto, 'cliente_id': pago.cliente_id}), 200

@app.route('/pagos/<int:id>', methods=['DELETE'])
def eliminar_pago(id):
    pago = Pago.query.get_or_404(id)
    db.session.delete(pago)
    db.session.commit()
    return jsonify({'mensaje': 'Pago eliminado exitosamente'}), 200

@app.route('/suscripciones', methods=['POST'])
def crear_suscripcion():
    data = request.get_json()
    nueva_suscripcion = Suscripcion(tipo=data['tipo'], precio=data['precio'], inicio=data['inicio'], fin=data['fin'], cliente_id=data['cliente_id'])
    db.session.add(nueva_suscripcion)
    db.session.commit()
    return jsonify({'id': nueva_suscripcion.id, 'tipo': nueva_suscripcion.tipo, 'precio': nueva_suscripcion.precio, 'inicio': nueva_suscripcion.inicio, 'fin': nueva_suscripcion.fin, 'cliente_id': nueva_suscripcion.cliente_id}), 201

@app.route('/suscripciones', methods=['GET'])
def obtener_suscripciones():
    suscripciones = Suscripcion.query.all()
    suscripciones_json = [{'id': suscripcion.id, 'tipo': suscripcion.tipo, 'precio': suscripcion.precio, 'inicio': suscripcion.inicio, 'fin': suscripcion.fin, 'cliente_id': suscripcion.cliente_id} for suscripcion in suscripciones]
    return jsonify(suscripciones_json), 200

@app.route('/suscripciones/<int:id>', methods=['PUT'])
def actualizar_suscripcion(id):
    data = request.get_json()
    suscripcion = Suscripcion.query.get_or_404(id)
    suscripcion.tipo = data.get('tipo', suscripcion.tipo)
    suscripcion.precio = data.get('precio', suscripcion.precio)
    suscripcion.inicio = data.get('inicio', suscripcion.inicio)
    suscripcion.fin = data.get('fin', suscripcion.fin)
    suscripcion.cliente_id = data.get('cliente_id', suscripcion.cliente_id)
    db.session.commit()
    return jsonify({'id': suscripcion.id, 'tipo': suscripcion.tipo, 'precio': suscripcion.precio, 'inicio': suscripcion.inicio, 'fin': suscripcion.fin, 'cliente_id': suscripcion.cliente_id}), 200

@app.route('/suscripciones/<int:id>', methods=['DELETE'])
def eliminar_suscripcion(id):
    suscripcion = Suscripcion.query.get_or_404(id)
    db.session.delete(suscripcion)
    db.session.commit()
    return jsonify({'mensaje': 'Suscripción eliminada exitosamente'}), 200


if __name__ == '__main__':
    app.run(debug=True)
  
