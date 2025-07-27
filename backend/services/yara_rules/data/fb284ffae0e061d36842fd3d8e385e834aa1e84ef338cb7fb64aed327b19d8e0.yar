rule auto_rule_20250726204618_4314 {
  strings:
    $o0 = "dword_4292B5" wide ascii nocase
    $o1 = "CreateBitmapIndirect" wide ascii nocase
  condition:
    all of them
}