rule auto_rule_20250726091148_8920 {
  strings:
    $o0 = "UnwindUp1_0" wide ascii nocase
    $o1 = "stream" wide ascii nocase
    $o2 = "__endstdio" wide ascii nocase
    $o3 = "xC000008E" wide ascii nocase
    $o4 = "word_4698EC" wide ascii nocase
  condition:
    5 of ($o*)
}