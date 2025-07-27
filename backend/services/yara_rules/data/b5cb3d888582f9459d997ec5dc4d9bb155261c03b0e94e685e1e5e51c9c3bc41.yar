rule auto_rule_20250726105211_7657 {
  strings:
    $o0 = "dword_475D04" wide ascii nocase
    $o1 = "dword_475E30" wide ascii nocase
  condition:
    all of them
}