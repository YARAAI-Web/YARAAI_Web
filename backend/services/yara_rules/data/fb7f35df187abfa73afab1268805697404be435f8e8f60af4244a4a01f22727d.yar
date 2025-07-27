rule auto_rule_20250726224517_3154 {
  strings:
    $o0 = "dword_41D97C" wide ascii nocase
    $o1 = "hTemplateFile" wide ascii nocase
    $o2 = "ValidateRect" wide ascii nocase
  condition:
    3 of ($o*)
}