from . import create_app

api_app = create_app()

if __name__ == '__main__':
    api_app.run(debug=True)