rule auto_rule_20250726213101_8573 {
  strings:
    $o0 = "GetTickCount_0" wide ascii nocase
    $o1 = "GetClipCursor" wide ascii nocase
  condition:
    all of them
}