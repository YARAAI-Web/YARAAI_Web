rule auto_rule_20250726195652_8212 {
  strings:
    $o0 = "cchText" wide ascii nocase
    $o1 = "dword_420B54" wide ascii nocase
  condition:
    all of them
}