rule auto_rule_20250727013052_4778 {
  strings:
    $o0 = "dword_640303FC" wide ascii nocase
  condition:
    all of them
}