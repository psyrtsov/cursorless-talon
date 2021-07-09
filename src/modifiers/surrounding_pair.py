from talon import Context, Module

mod = Module()
ctx = Context()

ctx.matches = r"""
tag: user.cursorless
"""

pair_symbols = {
    "angle": "angleBrackets",
    "diamond": "angleBrackets",
    "curly": "curlyBrackets",
    "round": "parentheses",
    "square": "squareBrackets",
    "quad": "doubleQuotes",
    "twin": "singleQuotes",
}

mod.list("cursorless_pair_symbol", desc="A symbol that comes in pairs, eg brackets")
ctx.lists["self.cursorless_pair_symbol"] = pair_symbols


@mod.capture(rule=("{user.cursorless_pair_symbol}"))
def cursorless_surrounding_pair(m) -> str:
    """Surrounding pair modifiers"""
    return {
        "transformation": {
            "type": "surroundingPair",
            "delimiter": m.pair_symbol
        }
    }