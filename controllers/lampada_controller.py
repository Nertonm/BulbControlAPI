from flask import Blueprint, request, jsonify
from services.lampada_service import set_lamp_state_service

# Criando um Blueprint
lamp_blueprint = Blueprint('lamp', __name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@lamp_blueprint.route('/set_estado', methods=['PUT'])
def set_lamp_state_route():
    try:
        # Obtendo dados do corpo da requisição
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Chamando o serviço para mudar o estado da lâmpada
        response = set_lamp_state_service(data)
        return jsonify(response), 200  # Retorna o JSON de resposta do serviço
    except Exception as e:
        # Lida com erros de maneira genérica
        return jsonify({"error": str(e)}), 500

  
# @lamp_blueprint.route('/set_color', methods=['PUT'])
# def set_lamp_color_route():
#     try:
#         # Obtendo dados do corpo da requisição
#         data = request.get_json()
#         if not data:
#             return jsonify({"error": "No data provided"}), 400
        
#         # Chamando o serviço para mudar a cor da lâmpada
#         response = set_lamp_color_service(data)
#         return jsonify(response), 200  # Retorna o JSON de resposta do serviço
#     except Exception as e:
#         # Lida com erros de maneira genérica
#         return jsonify({"error": str(e)}), 500

# @lamp_blueprint.route('/set_colour', methods=['PUT'])
# def set_lamp_colour_route():
#     try:
#         # Obtendo dados do corpo da requisição
#         data = request.get_json()
#         if not data:
#             return jsonify({"error": "No data provided"}), 400
        
#         # Chamando o serviço para mudar a cor da lâmpada
#         response = set_lamp_colour_service(data)
#         return jsonify(response), 200  # Retorna o JSON de resposta do serviço
#     except Exception as e:
#         # Lida com erros de maneira genérica
#         return jsonify({"error": str(e)}), 500

# @lamp_blueprint.route('/set_brightness', methods=['PUT'])
# def set_lamp_brightness_route():
#     try:
#         # Obtendo dados do corpo da requisição
#         data = request.get_json()
#         if not data:
#             return jsonify({"error": "No data provided"}), 400
        
#         # Chamando o serviço para mudar a cor da lâmpada
#         response = set_lamp_brightness_service(data)
#         return jsonify(response), 200  # Retorna o JSON de resposta do serviço
#     except Exception as e:
#         # Lida com erros de maneira genérica
#         return jsonify({"error": str(e)}), 500