rule auto_rule_20250726230635_8261 {
  strings:
    $o0 = "dword_10066DE8" wide ascii nocase
  condition:
    all of them
}