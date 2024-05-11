import pytest
from src.mcfg_parser.tree import MCFGTree
from src.mcfg_parser.grammar import MCFGRuleElement, MCFGRule, MCFGRuleElementInstance, MCFGGrammar
from src.mcfg_parser.parser import MCFGGrammarParser
#grammar = MCFGGrammar.from_string(grammar_definition)


@pytest.fixture
def example_grammar():
    grammar_rules = [
        "S(uv) -> NP(u) VP(v)",
        "S(uv) -> NPwh(u) VP(v)",
        "S(vuw) -> Aux(u) Swhmain(v, w)",
        "S(uwv) -> NPdisloc(u, v) VP(w)",
        "S(uwv) -> NPwhdisloc(u, v) VP(w)",
        "Sbar(uv) -> C(u) S(v)",
        "Sbarwh(v, uw) -> C(u) Swhemb(v, w)",
        "Sbarwh(u, v) -> NPwh(u) VP(v)",
        "Swhmain(v, uw) -> NP(u) VPwhmain(v, w)",
        "Swhmain(w, uxv) -> NPdisloc(u, v) VPwhmain(w, x)",
        "Swhemb(v, uw) -> NP(u) VPwhemb(v, w)",
        "Swhemb(w, uxv) -> NPdisloc(u, v) VPwhemb(w, x)",
        "Src(v, uw) -> NP(u) VPrc(v, w)",
        "Src(w, uxv) -> NPdisloc(u, v) VPrc(w, x)",
        "Src(u, v) -> N(u) VP(v)",
        "Swhrc(u, v) -> Nwh(u) VP(v)",
        "Swhrc(v, uw) -> NP(u) VPwhrc(v, w)",
        "Sbarwhrc(v, uw) -> C(u) Swhrc(v, w)",
        "VP(uv) -> Vpres(u) NP(v)",
        "VP(uv) -> Vpres(u) Sbar(v)",
        "VPwhmain(u, v) -> NPwh(u) Vroot(v)",
        "VPwhmain(u, wv) -> NPwhdisloc(u, v) Vroot(w)",
        "VPwhmain(v, uw) -> Vroot(u) Sbarwh(v, w)",
        "VPwhemb(u, v) -> NPwh(u) Vpres(v)",
        "VPwhemb(u, wv) -> NPwhdisloc(u, v) Vpres(w)",
        "VPwhemb(v, uw) -> Vpres(u) Sbarwh(v, w)",
        "VPrc(u, v) -> N(u) Vpres(v)",
        "VPrc(v, uw) -> Vpres(u) Nrc(v, w)",
        "VPwhrc(u, v) -> Nwh(u) Vpres(v)",
        "VPwhrc(v, uw) -> Vpres(u) Sbarwhrc(v, w)",
        "NP(uv) -> D(u) N(v)",
        "NP(uvw) -> D(u) Nrc(v, w)",
        "NPdisloc(uv, w) -> D(u) Nrc(v, w)",
        "NPwh(uv) -> Dwh(u) N(v)",
        "NPwh(uvw) -> Dwh(u) Nrc(v, w)",
        "NPwhdisloc(uv, w) -> Dwh(u) Nrc(v, w)",
        "Nrc(v, uw) -> C(u) Src(v, w)",
        "Nrc(u, vw) -> N(u) Swhrc(v, w)",
        "Nrc(u, vwx) -> Nrc(u, v) Swhrc(w, x)",
        "Dwh(which)",
        "Nwh(who)",
        "D(the)",
        "D(a)",
        "N(greyhound)",
        "N(human)",
        "Vpres(believes)",
        "Vroot(believe)",
        "Aux(does)",
        "C(that)"
    ]

    rules = {MCFGRule.from_string(rule) for rule in grammar_rules}
    return MCFGGrammar(rules, 'S')


def test_parse_simple_sentence(example_grammar):
    parser = MCFGGrammarParser(example_grammar)
    sentence = ['the', 'greyhound', 'believes']
    parse_tree = parser.parse(sentence)
    assert parse_tree is not None  # Expecting a successful parse


def test_parse_invalid_sentence(example_grammar):
    parser = MCFGGrammarParser(example_grammar)
    sentence = ['the', 'human', 'jumped']
    parse_tree = parser.parse(sentence)
    assert parse_tree is None  # No parse expected