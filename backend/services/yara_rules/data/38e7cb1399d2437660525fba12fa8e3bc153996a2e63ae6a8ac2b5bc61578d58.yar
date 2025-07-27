rule auto_rule_20250726094049_1887 {
  strings:
    $o0 = "dword_7F918" wide ascii nocase
    $o1 = "dword_7F9C8" wide ascii nocase
    $o2 = "stru_7EF0C" wide ascii nocase
    $o3 = "KeDetachProcess" wide ascii nocase
  condition:
    4 of ($o*)
}