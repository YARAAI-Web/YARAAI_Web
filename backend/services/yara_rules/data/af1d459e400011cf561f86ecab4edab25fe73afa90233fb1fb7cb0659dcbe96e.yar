rule auto_rule_20250726234739_1083 {
  strings:
    $o0 = "GetSystemTime" wide ascii nocase
    $o1 = "fccHandler" wide ascii nocase
  condition:
    all of them
}