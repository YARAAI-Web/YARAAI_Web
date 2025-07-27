rule auto_rule_20250726140140_8280 {
  strings:
    $o0 = "dword_4771B4" wide ascii nocase
  condition:
    all of them
}