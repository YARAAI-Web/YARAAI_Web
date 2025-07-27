rule auto_rule_20250726094720_0920 {
  strings:
    $o0 = "x1F9Bu" wide ascii nocase
    $o1 = "local_unwind2" wide ascii nocase
    $o2 = "aProductname" wide ascii nocase
  condition:
    3 of ($o*)
}