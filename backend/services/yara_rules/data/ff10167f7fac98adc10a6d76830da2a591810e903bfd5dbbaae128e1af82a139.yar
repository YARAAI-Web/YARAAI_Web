rule auto_rule_20250726064610_8280 {
  strings:
    $o0 = "dword_41B000" wide ascii nocase
    $o1 = "dword_401328" wide ascii nocase
  condition:
    all of them
}