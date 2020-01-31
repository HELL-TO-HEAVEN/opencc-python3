

DICT_FROM = \
    { 'cn': ('STCharacters', 'STPhrases')
    , 'hk': ('HKVariantsRev', 'HKVariantsRevPhrases')
    , 'tw': ('TWVariantsRev', 'TWVariantsRevPhrases')
    , 'twp': ('TWVariantsRev', 'TWVariantsRevPhrases', 'TWPhrasesRev')
    , 'jp': ('JPVariantsRev',)
    }

DICT_TO = \
    { 'cn': ('TSCharacters', 'TSPhrases')
    , 'hk': ('HKVariants', 'HKVariantsPhrases')
    , 'tw': ('TWVariants',)
    , 'twp': ('TWVariants', 'TWPhrasesIT', 'TWPhrasesName', 'TWPhrasesOther')
    , 'jp': ('JPVariants',)
    }