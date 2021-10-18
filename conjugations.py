INFINITIVE = 'INF'
PAST_PARTICIPLE = 'PAST_PART'
PRESENT_PARTICIPLE = 'PRESENT_PART'

INDICATIVE = 'IND'
SUBJUNCTIVE = 'SUB'
IMPERATIVE = 'IMP'
CONTINUOUS = 'CONT'
PERFECT = 'PERF'
PERFECT_SUBJUNCTIVE = 'PERF_SUBJ'

PRESENT = 'PRES'
PRETERIT = 'PRET'
IMPERFECT = 'IMP'
PAST = 'PAST'
CONDITIONAL = 'COND'
FUTURE = 'FUT'

AFFIRMATIVE = 'AFF'
NEGATIVE = 'NEG'

YO = 'YO'
TU = 'TU'
EL_ELLA_USTED = 'EL'
NOSOTROS = 'NOS'
VOSOTROS = 'VOS'
ELLOS_ELLAS_UDS = 'ELLOS'
VOS = 'VOS(TU)'

SUBJECTS = [YO, TU, EL_ELLA_USTED, NOSOTROS, VOSOTROS, ELLOS_ELLAS_UDS, VOS]

VALID_CONJUGATIONS = {
    INDICATIVE: [
        PRESENT,
        PRETERIT,
        IMPERFECT,
        CONDITIONAL,
        FUTURE
    ],
    SUBJUNCTIVE: [
        PRESENT,
        IMPERFECT,
        FUTURE
    ],
    IMPERATIVE: [
        AFFIRMATIVE,
        NEGATIVE
    ],
    CONTINUOUS: [
        PRESENT,
        PRETERIT,
        IMPERFECT,
        CONDITIONAL,
        FUTURE
    ],
    PERFECT: [
        PRESENT,
        PRETERIT,
        PAST,
        CONDITIONAL,
        FUTURE
    ],
    PERFECT_SUBJUNCTIVE: [
        PRESENT,
        PAST,
        FUTURE
    ]
}

def get_json_path_for_conjugation(mode: str, tense: str) -> str:
    if mode == IMPERATIVE:
        return 'imperative' if tense == AFFIRMATIVE else 'negativeImperative' if tense == NEGATIVE else None
    try:
        if tense not in VALID_CONJUGATIONS[mode]:
            return None
        jsonMode = {INDICATIVE: 'Indicative', SUBJUNCTIVE: 'Subjunctive', CONTINUOUS: 'Continuous', PERFECT: 'Perfect', PERFECT_SUBJUNCTIVE: 'PerfectSubjunctive'}[mode]
        jsonTense = {PRESENT: 'present', PRETERIT: 'preterit', IMPERFECT: 'imperfect', PAST: 'past', CONDITIONAL: 'conditional', FUTURE: 'future'}[tense]
        return jsonTense + jsonMode
    except KeyError:
        return None

def get_position_for_subject(subject: str) -> int:
    return {YO: 0, TU: 1, EL_ELLA_USTED: 2, NOSOTROS: 3, VOSOTROS: 4, ELLOS_ELLAS_UDS: 5, VOS: 6}[subject]
