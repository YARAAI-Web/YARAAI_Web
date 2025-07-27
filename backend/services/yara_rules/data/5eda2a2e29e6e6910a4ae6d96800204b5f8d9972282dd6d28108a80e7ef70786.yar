rule auto_rule_20250727032313_3328 {
  strings:
    $o0 = "dword_4479F0" wide ascii nocase
    $o1 = "_inc" wide ascii nocase
    $o2 = "_FillZeroMan" wide ascii nocase
  condition:
    3 of ($o*)
}