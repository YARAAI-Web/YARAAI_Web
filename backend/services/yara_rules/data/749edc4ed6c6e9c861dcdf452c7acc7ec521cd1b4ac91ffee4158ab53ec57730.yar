rule auto_rule_20250726072210_8445 {
  strings:
    $o0 = "dword_607004" wide ascii nocase
  condition:
    all of them
}