from app import create_app

app = create_app()
'''
Exexcuta a função create_app()
que cria a aplicação Flask
e retorna o objeto app.
Em seguida, a aplicação é executada com debug=True, 
permitindo que erros sejam exibidos no console durante
o desenvolvimento.
'''

if __name__ == "__main__":
    app.run(debug=True)