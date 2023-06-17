from flask_graphql import GraphQLView
from models.schema import schema

from api_config import (
    app,
    db
)


app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True #Interfaz grafica
))

@app.route('/', methods=['GET', 'POST', 'PUT']) # @ decorador
def index():
    return 'Hola Mundo desde Flask'

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)