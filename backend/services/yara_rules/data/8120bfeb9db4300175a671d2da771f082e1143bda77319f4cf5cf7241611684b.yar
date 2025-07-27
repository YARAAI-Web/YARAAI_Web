rule auto_rule_20250726231113_1797 {
  strings:
    $o0 = "dword_446EC4" wide ascii nocase
    $o1 = "dword_44602C" wide ascii nocase
  condition:
    all of them
}