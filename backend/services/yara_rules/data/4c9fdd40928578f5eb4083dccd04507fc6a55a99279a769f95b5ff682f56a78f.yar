rule auto_rule_20250726211341_9349 {
  strings:
    $o0 = "dword_78158" wide ascii nocase
    $o1 = "dword_781F4" wide ascii nocase
  condition:
    all of them
}