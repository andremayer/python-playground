from bottle import Bottle, run
import uuid_service
import calculator
import calendar_service
import text_service
import random_service

main_app = Bottle()

main_app.merge(uuid_service.app)
main_app.merge(calculator.app)
main_app.merge(calendar_service.app)
main_app.merge(text_service.app)
main_app.merge(random_service.app)

if __name__ == '__main__':
    run(main_app, host='localhost', port=8080, debug=True, server='wsgiref')