rule auto_rule_20250726151723_0813 {
  strings:
    $o0 = "dword_42D197" wide ascii nocase
    $o1 = "x8A8C" wide ascii nocase
    $o2 = "x4196D1" wide ascii nocase
    $o3 = "dword_42B000" wide ascii nocase
  condition:
    4 of ($o*)
}