rule auto_rule_20250726215525_0630 {
  strings:
    $o0 = "v262" wide ascii nocase
    $o1 = "dword_4071E4" wide ascii nocase
    $o2 = "v276" wide ascii nocase
    $o3 = "kr28_4" wide ascii nocase
    $o4 = "dword_407058" wide ascii nocase
  condition:
    4 of ($o*)
}