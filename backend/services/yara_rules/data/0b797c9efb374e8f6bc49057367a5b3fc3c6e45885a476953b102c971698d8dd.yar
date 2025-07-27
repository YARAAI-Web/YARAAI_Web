rule auto_rule_20250727022337_9674 {
  strings:
    $o0 = "dword_2AA01110" wide ascii nocase
  condition:
    all of them
}