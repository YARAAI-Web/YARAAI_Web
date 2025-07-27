rule auto_rule_20250727034333_5727 {
  strings:
    $o0 = "pszSet" wide ascii nocase
    $o1 = "uHilite" wide ascii nocase
    $o2 = "pszURL" wide ascii nocase
  condition:
    3 of ($o*)
}