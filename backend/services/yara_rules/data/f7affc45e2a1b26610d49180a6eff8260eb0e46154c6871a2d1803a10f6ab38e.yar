rule auto_rule_20250726134914_6010 {
  strings:
    $o0 = "x1A32u" wide ascii nocase
    $o1 = "DefaultChar" wide ascii nocase
    $o2 = "dword_421CA2" wide ascii nocase
    $o3 = "dword_42C000" wide ascii nocase
  condition:
    4 of ($o*)
}