from querytranslator import index


class Translator:
    def __init__(self,
                 text):
        self.config = index.JsonLoader('../config.json').load_json()

        self.source_lang = None
        self.target_lang = None
        self.translated_content = None
        self.content = text

    def deepl_lang_checker(self):
        deepl_target_lang = self.config['translate']['deepl']['target_lang'],
        deepl_source_lang = self.config['translate']['deepl']['source_lang']

        deepl_target_lang = deepl_target_lang[0]
        deepl_source_lang = deepl_source_lang[1]

        lang_codes_list = index.lang_codes_checker(upper=True)
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


if __name__ == "__main__":
    translated_content = Translator('今日の天気').deepl_translate()
    print(translated_content)
