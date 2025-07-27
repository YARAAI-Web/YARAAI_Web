rule auto_rule_20250726120029_4742 {
  strings:
    $o0 = "dword_6402F990" wide ascii nocase
  condition:
    all of them
}