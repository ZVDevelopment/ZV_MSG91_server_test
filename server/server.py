from flask import Flask, request, abort
from msg91_service.test_WA import  notify_WH_message, send_simple_message, send_admin_reply, send_template_message

app = Flask(__name__)


@app.route("/")
def root():
    return "Hello from ZV-Bot Server!"


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("---- STATUS = ", request.json, "\n\n")
        # notify_WH_message(from_num, msg_recieved)
        return 'Webhook received!', 200
    else:
        abort(400)



if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=8080)