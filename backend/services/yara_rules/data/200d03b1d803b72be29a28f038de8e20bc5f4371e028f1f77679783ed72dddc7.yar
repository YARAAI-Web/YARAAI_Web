rule auto_rule_20250726182137_0404 {
  strings:
    $o0 = "dword_41D978" wide ascii nocase
    $o1 = "hdca" wide ascii nocase
    $o2 = "dword_41DA98" wide ascii nocase
    $o3 = "lpPaint" wide ascii nocase
    $o4 = "lpWindowName" wide ascii nocase
  condition:
    4 of ($o*)
}