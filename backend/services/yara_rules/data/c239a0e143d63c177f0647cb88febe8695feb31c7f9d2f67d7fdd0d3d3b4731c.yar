rule auto_rule_20250726224337_3893 {
  strings:
    $o0 = "dword_406555" wide ascii nocase
    $o1 = "byte_404077" wide ascii nocase
    $o2 = "lpPaint" wide ascii nocase
    $o3 = "hTemplateFile" wide ascii nocase
  condition:
    4 of ($o*)
}