rule auto_rule_20250727024412_2958 {
  strings:
    $o0 = "UnwindUp3_0" wide ascii nocase
    $o1 = "nProgram" wide ascii nocase
    $o2 = "off_45C920" wide ascii nocase
  condition:
    3 of ($o*)
}