rule auto_rule_20250727022728_7695 {
  strings:
    $o0 = "EECh" wide ascii nocase
    $o1 = "dword_640303EC" wide ascii nocase
  condition:
    all of them
}