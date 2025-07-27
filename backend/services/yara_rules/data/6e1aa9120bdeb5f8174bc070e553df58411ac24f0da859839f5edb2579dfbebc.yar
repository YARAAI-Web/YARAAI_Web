rule auto_rule_20250726103159_7612 {
  strings:
    $o0 = "uValue" wide ascii nocase
    $o1 = "fBlockIt" wide ascii nocase
    $o2 = "nCmdShow" wide ascii nocase
  condition:
    3 of ($o*)
}