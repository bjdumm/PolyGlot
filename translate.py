import pickle
import six
from google.cloud import translate_v2 as trans



def list_languages_with_target(target):
    """Lists all available languages and localizes them to the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    results = translate_client.get_languages(target_language=target)

    for language in results:
        print(u"{name} ({language})".format(**language))


def explicit():
    from google.cloud import storage
    storage_client = storage.Client.from_service_account_json('polylingoios-456d2388281d.json')
    buckets = list(storage_client.list_buckets())
    print(buckets)


def translate_text(target, text):
    #translate_text("es" , "Welcome")
    #$env:GOOGLE_APPLICATION_CREDENTIALS="polylingoios-456d2388281d.json"

    trans_client = trans.Client()
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = trans_client.translate(text, target_language=target)
    return result["translatedText"]
   
   # print("Translation: {}".format(result["translatedText"]))
    
def list_languages():
    tc = trans.Client()
    results = tc.get_languages()
    print(results)
    return results

#list_languages()
#s = translate_text("de", "Test")














"""
available = list_languages()
lang = "German"
iso = ""
for l in available:
    if l['name'] == lang:
        iso = l['language']
print(iso)
"""