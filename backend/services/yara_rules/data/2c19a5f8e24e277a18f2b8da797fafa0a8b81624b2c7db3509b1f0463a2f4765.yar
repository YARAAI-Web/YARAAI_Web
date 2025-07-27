rule auto_rule_20250726133205_4040 {
  strings:
    $o0 = "__addl" wide ascii nocase
    $o1 = "Program" wide ascii nocase
    $o2 = "word_418A02" wide ascii nocase
    $o3 = "report_failure" wide ascii nocase
    $o4 = "off_44D568" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726133208_8123 {
  strings:
    $o0 = "dword_44D6F4" wide ascii nocase
    $o1 = "GdipDeleteBrush" wide ascii nocase
    $o2 = "acmStreamUnprepareHeader" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726133212_1133 {
  condition:
    auto_rule_20250726133205_4040 or auto_rule_20250726133208_8123
}