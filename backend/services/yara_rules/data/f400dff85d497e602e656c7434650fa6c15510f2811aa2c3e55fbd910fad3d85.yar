rule auto_rule_20250726184103_0642 {
  strings:
    $o0 = "UnwindUp5_0" wide ascii nocase
    $o1 = "DrawDibGetBuffer" wide ascii nocase
    $o2 = "ReturnValue" wide ascii nocase
  condition:
    3 of ($o*)
}