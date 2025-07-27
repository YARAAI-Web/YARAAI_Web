rule auto_rule_20250726105939_3340 {
  strings:
    $o0 = "dword_449AF0" wide ascii nocase
  condition:
    all of them
}