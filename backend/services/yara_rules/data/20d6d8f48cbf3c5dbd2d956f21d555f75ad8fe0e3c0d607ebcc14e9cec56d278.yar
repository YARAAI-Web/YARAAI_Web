rule auto_rule_20250727044633_4029 {
  strings:
    $o0 = "szShortPath" wide ascii nocase
    $o1 = "pbmi" wide ascii nocase
    $o2 = "dword_43468B" wide ascii nocase
  condition:
    3 of ($o*)
}