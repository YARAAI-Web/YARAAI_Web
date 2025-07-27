rule auto_rule_20250727031513_3032 {
  strings:
    $o0 = "x2868u" wide ascii nocase
    $o1 = "dword_426ECD" wide ascii nocase
  condition:
    all of them
}