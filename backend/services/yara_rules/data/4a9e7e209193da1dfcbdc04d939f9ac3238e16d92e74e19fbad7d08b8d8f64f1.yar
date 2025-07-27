rule auto_rule_20250726111014_4089 {
  strings:
    $o0 = "dword_426389" wide ascii nocase
  condition:
    all of them
}