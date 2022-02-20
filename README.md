# QueryTranslator
### Usage
### Search params
```
- Specify the target/source language
    The brown fox jumps @ja
    @en 茶色いきつねは飛び跳ねる 
```
### Config params
All settings are managed by `config.json`.  
The default settings are as follows:

```json
{
  "translation_source": {
    "utilize": "deepl_translate",
    "deepl_translate": {
      "api_key": "xxx",
      "target_lang": "EN",
      "source_lang": "JA"
    }
  },
  "server": {
    "port_number": 8041
  },
  "search_engine": {
    "site": "google"
  }
}
```

#### Parameter options
<details>
  <summary>
    Target language codes (deepl_translate)
  </summary>
  <div>
    <ul> <li>"BG" - Bulgarian</li><li>"CS" - Czech</li><li>"DA" - Danish</li><li>"DE" - German</li><li>"EL" - Greek</li><li>"EN-GB" (not supported) - English (British)</li><li>"EN-US" - English (American)</li><li>"EN" - English (unspecified variant for backward compatibility; please select EN-GB or EN-US instead)</li><li>"ES" - Spanish</li><li>"ET" - Estonian</li><li>"FI" - Finnish</li><li>"FR" - French</li><li>"HU" - Hungarian</li><li>"IT" - Italian</li><li>"JA" - Japanese</li><li>"LT" - Lithuanian</li><li>"LV" - Latvian</li><li>"NL" - Dutch</li><li>"PL" - Polish</li><li>"PT-PT" - Portuguese (all Portuguese varieties excluding Brazilian Portuguese)</li><li>"PT-BR" (not supported) - Portuguese (Brazilian)</li><li>"PT" - Portuguese (unspecified variant for backward compatibility; please select PT-PT or PT-BR instead)</li><li>"RO" - Romanian</li><li>"RU" - Russian</li><li>"SK" - Slovak</li><li>"SL" - Slovenian</li><li>"SV" - Swedish</li><li>"ZH" - Chinese</li> </ul>
  </div>
</details>

<details>
  <summary>
    Source language codes (deepl_translate)
  </summary>
  <div>
    <ul> <li>"BG" - Bulgarian</li><li>"CS" - Czech</li><li>"DA" - Danish</li><li>"DE" - German</li><li>"EL" - Greek</li><li>"EN" - English</li><li>"ES" - Spanish</li><li>"ET" - Estonian</li><li>"FI" - Finnish</li><li>"FR" - French</li><li>"HU" - Hungarian</li><li>"IT" - Italian</li><li>"JA" - Japanese</li><li>"LT" - Lithuanian</li><li>"LV" - Latvian</li><li>"NL" - Dutch</li><li>"PL" - Polish</li><li>"PT" - Portuguese (all Portuguese varieties mixed)</li><li>"RO" - Romanian</li><li>"RU" - Russian</li><li>"SK" - Slovak</li><li>"SL" - Slovenian</li><li>"SV" - Swedish</li><li>"ZH" - Chinese</li> </ul>
  </div>
</details>