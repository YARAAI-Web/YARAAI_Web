rule auto_rule_20250726180557_0620 {
  strings:
    $o0 = "off_46703C" wide ascii nocase
    $o1 = "off_467058" wide ascii nocase
    $o2 = "UnwindUp5_0" wide ascii nocase
  condition:
    3 of ($o*)
}