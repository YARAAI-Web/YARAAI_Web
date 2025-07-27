rule auto_rule_20250726062818_5804 {
  strings:
    $o0 = "dword_7816C" wide ascii nocase
    $o1 = "dword_781B4" wide ascii nocase
  condition:
    all of them
}