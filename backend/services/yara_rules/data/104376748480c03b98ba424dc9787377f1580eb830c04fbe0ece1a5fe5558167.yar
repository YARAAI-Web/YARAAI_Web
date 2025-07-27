rule auto_rule_20250726122256_4888 {
  strings:
    $o0 = "overrun" wide ascii nocase
    $o1 = "_abnormal_termination" wide ascii nocase
    $o2 = "off_45C58C" wide ascii nocase
    $o3 = "UnwindUp3_0" wide ascii nocase
  condition:
    4 of ($o*)
}