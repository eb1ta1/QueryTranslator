from flask import Flask, request, redirect

app = Flask(__name__)


class JsonLoader:
    def __init__(self, json_path) -> None:
        self.json_path = json_path

    def load_json(self):
        import json
        config_json_file = open(self.json_path, 'r')
        config_json = json.load(config_json_file)
        return config_json


json_value = JsonLoader('../config.json').load_json()
preferred_port_number = json_value['server']['preferred_port_number']


def lang_codes_checker(upper=False):
    import pickle
    f = open("./langcodes.txt", "rb")
    lang_codes = pickle.load(f)
    if upper:
        for i in range(len(lang_codes)):
            lang_codes[i] = lang_codes[i].upper()
    return lang_codes


@app.route('/')
def get_request():
    contents = request.args.get('q', '')
    from translator import Translator
    translated_content = Translator(contents).deepl_translate()
    domain = f'https://www.google.com/search?q={translated_content}&gl=us&hl=en&gws_rd=cr&pws=0'
    return redirect(domain)


if __name__ == "__main__":
    if preferred_port_number:
        try:
            app.run(port=preferred_port_number, debug=False)
        except OSError:
            print('Oops! The port number may be duplicated. Please check config.json')
