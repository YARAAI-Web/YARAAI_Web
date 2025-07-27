rule auto_rule_20250726104240_2513 {
  strings:
    $o0 = "dword_4767D4" wide ascii nocase
    $o1 = "_IsZeroMan" wide ascii nocase
    $o2 = "_hw_cw" wide ascii nocase
  condition:
    3 of ($o*)
}