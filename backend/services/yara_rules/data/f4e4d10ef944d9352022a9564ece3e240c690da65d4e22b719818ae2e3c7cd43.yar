rule auto_rule_20250727043906_5633 {
  strings:
    $o0 = "hSCManager" wide ascii nocase
    $o1 = "dword_6402E994" wide ascii nocase
  condition:
    all of them
}