from flask import Flask, request, redirect
import urllib.parse

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
port_number = json_value['server']['port_number']


class Translator:
    def __init__(self,
                 text):
        self.config = JsonLoader('../config.json').load_json()

        self.source_lang = None
        self.target_lang = None
        self.translated_content = None
        self.content = text

    def deepl_lang_checker(self):
        deepl_target_lang = self.config['translate']['deepl']['target_lang'],
        deepl_source_lang = self.config['translate']['deepl']['source_lang']

        deepl_target_lang = deepl_target_lang[0]
        deepl_source_lang = deepl_source_lang[1]

        lang_codes_list = lang_codes_checker(upper=True)
        if deepl_target_lang in ['EN', 'EN-US', 'EN-GB']:
            self.target_lang = 'EN-US'
        elif deepl_target_lang in ['PT', 'PT-PT', 'PT-BR']:
            self.target_lang = 'PT-PT'
        elif deepl_target_lang in lang_codes_list:
            self.target_lang = deepl_target_lang
        else:
            print(lang_codes_list[:3])

        if deepl_source_lang in ['EN', 'EN-US', 'EN-GB']:
            self.source_lang = 'EN-US'
        elif deepl_source_lang in ['PT', 'PT-PT', 'PT-BR']:
            self.source_lang = 'PT-PT'
        elif deepl_source_lang in lang_codes_list:
            self.source_lang = deepl_source_lang

    def googletrans(self):
        """
        The use of googletrans is DEPRECATED
        """
        import googletrans
        self.translated_content = googletrans.Translator().translate(
            self.content, src=self.source_lang, dest=self.target_lang)
        return self.translated_content.text

    def deepl_translate(self):
        import deepl
        self.deepl_lang_checker()
        api_key = self.config['translate']['deepl']['api_key']
        self.translated_content = deepl.Translator(api_key).translate_text(self.content,
                                                                           target_lang=self.target_lang,
                                                                           source_lang=self.source_lang)
        return self.translated_content

    def google_cloud_translate(self):
        pass

    def aws_translate(self):
        pass


def lang_codes_checker(upper=False):
    import pickle
    f = open("./langcodes.txt", "rb")
    lang_codes = pickle.load(f)
    if upper:
        for i in range(len(lang_codes)):
            lang_codes[i] = lang_codes[i].upper()
    return lang_codes


def check_query(query):
    default_site = json_value['sites']['default_site']
    query_list = query.split()
    site_query_list = [default_site]
    not_flag = False
    new_query_list = []
    for i in range(len(query_list)):
        if query_list[i][0] == '@':
            if query_list[i][1:] not in ['not']:
                site_query_list.append(query_list[i][1:])
            else:
                not_flag = True
        else:
            new_query_list.append(query_list[i])

    query = ' '.join(new_query_list)
    print(query)

    if not_flag:
        content = urllib.parse.quote_plus(query)
    else:
        content = urllib.parse.quote_plus(str(Translator(query).deepl_translate()))

    return content, site_query_list


@app.route('/search/')
def get_request():
    query = request.args.get('q', '')
    content, site_query_list = check_query(query)
    if not site_query_list[-1] in json_value['sites'].keys():
        content = f'{content} \'{site_query_list[-1]}\''
        default_site = json_value['sites']['default_site']
        url = str(json_value['sites'][default_site]['url']).replace('%query', content)
    else:
        url = str(json_value['sites'][site_query_list[-1]]['url']).replace('%query', content)
    return redirect(url)


@app.route('/search/<string:site_name>/')
def get_request_specific_site(site_name):
    query = request.args.get('q', '')
    content, site_query_list = check_query(query)
    url = str(json_value['sites'][site_name]['url']).replace('%query', content)
    return redirect(url)


if __name__ == "__main__":
    if port_number:
        try:
            app.run(port=port_number, debug=False)
        except OSError:
            print('Oops! The port number may be duplicated. Please check config.json')
