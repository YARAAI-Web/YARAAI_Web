rule auto_rule_20250726224650_8290 {
  strings:
    $o0 = "lpCharType" wide ascii nocase
    $o1 = "dword_46715C" wide ascii nocase
    $o2 = "nModule" wide ascii nocase
  condition:
    3 of ($o*)
}