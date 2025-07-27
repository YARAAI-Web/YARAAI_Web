rule auto_rule_20250726141512_6270 {
  strings:
    $o0 = "off_456490" wide ascii nocase
    $o1 = "UpdateResourceA" wide ascii nocase
    $o2 = "UnwindUp2_0" wide ascii nocase
    $o3 = "program" wide ascii nocase
  condition:
    4 of ($o*)
}