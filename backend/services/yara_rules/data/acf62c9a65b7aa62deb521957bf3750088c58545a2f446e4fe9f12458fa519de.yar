rule auto_rule_20250726111635_1412 {
  strings:
    $o0 = "dword_6402E990" wide ascii nocase
    $o1 = "Destinationa" wide ascii nocase
  condition:
    all of them
}