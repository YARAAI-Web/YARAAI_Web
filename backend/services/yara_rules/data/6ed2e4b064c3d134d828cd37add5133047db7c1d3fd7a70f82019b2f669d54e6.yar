rule auto_rule_20250726114934_0550 {
  strings:
    $o0 = "dword_4242A0" wide ascii nocase
  condition:
    all of them
}