rule auto_rule_20250726163834_6950 {
  strings:
    $o0 = "dword_433580" wide ascii nocase
    $o1 = "dword_433588" wide ascii nocase
  condition:
    all of them
}