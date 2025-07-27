rule auto_rule_20250726110459_7325 {
  strings:
    $o0 = "dword_467B58" wide ascii nocase
  condition:
    all of them
}