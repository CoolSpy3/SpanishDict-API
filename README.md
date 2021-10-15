# SpanishDict API
Provides an (unofficial) api interface for [spanishdict.com](https://spanishdict.com)

## Translations
To translate a word, call `translate_word(<word>)`.

## Conjugations
To conjugate a word, call `conjugate_word(<word>)`. This returns a 3d `dict` where specific conjugations can be accessed with the keys `[mode][tense][subject]`. The constants for these keys can be found in the `conjugations` submodule.

## Caching
By default, this API caches the recieved JSON data. To disable this behavior, call `set_cache_enabled(False)`.
