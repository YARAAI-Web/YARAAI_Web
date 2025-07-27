rule auto_rule_20250726131744_3470 {
  strings:
    $o0 = "dword_4D3058" wide ascii nocase
  condition:
    all of them
}