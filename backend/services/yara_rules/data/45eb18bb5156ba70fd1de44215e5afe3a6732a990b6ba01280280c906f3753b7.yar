rule auto_rule_20250726215156_5323 {
  strings:
    $o0 = "dword_6403034C" wide ascii nocase
  condition:
    all of them
}